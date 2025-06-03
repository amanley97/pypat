import subprocess
from pathlib import Path
from conversion.gem5_to_mcpat import run_conversion

def gen_dirs(target_dir: str):
    return {
        "current_dir": Path(__file__).resolve().parent,
        "base_path": Path(target_dir),
        "stats_file": Path(target_dir)/"stats.h5",
        "config_file": Path(target_dir)/"config.json",
        "mcpat_file": Path(target_dir)/"mcpat_conv.xml"
    }
    

def run_mcpat(currentwd: Path, target: Path, mcpat_input: Path):
    mcpat_executable = currentwd / "mcpat"
    mcpat_output = target / "mcpat_results.txt"

    command = [mcpat_executable, "-infile", mcpat_input, "-print_level 1"]

    try:
        with open(mcpat_output, "w") as out_file:
            subprocess.run(command, check=True, stdout=out_file)
        print("McPAT run completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running McPAT: {e}")

def run(target_dir: str):
    """
    Runs the gem5 to mcpat flow.

    [gem5_stats, gem5_config] -> mcpat-input.xml -> mcpat-results.txt

    Note the input file must contain the following:
        target_dir
        ├── config.json
        └── stats.h5
    """
    d = gen_dirs(target_dir)

    print(f"Running McPAT conversion and analysis for: {d["base_path"]}")

    run_conversion(
        stats_file=d["stats_file"],
        config_file=d["config_file"],
        outfile=d["mcpat_file"]
    )

    run_mcpat(
        currentwd=d["current_dir"], 
        target=d["base_path"],
        mcpat_input=d["mcpat_file"]
    )