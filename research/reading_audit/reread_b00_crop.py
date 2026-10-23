"""Re-read brief, batch b00 (morosini1588): crop a line of a DECODE cipher page for checking figures.

    python reread_b00_crop.py R43 308r 5 [--n 1] [--x0 0 --x1 1] [--scale 1.6] [--rows]

Finds the page image (IMG_R<rec>_I*_P<k>.jpg in the scratchpad image folder, P<k> = the page's position in the
DECODE transcription), finds the written rows by ink projection, and saves rows line..line+n-1 (1-based, counted like
the transcription's lines) as a jpg in the scratchpad (path printed). --x0/--x1 crop horizontally (fractions of the
width) so a part of a line can be enlarged; --rows prints the detected row bands instead.
Images are ASV material and stay in the scratchpad (not the repository).
"""
import argparse, glob, os, re, sys
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
SCR = r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\b00'


def page_index(rec, page):
    import reread_b00_decode as d
    path = None
    c = glob.glob(os.path.join(d.TDIR, 'decode', f'DOC_{rec}_D1[67]*.txt'))
    path = c[0] if c else os.path.join(d.TDIR, f'{rec}_transcription_decode.txt')
    pages = [p for p, items in d.parse(path) if p]
    pages = [p.lstrip('0') for p in pages]
    return pages.index(page.lstrip('0')) + 1, len(pages)


def find_image(rec, k):
    for root in (os.path.join(SCR, 'img', rec), os.path.join(r'C:\Users\dbour\cypher\targets\morosini1588\img')):
        f = glob.glob(os.path.join(root, f'IMG_{rec}_I*_P{k}.jpg'))
        if f:
            return f[0]
    raise SystemExit(f'no image for {rec} P{k}')


def rows(im):
    g = np.asarray(im.convert('L'), dtype=np.float32)
    h, w = g.shape
    band = g[:, int(w * 0.08):int(w * 0.95)]
    ink = (band < 120).sum(axis=1).astype(float)
    k = max(3, h // 400)
    ink = np.convolve(ink, np.ones(k) / k, mode='same')
    thr = max(ink.max() * 0.12, 8)
    on = ink > thr
    out, start = [], None
    for y, v in enumerate(on):
        if v and start is None:
            start = y
        if not v and start is not None:
            if y - start > h // 200:
                out.append((start, y))
            start = None
    # merge bands closer than a third of the median gap, split very tall ones
    if not out:
        return out
    hts = sorted(b - a for a, b in out)
    med = hts[len(hts) // 2]
    merged = []
    for a, b in out:
        if merged and a - merged[-1][1] < med * 0.25:
            merged[-1] = (merged[-1][0], b)
        else:
            merged.append((a, b))
    return [(a, b) for a, b in merged if b - a > med * 0.4]


def grid(rs):
    """Centre of the first cipher row and the line spacing, from the detected bands."""
    cs = [(a + b) / 2 for a, b in rs]
    d = sorted(y - x for x, y in zip(cs, cs[1:]))
    sp = d[len(d) // 2]
    for i in range(len(cs) - 1):
        if abs((cs[i + 1] - cs[i]) - sp) < sp * 0.25:
            return cs[i], sp
    return cs[0], sp


def first_line(rec, page):
    import reread_b00_decode as d
    c = glob.glob(os.path.join(d.TDIR, 'decode', f'DOC_{rec}_D1[67]*.txt'))
    path = c[0] if c else os.path.join(d.TDIR, f'{rec}_transcription_decode.txt')
    for p, items in d.parse(path):
        if p and p.lstrip('0') == page.lstrip('0') and items:
            return items[0]['line']
    return 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('rec')
    ap.add_argument('page')
    ap.add_argument('line', type=int, nargs='?', default=1)
    ap.add_argument('--n', type=int, default=1)
    ap.add_argument('--x0', type=float, default=0.0)
    ap.add_argument('--x1', type=float, default=1.0)
    ap.add_argument('--scale', type=float, default=1.0)
    ap.add_argument('--rows', action='store_true')
    ap.add_argument('--k', type=int, help='image position P<k> if the page name is not in the transcription')
    a = ap.parse_args()
    k = a.k or page_index(a.rec, a.page)[0]
    f = find_image(a.rec, k)
    im = Image.open(f)
    rs = rows(im)
    if a.rows:
        print(f, im.size, len(rs), 'rows')
        for i, (y0, y1) in enumerate(rs, 1):
            print(i, y0, y1)
        print('grid (first row centre, spacing):', grid(rs), 'first transcription line:', first_line(a.rec, a.page))
        return
    first, sp = grid(rs)
    f0 = first_line(a.rec, a.page)
    yc0 = first + (a.line - f0) * sp
    yc1 = first + (a.line + a.n - 1 - f0) * sp
    y0 = int(max(0, yc0 - sp * 0.75))
    y1 = int(min(im.size[1], yc1 + sp * 0.75))
    W = im.size[0]
    crop = im.crop((int(W * a.x0), y0, int(W * a.x1), y1))
    if a.scale != 1.0:
        crop = crop.resize((int(crop.size[0] * a.scale), int(crop.size[1] * a.scale)))
    os.makedirs(os.path.join(SCR, 'crops'), exist_ok=True)
    out = os.path.join(SCR, 'crops', f'{a.rec}_{a.page}_l{a.line}-{a.line + a.n - 1}_{a.x0:.2f}-{a.x1:.2f}.jpg')
    crop.save(out, quality=88)
    print(out, f'(rows found: {len(rs)}; image {os.path.basename(f)})')


if __name__ == '__main__':
    main()
