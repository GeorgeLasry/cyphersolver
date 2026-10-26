"""Session-2 loop 23: are large-number units a Harappa habit?"""
import loopkit as L
import s2kit as K
from hyp_s2_s2common import LARGE, SMALL, units
from scipy.stats import fisher_exact

TITLE = 'large-number units by city'
REG = '''Lines with a large-number unit against lines with a small-number unit (set 552 groups, 740 and 520 left out); share
from Harappa against Mohenjo-daro (`hyp_s2_largesite.py`).

- **LS1** On A large-number lines are from Harappa more often (Fisher p < 0.05).
- **LS2** The same on B (site from the records; lines without a site left out).
- Progress rule: none: an LS1 + LS2 result would be a confound check on set 552 (site), recorded as an audit.'''
SUMMARY = ''


def run(rd):
    global SUMMARY
    DA, DB = K.ab()
    out = []
    for key, name, S in (('LS1', 'A', DA), ('LS2', 'B', DB)):
        site = lambda t: L.META.get(t, ('', '', ''))[0]
        lg = {t for t, i in units(S, LARGE - {'740'})}
        sm = {t for t, i in units(S, SMALL - {'520'})} - lg
        tab = [[sum(site(t) == 'Harappa' for t in X), sum(site(t) == 'Mohenjo-daro' for t in X)] for X in (lg, sm)]
        p = fisher_exact(tab, alternative='greater')[1]
        rd.rec(key, 'large-number lines from Harappa, %s' % name, 'large H %d / M %d; small H %d / M %d; p = %.4f' % (tab[0][0], tab[0][1], tab[1][0], tab[1][1], p), p < 0.05)
        out.append((p < 0.05, tab))
    SUMMARY = 'A large H/M %s, small %s; B large %s, small %s (audit of set 552).' % (out[0][1][0], out[0][1][1], out[1][1][0], out[1][1][1])
    return False
