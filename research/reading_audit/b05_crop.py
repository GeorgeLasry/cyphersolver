"""b05: crop a DECODE page image of the Schenck letters into the scratchpad.

    python b05_crop.py <rec> <page> <x0> <y0> <x1> <y1> [width]   (fractions 0-1 of the page; output width, default 1500)
"""
import sys, os, glob
from PIL import Image
D = r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\schenck'
rec, page = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(float, sys.argv[3:7])
w = int(sys.argv[7]) if len(sys.argv) > 7 else 1500
f = glob.glob(os.path.join(D, 'IMG_R%s_*_P%s.jpg' % (rec, page)))[0]
im = Image.open(f)
W, H = im.size
c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
if c.size[0] != w: c = c.resize((w, int(c.size[1] * w / c.size[0])), Image.LANCZOS)
o = os.path.join(D, 'c', 'R%s_P%s_%d_%d_%d_%d.jpg' % (rec, page, x0 * 100, y0 * 100, x1 * 100, y1 * 100))
c.save(o, quality=88)
print(o)
