"""b28: crop one text line (centre y, +-half) into k pieces at a scale. python b28_line.py <img> <outprefix> y [k] [scale] [half] [x0] [x1]"""
import sys
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS = None
a = sys.argv; im = Image.open(a[1]).convert('L'); y = int(a[3])
k = int(a[4]) if len(a) > 4 else 3; sc = float(a[5]) if len(a) > 5 else 0.85; hf = int(a[6]) if len(a) > 6 else 60
x0 = int(a[7]) if len(a) > 7 else 950; x1 = int(a[8]) if len(a) > 8 else 6750
w = (x1 - x0) // k
for i in range(k):
    c = im.crop((max(0, x0 + i*w - 60), y - hf, min(im.width, x0 + (i+1)*w + 60), y + hf))
    c = c.resize((int(c.width*sc), int(c.height*sc)), Image.LANCZOS)
    ImageOps.autocontrast(c, cutoff=1).save('%s%d.jpg' % (a[2], i), quality=90)
