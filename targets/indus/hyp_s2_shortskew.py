"""Session-2 loop 20: which heads belong to short labels (set 551), replicated sign by sign."""
from collections import Counter

import rtools as R
import s2kit as K
from scipy.stats import binomtest, fisher_exact

TITLE = 'the heads of short labels'
REG = '''Heads (sign before an ending) in two-sign lines against lines of 5+ signs; heads with 5+ A tokens skewed at p < 0.05
(Fisher) on A; checked on B (3+ tokens) (`hyp_s2_shortskew.py`).

- **SS1** 3+ skewed heads on A.
- **SS2** 75%+ of the testable ones lean the same way on B (binomial p < 0.05).
- Progress rule: SS1 and SS2.'''
SUMMARY = ''


def heads(S):
    sh = Counter(t[0] for t in S if len(t) == 2 and t[1] in R.END)
    lo = Counter(t[i] for t in S if len(t) >= 5 for i in range(len(t) - 1) if t[i + 1] in R.END)
    return sh, lo


def run(rd):
    global SUMMARY
    DA, DB = K.ab()
    sa, la = heads(DA)
    sb, lb = heads(DB)
    ns, nl = sum(sa.values()), sum(la.values())
    sk = {}
    for g in set(sa) | set(la):
        a, b = sa[g], la[g]
        if a + b >= 5 and fisher_exact([[a, ns - a], [b, nl - b]])[1] < 0.05:
            sk[g] = a / ns > b / nl
    nbs, nbl = max(1, sum(sb.values())), max(1, sum(lb.values()))
    rep = [(g, d) for g, d in sk.items() if sb[g] + lb[g] >= 3]
    same = sum((sb[g] / nbs > lb[g] / nbl) == d for g, d in rep)
    p = binomtest(same, len(rep), 0.5, alternative='greater').pvalue if rep else 1
    ok1, ok2 = len(sk) >= 3, bool(rep) and same / len(rep) >= 0.75 and p < 0.05
    rd.rec('SS1', '3+ skewed heads', 'short-label heads %s; long-text heads %s' % (' '.join(sorted(g for g, d in sk.items() if d)), ' '.join(sorted(g for g, d in sk.items() if not d))), ok1)
    rd.rec('SS2', 'skews replicate on B', '%d of %d, p = %.4f' % (same, len(rep), p), ok2)
    SUMMARY = 'skewed %d; same way on B %d/%d.' % (len(sk), same, len(rep))
    return ok1 and ok2
