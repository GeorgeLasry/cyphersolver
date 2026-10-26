"""Session-2 loop 25: the numbers that count fish against those that count other signs."""
import s2kit as K
from numerals import NUMS
from scipy.stats import mannwhitneyu

TITLE = 'values that count fish'
REG = '''Value of a numeral directly before a fish sign (220-259) against before any other non-numeral (`hyp_s2_fishval.py`).

- **FV1** On A, fish are counted with smaller values (Mann-Whitney p < 0.05).
- **FV2** The same on B.
- Progress rule: none if it only restates set 552 (small numbers count fish); recorded as consistency.'''
SUMMARY = ''
FISH = {str(x) for x in range(220, 260)}


def run(rd):
    global SUMMARY
    DA, DB = K.ab()
    out = []
    for key, name, S in (('FV1', 'A', DA), ('FV2', 'B', DB)):
        f = [NUMS[t[i - 1]][0] for t in S for i in range(1, len(t)) if t[i] in FISH and t[i - 1] in NUMS]
        o = [NUMS[t[i - 1]][0] for t in S for i in range(1, len(t)) if t[i] not in FISH and t[i] not in NUMS and t[i - 1] in NUMS]
        p = mannwhitneyu(f, o, alternative='less').pvalue if f and o else 1
        rd.rec(key, 'fish counted with smaller values, %s' % name, 'mean %.2f (%d) against %.2f (%d), p = %.4g' % (sum(f) / max(1, len(f)), len(f), sum(o) / max(1, len(o)), len(o), p), p < 0.05)
        out.append(p < 0.05)
    SUMMARY = 'A %s, B %s: restates set 552 (consistency).' % tuple(out)
    return False
