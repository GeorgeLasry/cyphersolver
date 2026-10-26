"""Session-2 loops 42-47: rare signs and positional rules (VARIANT)."""
from collections import Counter

import rtools as R
import s2kit as K
from scipy.stats import fisher_exact, mannwhitneyu

V = 'fishend'
SPEC = {
    'rarepos': ('rare signs stand mid-line', True),
    'rarelong': ('rare signs come in long lines', True),
    'fin400': ('400 after an ending closes the line (consistency)', False),
    'jarinit': ('the jar 740 does not open a line (consistency)', False),
    'numinit': ('numerals open lines more than other signs (consistency)', False),
    'fishend': ('fish signs stand before 520 more than other heads do (consistency)', False),
}
TITLE, PROG = SPEC[V]
REG = '''(`hyp_s2_r.py`, VARIANT=%s). Rare = 3 or fewer tokens in the sample.

- **R1** On A: %s (p < 0.05).
- **R2** The same on B.
- Progress rule: %s''' % (V, TITLE, 'R1 and R2.' if PROG else 'none (re-tests a known rule).')
SUMMARY = ''


def test(S):
    occ = Counter(g for t in S for g in t)
    if V == 'rarepos':
        mid = lambda t, i: 0 < i < len(t) - 1
        r = [mid(t, i) for t in S if len(t) >= 3 for i, g in enumerate(t) if occ[g] <= 3]
        o = [mid(t, i) for t in S if len(t) >= 3 for i, g in enumerate(t) if occ[g] > 3]
        return fisher_exact([[sum(r), len(r) - sum(r)], [sum(o), len(o) - sum(o)]], alternative='greater')[1], '%d/%d vs %d/%d' % (sum(r), len(r), sum(o), len(o))
    if V == 'rarelong':
        a = [len(t) for t in S if any(occ[g] <= 3 for g in t)]
        b = [len(t) for t in S if not any(occ[g] <= 3 for g in t)]
        return mannwhitneyu(a, b, alternative='greater').pvalue, 'mean %.2f (%d) vs %.2f (%d)' % (sum(a) / len(a), len(a), sum(b) / len(b), len(b))
    if V == 'fin400':
        x = [all(g in ('400', '90') for g in t[i + 1:]) for t in S for i in range(len(t)) if t[i] == '400' and i and t[i - 1] in R.END]
        return (0.0 if x and sum(x) / len(x) >= 0.8 else 1.0), '%d of %d final' % (sum(x), len(x))
    if V == 'jarinit':
        a = sum(t[0] == '740' for t in S); n = occ['740']
        return (0.0 if n and a / n < 0.02 else 1.0), '%d of %d initial' % (a, n)
    if V == 'numinit':
        x = [i == 0 for t in S for i, g in enumerate(t) if g in R.NUMS]
        y = [i == 0 for t in S for i, g in enumerate(t) if g not in R.NUMS]
        return fisher_exact([[sum(x), len(x) - sum(x)], [sum(y), len(y) - sum(y)]], alternative='greater')[1], '%d/%d vs %d/%d' % (sum(x), len(x), sum(y), len(y))
    F = {str(x) for x in range(220, 260)}
    x = [t[i + 1] == '520' for t in S for i in range(len(t) - 1) if t[i] in F and t[i + 1] in R.END]
    y = [t[i + 1] == '520' for t in S for i in range(len(t) - 1) if t[i] not in F and t[i + 1] in R.END]
    return fisher_exact([[sum(x), len(x) - sum(x)], [sum(y), len(y) - sum(y)]], alternative='greater')[1], '%d/%d vs %d/%d' % (sum(x), len(x), sum(y), len(y))


def run(rd):
    global SUMMARY
    DA, DB = K.ab()
    pa, ta = test(DA)
    pb, tb = test(DB)
    rd.rec('R1', TITLE + ', A', '%s, p = %.4g' % (ta, pa), pa < 0.05)
    rd.rec('R2', TITLE + ', B', '%s, p = %.4g' % (tb, pb), pb < 0.05)
    SUMMARY = 'A %s; B %s.' % (ta, tb)
    return PROG and pa < 0.05 and pb < 0.05
