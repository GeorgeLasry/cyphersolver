"""Set 371 (goal run loop 17): region within square seals; object kind within the north. Split C. Writes results/predict_test371.md."""
from collections import Counter

import loopkit as L
import rtools as R
from scipy.stats import binomtest, fisher_exact


def test(tr, te, lab, a, b, keep, rd, key, title):
    def cnt(S):
        c = {a: Counter(), b: Counter()}
        for t in S:
            if keep(t) and lab(t) in c:
                c[lab(t)].update(t)
        return c, {k: max(1, sum(v.values())) for k, v in c.items()}
    (ca, na), (cb, nb) = cnt(tr), cnt(te)
    sk = {}
    for g in set(ca[a]) | set(ca[b]):
        x, y = ca[a][g], ca[b][g]
        if x + y >= 10 and fisher_exact([[x, na[a] - x], [y, na[b] - y]])[1] < 0.01:
            sk[g] = x / na[a] > y / na[b]
    rep = [(g, d) for g, d in sk.items() if cb[a][g] + cb[b][g] >= 3]
    same = sum((cb[a][g] / nb[a] > cb[b][g] / nb[b]) == d for g, d in rep)
    p = binomtest(same, len(rep), 0.5, alternative='greater').pvalue if rep else 1
    rd.say('- %s: %d skewed (%s: %s; %s: %s); tokens train %s.' % (title, len(sk), a, ' '.join(sorted(g for g, d in sk.items() if d)), b, ' '.join(sorted(g for g, d in sk.items() if not d)), na))
    ok = bool(rep) and same / len(rep) >= 0.75 and p < 0.05
    rd.rec(key, title, '%d of %d lean the same way, p = %.4f' % (same, len(rep), p), ok)
    return ok


def main():
    rd = R.Round('Three-hundred-and-seventy-first registered predictions: goal loop 17, region and object kind separated', 'predict_test371')
    _, (tr, te) = L.splits_c()
    reg = lambda t: R.region(L.META.get(t, ('', '', ''))[0])
    o1 = test(tr, te, reg, 'sindh', 'north', lambda t: L.SUBTYPE.get(t) == 'SEAL:S', rd, 'SR1', 'region within square seals')
    o2 = test(tr, te, lambda t: L.SUBTYPE.get(t), 'SEAL:S', 'TAB:B', lambda t: reg(t) == 'north', rd, 'SR2', 'object kind within the north')
    rd.rec('P', 'progress rule: either holds', 'SR1 %s, SR2 %s' % (o1, o2), o1 or o2)
    rd.finish()


if __name__ == '__main__':
    main()
