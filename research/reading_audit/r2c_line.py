"""r2c (23 Oct 2026): crop transcription line i of n on one side of a kurtz1639 image, by ink-band segmentation.
    python research/reading_audit/r2c_line.py <stem> <L|R|F> <i> <n> [out] [ctx lines]"""
import sys, os
import numpy as np
from PIL import Image
IMG = r'C:/Users/dbour/cypher/targets/kurtz1639/img'
OUT = r'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/6b6912a8-0ad3-4eda-b63e-c79291f1bcc5/scratchpad/reread/r2c'
stem, side, i, n = sys.argv[1], sys.argv[2].upper(), int(sys.argv[3]), int(sys.argv[4])
out = sys.argv[5] if len(sys.argv) > 5 else 'line.jpg'; ctx = int(sys.argv[6]) if len(sys.argv) > 6 else 1
im = Image.open(os.path.join(IMG, stem + '.jpg')).convert('L'); w, h = im.size
x0, x1 = {'L': (0, w // 2), 'R': (w // 2, w), 'F': (0, w)}[side]
a = np.asarray(im.crop((x0, 0, x1, h)), dtype=float)
a = a[:, int(a.shape[1] * .08):int(a.shape[1] * .95)]
ink = (a < a.mean() - 45).sum(1).astype(float)
k = int(os.environ.get("K", 9)); sm = np.convolve(ink, np.ones(k) / k, 'same')
thr = max(sm.max() * float(os.environ.get("T", .2)), 3)
bands, on = [], None
for y, v in enumerate(sm):
    if v > thr and on is None: on = y
    if v <= thr and on is not None:
        if y - on > 15: bands.append((on, y))
        on = None
# merge tiny gaps
m = []
for b in bands:
    if m and b[0] - m[-1][1] < 12: m[-1] = (m[-1][0], b[1])
    else: m.append(b)
j = min(len(m) - 1, max(0, round((i - 1) * len(m) / n)))
j0, j1 = max(0, j - ctx), min(len(m) - 1, j + ctx)
y0, y1 = max(0, m[j0][0] - 20), min(h, m[j1][1] + 20)
c = Image.open(os.path.join(IMG, stem + '.jpg')).crop((x0, y0, x1, y1))
if c.width > 1800: c = c.resize((1800, int(c.height * 1800 / c.width)))
c.save(os.path.join(OUT, out), quality=90)
print(out, 'bands', len(m), 'for', n, 'lines; picked', j + 1, (y0, y1))
