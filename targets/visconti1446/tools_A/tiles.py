"""Cut a slip image into deskewed 2-line, one-third-width tiles.
usage: tiles.py <src> <prefix> x0 x1 [angle_deg] [y0 y1]"""
import sys, numpy as np
from PIL import Image
src, pre = sys.argv[1], sys.argv[2]
x0, x1 = int(sys.argv[3]), int(sys.argv[4])
ang = float(sys.argv[5]) if len(sys.argv) > 5 else 0.0
im = Image.open(src).convert('L')
if len(sys.argv) > 7:
    im = im.crop((0, int(sys.argv[6]), im.width, int(sys.argv[7])))
im = im.rotate(ang, resample=Image.BICUBIC, fillcolor=200)
a = np.array(im).astype(float)
d = (a[:, x0:x1] < 110).sum(1)
d = np.convolve(d, np.ones(21) / 21, 'same')
pk = [y for y in range(25, len(d) - 25) if d[y] == d[y - 25:y + 26].max() and d[y] > 0.25 * d.max()]
print('peaks', pk, 'diffs', np.diff(pk))
im.save(pre + '_desk.jpg')
w = (x1 - x0) / 3
for i in range(0, len(pk), 2):
    ya = pk[i] - 50
    yb = (pk[i + 1] if i + 1 < len(pk) else pk[i]) + 50
    for j in range(3):
        xa = int(x0 + j * w - 40); xb = int(x0 + (j + 1) * w + 40)
        t = im.crop((xa, ya, xb, yb))
        t = t.resize((int(t.width * 1.5), int(t.height * 1.5)), Image.LANCZOS)
        t.save(f'{pre}_L{i+1:02d}{"abc"[j]}.jpg')
