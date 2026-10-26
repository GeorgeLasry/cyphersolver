"""Set 376 (goal run loop 22): seal size (ICIT field 31, first dimension) and the text on square seals; split C.
Writes results/predict_test376.md."""
from collections import Counter
from statistics import median

import loopkit as L
import rtools as R
from scipy.stats import binomtest, fisher_exact, spearmanr


def size(t):
    v = L.field(31).get(t)
    try:
        x = float(v)
    except (TypeError, ValueError):
        return None
    return x if x > 0 else None


def main():
    rd = R.Round('Three-hundred-and-seventy-sixth registered predictions: goal loop 22, seal size', 'predict_test376')
    _, (tr, te) = L.splits_c()
    sq = lambda S: [t for t in S if L.SUBTYPE.get(t) == 'SEAL:S' and size(t)]
    A, B = sq(tr), sq(te)
    cut = median(size(t) for t in A)
    lab = lambda t: 'large' if size(t) > cut else 'small'

    def cnt(S):
        c = {'large': Counter(), 'small': Counter()}
        for t in S:
            c[lab(t)].update(t)
        return c, {k: max(1, sum(v.values())) for k, v in c.items()}
    (ca, na), (cb, nb) = cnt(A), cnt(B)
    sk = {}
    for g in set(ca['large']) | set(ca['small']):
        x, y = ca['large'][g], ca['small'][g]
        if x + y >= 10 and fisher_exact([[x, na['large'] - x], [y, na['small'] - y]])[1] < 0.01:
            sk[g] = x / na['large'] > y / na['small']
    rep = [(g, d) for g, d in sk.items() if cb['large'][g] + cb['small'][g] >= 3]
    same = sum((cb['large'][g] / nb['large'] > cb['small'][g] / nb['small']) == d for g, d in rep)
    p = binomtest(same, len(rep), 0.5, alternative='greater').pvalue if rep else 1
    rd.say('- %d square seals with a size on C-train, %d on C-test; median %.2f. Skewed signs: large %s; small %s.' % (
        len(A), len(B), cut, ' '.join(sorted(g for g, d in sk.items() if d)), ' '.join(sorted(g for g, d in sk.items() if not d))))
    rd.say()
    ok1 = bool(rep) and same / len(rep) >= 0.75 and p < 0.05
    rd.rec('LS1', 'large- and small-seal signs replicate', '%d of %d lean the same way, p = %.4f' % (same, len(rep), p), ok1)
    ra, pa = spearmanr([size(t) for t in A], [len(t) for t in A])
    rb, pb = spearmanr([size(t) for t in B], [len(t) for t in B])
    ok2 = ra > 0 and rb > 0 and pa < 0.05 and pb < 0.05
    rd.rec('LS2', 'longer texts on larger seals', 'C-train rho %.2f (p = %.2g), C-test rho %.2f (p = %.2g)' % (ra, pa, rb, pb), ok2)
    rd.rec('P', 'progress rule: LS1 (a replicated finding)', 'LS1 %s' % ok1, ok1)
    rd.finish()


if __name__ == '__main__':
    main()
