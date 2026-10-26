"""Set 384 (goal run loop 30): rectangular (SEAL:R) against square seals. Writes results/predict_test384.md."""
from collections import Counter

import loopkit as L
import rtools as R
from predict_test379 import mantel_haenszel
from scipy.stats import binomtest, fisher_exact


def main():
    rd = R.Round('Three-hundred-and-eighty-fourth registered predictions: goal loop 30, rectangular against square seals', 'predict_test384')
    _, (tr, te) = L.splits_c()
    lab = lambda t: {'SEAL:R': 'rect', 'SEAL:S': 'square'}.get(L.SUBTYPE.get(t))

    def cnt(S):
        c = {'rect': Counter(), 'square': Counter()}
        for t in S:
            if lab(t):
                c[lab(t)].update(t)
        return c, {k: max(1, sum(v.values())) for k, v in c.items()}
    (ca, na), (cb, nb) = cnt(tr), cnt(te)
    sk = {}
    for g in set(ca['rect']) | set(ca['square']):
        x, y = ca['rect'][g], ca['square'][g]
        if x + y >= 10 and fisher_exact([[x, na['rect'] - x], [y, na['square'] - y]])[1] < 0.01:
            sk[g] = x / na['rect'] > y / na['square']
    rep = [(g, d) for g, d in sk.items() if cb['rect'][g] + cb['square'][g] >= 3]
    same = sum((cb['rect'][g] / nb['rect'] > cb['square'][g] / nb['square']) == d for g, d in rep)
    p = binomtest(same, len(rep), 0.5, alternative='greater').pvalue if rep else 1
    rd.say('- skewed: rectangular %s; square %s.' % (' '.join(sorted(g for g, d in sk.items() if d)), ' '.join(sorted(g for g, d in sk.items() if not d))))
    ok1 = bool(rep) and same / len(rep) >= 0.75 and p < 0.05
    rd.rec('BR1', 'rectangular / square skews replicate on C-test', '%d of %d, p = %.4f' % (same, len(rep), p), ok1)
    allines = sorted(set(tr) | set(te))
    band = lambda t: min(max(len(t), 2), 7)
    ends = lambda t: any(g in R.END for g in t[-2:])
    tabs = []
    for b in sorted({band(t) for t in allines}):
        r_ = [ends(t) for t in allines if band(t) == b and lab(t) == 'rect']
        s_ = [ends(t) for t in allines if band(t) == b and lab(t) == 'square']
        tabs.append([[sum(r_), len(r_) - sum(r_)], [sum(s_), len(s_) - sum(s_)]])
    orr, p2 = mantel_haenszel(tabs)
    ok2 = orr < 1 and p2 < 0.05
    rd.rec('BR2', 'rectangular seals close with 740/520 less often at equal length', 'odds ratio %.2f, p = %.4f' % (orr, p2), ok2)
    rd.rec('P', 'progress rule: BR1 (replicated finding)', 'BR1 %s' % ok1, ok1)
    rd.finish()


if __name__ == '__main__':
    main()
