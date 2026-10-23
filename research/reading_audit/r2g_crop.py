"""r2g: crop a region of an image into strips for reading. usage: r2g_crop.py IMG x0 y0 x1 y1 rows OUTPREFIX [scale]"""
import sys
from PIL import Image
f, x0, y0, x1, y1, rows, out = sys.argv[1], *map(int, sys.argv[2:7]), sys.argv[7]
sc = float(sys.argv[8]) if len(sys.argv) > 8 else 1.0
im = Image.open(f)
h = (y1 - y0) / rows
for r in range(rows):
    c = im.crop((x0, int(y0 + r * h) - 20, x1, int(y0 + (r + 1) * h) + 20))
    if sc != 1.0: c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
    c.save('%s_%d.png' % (out, r))
