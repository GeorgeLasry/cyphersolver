"""b28: crop + scale a region of an image into the scratchpad (optional rotation first).
    python b28_crop.py <img> <out> x0 y0 x1 y1 [scale] [rot]
    x0..y1 are in the rotated frame; rot in degrees counter-clockwise (PIL), e.g. -90 or 90; scale may be <1."""
import sys
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS = None
im = Image.open(sys.argv[1]).convert('L')
rot = int(sys.argv[8]) if len(sys.argv) > 8 else 0
if rot: im = im.rotate(rot, expand=True)
x0, y0, x1, y1 = map(int, sys.argv[3:7]); sc = float(sys.argv[7]) if len(sys.argv) > 7 else 2
if x1 <= 0: x1 = im.width
if y1 <= 0: y1 = im.height
c = im.crop((x0, y0, x1, y1)); c = c.resize((max(1, int(c.width*sc)), max(1, int(c.height*sc))), Image.LANCZOS)
ImageOps.autocontrast(c, cutoff=1).save(sys.argv[2], quality=90)
print(im.size, c.size)
