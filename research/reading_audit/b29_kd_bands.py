"""b29: rotate a Kauderbach R1954 page (-90) and cut it into bands of n lines, left/right halves, for reading.
    python b29_kd_bands.py <img> <outprefix> x0 x1 y0 y1 nlines lines_per_band scale"""
import sys
from PIL import Image, ImageOps
a = sys.argv
im = Image.open(a[1]).convert('L').rotate(-90, expand=True)
x0, x1, y0, y1, n, per = map(int, a[3:9]); sc = float(a[9])
h = (y1 - y0) / n; mid = (x0 + x1) // 2
for k in range(0, n, per):
    ya = int(y0 + k * h - 0.25 * h); yb = int(y0 + (k + per) * h + 0.25 * h)
    for side, (u, v) in (('L', (x0, mid + 120)), ('R', (mid - 120, x1))):
        c = im.crop((u, ya, v, yb)); c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
        ImageOps.autocontrast(c, cutoff=1).save('%s%02d_%s.jpg' % (a[2], k, side), quality=85)
print(im.size, 'line height', h)
