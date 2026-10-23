"""b09: cut a page image into horizontal strips (optionally a sub-box) for reading at native resolution.
usage: python b09_crop.py <image> <outprefix> <y0> <y1> <step> [x0 x1] [scale]"""
import sys
from PIL import Image, ImageOps
im = Image.open(sys.argv[1]).convert('RGB')
y0, y1, step = map(int, sys.argv[3:6])
x0, x1 = (int(sys.argv[6]), int(sys.argv[7])) if len(sys.argv) > 7 else (0, im.size[0])
sc = float(sys.argv[8]) if len(sys.argv) > 8 else 1.0
k = 0
for y in range(y0, y1, step):
    c = im.crop((x0, y, x1, min(y + step + 40, y1 + 40)))
    if sc != 1.0:
        c = c.resize((int(c.size[0] * sc), int(c.size[1] * sc)), Image.LANCZOS)
    c = ImageOps.autocontrast(c, cutoff=1)
    c.save('%s_%02d.jpg' % (sys.argv[2], k), quality=88); k += 1
print(k)
