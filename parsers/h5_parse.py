import re
import argparse
from pathlib import Path
from typing import Dict
import h5py

def extract_gem5_config_params(cmdline_file: Path) -> Dict[str, str]:
    params = {}
    with open(cmdline_file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith("command line:"):
            tokens = line.split()
            for i, token in enumerate(tokens):
                if token.startswith("--") and "=" in token:
                    key, val = token.lstrip("--").split("=", 1)
                    if key != "outdir":
                        params[key] = val
                elif token == "--bin" and i + 1 < len(tokens):
                    params["bin"] = tokens[i + 1]
    return params

def parse_mcpat_metrics_with_units(file_path: Path) -> dict:
    with open(file_path, "r") as f:
        lines = f.readlines()
    results = {}
    current_group = "mcpat"
    kv_pattern = re.compile(r"^\s*([\w\s\/\(\)-]+)\s*=\s*([0-9.eE+-]+)\s*(\w+\^?\d*|W|mm\^2)?\s*$")
    for line in lines:
        line = line.strip()
        if line.endswith(":") and not line.startswith("McPAT"):
            current_group = line[:-1].strip().lower().replace(" ", "_").replace("/", "_")
            continue
        match = kv_pattern.match(line)
        if match:
            key = match.group(1).strip().lower().replace(" ", "_").replace("/", "_")
            val = float(match.group(2))
            unit = match.group(3) or ""
            group_key = f"{current_group}/{key}"
            results[group_key] = (val, unit)
    return results

def copy_stats_h5_to_output(stats_h5: Path, dst_group):
    with h5py.File(stats_h5, "r") as stats_src:
        def recursive_copy(src_group, dst_group):
            for key in src_group:
                item = src_group[key]
                if isinstance(item, h5py.Dataset):
                    if key in dst_group:
                        del dst_group[key]
                    dst_group.create_dataset(key, data=item[()])
                    for attr_key, attr_val in item.attrs.items():
                        dst_group[key].attrs[attr_key] = attr_val
                elif isinstance(item, h5py.Group):
                    new_group = dst_group.require_group(key)
                    recursive_copy(item, new_group)
        stats_dst = dst_group.create_group("stats")
        recursive_copy(stats_src, stats_dst)

def write_all_to_hdf5(config: Dict[str, str], mcpat_data: dict, stats_h5: Path, out_path: Path, group_name: str):
    with h5py.File(out_path, "a") as h5f:
        root_group = h5f.require_group(group_name)

        cfg_group = root_group.require_group("config")
        for key, val in config.items():
            cfg_group.create_dataset(key, data=val)

        for path, (value, unit) in mcpat_data.items():
            group_path, key = path.rsplit("/", 1)
            group = root_group.require_group(f"mcpat/{group_path}")
            dset = group.create_dataset(key, data=value)
            if unit:
                dset.attrs["unit"] = unit

        copy_stats_h5_to_output(stats_h5, root_group)

def main():
    parser = argparse.ArgumentParser(
        description="Combine gem5 config, McPAT output, and gem5 stats.h5 into a grouped HDF5 summary."
    )
    parser.add_argument("input_dir", type=Path, help="Directory containing cmdline.txt, mcpat_results.txt, and stats.h5")
    parser.add_argument("group_name", type=str, help="Top-level group name for this dataset in the output HDF5")
    parser.add_argument("output_h5", type=Path, help="Output HDF5 file")

    args = parser.parse_args()
    input_dir = args.input_dir

    cmdline_path = input_dir / "cmdline.txt"
    mcpat_path = input_dir / "mcpat_results.txt"
    stats_path = input_dir / "stats.h5"

    if not cmdline_path.exists() or not mcpat_path.exists() or not stats_path.exists():
        raise FileNotFoundError("One or more required files are missing from input_dir.")

    config = extract_gem5_config_params(cmdline_path)
    mcpat = parse_mcpat_metrics_with_units(mcpat_path)
    write_all_to_hdf5(config, mcpat, stats_path, args.output_h5, args.group_name)

    print(f"✅ Written group '{args.group_name}' to {args.output_h5}")

if __name__ == "__main__":
    main()