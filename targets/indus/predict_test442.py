"""Set 442 (goal run loop 88): the '33 520' unit without the stroked U, and the closing formula on rectangular seals.
Writes results/predict_test442.md."""
from statistics import median

import rtools as R
from predict_test379 import mantel_haenszel
from predict_test430 import seals
from predict_test441 import has_formula
from scipy.stats import fisher_exact


def unit(t):
    return any(t[i] == '33' and t[i + 1] == '520' for i in range(len(t) - 1)) and not has_formula(t)


def main():
    rd = R.Round('Four-hundred-and-forty-second registered predictions: goal loop 88, the 33 520 unit and rectangular seals', 'predict_test442')
    sq = seals(31)
    cut = median(s for s, t, x in sq)
    band = lambda t: min(max(len(t), 2), 7)
    tabs = []
    for k in sorted({(band(t), x) for s, t, x in sq}):
        lg = [unit(t) for s, t, x in sq if (band(t), x) == k and s > cut]
        sm = [unit(t) for s, t, x in sq if (band(t), x) == k and s <= cut]
        tabs.append([[sum(lg), len(lg) - sum(lg)], [sum(sm), len(sm) - sum(sm)]])
    o1, p1 = mantel_haenszel(tabs)
    rd.rec('FU1', "'33 520' without a stroked U before it goes with large square seals", 'odds ratio %.2f, p = %.4f' % (o1, p1), o1 > 1 and p1 < 0.05)
    A, B, rowsA, recs, F = R.load_all()
    rc = []
    for r in F:
        rec = recs.get(r['sealid'])
        if rec and str(rec[20]).startswith('SEAL:R') and r['flat']:
            try:
                s = float(rec[31])
            except (TypeError, ValueError):
                continue
            if s > 0:
                rc.append((s, tuple(r['flat'])))
    c2 = median(s for s, t in rc)
    a = sum(has_formula(t) for s, t in rc if s > c2)
    na = sum(1 for s, t in rc if s > c2)
    c = sum(has_formula(t) for s, t in rc if s <= c2)
    nc = sum(1 for s, t in rc if s <= c2)
    o2, p2 = fisher_exact([[a, na - a], [c, nc - c]], alternative='greater')
    rd.rec('FR1', 'large rectangular seals carry the closing formula more often', '%d of %d against %d of %d, p = %.4f' % (a, na, c, nc, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'FU1 %s, FR1 %s' % (o1 > 1 and p1 < 0.05, p2 < 0.05), (o1 > 1 and p1 < 0.05) or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
