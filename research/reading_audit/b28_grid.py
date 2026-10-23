"""b28: cut a page into a grid of overlapping crops (rows of n lines, k columns) for reading.
    python b28_grid.py <img> <outprefix> x0 x1 y0 y1 step h cols scale"""
import sys
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS = None
a = sys.argv
im = Image.open(a[1]).convert('L')
x0, x1, y0, y1, step, h, cols = map(int, a[3:10]); sc = float(a[10])
w = (x1 - x0) // cols; i = 0; y = y0
while y < y1:
    for c in range(cols):
        u = max(0, x0 + c * w - 80); v = min(im.width, x0 + (c + 1) * w + 80)
        cr = im.crop((u, y, v, y + h)); cr = cr.resize((int(cr.width*sc), int(cr.height*sc)), Image.LANCZOS)
        ImageOps.autocontrast(cr, cutoff=1).save('%s%02d%s.jpg' % (a[2], i, 'abc'[c]), quality=88)
    i += 1; y += step
print(i, 'rows')
