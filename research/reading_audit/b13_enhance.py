"""b13: enhance a faded page region (blur background minus image, autocontrast) into the scratchpad.
usage: b13_enhance.py <image> <out.jpg> x0 x1 y0 y1 [scale] [blur]"""
import sys
from PIL import Image, ImageFilter, ImageOps, ImageChops
im = Image.open(sys.argv[1]).convert('L')
W, H = im.size
x0, x1, y0, y1 = (float(a) for a in sys.argv[3:7])
sc = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
bl = float(sys.argv[8]) if len(sys.argv) > 8 else 20
c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
bg = c.filter(ImageFilter.GaussianBlur(bl))
d = ImageChops.subtract(bg, c)
d = ImageOps.autocontrast(d, cutoff=0.5)
d = ImageOps.invert(d)
if sc != 1.0:
    d = d.resize((int(d.width * sc), int(d.height * sc)), Image.LANCZOS)
d.save(sys.argv[2], quality=90)
print(sys.argv[2], d.size)
