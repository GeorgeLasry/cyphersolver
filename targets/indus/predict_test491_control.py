"""Audit of set 491 CT2 (not registered): drop copy pairs with identical first and second dimensions (possible double
records), and report the CISI numbers of the remaining pairs."""
import random
from collections import defaultdict

import rtools as R

rnd = random.Random(4910)
A, B, rowsA, recs, F = R.load_all()
md = []
for r in F:
    rec = recs.get(r['sealid'])
    if rec and r['site'] == 'Mohenjo-daro' and str(rec[20]).startswith('SEAL:S') and r['flat'] and len(r['flat']) >= 2:
        m = str(rec[18]).split(':')[0]
        if m not in ('', '-', 'None'):
            md.append((tuple(r['flat']), m, (str(rec[31]), str(rec[32])), rec[1]))
by = defaultdict(list)
for k, x in enumerate(md):
    by[x[0]].append(k)
gr = [v for v in by.values() if len(v) > 1]
pairs = [(g[a], g[b]) for g in gr for a in range(len(g)) for b in range(a + 1, len(g))]
keep = [(i, j) for i, j in pairs if md[i][2] != md[j][2] or md[i][2] == ('0', '0')]
mot = [x[1] for x in md]
o = sum(mot[i] == mot[j] for i, j in keep)
ge = 0
for _ in range(1000):
    mm = list(mot)
    rnd.shuffle(mm)
    ge += sum(mm[i] == mm[j] for i, j in keep) >= o
print('pairs %d, kept after dropping identical dimensions %d, same motif %d, p = %.4f' % (len(pairs), len(keep), o, (ge + 1) / 1001))
for i, j in keep[:12]:
    print(md[i][3], md[j][3], md[i][1], md[j][1], ' '.join(md[i][0]))
bylen = defaultdict(list)
for k, x in enumerate(md):
    bylen[len(x[0])].append(k)
ge2 = 0
for _ in range(1000):
    mm = list(mot)
    for L_, ix in bylen.items():
        vv = [mot[i] for i in ix]
        rnd.shuffle(vv)
        for i, v in zip(ix, vv):
            mm[i] = v
    ge2 += sum(mm[i] == mm[j] for i, j in keep) >= o
print('length-matched null: p = %.4f; unicorn share of these seals %.2f' % ((ge2 + 1) / 1001, sum(m == 'Bull1' for m in mot) / len(mot)))
