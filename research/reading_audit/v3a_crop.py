"""v3 verify (a): crop a band of an image into n horizontal pieces, contrast-stretched, saved to the scratchpad.

    python research/reading_audit/v3a_crop.py <image> <y0> <y1> <x0> <x1> <pieces> <name> [scale]
"""
import sys
from PIL import Image, ImageOps
OUT = r'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/6b6912a8-0ad3-4eda-b63e-c79291f1bcc5/scratchpad/reread/v3/'
f, y0, y1, x0, x1, n, name = sys.argv[1], *map(int, sys.argv[2:7]), sys.argv[7]
sc = float(sys.argv[8]) if len(sys.argv) > 8 else 1.0
im = ImageOps.autocontrast(Image.open(f).convert('L'), cutoff=1)
w = (x1 - x0) // n
for i in range(n):
    c = im.crop((x0 + i * w - (20 if i else 0), y0, x0 + (i + 1) * w + 20, y1))
    if sc != 1: c = c.resize((int(c.width * sc), int(c.height * sc)))
    c.save(OUT + f'{name}_{i}.png'); print(OUT + f'{name}_{i}.png')
