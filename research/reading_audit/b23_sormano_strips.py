"""b23 re-read, sormano: cut a page of BnF fr. 3096 (raw/full<view>.jpg in the main checkout, which is the
IIIF full-resolution master, 8.6k px wide) into line strips for reading by eye.

    python b23_sormano_strips.py <view> <x0> <x1> <y0> <y1> <tag> [scale=0.8] [halves=2]

Line bands come from the horizontal ink profile; each band is padded and split into <halves> overlapping
pieces, saved as <OUT>/<tag>_L<nn><a|b>.jpg with the band's y-range printed (so a line can be re-cut).
"""
import sys
import numpy as np
from PIL import Image, ImageOps

RAW = 'C:/Users/dbour/cypher/targets/sormano/raw/full%d.jpg'
OUT = ('C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/'
       '6b6912a8-0ad3-4eda-b63e-c79291f1bcc5/scratchpad/reread/sormano/')


def bands(a, minh=40):
    ink = (a < 110).sum(1).astype(float)
    k = np.ones(25) / 25
    s = np.convolve(ink, k, 'same')
    thr = max(8.0, 0.18 * np.percentile(s, 90))
    on = s > thr
    out, i = [], 0
    while i < len(on):
        if on[i]:
            j = i
            while j < len(on) and on[j]:
                j += 1
            if j - i >= minh:
                out.append((i, j))
            i = j
        else:
            i += 1
    # split overly tall bands at their minimum
    res = []
    for (i, j) in out:
        while j - i > 230:
            m = i + 80 + int(np.argmin(s[i + 80:j - 80]))
            res.append((i, m)); i = m
        res.append((i, j))
    return res


def main():
    view, x0, x1, y0, y1, tag = sys.argv[1:7]
    view, x0, x1, y0, y1 = map(int, (view, x0, x1, y0, y1))
    scale = float(sys.argv[7]) if len(sys.argv) > 7 else 0.8
    halves = int(sys.argv[8]) if len(sys.argv) > 8 else 2
    im = Image.open(RAW % view).convert('L').crop((x0, y0, x1, y1))
    a = np.asarray(im)
    for n, (i, j) in enumerate(bands(a)):
        ti, tj = max(0, i - 25), min(a.shape[0], j + 25)
        w = x1 - x0
        step = w // halves
        for h in range(halves):
            xa = max(0, h * step - 60); xb = min(w, (h + 1) * step + 60)
            c = im.crop((xa, ti, xb, tj))
            c = ImageOps.autocontrast(c, cutoff=1)
            c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
            c.save(OUT + '%s_L%02d%s.jpg' % (tag, n, 'abcd'[h]), quality=92)
        print('%s L%02d y=%d-%d' % (tag, n, y0 + ti, y0 + tj))


if __name__ == '__main__':
    main()
