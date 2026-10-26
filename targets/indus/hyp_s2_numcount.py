"""Session-2 loop 17: does the size of the number decide what is counted?"""
from collections import Counter

import rtools as R
import s2kit as K
from numerals import NUMS
from scipy.stats import binomtest, fisher_exact

TITLE = 'small and large numbers count different signs'
REG = '''Sign directly after a numeral; numerals 1-3 'small', 4+ 'large' (numerals.NUMS values). Counted signs with 6+ A tokens
skewed small / large at p < 0.05 (Fisher) on A (`hyp_s2_numcount.py`).

- **NC1** 3+ skewed signs on A.
- **NC2** 75%+ of skewed signs with 3+ B tokens lean the same way on B (binomial p < 0.05).
- Progress rule: NC1 and NC2.'''
SUMMARY = ''


def cnt(S):
    c = {'s': Counter(), 'l': Counter()}
    for t in S:
        for i in range(1, len(t)):
            if t[i - 1] in NUMS and t[i] not in NUMS:
                c['s' if NUMS[t[i - 1]][0] <= 3 else 'l'][t[i]] += 1
    return c


def run(rd):
    global SUMMARY
    DA, DB = K.ab()
    ca, cb = cnt(DA), cnt(DB)
    ns, nl = sum(ca['s'].values()), sum(ca['l'].values())
    sk = {}
    for g in set(ca['s']) | set(ca['l']):
        a, b = ca['s'][g], ca['l'][g]
        if a + b >= 6 and fisher_exact([[a, ns - a], [b, nl - b]])[1] < 0.05:
            sk[g] = a / ns > b / nl
    nbs, nbl = max(1, sum(cb['s'].values())), max(1, sum(cb['l'].values()))
    rep = [(g, d) for g, d in sk.items() if cb['s'][g] + cb['l'][g] >= 3]
    same = sum((cb['s'][g] / nbs > cb['l'][g] / nbl) == d for g, d in rep)
    p = binomtest(same, len(rep), 0.5, alternative='greater').pvalue if rep else 1
    ok1 = len(sk) >= 3
    ok2 = bool(rep) and same / len(rep) >= 0.75 and p < 0.05
    rd.rec('NC1', '3+ skewed counted signs on A', 'small: %s; large: %s' % (' '.join(sorted(g for g, d in sk.items() if d)), ' '.join(sorted(g for g, d in sk.items() if not d))), ok1)
    rd.rec('NC2', 'skews replicate on B', '%d of %d, p = %.4f' % (same, len(rep), p), ok2)
    SUMMARY = 'skewed %d on A; same way on B %d/%d.' % (len(sk), same, len(rep))
    return ok1 and ok2
