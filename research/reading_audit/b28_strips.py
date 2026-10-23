"""b28: cut a page into overlapping half-width strips (rotated) for reading.
    python b28_strips.py <img> <outprefix> x0 x1 y0 y1 [step] [h] [scale] [rot]"""
import sys
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS = None
a = sys.argv
im = Image.open(a[1]).convert('L')
x0, x1, y0, y1 = map(int, a[3:7]); step = int(a[7]) if len(a) > 7 else 370; h = int(a[8]) if len(a) > 8 else 420
sc = float(a[9]) if len(a) > 9 else 0.85; rot = int(a[10]) if len(a) > 10 else -90
if rot: im = im.rotate(rot, expand=True)
mid = (x0 + x1) // 2; i = 0; y = y0
while y < y1:
    for side, (u, v) in (('L', (x0, mid + 100)), ('R', (mid - 100, x1))):
        c = im.crop((u, y, v, y + h)); c = c.resize((int(c.width*sc), int(c.height*sc)), Image.LANCZOS)
        ImageOps.autocontrast(c, cutoff=1).save('%s%s_%02d.jpg' % (a[2], side, i), quality=88)
    i += 1; y += step
print(i, 'strips')
