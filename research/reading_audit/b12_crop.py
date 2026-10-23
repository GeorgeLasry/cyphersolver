"""b12: crop a page image into horizontal strips (optionally a column box) for reading at native resolution.
usage: b12_crop.py <image> <outprefix> <nstrips> [x0 x1 y0 y1 as fractions] [maxw]"""
import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert('RGB')
W, H = im.size
n = int(sys.argv[3])
x0, x1, y0, y1 = (float(a) for a in sys.argv[4:8]) if len(sys.argv) > 7 else (0, 1, 0, 1)
maxw = int(sys.argv[8]) if len(sys.argv) > 8 else 1600
X0, X1, Y0, Y1 = int(x0 * W), int(x1 * W), int(y0 * H), int(y1 * H)
h = (Y1 - Y0) / n
for i in range(n):
    a = int(Y0 + i * h - (40 if i else 0)); b = int(min(Y1, Y0 + (i + 1) * h + 40))
    c = im.crop((X0, a, X1, b))
    if c.width > maxw:
        c = c.resize((maxw, int(c.height * maxw / c.width)))
    c.save('%s_%d.jpg' % (sys.argv[2], i + 1), quality=88)
    print('%s_%d.jpg' % (sys.argv[2], i + 1), c.size)
