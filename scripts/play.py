#!/usr/bin/env python3
"""Reserved public play entrypoint for SigLoMa-Code."""

import argparse
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Reserved play entrypoint for the future SigLoMa training stack."
    )
    parser.add_argument(
        "--config",
        default="configs/play.example.yaml",
        help="Path to the play or evaluation config file.",
    )
    parser.add_argument(
        "--checkpoint",
        default=None,
        help="Optional checkpoint override for future play runs.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args, extra_args = parser.parse_known_args()
    config_path = Path(args.config)

    print("SigLoMa-Code play entrypoint placeholder")
    print("config: {0}".format(config_path))
    if args.checkpoint:
        print("checkpoint: {0}".format(args.checkpoint))
    if extra_args:
        print("extra_args: {0}".format(" ".join(extra_args)))
    print("Play or evaluation code has not been migrated into this repository yet.")
    print("Keep this command shape stable and plug the real inference or evaluation pipeline in here later.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
