"""r2l: line centres of f. 373r/v (Gallica views 422/423, full size) by ink profile, and line crops for reading.
    python r2l_lines373.py rows <view> <x0> <x1> <y0> <y1>
    python r2l_lines373.py crop <view> <name> <yc> <x0> <x1> [half] [scale]"""
import sys
import numpy as np
from PIL import Image, ImageOps
M = 'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/6b6912a8-0ad3-4eda-b63e-c79291f1bcc5/scratchpad/reread/r2l/maisse/'
cmd, view = sys.argv[1], sys.argv[2]
im = Image.open(M + f'v{view}.jpg' if 'r' not in view else M + f'v{view}.jpg').convert('L')
if cmd == 'rows':
    x0, x1, y0, y1 = map(int, sys.argv[3:7])
    a = 255 - np.asarray(im.crop((x0, y0, x1, y1)), dtype=np.float32)
    p = np.convolve(a.mean(1), np.ones(25) / 25, 'same')
    pk = [i for i in range(30, len(p) - 30) if p[i] == p[i - 30:i + 31].max() and p[i] > p.mean() * 0.8]
    print(len(pk), [y0 + i for i in pk])
else:
    name, yc, x0, x1 = sys.argv[3], *map(int, sys.argv[4:7])
    hh = int(sys.argv[7]) if len(sys.argv) > 7 else 70
    sc = float(sys.argv[8]) if len(sys.argv) > 8 else 0.8
    c = im.crop((x0, yc - hh, x1, yc + hh)); c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
    ImageOps.autocontrast(c, cutoff=1).save(M + name + '.png')
