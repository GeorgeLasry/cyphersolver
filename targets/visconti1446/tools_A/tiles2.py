"""Deskew by projection variance, find line centres, cut 2-line third-width tiles.
usage: tiles2.py src prefix x0 x1 nlines [y0 y1]"""
import sys, numpy as np
from PIL import Image
src, pre = sys.argv[1], sys.argv[2]; x0, x1, n = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
im0 = Image.open(src).convert('L')
best = None
import os
angs=[float(os.environ['ANG'])] if os.environ.get('ANG') else np.arange(-1.5, 1.51, 0.05)
for ang in angs:
    a = np.array(im0.rotate(ang, resample=Image.BILINEAR, fillcolor=200))[:, x0:x1] < 110
    p = a.sum(1).astype(float); v = p.var()
    if best is None or v > best[0]: best = (v, ang, p)
_, ang, p = best
im = im0.rotate(ang, resample=Image.BICUBIC, fillcolor=200)
ps = np.convolve(p, np.ones(9) / 9, 'same')
# greedy: pick n highest peaks at least 45 px apart
order = np.argsort(-ps); pk = []
for y in order:
    if all(abs(y - q) > 45 for q in pk): pk.append(int(y))
    if len(pk) == n: break
pk.sort()
import os
if os.environ.get('PEAKS'): pk=[int(x) for x in os.environ['PEAKS'].split(',')]
print('angle', round(float(ang), 2), 'peaks', pk, 'diffs', list(np.diff(pk)))
im.save(pre + '_desk.jpg')
open(pre + '_peaks.txt', 'w').write(' '.join(map(str, pk)))
NP=int(os.environ.get('NPIECE','3')); w = (x1 - x0) / NP
for i in range(0, len(pk), 2):
    ya = pk[i] - 50; yb = (pk[i + 1] if i + 1 < len(pk) else pk[i]) + 50
    for j in range(NP):
        xa = int(x0 + j * w - 40); xb = int(x0 + (j + 1) * w + 40)
        t = im.crop((xa, ya, xb, yb)); t = t.resize((int(t.width * 1.5), int(t.height * 1.5)), Image.LANCZOS)
        t.save(f'{pre}_L{i+1:02d}{"abcdef"[j]}.jpg')
