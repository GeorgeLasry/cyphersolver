"""Audit of set 389 TT1 (not registered): same-site null, exact-size duplicates, and CISI numbers of the copies."""
import random
from collections import defaultdict
from statistics import pstdev

import rtools as R

rnd = random.Random(3890)
A, B, rowsA, recs, F = R.load_all()
sq = []
for r in F:
    rec = recs.get(r['sealid'])
    if rec and str(rec[20]).startswith('SEAL:S') and r['flat']:
        try:
            sz = float(rec[31])
        except (TypeError, ValueError):
            continue
        if sz > 0:
            sq.append((sz, tuple(r['flat']), r['site'], rec[1], rec[32]))
by = defaultdict(list)
for x in sq:
    if len(x[1]) >= 2:
        by[x[1]].append(x)
groups = [v for v in by.values() if len(v) > 1]
exact = sum(1 for v in groups if len({(x[0], x[4]) for x in v}) < len(v))
print('groups', len(groups), 'with an exact repeat of both dimensions', exact)
for v in groups[:8]:
    print(' '.join(v[0][1]), [(x[3], x[2], x[0], x[4]) for x in v])
site_sizes = defaultdict(list)
for x in sq:
    site_sizes[x[2]].append(x[0])
obs = sum(pstdev([x[0] for x in v]) for v in groups) / len(groups)
ge = 0
for _ in range(1000):
    sim = sum(pstdev([rnd.choice(site_sizes[x[2]]) for x in v]) for v in groups) / len(groups)
    ge += sim <= obs
print('same-site null: mean spread %.2f, as tight in %d of 1000' % (obs, ge))
dd = [v for v in groups if len({(x[0], x[4]) for x in v}) == len(v)]
obs2 = sum(pstdev([x[0] for x in v]) for v in dd) / len(dd)
ge2 = sum(sum(pstdev([rnd.choice(site_sizes[x[2]]) for x in v]) for v in dd) / len(dd) <= obs2 for _ in range(1000))
print('without exact repeats (%d groups): spread %.2f, same-site null as tight in %d of 1000' % (len(dd), obs2, ge2))
len_sizes = defaultdict(list)
for x in sq:
    len_sizes[len(x[1])].append(x[0])
ge3 = sum(sum(pstdev([rnd.choice(len_sizes[len(x[1])]) for x in v]) for v in dd) / len(dd) <= obs2 for _ in range(1000))
print('same-length null (%d groups): as tight in %d of 1000' % (len(dd), ge3))
ls = defaultdict(list)
for x in sq:
    ls[(len(x[1]), x[2])].append(x[0])
ge4 = sum(sum(pstdev([rnd.choice(ls[(len(x[1]), x[2])]) for x in v]) for v in dd) / len(dd) <= obs2 for _ in range(1000))
print('same-length-and-site null: as tight in %d of 1000' % ge4)
