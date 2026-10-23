"""b18 caprile: find text-line centres in a region by ink projection and cut each line into strips (scratchpad).

    python research/reading_audit/b18_caprile_lines.py <image> <x0> <y0> <x1> <y1> <prefix> [parts] [scale]   (env CENTRES=y1,y2,... overrides the detected line centres)
"""
import sys, pathlib, os
import numpy as np
from PIL import Image, ImageOps
OUT = pathlib.Path(r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\b18\caprile')
img, x0, y0, x1, y1, pre = sys.argv[1], *map(int, sys.argv[2:6]), sys.argv[6]
parts = int(sys.argv[7]) if len(sys.argv) > 7 else 2
sc = float(sys.argv[8]) if len(sys.argv) > 8 else 1.0
im = ImageOps.autocontrast(Image.open(img).convert('L'), cutoff=float(os.environ.get('CUTOFF', '0')))
a = np.asarray(im.crop((x0, y0, x1, y1)), dtype=float)
ink = (a < 110).sum(1)
k = np.convolve(ink, np.ones(15) / 15, 'same')
peaks = [i for i in range(10, len(k) - 10) if k[i] == k[max(0, i - 25):i + 26].max() and k[i] > 0.25 * k.max()]
import os
if os.environ.get('CENTRES'): peaks = [int(v) - y0 for v in os.environ['CENTRES'].split(',')]
print('line centres', [y0 + p for p in peaks])
w = (x1 - x0) // parts
for li, p in enumerate(peaks):
    for j in range(parts):
        c = im.crop((x0 + j * w - 30, y0 + p - 65, x0 + (j + 1) * w + 30, y0 + p + 65))
        if sc != 1: c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
        c.save(OUT / f'{pre}_L{li+1:02d}_{j}.png')
