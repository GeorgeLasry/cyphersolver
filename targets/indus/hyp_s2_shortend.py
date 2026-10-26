"""Session-2 loop 21: do short labels prefer one ending?"""
import rtools as R
import s2kit as K
from scipy.stats import fisher_exact

TITLE = 'the ending of short labels'
REG = '''Share of 520 among the endings of two-sign lines against lines of 5+ signs (`hyp_s2_shortend.py`).

- **SE1** On A the share differs (Fisher p < 0.05); the direction is the prediction for B.
- **SE2** B shows the same direction (one-sided Fisher p < 0.05).
- Progress rule: SE1 and SE2.'''
SUMMARY = ''


def tab(S):
    sh = [t[1] for t in S if len(t) == 2 and t[1] in R.END]
    lo = [t[i + 1] for t in S if len(t) >= 5 for i in range(len(t) - 1) if t[i + 1] in R.END]
    return [[sh.count('520'), len(sh) - sh.count('520')], [lo.count('520'), len(lo) - lo.count('520')]]


def run(rd):
    global SUMMARY
    DA, DB = K.ab()
    ta = tab(DA)
    pa = fisher_exact(ta)[1]
    up = ta[0][0] / max(1, sum(ta[0])) > ta[1][0] / max(1, sum(ta[1]))
    rd.rec('SE1', 'short labels differ in 520 share on A', 'short %d of %d, long %d of %d, p = %.4f' % (ta[0][0], sum(ta[0]), ta[1][0], sum(ta[1]), pa), pa < 0.05)
    tb = tab(DB)
    pb = fisher_exact(tb, alternative='greater' if up else 'less')[1]
    rd.rec('SE2', 'same direction on B', 'short %d of %d, long %d of %d, p = %.4f' % (tb[0][0], sum(tb[0]), tb[1][0], sum(tb[1]), pb), pb < 0.05)
    SUMMARY = 'A short 520 %d/%d vs long %d/%d; B %d/%d vs %d/%d.' % (ta[0][0], sum(ta[0]), ta[1][0], sum(ta[1]), tb[0][0], sum(tb[0]), tb[1][0], sum(tb[1]))
    return pa < 0.05 and pb < 0.05
