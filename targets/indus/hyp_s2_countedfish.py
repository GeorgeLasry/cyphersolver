"""Session-2 loop 26: does a counted fish take a different ending from an uncounted fish?"""
import rtools as R
import s2kit as K
from numerals import NUMS
from scipy.stats import fisher_exact

TITLE = 'endings after counted fish'
REG = '''Fish signs (220-259) directly followed by an ending; counted (a numeral before the fish) against uncounted; share of
520 among the endings (`hyp_s2_countedfish.py`).

- **CF1** On A the 520 share differs between counted and uncounted fish (Fisher p < 0.05); direction is B's prediction.
- **CF2** Same direction on B (one-sided p < 0.05).
- Progress rule: CF1 and CF2.'''
SUMMARY = ''
FISH = {str(x) for x in range(220, 260)}


def tab(S):
    a = [[0, 0], [0, 0]]
    for t in S:
        for i in range(len(t) - 1):
            if t[i] in FISH and t[i + 1] in R.END:
                row = 0 if i > 0 and t[i - 1] in NUMS else 1
                a[row][0 if t[i + 1] == '520' else 1] += 1
    return a


def run(rd):
    global SUMMARY
    DA, DB = K.ab()
    a = tab(DA)
    p1 = fisher_exact(a)[1]
    up = a[0][0] / max(1, sum(a[0])) > a[1][0] / max(1, sum(a[1]))
    rd.rec('CF1', 'counted fish differ in 520 share on A', 'counted %d of %d, uncounted %d of %d, p = %.4f' % (a[0][0], sum(a[0]), a[1][0], sum(a[1]), p1), p1 < 0.05)
    b = tab(DB)
    p2 = fisher_exact(b, alternative='greater' if up else 'less')[1]
    rd.rec('CF2', 'same on B', 'counted %d of %d, uncounted %d of %d, p = %.4f' % (b[0][0], sum(b[0]), b[1][0], sum(b[1]), p2), p2 < 0.05)
    SUMMARY = 'A counted 520 %d/%d vs %d/%d; B %d/%d vs %d/%d.' % (a[0][0], sum(a[0]), a[1][0], sum(a[1]), b[0][0], sum(b[0]), b[1][0], sum(b[1]))
    return p1 < 0.05 and p2 < 0.05
