import csv
import re
import argparse
from pathlib import Path
from typing import Dict


def read_config_csv(config_csv_path: Path) -> Dict[str, str]:
    with open(config_csv_path, "r") as f:
        reader = csv.DictReader(f)
        row = next(reader)
        return {f"config.{k}": v for k, v in row.items()}


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
            results[f"mcpat.{current_group}.{key}"] = val
    return results


def extract_stats_metrics(stats_file: Path) -> Dict[str, float]:
    desired_keys = {
        "simSeconds", "simTicks", "finalTick", "simFreq", "hostSeconds",
        "hostTickRate", "hostMemory", "simInsts", "simOps",
        "hostInstRate", "hostOpRate"
    }

    cpu_keys = {"numCycles", "cpi", "ipc"}
    l2_pattern = re.compile(r'^system\.l2cache\.(\w+)::(\w+)\s+([0-9.eE+-]+)')
    cpu_pattern = re.compile(r'^system\.cpu\.(\w+)\s+([0-9.eE+-]+)')

    results = {}

    with open(stats_file, "r") as f:
        for line in f:
            tokens = line.strip().split()
            if len(tokens) >= 2:
                key = tokens[0]
                if key in desired_keys:
                    results[f"stats.{key}"] = float(tokens[1])

            l2_match = l2_pattern.match(line.strip())
            if l2_match:
                path = f"stats.l2cache.{l2_match.group(1)}.{l2_match.group(2)}"
                results[path] = float(l2_match.group(3))

            cpu_match = cpu_pattern.match(line.strip())
            if cpu_match and cpu_match.group(1) in cpu_keys:
                path = f"stats.cpu.{cpu_match.group(1)}"
                results[path] = float(cpu_match.group(2))

    return results


def generate_csv(input_dir: Path, output_csv: Path):
    config_path = input_dir / "config.csv"
    mcpat_path = input_dir / "mcpat_results.txt"
    stats_path = input_dir / "stats.txt"

    if not config_path.exists() or not mcpat_path.exists() or not stats_path.exists():
        raise FileNotFoundError("One or more required files are missing from input_dir.")

    config = read_config_csv(config_path)
    mcpat = parse_mcpat_metrics_with_units(mcpat_path)
    stats = extract_stats_metrics(stats_path)

    all_data = {**config, **stats, **mcpat}
    write_header = not output_csv.exists() or output_csv.stat().st_size == 0

    with open(output_csv, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=sorted(all_data.keys()))
        if write_header:
            writer.writeheader()
        writer.writerow(all_data)

    print(f"✅ CSV row appended to {output_csv}")


def main():
    parser = argparse.ArgumentParser(description="Extract data and write to CSV")
    parser.add_argument("input_dir", type=Path, help="Input directory with config.csv, mcpat_results.txt, and stats.txt")
    parser.add_argument("output_csv", type=Path, help="Path to output CSV file")
    args = parser.parse_args()
    generate_csv(args.input_dir, args.output_csv)


if __name__ == "__main__":
    main()
