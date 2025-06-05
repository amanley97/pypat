import subprocess
from pathlib import Path
from .gem5_to_mcpat import run_conversion


def gen_dirs(target_dir: Path):
    stats_txt = target_dir / "stats.txt"
    stats_h5 = target_dir / "stats.h5"

    if stats_txt.exists():
        stats_file = stats_txt
    elif stats_h5.exists():
        stats_file = stats_h5
    else:
        raise FileNotFoundError(f"No stats.txt or stats.h5 found in {target_dir}")

    return {
        "current_dir": Path(__file__).resolve().parent,
        "base_path": target_dir,
        "stats_file": stats_file,
        "config_file": target_dir / "config.json",
        "mcpat_file": target_dir / "conv.xml",
    }


def run_mcpat(currentwd: Path, target: Path, mcpat_input: Path):
    mcpat_executable = currentwd.parent / "mcpat"
    mcpat_output = target / "mcpat_results.txt"

    command = [mcpat_executable, "-infile", mcpat_input.resolve(), "-print_level 1"]

    try:
        with open(mcpat_output, "w") as out_file:
            subprocess.run(command, check=True, stdout=out_file)
        print("McPAT run completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running McPAT: {e}")


def run(target_dir: Path|str):
    """
    Runs the gem5 to McPAT flow.

    [gem5_stats, gem5_config] -> mcpat-input.xml -> mcpat-results.txt

    The input directory must contain:
        ├── config.json
        └── stats.txt or stats.h5
    """
    if isinstance(target_dir, str):
        target_dir = Path(target_dir)

    d = gen_dirs(target_dir)

    print(f"Running McPAT conversion and analysis for: {d['base_path']}")

    run_conversion(
        stats_file=d["stats_file"],
        config_file=d["config_file"],
        outfile=d["mcpat_file"],
        template=None,
    )

    run_mcpat(
        currentwd=d["current_dir"],
        target=d["base_path"],
        mcpat_input=d["mcpat_file"],
    )
