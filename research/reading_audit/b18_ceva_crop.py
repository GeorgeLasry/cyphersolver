"""b18 (ceva1632): cut a page image into overlapping horizontal strips (scaled) in the scratchpad.

    python research/reading_audit/b18_ceva_crop.py <image> <n_strips> [scale] [x0 x1]
"""
import sys, pathlib
from PIL import Image, ImageOps
OUT = pathlib.Path(r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\b18\ceva\strips')
OUT.mkdir(exist_ok=True)
im = ImageOps.autocontrast(Image.open(sys.argv[1]).convert('L'), cutoff=1)
n = int(sys.argv[2]); sc = float(sys.argv[3]) if len(sys.argv) > 3 else 0.6
W, H = im.size
x0, x1 = (int(sys.argv[4]), int(sys.argv[5])) if len(sys.argv) > 5 else (0, W)
h = H // n
stem = pathlib.Path(sys.argv[1]).stem
for i in range(n):
    c = im.crop((x0, max(0, i*h-60), x1, min(H, (i+1)*h+60)))
    c = c.resize((int(c.width*sc), int(c.height*sc)), Image.LANCZOS)
    f = OUT / f'{stem}_s{i}.jpg'; c.save(f, quality=88); print(f)
