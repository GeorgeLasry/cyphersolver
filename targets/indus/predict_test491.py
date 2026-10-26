"""Set 491 (goal run loop 137): copies of a seal text: thickness (same length, same site null); motif within Mohenjo-daro.
Writes results/predict_test491.md."""
import random
from collections import defaultdict
from statistics import pstdev

import rtools as R


def main():
    rnd = random.Random(491)
    rd = R.Round('Four-hundred-and-ninety-first registered predictions: goal loop 137, copies: thickness and motif', 'predict_test491')
    A, B, rowsA, recs, F = R.load_all()
    rows = []
    for r in F:
        rec = recs.get(r['sealid'])
        if rec and str(rec[20]).startswith('SEAL:S') and r['flat'] and len(r['flat']) >= 2:
            try:
                th = float(rec[33])
            except (TypeError, ValueError):
                th = 0
            rows.append((tuple(r['flat']), r['site'], th, str(rec[18]).split(':')[0]))
    th_rows = [x for x in rows if x[2] > 0]
    by = defaultdict(list)
    for x in th_rows:
        by[x[0]].append(x)
    groups = [v for v in by.values() if len(v) > 1]
    pool = defaultdict(list)
    for x in th_rows:
        pool[(len(x[0]), x[1])].append(x[2])
    obs = sum(pstdev([x[2] for x in g]) for g in groups) / max(1, len(groups))
    ge = sum(sum(pstdev([rnd.choice(pool[(len(x[0]), x[1])]) for x in g]) for g in groups) / max(1, len(groups)) <= obs for _ in range(1000))
    p1 = (ge + 1) / 1001
    rd.rec('CT1', 'copies are closer in thickness than seals of the same length and site', '%d groups, spread %.2f, p = %.4f' % (len(groups), obs, p1), p1 < 0.05)
    md = [x for x in rows if x[1] == 'Mohenjo-daro' and x[3] not in ('', '-', 'None')]
    byt = defaultdict(list)
    for k, x in enumerate(md):
        byt[x[0]].append(k)
    gr = [v for v in byt.values() if len(v) > 1]
    mot = [x[3] for x in md]
    stat = lambda m: sum(m[g[a]] == m[g[b]] for g in gr for a in range(len(g)) for b in range(a + 1, len(g)))
    o = stat(mot)
    n = sum(len(g) * (len(g) - 1) // 2 for g in gr)
    ge2 = 0
    for _ in range(1000):
        mm = list(mot)
        rnd.shuffle(mm)
        ge2 += stat(mm) >= o
    p2 = (ge2 + 1) / 1001
    rd.rec('CT2', 'copies at Mohenjo-daro share the motif more than chance', '%d of %d pairs, p = %.4f' % (o, n, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'CT1 %s, CT2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
