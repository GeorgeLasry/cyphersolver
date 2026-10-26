"""Session-2 loop 8: two separated numerals in one line: is the first larger (ledger order)?"""
import s2kit as K
from numerals import NUMS
from scipy.stats import binomtest

TITLE = 'order of two numerals in a line'
REG = '''Lines with two numerals not adjacent (values from numerals.NUMS), unequal values (`hyp_s2_numorder.py`).

- **NO1** On A the first numeral is larger more often than smaller (binomial p < 0.05) or smaller more often; the
  direction found on A is registered as the prediction for B.
- **NO2** B shows the same direction (binomial p < 0.05).
- Progress rule: NO1 and NO2.'''
SUMMARY = ''


def counts(S):
    big = small = 0
    for t in S:
        idx = [i for i, g in enumerate(t) if g in NUMS]
        for a in range(len(idx)):
            for b in range(a + 1, len(idx)):
                if idx[b] - idx[a] >= 2:
                    va, vb = NUMS[t[idx[a]]][0], NUMS[t[idx[b]]][0]
                    big += va > vb
                    small += va < vb
    return big, small


def run(rd):
    global SUMMARY
    DA, DB = K.ab()
    ba, sa = counts(DA)
    pa = binomtest(ba, ba + sa, 0.5).pvalue if ba + sa else 1
    dirn = ba > sa
    rd.rec('NO1', 'a direction on A', 'first larger %d, smaller %d, p = %.4f' % (ba, sa, pa), pa < 0.05)
    bb, sb = counts(DB)
    pb = binomtest(bb if dirn else sb, bb + sb, 0.5, alternative='greater').pvalue if bb + sb else 1
    rd.rec('NO2', 'the same direction on B', 'first larger %d, smaller %d, p = %.4f' % (bb, sb, pb), pb < 0.05)
    SUMMARY = 'A larger-first %d vs %d; B %d vs %d.' % (ba, sa, bb, sb)
    return pa < 0.05 and pb < 0.05
