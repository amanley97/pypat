import argparse
import h5py
import math


def flatten_h5(group, prefix=""):
    result = {}
    for key, item in group.items():
        path = f"{prefix}.{key}" if prefix else key
        if isinstance(item, h5py.Group):
            result.update(flatten_h5(item, path))
        elif isinstance(item, h5py.Dataset):
            try:
                value = item[()]
                if hasattr(value, "shape") and value.shape != ():  # not scalar
                    flat_value = value.flatten()
                    flat_value = [
                        (
                            float(x)
                            if not (isinstance(x, float) and math.isnan(x))
                            else "nan"
                        )
                        for x in flat_value
                    ]
                    result[path] = flat_value
                else:
                    result[path] = float(value) if not math.isnan(value) else "nan"
            except Exception:
                result[path] = str(item[()])
    return result


def search(stats, term, search_values=False):
    matches = {}
    for k, v in stats.items():
        if search_values:
            if term.lower() in str(v).lower():
                matches[k] = v
        else:
            if term.lower() in k.lower():
                matches[k] = v
    return matches


def main():
    parser = argparse.ArgumentParser(description="Search gem5 HDF5 stats file.")
    parser.add_argument("stats_file", help="Path to HDF5 stats file")
    parser.add_argument("query", help="Search query (key or value substring)")
    parser.add_argument(
        "-v", "--values", action="store_true", help="Search in values instead of keys"
    )

    args = parser.parse_args()

    with h5py.File(args.stats_file, "r") as f:
        flat_stats = flatten_h5(f)
        results = search(flat_stats, args.query, args.values)

    if results:
        for k, v in sorted(results.items()):
            print(f"{k}: {v}")
    else:
        print("No matches found.")


if __name__ == "__main__":
    main()
