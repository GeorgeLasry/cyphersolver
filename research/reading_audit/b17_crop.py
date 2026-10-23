"""b17: cut horizontal strips from a page image (fractions of height), optionally enhanced, for reading at native resolution.

    python research/reading_audit/b17_crop.py <image> <outprefix> <y0> <y1> [<x0> <x1>] [--n K] [--w W]
y and x are fractions of the image (0-1); the band is cut into K strips of equal height, each resized to width W (default 1600).
"""
import sys
from PIL import Image, ImageOps
a = [x for x in sys.argv[1:] if not x.startswith('--')]
opt = dict(zip(sys.argv[1:], sys.argv[2:]))
n = int(opt.get('--n', 1)); W = int(opt.get('--w', 1600))
im = Image.open(a[0]).convert('L')
X, Y = im.size
y0, y1 = float(a[2]), float(a[3])
x0, x1 = (float(a[4]), float(a[5])) if len(a) > 5 else (0.0, 1.0)
h = (y1 - y0) / n
for k in range(n):
    c = im.crop((int(x0 * X), int((y0 + k * h) * Y), int(x1 * X), int((y0 + (k + 1) * h) * Y)))
    c = ImageOps.autocontrast(c, cutoff=1)
    if c.size[0] != W: c = c.resize((W, int(c.size[1] * W / c.size[0])), Image.LANCZOS)
    c.save('%s_%d.jpg' % (a[1], k), quality=90)
    print('%s_%d.jpg' % (a[1], k), c.size)
