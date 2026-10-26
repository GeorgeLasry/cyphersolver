"""Session-2 loop 48: audit of set 578 (rare signs in long lines): per-token rate, not per line."""
from collections import Counter

import s2kit as K
from scipy.stats import fisher_exact

TITLE = 'audit: rare-sign rate per token by line length'
REG = '''Set 578 compared lines with and without a rare sign; a longer line has more chances to hold one. Here the share of
tokens that are rare (3 or fewer tokens in the sample), lines of 5+ signs against lines of 2-4 (`hyp_s2_rareaudit.py`).

- **RA1** On A the rare share per token is higher in long lines (Fisher p < 0.05).
- **RA2** The same on B.
- Progress rule: none (audit); if RA1 or RA2 fails, set 578 is withdrawn and the session-2 streak recounted.'''
SUMMARY = ''


def run(rd):
    global SUMMARY
    DA, DB = K.ab()
    out = []
    for key, S in (('RA1', DA), ('RA2', DB)):
        occ = Counter(g for t in S for g in t)
        lo = [occ[g] <= 3 for t in S if len(t) >= 5 for g in t]
        sh = [occ[g] <= 3 for t in S if 2 <= len(t) <= 4 for g in t]
        p = fisher_exact([[sum(lo), len(lo) - sum(lo)], [sum(sh), len(sh) - sum(sh)]], alternative='greater')[1]
        rd.rec(key, 'rare share per token higher in long lines', '%d of %d against %d of %d, p = %.4f' % (sum(lo), len(lo), sum(sh), len(sh), p), p < 0.05)
        out.append(p < 0.05)
    SUMMARY = 'RA1 %s, RA2 %s (audit of set 578).' % tuple(out)
    return False
