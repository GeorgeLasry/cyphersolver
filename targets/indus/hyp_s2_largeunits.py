"""Session-2 loop 19: are the large-number signs units of measure (no ending after them, at the line end)?"""
import rtools as R
import s2kit as K
from hyp_s2_s2common import LARGE, SMALL, units
from scipy.stats import fisher_exact

TITLE = 'large-number signs as units'
REG = '''Counted tokens (directly after a numeral) of set 552's large-number signs (740 left out, being the ending itself)
against its small-number signs (520 left out) (`hyp_s2_largeunits.py`).

- **LU1** On A, large-number tokens are followed by 740 / 520 less often than small-number tokens (Fisher p < 0.05).
- **LU2** The same on B.
- Progress rule: LU1 and LU2 (things counted in large numbers are not named: units / commodities).'''
SUMMARY = ''


def run(rd):
    global SUMMARY
    DA, DB = K.ab()
    out = []
    for key, name, S in (('LU1', 'A', DA), ('LU2', 'B', DB)):
        lg = units(S, LARGE - {'740'})
        sm = units(S, SMALL - {'520'})
        a = sum(i + 1 < len(t) and t[i + 1] in R.END for t, i in lg)
        b = sum(i + 1 < len(t) and t[i + 1] in R.END for t, i in sm)
        p = fisher_exact([[a, len(lg) - a], [b, len(sm) - b]], alternative='less')[1]
        ok = p < 0.05
        rd.rec(key, 'large-number signs take the ending less, %s' % name, 'large %d of %d, small %d of %d, p = %.4f' % (a, len(lg), b, len(sm), p), ok)
        out.append((ok, a, len(lg), b, len(sm)))
    SUMMARY = 'ending after: A large %d/%d vs small %d/%d; B %d/%d vs %d/%d.' % (out[0][1:] + out[1][1:])
    return out[0][0] and out[1][0]
