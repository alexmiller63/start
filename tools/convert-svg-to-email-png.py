#!/usr/bin/env python3

import argparse
from pathlib import Path

import cairosvg


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("svgs", nargs="+", type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--display-size", type=int, default=13)
    parser.add_argument("--scale", type=int, default=4)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_size = args.display_size * args.scale

    for source in args.svgs:
        if source.suffix.lower() != ".svg":
            raise SystemExit(f"Not an SVG: {source}")
        destination = args.output_dir / f"{source.stem}-email.png"
        if destination.exists() and not args.overwrite:
            print(f"Skipping existing: {destination}")
            continue
        print(f"Converting {source} -> {destination}")
        cairosvg.svg2png(
            url=str(source),
            write_to=str(destination),
            output_width=output_size,
            output_height=output_size,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
