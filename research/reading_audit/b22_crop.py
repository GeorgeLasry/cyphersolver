"""b22: cut a page image into horizontal strips (with overlap) for reading the interlinear decipherment.

    python research/reading_audit/b22_crop.py <image> <outprefix> <y0> <y1> <step> [<x0> <x1> <width>]
"""
import sys
from PIL import Image
im = Image.open(sys.argv[1])
pre = sys.argv[2]; y0, y1, step = map(int, sys.argv[3:6])
x0 = int(sys.argv[6]) if len(sys.argv) > 6 else 0
x1 = int(sys.argv[7]) if len(sys.argv) > 7 else im.size[0]
W = int(sys.argv[8]) if len(sys.argv) > 8 else 1800
k = 0; y = y0
while y < y1:
    c = im.crop((x0, y, x1, min(y + step + step // 5, im.size[1])))
    if c.size[0] > W: c = c.resize((W, int(c.size[1] * W / c.size[0])))
    c.save('%s_%02d.jpg' % (pre, k), quality=88); print('%s_%02d.jpg' % (pre, k), y)
    k += 1; y += step
