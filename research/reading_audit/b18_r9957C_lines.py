"""b18 fork C: find written lines of an R9957 page (row ink profile) between two heights and cut each line into two
halves at a scale (scratchpad reread/b18/C/<page>_L<nn><a|b>.jpg).
    python research/reading_audit/b18_r9957C_lines.py <page> y0 y1 [scale]
"""
import sys, pathlib
import numpy as np
from PIL import Image, ImageOps
OUT = pathlib.Path(r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\b18\C')
pg = sys.argv[1]; y0f, y1f = float(sys.argv[2]), float(sys.argv[3]); sc = float(sys.argv[4]) if len(sys.argv) > 4 else 1.6
im = Image.open(rf'C:\Users\dbour\cypher\targets\charles1536\img\r9957_p{pg}.jpg').convert('L'); W, H = im.size
a = np.asarray(im).astype(float)
x0, x1 = int(0.08*W), int(0.97*W)
band = a[int(y0f*H):int(y1f*H), x0:x1]
ink = (band < 110).sum(1)
k = 9; sm = np.convolve(ink, np.ones(k)/k, 'same')
thr = max(4, sm.max()*0.15)
rows = []; on = False
for i, v in enumerate(sm):
    if v > thr and not on: s = i; on = True
    if v <= thr and on:
        if i - s > 12: rows.append((s, i))
        on = False
mids = [ (s+e)//2 + int(y0f*H) for s, e in rows ]
gap = int(np.median(np.diff(mids))) if len(mids) > 1 else 60
for n, m in enumerate(mids):
    top, bot = m - int(gap*0.75), m + int(gap*0.6)
    for half, (xa, xb) in (('a', (x0, int(0.55*W))), ('b', (int(0.50*W), x1))):
        c = ImageOps.autocontrast(im.crop((xa, top, xb, bot)), cutoff=1)
        c = c.resize((int(c.width*sc), int(c.height*sc)), Image.LANCZOS)
        c.save(OUT / f'p{pg}_L{n:02d}{half}.jpg', quality=92)
    print(n, m, round(m/H, 3))
