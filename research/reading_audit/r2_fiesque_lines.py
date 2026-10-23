"""r2_fiesque helper: split a native-resolution page crop into line strips (left/right halves, line found by ink profile
per half) and stack each line's halves into one image for viewing.
usage: python r2_fiesque_lines.py <crop.jpg> <outprefix> [lines e.g. 14-23] [scale]"""
import sys
from PIL import Image
import numpy as np
f, pre = sys.argv[1], sys.argv[2]
rng = sys.argv[3] if len(sys.argv) > 3 else None; sc = float(sys.argv[4]) if len(sys.argv) > 4 else 1.45
im = Image.open(f).convert('L'); A = np.array(im).astype(float); W = A.shape[1]; h = W // 2
halves = ((0, h + 50), (h - 50, W))
pks = []
for x0, x1 in halves:
    p = np.convolve((A[:, x0:x1] < 110).sum(1).astype(float), np.ones(15) / 15, 'same')
    pk = [i for i in range(50, len(p) - 51) if p[i] == p[i - 50:i + 51].max() and p[i] > 20]
    pks.append([y for j, y in enumerate(pk) if j == 0 or y - pk[j - 1] > 30])  # drop plateau duplicates
n = min(map(len, pks)); print('peaks a', pks[0]); print('peaks b', pks[1]); lo, hi = (map(int, rng.split('-')) if rng else (1, n))
for k in range(lo, hi + 1):
    parts = []
    for (x0, x1), pk in zip(halves, pks):
        y = pk[k - 1]; c = im.crop((x0, max(0, y - 85), x1, y + 75))
        parts.append(c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS))
    s = Image.new('L', (max(p.width for p in parts), sum(p.height for p in parts)), 255)
    yy = 0
    for p in parts: s.paste(p, (0, yy)); yy += p.height
    s.save(f'{pre}_{k:02d}.jpg')
    for tag, part in zip('ab', parts): part.save(f'{pre}_{k:02d}{tag}.jpg')
print(n, 'lines')
