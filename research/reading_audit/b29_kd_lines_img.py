"""b29: find text-line centres on a rotated R1954 page by row-ink profile and save each line as two half crops.
    python b29_kd_lines_img.py <rot.png> <outprefix> x0 x1 y0 y1 [scale] [minsep]"""
import sys
import numpy as np
from PIL import Image, ImageOps
a = sys.argv
im = Image.open(a[1]).convert('L')
x0, x1, y0, y1 = map(int, a[3:7]); sc = float(a[7]) if len(a) > 7 else 0.8; sep = int(a[8]) if len(a) > 8 else 110
g = np.asarray(im.crop((x0, y0, x1, y1)), dtype=np.float32)
ink = (g < g.mean() - 2.0 * g.std()).sum(1).astype(float)
k = np.ones(31) / 31; sm = np.convolve(ink, k, mode='same')
peaks = []
for i in np.argsort(-sm):
    if sm[i] < sm.max() * 0.25: break
    if all(abs(i - p) > sep for p in peaks): peaks.append(i)
peaks = sorted(peaks)
mid = (x0 + x1) // 2
for n, p in enumerate(peaks):
    yc = y0 + p
    for side, (u, v) in (('L', (x0, mid + 120)), ('R', (mid - 120, x1))):
        c = im.crop((u, yc - 75, v, yc + 70)); c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
        ImageOps.autocontrast(c, cutoff=1).save('%s%02d_%s.jpg' % (a[2], n, side), quality=85)
print(len(peaks), [int(y0 + p) for p in peaks])
