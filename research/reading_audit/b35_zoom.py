"""b35: rotate a page image and save one zoomed crop (scratchpad only).

    python b35_zoom.py <image> <rotate_degrees> x0 y0 x1 y1 <scale> <out>
"""
import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert('RGB')
rot = int(sys.argv[2])
if rot: im = im.rotate(rot, expand=True)
x0, y0, x1, y1 = map(int, sys.argv[3:7]); s = float(sys.argv[7])
c = im.crop((x0, y0, x1, y1)); c = c.resize((int(c.size[0] * s), int(c.size[1] * s)), Image.LANCZOS)
c.save(sys.argv[8], quality=92); print(c.size)
