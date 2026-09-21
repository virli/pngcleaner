"""Remove nearly transparent pixels from every PNG in the input directory."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


DEFAULT_ALPHA_THRESHOLD = 20


def clean_png(source: Path, destination: Path, alpha_threshold: int) -> None:
    """Set alpha values below *alpha_threshold* to fully transparent."""
    with Image.open(source) as image:
        # Convert palette, grayscale, and RGB images consistently to an alpha-capable
        # format before updating the alpha channel.
        rgba_image = image.convert("RGBA")
        alpha = rgba_image.getchannel("A")
        cleaned_alpha = alpha.point(
            lambda value: 0 if value < alpha_threshold else value
        )
        rgba_image.putalpha(cleaned_alpha)
        rgba_image.save(destination, "PNG")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Clean near-transparent pixels from PNG files."
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=DEFAULT_ALPHA_THRESHOLD,
        help=(
            "Alpha values below this value become 0 (default: "
            f"{DEFAULT_ALPHA_THRESHOLD}; valid range: 0-255)."
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not 0 <= args.threshold <= 255:
        raise SystemExit("--threshold must be between 0 and 255.")

    project_dir = Path(__file__).resolve().parent
    input_dir = project_dir / "input"
    output_dir = project_dir / "output"

    if not input_dir.is_dir():
        raise SystemExit(f"Input directory does not exist: {input_dir}")

    png_files = sorted(
        path for path in input_dir.iterdir() if path.is_file() and path.suffix.lower() == ".png"
    )
    if not png_files:
        print(f"No PNG files found in {input_dir}")
        return

    output_dir.mkdir(exist_ok=True)
    for source in png_files:
        destination = output_dir / source.name
        clean_png(source, destination, args.threshold)
        print(f"Cleaned: {source.name} -> {destination}")


if __name__ == "__main__":
    main()
