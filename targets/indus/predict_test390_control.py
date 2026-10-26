"""Audit of set 390 (not registered): shuffle-null versions of NL1/NL2 (sites shuffled among the objects involved)."""
import random
from collections import defaultdict

import rtools as R
from predict_test390 import body

rnd = random.Random(3900)
A, B, rowsA, recs, F = R.load_all()
seals, tabs = [], []
for r in F:
    rec = recs.get(r['sealid'])
    if not rec:
        continue
    ty = str(rec[20])
    for ln in r['seq']:
        b = body(tuple(ln)) if ln else None
        if b:
            (seals if ty.startswith('SEAL') else tabs if ty.startswith('TAB') else []).append([b, r['site'], r['sealid']])


def stat(seals, tabs):
    sb = defaultdict(list)
    for b, s, i in seals:
        sb[b].append((s, i))
    h1 = sum(s2 == s for b, s, i in tabs for s2, i2 in sb.get(b, []))
    h2 = 0
    for lst in sb.values():
        for a in range(len(lst)):
            for c in range(a + 1, len(lst)):
                if lst[a][1] != lst[c][1]:
                    h2 += lst[a][0] == lst[c][0]
    return h1, h2


o1, o2 = stat(seals, tabs)
g1 = g2 = 0
for _ in range(500):
    ss = [s for b, s, i in seals]
    ts = [s for b, s, i in tabs]
    allsites = ss + ts
    rnd.shuffle(allsites)
    s2 = [[b, allsites[k], i] for k, (b, s, i) in enumerate(seals)]
    t2 = [[b, allsites[len(seals) + k], i] for k, (b, s, i) in enumerate(tabs)]
    x1, x2 = stat(s2, t2)
    g1 += x1 >= o1
    g2 += x2 >= o2
print('NL1 observed %d, shuffle as high %d of 500; NL2 observed %d, shuffle as high %d of 500' % (o1, g1, o2, g2))
