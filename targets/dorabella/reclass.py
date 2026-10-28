"""Reclassify each glyph's orientation from the measured angles (angles_hull.json).

For each glyph, compare its angle with the circular mean angle of the other glyphs that share its
arc count and carry each consensus orientation (leave-one-out); take the nearest. Classes with no
other member at that arc count use the all-arc-count mean shifted by the arc count's mean offset.
Writes ct_measured.txt and prints the changes with both distances.
"""
import os, json
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(HERE, 'angles_hull.json')))


def cmean(a):
    a = np.radians(a)
    return np.degrees(np.arctan2(np.sin(a).mean(), np.cos(a).mean())) % 360


def cdist(a, b):
    d = abs(a - b) % 360
    return min(d, 360 - d)


out, changes = [], []
for r in R:
    arcs = r['consensus'][1]
    means = {}
    for o in 'ABCDEFGH':
        same = [s['angle'] for s in R if s is not r and s['consensus'] == o + arcs]
        allc = [s['angle'] for s in R if s is not r and s['consensus'][0] == o]
        if same:
            means[o] = cmean(same)
        elif allc:
            means[o] = cmean(allc)
    best = min(means, key=lambda o: cdist(r['angle'], means[o]))
    tok = best + arcs
    out.append(tok)
    if tok != r['consensus']:
        changes.append((r['i'], r['consensus'], tok, r['angle'],
                        cdist(r['angle'], means[r['consensus'][0]]), cdist(r['angle'], means[best])))

ct = open(os.path.join(HERE, 'ct.txt')).read().strip().splitlines()
lens = [len(l.split()) for l in ct]
lines, k = [], 0
for n in lens:
    lines.append(' '.join(out[k:k + n])); k += n
open(os.path.join(HERE, 'ct_measured.txt'), 'w').write('\n'.join(lines) + '\n')
print(f'{len(changes)} glyphs reclassified')
for c in changes:
    print(f'  #{c[0]:2d} {c[1]} -> {c[2]}  angle {c[3]:6.1f}  dist to consensus class {c[4]:5.1f}, to new {c[5]:5.1f}')
