"""b20: crop a page image into horizontal strips (optionally a sub-box) for reading at native resolution.
    python b20_crop.py <img> <outprefix> <y0> <y1> <nstrips> [x0 x1] [maxw]
"""
import sys
from PIL import Image
im = Image.open(sys.argv[1]); W, H = im.size
y0, y1, n = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
x0, x1 = (int(sys.argv[6]), int(sys.argv[7])) if len(sys.argv) > 7 else (0, W)
maxw = int(sys.argv[8]) if len(sys.argv) > 8 else 1600
step = (y1 - y0) / n
for i in range(n):
    a = int(y0 + i * step) - 20; b = int(y0 + (i + 1) * step) + 20
    c = im.crop((x0, max(0, a), x1, min(H, b)))
    if c.size[0] > maxw:
        c = c.resize((maxw, int(c.size[1] * maxw / c.size[0])))
    c.save('%s_%d.png' % (sys.argv[2], i + 1))
