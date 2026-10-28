"""Measure each glyph's opening direction on the 1937 first-edition plate (Powell, Memories of a
Variation, p. 98; archive.org in.ernet.dli.2015.155431, scan page 137, 2911 x 4373 px).

Each glyph is one connected stroke. Skeletonise it, take the two skeleton endpoints farthest apart,
and measure the angle from the skeleton's centroid to their midpoint: that is the direction the arcs
open. Orientation letters as in ct.txt (Hauer et al. 2025): A right, H up-right, G up, F up-left,
E left, D down-left, C down, B down-right. Prints per glyph the measured angle, the nearest
orientation, its margin to the 22.5-degree boundary, and the consensus token.
"""
import os, sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
from skimage.morphology import skeletonize, convex_hull_image

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, 'src', 'memories1937', 'cipher_full.png')
ANG = {'A': 0, 'H': 45, 'G': 90, 'F': 135, 'E': 180, 'D': 225, 'C': 270, 'B': 315}

a = np.array(Image.open(IMG)) < 128
lab, n = ndi.label(a, structure=np.ones((3, 3)))
glyphs = []
for i, sl in enumerate(ndi.find_objects(lab)):
    mask = lab[sl] == i + 1
    if mask.sum() > 150:
        glyphs.append((sl, mask))
lines = []
for lo, hi in ((0, 250), (250, 480), (480, 750)):
    L = [g for g in glyphs if lo <= (g[0][0].start + g[0][0].stop) / 2 < hi]
    lines.append(sorted(L, key=lambda g: g[0][1].start))
ct = open(os.path.join(HERE, 'ct.txt')).read().split()
METHOD = sys.argv[1] if len(sys.argv) > 1 else 'hull'


def endpoints(sk):
    ys, xs = np.nonzero(sk)
    nb = ndi.convolve(sk.astype(int), np.ones((3, 3), int), mode='constant') - 1
    e = [(y, x) for y, x in zip(ys, xs) if nb[y, x] == 1]
    return e, ys, xs


rows = []
k = 0
for li, L in enumerate(lines):
    for sl, mask in L:
        if METHOD == 'hull':          # concave side: hull minus ink, seen from the ink's centroid
            hull = convex_hull_image(mask)
            gap = hull & ~mask
            ys, xs = np.nonzero(mask); gy, gx = np.nonzero(gap)
            e = [0, 0]
            ang = np.degrees(np.arctan2(-(gy.mean() - ys.mean()), gx.mean() - xs.mean())) % 360
        else:
            sk = skeletonize(mask)
            e, ys, xs = endpoints(sk)
            if len(e) < 2:
                ang = float('nan')
            else:
                best = max(((p, q) for p in e for q in e), key=lambda pq: (pq[0][0] - pq[1][0]) ** 2 + (pq[0][1] - pq[1][1]) ** 2)
                my, mx = (best[0][0] + best[1][0]) / 2, (best[0][1] + best[1][1]) / 2
                cy, cx = ys.mean(), xs.mean()
                ang = np.degrees(np.arctan2(-(my - cy), mx - cx)) % 360    # y axis up
        near = min(ANG, key=lambda o: min(abs(ang - ANG[o]), 360 - abs(ang - ANG[o])))
        dev = min(abs(ang - ANG[near]), 360 - abs(ang - ANG[near]))
        rows.append((k, li + 1, ct[k], near, ang, 22.5 - dev, len(e), sl[1].start))
        k += 1

agree = sum(r[2][0] == r[3] for r in rows)
print(f'{len(rows)} glyphs; measured orientation = consensus at {agree}')
for r in rows:
    flag = '' if r[2][0] == r[3] else '  <-- differs'
    if r[5] < 8:
        flag += '  (near boundary)'
    print(f'{r[0]:2d} line{r[1]} x={r[7]:4d} consensus {r[2]} measured {r[3]} {r[4]:6.1f}deg margin {r[5]:4.1f} ends={r[6]}{flag}')

import json
json.dump([dict(i=r[0], line=r[1], consensus=r[2], angle=round(float(r[4]), 1), x=int(r[7])) for r in rows],
          open(os.path.join(HERE, f'angles_{METHOD}.json'), 'w'), indent=0)
