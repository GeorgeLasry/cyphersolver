"""b32: crop a band of a rotated page image (y0..y1, x0..x1 in full-res pixels) and save it, optionally scaled.
    python b32_band.py <img> <out.jpg> <x0> <y0> <x1> <y1> [scale]"""
import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert('L')
x0, y0, x1, y1 = map(int, sys.argv[3:7]); sc = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
c = im.crop((x0, y0, x1, y1))
if sc != 1.0:
    c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
c.save(sys.argv[2], quality=92)
