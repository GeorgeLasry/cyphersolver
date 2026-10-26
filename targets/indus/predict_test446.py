"""Set 446 (goal run loop 92): the name before the closing formula: fish heads and 520-class heads. A and B.
Writes results/predict_test446.md."""
from collections import Counter

import rtools as R
from scipy.stats import fisher_exact
from signs import load


def main():
    rd = R.Round('Four-hundred-and-forty-sixth registered predictions: goal loop 92, the name before the closing formula', 'predict_test446')
    A, B, *_ = R.load_all()
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    fish = lambda g: g.isdigit() and 220 <= int(g) <= 249
    r1, r2 = [], []
    for L in (DA, DB):
        pre_f = [t[i - 1] for t in L for i in range(1, len(t) - 1) if t[i] in ('705', '706') and t[i + 1] == '33']
        pre_7 = [t[i - 1] for t in L for i in range(1, len(t)) if t[i] == '740']
        pre_5 = Counter(t[i - 1] for t in L for i in range(1, len(t)) if t[i] == '520')
        tot = Counter(t[i - 1] for t in L for i in range(1, len(t)) if t[i] in R.END)
        cls520 = {g for g in tot if tot[g] >= 3 and pre_5[g] / tot[g] >= 0.5}
        a, n = sum(fish(g) for g in pre_f), len(pre_f)
        c, m = sum(fish(g) for g in pre_7), len(pre_7)
        r1.append((a, n, c, m, fisher_exact([[a, n - a], [c, m - c]], alternative='greater')[1]))
        a, c = sum(g in cls520 for g in pre_f), sum(g in cls520 for g in pre_7)
        r2.append((a, n, c, m, fisher_exact([[a, n - a], [c, m - c]], alternative='greater')[1]))
    ok1 = all(x[4] < 0.05 for x in r1)
    ok2 = all(x[4] < 0.05 for x in r2)
    rd.rec('FH1', 'the sign before the formula is a fish more often than the sign before 740, A and B', ['%d of %d against %d of %d, p = %.4f' % x for x in r1], ok1)
    rd.rec('FH2', 'it is a 520-class head more often than the sign before 740, A and B', ['%d of %d against %d of %d, p = %.4f' % x for x in r2], ok2)
    rd.rec('P', 'progress rule: either holds', 'FH1 %s, FH2 %s' % (ok1, ok2), ok1 or ok2)
    rd.finish()


if __name__ == '__main__':
    main()
