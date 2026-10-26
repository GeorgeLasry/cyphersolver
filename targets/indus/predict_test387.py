"""Set 387 (goal run loop 33): sign-pair skews between object kinds (split C). Writes results/predict_test387.md."""
from collections import Counter

import loopkit as L
import rtools as R
from scipy.stats import binomtest, fisher_exact


def bigram_test(tr, te, lab, a, b, rd, key, title):
    def cnt(S):
        c = {a: Counter(), b: Counter()}
        for t in S:
            if lab(t) in c:
                c[lab(t)].update(zip(t, t[1:]))
        return c, {k: max(1, sum(v.values())) for k, v in c.items()}
    (ca, na), (cb, nb) = cnt(tr), cnt(te)
    sk = {}
    for g in set(ca[a]) | set(ca[b]):
        x, y = ca[a][g], ca[b][g]
        if x + y >= 8 and fisher_exact([[x, na[a] - x], [y, na[b] - y]])[1] < 0.01:
            sk[g] = x / na[a] > y / na[b]
    rep = [(g, d) for g, d in sk.items() if cb[a][g] + cb[b][g] >= 3]
    same = sum((cb[a][g] / nb[a] > cb[b][g] / nb[b]) == d for g, d in rep)
    p = binomtest(same, len(rep), 0.5, alternative='greater').pvalue if rep else 1
    rd.say('- %s: %d skewed pairs (%s: %s; %s: %s).' % (title, len(sk), a, ' '.join('%s_%s' % g for g, d in sorted(sk.items()) if d), b, ' '.join('%s_%s' % g for g, d in sorted(sk.items()) if not d)))
    ok = bool(rep) and same / len(rep) >= 0.75 and p < 0.05
    rd.rec(key, title, '%d of %d lean the same way on C-test, p = %.4f' % (same, len(rep), p), ok)
    return ok


def main():
    rd = R.Round('Three-hundred-and-eighty-seventh registered predictions: goal loop 33, sign pairs by object kind', 'predict_test387')
    _, (tr, te) = L.splits_c()
    o1 = bigram_test(tr, te, lambda t: L.SUBTYPE.get(t), 'TAB:I', 'TAB:B', rd, 'BG1', 'incised against moulded tablets')
    kind = lambda t: {'SEAL': 'seal', 'TAB': 'tablet'}.get(L.META.get(t, ('', '', ''))[1])
    o2 = bigram_test(tr, te, kind, 'seal', 'tablet', rd, 'BG2', 'seals against tablets')
    rd.rec('P', 'progress rule: either holds', 'BG1 %s, BG2 %s' % (o1, o2), o1 or o2)
    rd.finish()


if __name__ == '__main__':
    main()
