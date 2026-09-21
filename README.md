# pngcleaner

`pngcleaner` is a command-line tool for cleaning transparent 2D PNG images.

It is intended for sprites, icons, game assets, and other images that use an
alpha channel. The cleaner removes unwanted stray colour from transparent or
partially transparent pixels and normalizes uneven colour around an image's
edges. This helps avoid visible halos, colour specks, and inconsistent borders
when the PNG is composited over different backgrounds.

## What it cleans

- Stray RGB colour left in fully transparent pixels
- Unexpected colour fringing around transparent edges
- Uneven or inconsistent edge colour in 2D PNG artwork

## Usage

The project runs from the command line. It accepts a transparent PNG as input,
processes its pixel data, and writes a cleaned PNG as output.

```text
pngcleaner <input.png> <output.png>
```

Keep the original image and write the cleaned result to a separate output path
so the result can be reviewed before replacing an asset.
