"""b26: cut a full-resolution leaf into line strips by horizontal ink projection (dubellay fr. 3005 f. 165, clair357).

    python research/reading_audit/b26_strips.py <image> <out prefix> x0 x1 y0 y1 [per=3]

Writes <prefix>_NN.jpg, each holding `per` consecutive text lines (with a margin), and prints the line bands.
"""
import sys
import numpy as np
from PIL import Image


def bands(a, thr):
    rows = (a < 140).sum(1)
    sm = np.convolve(rows, np.ones(15) / 15, 'same')
    on = sm > thr
    out, s = [], None
    for i, v in enumerate(on):
        if v and s is None: s = i
        if not v and s is not None:
            if i - s > 25: out.append((s, i))
            s = None
    if s is not None: out.append((s, len(on)))
    return out


def main(img, pre, x0, x1, y0, y1, per=3):
    x0, x1, y0, y1, per = map(int, (x0, x1, y0, y1, per))
    im = Image.open(img).convert('L')
    a = np.asarray(im.crop((x0, y0, x1, y1)))
    thr = max(8, (a < 140).sum(1).max() * 0.12)
    b = bands(a, thr)
    for i, (s, e) in enumerate(b): print(i, y0 + s, y0 + e)
    for k in range(0, len(b), per):
        grp = b[k:k + per]
        im.crop((x0, y0 + grp[0][0] - 30, x1, y0 + grp[-1][1] + 30)).save(f'{pre}_{k // per:02d}.jpg')


if __name__ == '__main__':
    main(*sys.argv[1:])


def lines2(img, pre, x0, x1, y0, y1):
    """Two lines per image, each image the full line width at native resolution (two half-width crops stacked)."""
    x0, x1, y0, y1 = map(int, (x0, x1, y0, y1))
    im = Image.open(img).convert('L')
    a = np.asarray(im.crop((x0, y0, x1, y1)))
    thr = max(8, (a < 140).sum(1).max() * 0.12)
    b = bands(a, thr)
    mid = (x0 + x1) // 2
    for i, (s, e) in enumerate(b):
        top, bot = y0 + s - 35, y0 + e + 35
        L = im.crop((x0, top, mid + 60, bot)); R = im.crop((mid - 60, top, x1, bot))
        o = Image.new('L', (max(L.width, R.width), L.height + R.height + 10), 255)
        o.paste(L, (0, 0)); o.paste(R, (0, L.height + 10))
        o.save(f'{pre}_L{i:02d}.jpg')
        print(i, top, bot)
