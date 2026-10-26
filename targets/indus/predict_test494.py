"""Set 494 (goal run loop 140): audit of set 493 UR1 against seal size, and on two halves. Writes results/predict_test494.md."""
import hashlib
from collections import Counter
from statistics import median

import rtools as R
from predict_test379 import mantel_haenszel


def main():
    rd = R.Round('Four-hundred-and-ninety-fourth registered predictions: goal loop 140, audit of the unicorn repeats', 'predict_test494')
    A, B, rowsA, recs, F = R.load_all()
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
    cnt = Counter(t for t, u, x, s in rows)
    cut = median(s for t, u, x, s in rows)
    band = lambda t: min(max(len(t), 2), 7)

    def mh(R_):
        tabs = []
        for k in sorted({(band(t), x, s > cut) for t, u, x, s in R_}):
            a = [cnt[t] > 1 for t, u, x, s in R_ if (band(t), x, s > cut) == k and u]
            c = [cnt[t] > 1 for t, u, x, s in R_ if (band(t), x, s > cut) == k and not u]
            tabs.append([[sum(a), len(a) - sum(a)], [sum(c), len(c) - sum(c)]])
        return mantel_haenszel(tabs)
    o1, p1 = mh(rows)
    rd.rec('UA1', 'UR1 holds with length x site x size-half strata', 'odds ratio %.2f, p = %.4f' % (o1, p1), o1 > 1 and p1 < 0.05)
    half = lambda t, s: int(hashlib.md5(('%s%.2f' % (' '.join(t), s)).encode()).hexdigest(), 16) % 2
    hs = [mh([r for r in rows if half(r[0], r[3]) == h]) for h in (0, 1)]
    rd.rec('UA2', 'UR1 leans the same way in both random halves', 'half 1 %.2f (p %.3f), half 2 %.2f (p %.3f)' % (hs[0] + hs[1]), all(o > 1 for o, p in hs))
    rd.rec('P', 'progress rule: none (audit of set 493)', '', False)
    rd.finish()


if __name__ == '__main__':
    main()
