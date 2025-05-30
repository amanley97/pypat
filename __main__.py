import argparse
from pathlib import Path
from pypat import run

def main():
    parser = argparse.ArgumentParser(description="Run gem5 to McPAT conversion and analysis.")
    parser.add_argument("target_dir", help="Path to the gem5 output directory. (Must contain stats.h5, config.json)")
    args = parser.parse_args()

    # RUN THE FLOW
    run(args.target_dir)


if __name__ == "__main__":
    main()
