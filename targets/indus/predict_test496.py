"""Set 496 (goal run loop 142): audit of set 488 (rare signs on large seals) with motif strata. Writes results/predict_test496.md."""
from collections import Counter
from statistics import median

import rtools as R
from predict_test379 import mantel_haenszel


def main():
    rd = R.Round('Four-hundred-and-ninety-sixth registered predictions: goal loop 142, audit of rare signs against the animal', 'predict_test496')
    A, B, rowsA, recs, F = R.load_all()
    cnt = Counter(g for r in F for g in r['flat'])
    rows = []
    for r in F:
        rec = recs.get(r['sealid'])
        if rec and str(rec[20]).startswith('SEAL:S') and r['flat']:
            m = str(rec[18]).split(':')[0]
            try:
                sz = float(rec[31])
            except (TypeError, ValueError):
                sz = 0
            if m not in ('', '-', 'None') and sz > 0:
                rows.append((tuple(r['flat']), m == 'Bull1', r['site'], sz))
    cut = median(s for t, u, x, s in rows)
    band = lambda t: min(max(len(t), 2), 7)
    rare = lambda t: any(cnt[g] <= 2 for g in t)

    def mh(R_, strat):
        tabs = []
        for k in sorted({strat(t, u, x) for t, u, x, s in R_}):
            lg = [rare(t) for t, u, x, s in R_ if strat(t, u, x) == k and s > cut]
            sm = [rare(t) for t, u, x, s in R_ if strat(t, u, x) == k and s <= cut]
            tabs.append([[sum(lg), len(lg) - sum(lg)], [sum(sm), len(sm) - sum(sm)]])
        return mantel_haenszel(tabs)
    o1, p1 = mh(rows, lambda t, u, x: (band(t), x, u))
    rd.rec('RA1', 'rare signs on large seals with length x site x motif strata', 'odds ratio %.2f, p = %.4f' % (o1, p1), o1 > 1 and p1 < 0.05)
    o2, p2 = mh([r for r in rows if r[1]], lambda t, u, x: (band(t), x))
    rd.rec('RA2', 'the same within unicorn seals', 'odds ratio %.2f, p = %.4f' % (o2, p2), o2 > 1 and p2 < 0.05)
    rd.rec('P', 'progress rule: none (audit of set 488)', '', False)
    rd.finish()


if __name__ == '__main__':
    main()
