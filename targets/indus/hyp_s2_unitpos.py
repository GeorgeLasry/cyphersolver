"""Session-2 loop 27: where small-number and large-number units stand in the line."""
import s2kit as K
from hyp_s2_s2common import LARGE, SMALL, units
from scipy.stats import mannwhitneyu

TITLE = 'position of small and large units'
REG = '''Relative position (index / (length - 1)) of set 552's counted signs, large group (740 out) against small (520 out)
(`hyp_s2_unitpos.py`).

- **UP1** On A the positions differ (Mann-Whitney two-sided p < 0.05); direction is B's prediction.
- **UP2** Same direction on B (one-sided p < 0.05).
- Progress rule: UP1 and UP2.'''
SUMMARY = ''


def pos(S, G):
    return [i / (len(t) - 1) for t, i in units(S, G) if len(t) > 1]


def run(rd):
    global SUMMARY
    DA, DB = K.ab()
    la, sa = pos(DA, LARGE - {'740'}), pos(DA, SMALL - {'520'})
    p1 = mannwhitneyu(la, sa).pvalue
    later = sum(la) / len(la) > sum(sa) / len(sa)
    rd.rec('UP1', 'positions differ on A', 'large mean %.2f (%d), small %.2f (%d), p = %.4f' % (sum(la) / len(la), len(la), sum(sa) / len(sa), len(sa), p1), p1 < 0.05)
    lb, sb = pos(DB, LARGE - {'740'}), pos(DB, SMALL - {'520'})
    p2 = mannwhitneyu(lb, sb, alternative='greater' if later else 'less').pvalue
    rd.rec('UP2', 'same on B', 'large mean %.2f (%d), small %.2f (%d), p = %.4f' % (sum(lb) / len(lb), len(lb), sum(sb) / len(sb), len(sb), p2), p2 < 0.05)
    SUMMARY = 'A large %.2f vs small %.2f; B %.2f vs %.2f.' % (sum(la) / len(la), sum(sa) / len(sa), sum(lb) / len(lb), sum(sb) / len(sb))
    return p1 < 0.05 and p2 < 0.05
