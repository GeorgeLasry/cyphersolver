"""b31: crop a band of a full-resolution page image into horizontal pieces for reading.

    python b31_crop.py <image> <outprefix> <y0> <y1> [<x0> <x1> [<pieces> [<outwidth>]]]
"""
import sys
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
a = sys.argv
im = Image.open(a[1]); W, H = im.size
y0, y1 = int(a[3]), int(a[4])
x0 = int(a[5]) if len(a) > 5 else 0
x1 = int(a[6]) if len(a) > 6 else W
n = int(a[7]) if len(a) > 7 else 2
ow = int(a[8]) if len(a) > 8 else 1800
step = (x1 - x0) / n
for i in range(n):
    c = im.crop((int(x0 + i * step - (40 if i else 0)), y0, int(x0 + (i + 1) * step), y1))
    if c.size[0] > ow:
        c = c.resize((ow, int(c.size[1] * ow / c.size[0])), Image.LANCZOS)
    c.save('%s_%d.jpg' % (a[2], i), quality=88)
    print('%s_%d.jpg' % (a[2], i), c.size)
