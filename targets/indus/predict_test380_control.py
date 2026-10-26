"""Audit of set 380 HS2 (not registered): recurrence of small- against large-seal texts within text-length bands."""
from collections import Counter
from statistics import median

import rtools as R
from predict_test379 import mantel_haenszel

A, B, rowsA, recs, F = R.load_all()
objs = []
for r in F:
    rec = recs.get(r['sealid'])
    if rec and str(rec[20]).startswith('SEAL:S') and r['flat']:
        try:
            sz = float(rec[31])
        except (TypeError, ValueError):
            continue
        if sz > 0:
            objs.append((sz, tuple(r['flat'])))
cut = median(s for s, t in objs)
cnt = Counter(t for s, t in objs)
band = lambda t: min(max(len(t), 2), 7)
tabs = []
for b in sorted({band(t) for s, t in objs}):
    sm = [cnt[t] > 1 for s, t in objs if band(t) == b and s <= cut]
    lg = [cnt[t] > 1 for s, t in objs if band(t) == b and s > cut]
    print('band', b, 'small %d/%d large %d/%d' % (sum(sm), len(sm), sum(lg), len(lg)))
    tabs.append([[sum(sm), len(sm) - sum(sm)], [sum(lg), len(lg) - sum(lg)]])
print('MH odds ratio small/large %.2f, p = %.4f' % mantel_haenszel(tabs))
