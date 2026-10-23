"""b29: crop given text lines of a rotated R1954 page by centre y (list), each as 3 overlapping thirds at a scale.
    python b29_kd_line.py <rot.png> <outprefix> x0 x1 scale y1 [y2 ...]"""
import sys
from PIL import Image, ImageOps
a = sys.argv
im = Image.open(a[1]).convert('L')
x0, x1 = int(a[3]), int(a[4]); sc = float(a[5])
w = (x1 - x0) // 3
for y in map(int, a[6:]):
    for j in range(3):
        u = max(0, x0 + j * w - 80); v = min(im.width, x0 + (j + 1) * w + 80)
        c = im.crop((u, y - 70, v, y + 70)); c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
        ImageOps.autocontrast(c, cutoff=1).save('%s%d_%d.jpg' % (a[2], y, j), quality=85)
