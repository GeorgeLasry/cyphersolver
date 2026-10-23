"""Crop a band of a kurtz1639 DECODE image for checking figures (batch b06; copied for r2c, 23 Oct 2026).

    python research/reading_audit/b06_crop.py <image-stem> <side: L|R|F> <y0 frac> <y1 frac> [out-name] [x0 x1 fracs]
Images are read from the main checkout's git-ignored img/ folder; crops go to the session scratchpad only.
"""
import sys, os
from PIL import Image
IMG = r'C:/Users/dbour/cypher/targets/kurtz1639/img'
OUT = r'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/6b6912a8-0ad3-4eda-b63e-c79291f1bcc5/scratchpad/reread/r2c'
stem, side, y0, y1 = sys.argv[1], sys.argv[2].upper(), float(sys.argv[3]), float(sys.argv[4])
name = sys.argv[5] if len(sys.argv) > 5 else 'c.jpg'
im = Image.open(os.path.join(IMG, stem + '.jpg')); w, h = im.size
x0, x1 = {'L': (0, w // 2), 'R': (w // 2, w), 'F': (0, w)}[side]
if len(sys.argv) > 7:
    a, b = float(sys.argv[6]), float(sys.argv[7]); x0, x1 = x0 + int((x1 - x0) * a), x0 + int((x1 - x0) * b)
c = im.crop((x0, int(h * y0), x1, int(h * y1)))
if c.width > 1800: c = c.resize((1800, int(c.height * 1800 / c.width)))
os.makedirs(OUT, exist_ok=True); c.save(os.path.join(OUT, name), quality=90)
print(os.path.join(OUT, name), c.size)
