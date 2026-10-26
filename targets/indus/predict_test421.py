"""Set 421 (goal run loop 67): opening and final signs, seals against tablets (skew test on one position, split C).
Writes results/predict_test421.md."""
from collections import Counter

import loopkit as L
import rtools as R
from scipy.stats import binomtest, fisher_exact


def pos_test(tr, te, kind, pick, rd, key, title):
    def cnt(S):
        c = {'seal': Counter(), 'tablet': Counter()}
        for t in S:
            k = kind(t)
            if k in c:
                c[k][pick(t)] += 1
        return c, {k: max(1, sum(v.values())) for k, v in c.items()}
    (ca, na), (cb, nb) = cnt(tr), cnt(te)
    sk = {}
    for g in set(ca['seal']) | set(ca['tablet']):
        x, y = ca['seal'][g], ca['tablet'][g]
        if x + y >= 10 and fisher_exact([[x, na['seal'] - x], [y, na['tablet'] - y]])[1] < 0.01:
            sk[g] = x / na['seal'] > y / na['tablet']
    rep = [(g, d) for g, d in sk.items() if cb['seal'][g] + cb['tablet'][g] >= 3]
    same = sum((cb['seal'][g] / nb['seal'] > cb['tablet'][g] / nb['tablet']) == d for g, d in rep)
    p = binomtest(same, len(rep), 0.5, alternative='greater').pvalue if rep else 1
    rd.say('- %s: seal %s; tablet %s.' % (title, ' '.join(sorted(g for g, d in sk.items() if d)), ' '.join(sorted(g for g, d in sk.items() if not d))))
    ok = bool(rep) and same / len(rep) >= 0.75 and p < 0.05
    rd.rec(key, title, '%d of %d lean the same way, p = %.4f' % (same, len(rep), p), ok)
    return ok


def main():
    rd = R.Round('Four-hundred-and-twenty-first registered predictions: goal loop 67, opening and final signs by object kind', 'predict_test421')
    _, (tr, te) = L.splits_c()
    kind = lambda t: {'SEAL': 'seal', 'TAB': 'tablet'}.get(L.META.get(t, ('', '', ''))[1])
    o1 = pos_test(tr, te, kind, lambda t: t[0], rd, 'OP1', 'opening signs')
    o2 = pos_test(tr, te, kind, lambda t: t[-1], rd, 'OP2', 'final signs')
    rd.rec('P', 'progress rule: either holds', 'OP1 %s, OP2 %s' % (o1, o2), o1 or o2)
    rd.finish()


if __name__ == '__main__':
    main()
