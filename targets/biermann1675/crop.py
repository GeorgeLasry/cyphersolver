"""crop.py <img> <x0> <y0> <x1> <y1> <out> [width]: crop by fractions of the image size, resize to width."""
import sys
from PIL import Image

src, x0, y0, x1, y1, out = sys.argv[1], *map(float, sys.argv[2:6]), sys.argv[6]
W = int(sys.argv[7]) if len(sys.argv) > 7 else 1800
im = Image.open(src).convert('L')
w, h = im.size
c = im.crop((int(w * x0), int(h * y0), int(w * x1), int(h * y1)))
c.resize((W, int(c.height * W / c.width))).save(out, quality=85)
