"""Session-2 loop 29: audit of set 562 (large-number units at the line end): length and two-sign lines."""
import s2kit as K
from hyp_s2_s2common import LARGE, SMALL, units
from scipy.stats import mannwhitneyu

TITLE = 'audit: unit position by line length'
REG = '''Set 562 restricted to lines of 4+ signs (a unit cannot fill the line) and compared within length bands 4, 5, 6+
(`hyp_s2_posaudit.py`).

- **PA1** On A, in lines of 4+ signs, large units stand later than small units (Mann-Whitney p < 0.05) and in every
  length band the large mean is later.
- **PA2** On B, lines of 4+ signs, same direction (p < 0.05).
- Progress rule: none (audit); a failure withdraws set 562.'''
SUMMARY = ''


def pos(S, G, f=lambda t: True):
    return [i / (len(t) - 1) for t, i in units(S, G) if len(t) >= 4 and f(t)]


def run(rd):
    global SUMMARY
    DA, DB = K.ab()
    L, Sm = LARGE - {'740'}, SMALL - {'520'}
    la, sa = pos(DA, L), pos(DA, Sm)
    p1 = mannwhitneyu(la, sa, alternative='greater').pvalue
    bands = []
    for lo, hi in ((4, 4), (5, 5), (6, 99)):
        f = lambda t, lo=lo, hi=hi: lo <= len(t) <= hi
        x, y = pos(DA, L, f), pos(DA, Sm, f)
        if x and y:
            bands.append(sum(x) / len(x) > sum(y) / len(y))
    ok1 = p1 < 0.05 and all(bands)
    rd.rec('PA1', 'later in lines of 4+, every band, A', 'large %.2f (%d), small %.2f (%d), p = %.4g; bands later %s' % (sum(la) / len(la), len(la), sum(sa) / len(sa), len(sa), p1, bands), ok1)
    lb, sb = pos(DB, L), pos(DB, Sm)
    p2 = mannwhitneyu(lb, sb, alternative='greater').pvalue if lb and sb else 1
    rd.rec('PA2', 'later in lines of 4+, B', 'large %.2f (%d), small %.2f (%d), p = %.4g' % (sum(lb) / max(1, len(lb)), len(lb), sum(sb) / max(1, len(sb)), len(sb), p2), p2 < 0.05)
    SUMMARY = 'PA1 %s, PA2 %s (audit of set 562).' % (ok1, p2 < 0.05)
    return False
