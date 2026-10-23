"""r2d (23 Oct 2026): find the writing lines of a page image (dark-ink row profile) and crop chosen lines.

    python research/reading_audit/r2d_lines.py <image>                        list line centres
    python research/reading_audit/r2d_lines.py <image> <out.jpg> <i> [j] [x0 x1]   crop lines i..j (1-based, as listed)
"""
import sys
import numpy as np
from PIL import Image


def find(im):
    g = np.asarray(im.convert('L'), dtype=np.float32)
    H, W = g.shape
    band = g[:, int(W * 0.12):int(W * 0.95)]
    prof = (band < 105).sum(1).astype(float)
    k = np.ones(25) / 25; sm = np.convolve(prof, k, 'same')
    thr = max(8.0, sm.max() * 0.18)
    lines, inside = [], False
    for y, v in enumerate(sm):
        if v > thr and not inside: inside, a = True, y
        elif v <= thr and inside:
            inside = False
            if y - a > 25: lines.append((a, y))
    return lines


if __name__ == '__main__':
    im = Image.open(sys.argv[1])
    L = find(im)
    if len(sys.argv) < 4:
        for n, (a, b) in enumerate(L, 1): print(n, a, b)
    else:
        i = int(sys.argv[3]); j = int(sys.argv[4]) if len(sys.argv) > 4 else i
        x0, x1 = (float(sys.argv[5]), float(sys.argv[6])) if len(sys.argv) > 6 else (0.0, 1.0)
        W, H = im.size
        a = max(0, L[i - 1][0] - 30); b = min(H, L[j - 1][1] + 30)
        c = im.crop((int(x0 * W), a, int(x1 * W), b)).convert('RGB')
        if c.size[0] > 1900: c = c.resize((1900, int(c.size[1] * 1900 / c.size[0])))
        c.save(sys.argv[2], quality=88); print(sys.argv[2], c.size)
