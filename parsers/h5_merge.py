import h5py
from pathlib import Path
import sys

def merge_h5_files(input_files, output_file):
    with h5py.File(output_file, "w") as h5out:
        for i, file_path in enumerate(input_files):
            with h5py.File(file_path, "r") as h5in:
                grp = h5out.create_group(f"sample_{i}")
                for key in h5in:
                    h5in.copy(key, grp)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python merge.py output.h5 input1.h5 input2.h5 ...")
        sys.exit(1)

    out = Path(sys.argv[1])
    inputs = [Path(f) for f in sys.argv[2:]]
    merge_h5_files(inputs, out)
