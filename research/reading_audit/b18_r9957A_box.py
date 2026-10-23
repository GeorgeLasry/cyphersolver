"""b18 fork A: crop a box (fractions) of an R9957 image, autocontrast, scale, into scratchpad reread/b18/A.
    python research/reading_audit/b18_r9957A_box.py <pN> <name> x0 y0 x1 y1 [scale]
"""
import sys, pathlib
from PIL import Image, ImageOps
OUT = pathlib.Path(r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\b18\A')
im = Image.open(rf'C:\Users\dbour\cypher\targets\charles1536\img\r9957_{sys.argv[1]}.jpg').convert('L'); W, H = im.size
x0, y0, x1, y1 = [float(v) for v in sys.argv[3:7]]; sc = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
c = ImageOps.autocontrast(im.crop((int(x0*W), int(y0*H), int(x1*W), int(y1*H))), cutoff=1)
if sc != 1: c = c.resize((int(c.width*sc), int(c.height*sc)), Image.LANCZOS)
f = OUT / f'{sys.argv[2]}.jpg'; c.save(f, quality=92); print(f, c.size)
