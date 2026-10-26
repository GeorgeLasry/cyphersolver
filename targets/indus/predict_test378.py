"""Set 378 (goal run loop 24): seal size and workmanship skews on the fixed split (more power than split C).
Writes results/predict_test378.md."""
from collections import Counter
from statistics import median

import loopkit as L
import rtools as R
from predict_test376 import size
from scipy.stats import binomtest, fisher_exact


def skew(A, B, lab, a, b, rd, key, title):
    def cnt(S):
        c = {a: Counter(), b: Counter()}
        for t in S:
            if lab(t) in c:
                c[lab(t)].update(t)
        return c, {k: max(1, sum(v.values())) for k, v in c.items()}
    (ca, na), (cb, nb) = cnt(A), cnt(B)
    sk = {}
    for g in set(ca[a]) | set(ca[b]):
        x, y = ca[a][g], ca[b][g]
        if x + y >= 10 and fisher_exact([[x, na[a] - x], [y, na[b] - y]])[1] < 0.01:
            sk[g] = x / na[a] > y / na[b]
    rep = [(g, d) for g, d in sk.items() if cb[a][g] + cb[b][g] >= 3]
    same = sum((cb[a][g] / nb[a] > cb[b][g] / nb[b]) == d for g, d in rep)
    p = binomtest(same, len(rep), 0.5, alternative='greater').pvalue if rep else 1
    rd.say('- %s: skewed %s: %s; %s: %s.' % (title, a, ' '.join(sorted(g for g, d in sk.items() if d)), b, ' '.join(sorted(g for g, d in sk.items() if not d))))
    ok = bool(rep) and same / len(rep) >= 0.75 and p < 0.05
    rd.rec(key, title, '%d of %d lean the same way on the fixed test, p = %.4f' % (same, len(rep), p), ok)
    return ok


def main():
    rd = R.Round('Three-hundred-and-seventy-eighth registered predictions: goal loop 24, seal size and workmanship on the fixed split', 'predict_test378')
    (tr, te), _ = L.splits()
    sq = lambda S: [t for t in S if L.SUBTYPE.get(t) == 'SEAL:S']
    A, B = sq(tr), sq(te)
    cut = median(size(t) for t in A if size(t))
    o1 = skew(A, B, lambda t: (('large' if size(t) > cut else 'small') if size(t) else None), 'large', 'small', rd, 'FS1', 'large against small square seals')
    wk = L.field(22)
    q = lambda t: {'Good': 'fine', 'Fine': 'fine', 'Poor': 'poor', 'Fair': 'poor'}.get(wk.get(t))
    o2 = skew(A, B, q, 'fine', 'poor', rd, 'FS2', 'good/fine against poor/fair seals')
    rd.rec('P', 'progress rule: either holds', 'FS1 %s, FS2 %s' % (o1, o2), o1 or o2)
    rd.finish()


if __name__ == '__main__':
    main()
