import argparse
from pathlib import Path
from pypat import run_pypat


def main():
    parser = argparse.ArgumentParser(
        description="Run gem5 to McPAT conversion and analysis."
    )
    parser.add_argument(
        "target_dir",
        type=Path,
        help="Path to the gem5 output directory. (Must contain stats.txt (or stats.h5), config.json)",
    )
    args = parser.parse_args()

    # RUN THE FLOW
    run_pypat(args.target_dir)


if __name__ == "__main__":
    main()
