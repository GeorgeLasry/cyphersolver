"""Session-2 loops 30-33: four follow-ups of set 562 (one module per loop via VARIANT)."""
import os

import rtools as R
import s2kit as K
from hyp_s2_s2common import LARGE, SMALL, units
from scipy.stats import binomtest, fisher_exact

V = 'after'
L, Sm = LARGE - {'740'}, SMALL - {'520'}
OP = {'104', '491', '692', '817', '820', '853', '861', '920'}
SPEC = {
    'after': ('what follows a large unit', 'large units not at the line end are followed by 400 / 90 more often than small units', lambda t, i: i + 1 < len(t) and t[i + 1] in ('400', '90'), lambda t, i: i + 1 < len(t)),
    'before': ('what precedes a small unit', 'small units stand right after the line opening (index 1, after one sign) more often than large units', lambda t, i: i == 1, lambda t, i: True),
    'heading': ('heading lines and large units', 'lines with a large unit open with an opener (set 539) more often than lines with a small unit', None, None),
    'order': ('small before large', 'in lines with both, the small unit precedes the large one (binomial against 50%)', None, None),
}
TITLE, CLAIM, HIT, ELIG = SPEC[V]
REG = '''Follow-up of set 562 (`hyp_s2_unitpack.py`, VARIANT=%s). Large / small = set 552's counted signs (740, 520 out).

- **U1** On A: %s (p < 0.05).
- **U2** The same on B (p < 0.05).
- Progress rule: U1 and U2.''' % (V, CLAIM)
SUMMARY = ''


def two(S):
    if V in ('after', 'before'):
        a = [HIT(t, i) for t, i in units(S, L) if ELIG(t, i)]
        b = [HIT(t, i) for t, i in units(S, Sm) if ELIG(t, i)]
        big = V == 'after'
        x, y = (a, b) if big else (b, a)
        p = fisher_exact([[sum(x), len(x) - sum(x)], [sum(y), len(y) - sum(y)]], alternative='greater')[1]
        return p, '%d of %d against %d of %d' % (sum(x), len(x), sum(y), len(y))
    if V == 'heading':
        lg = {t for t, i in units(S, L)}
        sm = {t for t, i in units(S, Sm)} - lg
        x, y = sum(t[0] in OP for t in lg), sum(t[0] in OP for t in sm)
        p = fisher_exact([[x, len(lg) - x], [y, len(sm) - y]], alternative='greater')[1]
        return p, '%d of %d against %d of %d' % (x, len(lg), y, len(sm))
    pre = n = 0
    for t in S:
        li = [i for tt, i in units([t], L)]
        si = [i for tt, i in units([t], Sm)]
        if li and si:
            n += 1
            pre += min(si) < min(li)
    p = binomtest(pre, n, 0.5, alternative='greater').pvalue if n else 1
    return p, 'small first in %d of %d lines' % (pre, n)


def run(rd):
    global SUMMARY
    DA, DB = K.ab()
    pa, ta = two(DA)
    pb, tb = two(DB)
    rd.rec('U1', CLAIM + ', A', '%s, p = %.4g' % (ta, pa), pa < 0.05)
    rd.rec('U2', CLAIM + ', B', '%s, p = %.4g' % (tb, pb), pb < 0.05)
    SUMMARY = 'A %s; B %s.' % (ta, tb)
    return pa < 0.05 and pb < 0.05
