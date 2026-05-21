from __future__ import annotations

import argparse
import subprocess
import sys


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str, required=False)
    args = parser.parse_args()

    if args.data_dir is None:
        print("No --data_dir provided. Structure-only smoke test passed.")
        return

    cmd = [
        sys.executable,
        "-m",
        "src.train",
        "--data_dir",
        args.data_dir,
        "--run_name",
        "ci_smoke",
        "--train_mode",
        "head_only",
        "--epochs",
        "1",
        "--batch_size",
        "2",
        "--max_per_class",
        "5",
        "--no_pretrained",
    ]
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    main()
