"""b29: cut a page into overlapping half-width bands of a few written lines for reading.
    python b29_strips.py <img> <outprefix> x0 x1 y0 y1 band_h step scale
Writes <outprefix>NN_L.jpg / NN_R.jpg (left/right halves, 150 px overlap), autocontrast, greyscale."""
import sys
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS = None
a = sys.argv
im = Image.open(a[1]).convert('L')
x0, x1, y0, y1, bh, st = map(int, a[3:9]); sc = float(a[9])
mid = (x0 + x1) // 2; i = 0; y = y0
while y < y1:
    for side, (u, v) in (('L', (x0, mid + 150)), ('R', (mid - 150, x1))):
        c = im.crop((u, y, v, min(y + bh, im.height))); c = c.resize((int(c.width*sc), int(c.height*sc)), Image.LANCZOS)
        ImageOps.autocontrast(c, cutoff=1).save('%s%02d_%s.jpg' % (a[2], i, side), quality=85)
    i += 1; y += st
print(i, 'bands')
