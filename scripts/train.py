#!/usr/bin/env python3
"""Reserved public training entrypoint for SigLoMa-Code."""

import argparse
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Reserved training entrypoint for the future SigLoMa training stack."
    )
    parser.add_argument(
        "--config",
        default="configs/train.example.yaml",
        help="Path to the training config file.",
    )
    parser.add_argument(
        "--task",
        default=None,
        help="Optional task override for future training runs.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args, extra_args = parser.parse_known_args()
    config_path = Path(args.config)

    print("SigLoMa-Code training entrypoint placeholder")
    print("config: {0}".format(config_path))
    if args.task:
        print("task: {0}".format(args.task))
    if extra_args:
        print("extra_args: {0}".format(" ".join(extra_args)))
    print("Training code has not been migrated into this repository yet.")
    print("Keep this command shape stable and plug the real training pipeline in here later.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
