"""Set 370 (goal run loop 16): which signs carry the subtype effect (set 369)? Skews found on split C's training lines,
checked on C's test lines. Writes results/predict_test370.md."""
from collections import Counter

import loopkit as L
import rtools as R
from scipy.stats import binomtest, fisher_exact


def skewtest(tr, te, a, b, rd, key, title):
    def cnt(S):
        c = {a: Counter(), b: Counter()}
        for t in S:
            if L.SUBTYPE.get(t) in c:
                c[L.SUBTYPE[t]].update(t)
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
    rd.say('- %s vs %s: %d skewed on C-train (%s: %s; %s: %s).' % (a, b, len(sk), a, ' '.join(sorted(g for g, d in sk.items() if d)), b, ' '.join(sorted(g for g, d in sk.items() if not d))))
    ok = bool(rep) and same / len(rep) >= 0.75 and p < 0.05
    rd.rec(key, title, '%d of %d with 3+ C-test tokens lean the same way, binomial p = %.4f' % (same, len(rep), p), ok)
    return ok


def main():
    rd = R.Round('Three-hundred-and-seventieth registered predictions: goal loop 16, signs of the object kinds', 'predict_test370')
    _, (tr, te) = L.splits_c()
    o1 = skewtest(tr, te, 'SEAL:S', 'TAB:B', rd, 'SK1', 'square-seal against moulded-tablet signs replicate')
    o2 = skewtest(tr, te, 'TAB:I', 'TAB:C', rd, 'SK2', 'incised against copper tablet signs replicate')
    rd.rec('P', 'progress rule: either holds', 'SK1 %s, SK2 %s' % (o1, o2), o1 or o2)
    rd.finish()


if __name__ == '__main__':
    main()
