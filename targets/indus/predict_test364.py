"""Set 364 (goal run loop 10): which signs carry the region effect of set 357? Sindh against the north, discovered on
A, replicated on B. Writes results/predict_test364.md."""
from collections import Counter

import loopkit as L
import rtools as R
from grammar import lexical
from rtools import hyper_ge
from scipy.stats import binomtest, fisher_exact


def counts(S):
    c = {'sindh': Counter(), 'north': Counter()}
    for t in S:
        r = R.region(L.META.get(t, ('', '', ''))[0])
        if r in c:
            c[r].update(t)
    return c


def main():
    rd = R.Round('Three-hundred-and-sixty-fourth registered predictions: goal loop 10, regional signs', 'predict_test364')
    (tr, te), (DA, DB) = L.splits()
    ca, cb = counts(DA), counts(DB)
    na, nb = {k: sum(v.values()) for k, v in ca.items()}, {k: sum(v.values()) for k, v in cb.items()}
    tested, skew = [], {}
    for g in set(ca['sindh']) | set(ca['north']):
        s, n = ca['sindh'][g], ca['north'][g]
        if s + n < 15:
            continue
        tested.append(g)
        odds, p = fisher_exact([[s, na['sindh'] - s], [n, na['north'] - n]])
        if p < 0.01:
            skew[g] = s / na['sindh'] > n / na['north']
    rep = [(g, d) for g, d in skew.items() if cb['sindh'][g] + cb['north'][g] >= 5]
    same = sum((cb['sindh'][g] / nb['sindh'] > cb['north'][g] / nb['north']) == d for g, d in rep)
    pb = binomtest(same, len(rep), 0.5, alternative='greater').pvalue if rep else 1
    rd.say('- %d signs tested (15+ tokens in Sindh + north A lines); %d skewed at p < 0.01 (%d to Sindh).' % (len(tested), len(skew), sum(skew.values())))
    rd.say('- skewed signs: Sindh %s; north %s.' % (' '.join(sorted(g for g, d in skew.items() if d)), ' '.join(sorted(g for g, d in skew.items() if not d))))
    rd.say()
    ok1 = bool(rep) and same / len(rep) >= 0.75 and pb < 0.05
    rd.rec('RG1', 'regional skews replicate on B', '%d of %d skewed signs with 5+ B tokens lean the same way, binomial p = %.4f' % (same, len(rep), pb), ok1)
    lx_s = sum(lexical(g) for g in skew)
    lx_t = sum(lexical(g) for g in tested)
    p2 = hyper_ge(lx_s, len(skew) - lx_s, lx_t - lx_s, (len(tested) - len(skew)) - (lx_t - lx_s))
    ok2 = len(skew) > 0 and lx_s / len(skew) > (lx_t - lx_s) / max(1, len(tested) - len(skew)) and p2 < 0.05
    rd.rec('RG2', 'the skewed signs are lexical more often than the rest', 'lexical %d of %d skewed against %d of %d others, p = %.4f' % (lx_s, len(skew), lx_t - lx_s, len(tested) - len(skew), p2), ok2)
    rd.rec('P', 'progress rule: RG1 (a replicated finding)', 'RG1 %s' % ok1, ok1)
    rd.finish()


if __name__ == '__main__':
    main()
