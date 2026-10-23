"""b36: crop a region of a scratchpad image at native resolution (or scaled), for reading margins and cipher lines.

    python b36_crop.py <image> <out.jpg> x0 y0 x1 y1 [scale] [rot]
"""
import sys
from PIL import Image
a = sys.argv
im = Image.open(a[1]).convert('RGB')
c = im.crop(tuple(int(v) for v in a[3:7]))
s = float(a[7]) if len(a) > 7 else 1.0
if s != 1.0: c = c.resize((int(c.size[0] * s), int(c.size[1] * s)), Image.LANCZOS)
if len(a) > 8: c = c.rotate(int(a[8]), expand=True)
c.save(a[2], quality=92)
print(c.size)
