"""b19: crop a region of an image (full-resolution pixel box) and save it enlarged for reading.
    python b19_crop.py <image> <x0> <y0> <x1> <y1> <out.jpg> [scale]"""
import sys
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
f, x0, y0, x1, y1, out = sys.argv[1:7]
sc = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
im = Image.open(f).crop((int(x0), int(y0), int(x1), int(y1)))
if sc != 1.0: im = im.resize((int(im.size[0] * sc), int(im.size[1] * sc)), Image.LANCZOS)
im.convert('L').save(out, quality=90)
print(out, im.size)
