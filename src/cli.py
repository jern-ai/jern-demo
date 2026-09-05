"""Command-line interface for temperature conversions.

Usage:
    python3 -m src.cli <value> <from> <to>
    python3 src/cli.py <value> <from> <to>
"""

import argparse
import sys

from conversions import get_converter


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser for the temperature CLI.

    Returns:
        An :class:`argparse.ArgumentParser` expecting a value, a source
        scale, and a target scale.
    """
    parser = argparse.ArgumentParser(
        prog="temperature",
        description="Convert a temperature between scales.",
    )
    parser.add_argument("value", type=float, help="temperature value to convert")
    parser.add_argument("from_scale", metavar="from", help="scale to convert from")
    parser.add_argument("to_scale", metavar="to", help="scale to convert to")
    return parser


def main(argv=None) -> int:
    """Run the temperature CLI.

    Args:
        argv: Optional argument list (defaults to ``sys.argv[1:]``).

    Returns:
        The process exit code (0 on success, 1 on an unknown scale).
    """
    args = build_parser().parse_args(argv)
    try:
        converter = get_converter(args.from_scale, args.to_scale)
    except KeyError:
        sys.stderr.write(
            f"error: no conversion from {args.from_scale!r} to {args.to_scale!r}\n"
        )
        return 1
    print(converter(args.value))
    return 0


if __name__ == "__main__":
    sys.exit(main())
