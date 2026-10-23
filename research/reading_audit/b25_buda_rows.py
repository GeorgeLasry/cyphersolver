"""b25: horizontal ink profile of a plate to locate text-line baselines.
    python b25_buda_rows.py <img> x0 x1 y0 y1   -> prints row centres (ink minima of brightness)"""
import sys
import numpy as np
from PIL import Image
im = np.asarray(Image.open(sys.argv[1]).convert('L')).astype(float)
x0, x1, y0, y1 = map(int, sys.argv[2:6])
reg = im[y0:y1, x0:x1]
ink = (reg < np.percentile(reg, 12)).sum(1).astype(float)
k = np.ones(9) / 9; s = np.convolve(ink, k, 'same')
peaks = [i for i in range(5, len(s) - 5) if s[i] == s[max(0,i-12):i+13].max() and s[i] > s.mean() * 0.6]
out = []
for p in peaks:
    if not out or p - out[-1] > 25: out.append(p)
for n, p in enumerate(out, 1): print(n, y0 + p, int(s[p]))
