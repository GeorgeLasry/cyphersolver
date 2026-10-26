"""Set 461 (goal run loop 107; run() reused by set 462): tablet size and signs with length x site strata; C-train -> C-test.
Writes results/predict_test461.md."""
from collections import Counter
from statistics import median

import loopkit as L
import rtools as R
from predict_test379 import mantel_haenszel
from scipy.stats import binomtest


def run(sub, tr, te, rd, key):
    size = L.field(31)
    def sz(t):
        try:
            return float(size.get(t, 0))
        except ValueError:
            return 0
    A = [t for t in tr if L.SUBTYPE.get(t) == sub and sz(t) > 0]
    B = [t for t in te if L.SUBTYPE.get(t) == sub and sz(t) > 0]
    cut = median(sz(t) for t in A)
    strat = lambda t: (min(max(len(t), 2), 6), L.META.get(t, ('', '', ''))[0])
    cnt = Counter(g for t in A for g in t)
    sk = {}
    for g in [g for g, n in cnt.items() if n >= 10]:
        tabs = []
        for k in sorted({strat(t) for t in A}):
            lg = [g in t for t in A if strat(t) == k and sz(t) > cut]
            sm = [g in t for t in A if strat(t) == k and sz(t) <= cut]
            tabs.append([[sum(lg), len(lg) - sum(lg)], [sum(sm), len(sm) - sum(sm)]])
        o, p = mantel_haenszel(tabs)
        if p < 0.01:
            sk[g] = o > 1
    rate = lambda S, g, big: sum(g in t for t in S if (sz(t) > cut) == big) / max(1, sum(1 for t in S if (sz(t) > cut) == big))
    rep = [(g, d) for g, d in sk.items() if sum(g in t for t in B) >= 3]
    same = sum((rate(B, g, True) > rate(B, g, False)) == d for g, d in rep)
    p = binomtest(same, len(rep), 0.5, alternative='greater').pvalue if rep else 1
    ok = bool(rep) and same / len(rep) >= 0.75 and p < 0.05
    rd.rec(key, '%s: size skews (length x site held) replicate' % sub, 'skewed %s; %d of %d, p = %.4f' % (dict(sk), same, len(rep), p), ok)
    return ok


def main():
    rd = R.Round('Four-hundred-and-sixty-first registered predictions: goal loop 107, tablet size and signs', 'predict_test461')
    _, (tr, te) = L.splits_c()
    o1 = run('TAB:B', tr, te, rd, 'TS1')
    o2 = run('TAB:I', tr, te, rd, 'TS2')
    rd.rec('P', 'progress rule: either holds', 'TS1 %s, TS2 %s' % (o1, o2), o1 or o2)
    rd.finish()


if __name__ == '__main__':
    main()
