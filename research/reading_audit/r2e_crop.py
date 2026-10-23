"""r2e (23 Oct 2026): buda1489 V2831 per-row crops from the rotated plates (img/v2831_p<k>r.jpg, 3240x4320).
    python r2e_crop.py rows <page> X0 X1 Y0 Y1           -> row centres per x-block (rows_p<page>.json)
    python r2e_crop.py crop <page> <line> [n] [scale] [hh] [dy]
Crops go to the session scratchpad (reread/r2e/). Images are not public domain; never into the repository.
"""
import sys, json
import numpy as np
from PIL import Image, ImageOps
IMG = r'C:\Users\dbour\cypher\targets\buda1489\img\v2831_p{}r.jpg'
OUT = r'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/6b6912a8-0ad3-4eda-b63e-c79291f1bcc5/scratchpad/reread/r2e/'
B = 6


def rows(pg, X0, X1, Y0, Y1):
    a = np.asarray(Image.open(IMG.format(pg)).convert('L'), dtype=np.float32)
    w = (X1 - X0) // B
    res = []
    for b in range(B):
        prof = (255 - a[Y0:Y1, X0 + b * w:X0 + (b + 1) * w]).mean(axis=1)
        p = np.convolve(prof, np.ones(15) / 15, 'same')
        pk = [i for i in range(20, len(p) - 20) if p[i] == p[i - 20:i + 21].max() and p[i] > p.mean()]
        res.append([Y0 + i for i in pk])
    json.dump(dict(X0=X0, X1=X1, rows=res), open(OUT + f'rows_p{pg}.json', 'w'))
    for b, r in enumerate(res): print(b, len(r), r)


def crop(pg, ln, n=4, sc=2.0, hh=55, dy=0):
    d = json.load(open(OUT + f'rows_p{pg}.json'))
    X0, X1, R = d['X0'], d['X1'], d['rows']
    def clean(r):
        o = []
        for y in r:
            if y < d.get('ytop', 0): continue
            if o and y - o[-1] < 62: continue
            o.append(y)
        return o
    R = [clean(r) for r in R]
    w = (X1 - X0) // B
    # use per-block centres where the block has the canonical count, interpolate in x
    ref = max(set(len(r) for r in R), key=[len(r) for r in R].count)
    xs = [X0 + w * (b + .5) for b in range(B) if len(R[b]) == ref]
    ys = [R[b][ln - 1] for b in range(B) if len(R[b]) == ref]
    im = Image.open(IMG.format(pg)).convert('L')
    pw = (X1 - X0 + 80) // n
    for i in range(n):
        xa = X0 - 60 + i * pw; xb = xa + pw + 50
        yc = int(np.interp((xa + xb) / 2, xs, ys)) + dy
        c = im.crop((xa, yc - hh, xb, yc + hh))
        c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
        ImageOps.autocontrast(c, cutoff=1).save(OUT + f'p{pg}L{ln:02d}_{i + 1}.png')
    print('ok', pg, ln)


if __name__ == '__main__':
    a = sys.argv
    if a[1] == 'rows':
        rows(int(a[2]), *map(int, a[3:7]))
    else:
        crop(int(a[2]), int(a[3]), *(int(x) if i != 1 else float(x) for i, x in enumerate(a[4:])))


def zoom(pg, ln, xa, xb, sc=3.0, hh=60, dy=0, tag='z'):
    d = json.load(open(OUT + f'rows_p{pg}.json'))
    X0, X1, R = d['X0'], d['X1'], d['rows']
    def clean(r):
        o = []
        for y in r:
            if y < d.get('ytop', 0): continue
            if o and y - o[-1] < 62: continue
            o.append(y)
        return o
    R = [clean(r) for r in R]
    w = (X1 - X0) // B
    ref = max(set(len(r) for r in R), key=[len(r) for r in R].count)
    xs = [X0 + w * (b + .5) for b in range(B) if len(R[b]) == ref]
    ys = [R[b][ln - 1] for b in range(B) if len(R[b]) == ref]
    yc = int(np.interp((xa + xb) / 2, xs, ys)) + dy
    im = Image.open(IMG.format(pg)).convert('L')
    c = im.crop((xa, yc - hh, xb, yc + hh)); c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
    ImageOps.autocontrast(c, cutoff=1).save(OUT + f'p{pg}L{ln:02d}{tag}.png'); print('ok')
