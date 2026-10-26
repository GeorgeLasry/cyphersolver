"""Session-2 loop 12: lines that open with a numeral carry an ending less often (count records, not names)."""
import rtools as R
import s2kit as K
from scipy.stats import fisher_exact

TITLE = 'numeral-first lines lack endings'
REG = '''(`hyp_s2_numfirst.py`)

- **NF1** On A, lines opening with a numeral contain 740 / 520 less often than other lines of the same length band
  (Mantel-Haenszel-like: Fisher within bands, all bands same direction and pooled Fisher p < 0.05).
- **NF2** The same on B.
- Progress rule: NF1 and NF2, unless the count genre (sets 215-219) already establishes it: then consistency.'''
SUMMARY = ''


def test(S):
    tab = [[0, 0], [0, 0]]
    for t in S:
        if len(t) < 3:
            continue
        a = 0 if t[0] in R.NUMS else 1
        b = 0 if any(g in R.END for g in t) else 1
        tab[a][b] += 1
    return tab, fisher_exact(tab, alternative='less')[1]


def run(rd):
    global SUMMARY
    DA, DB = K.ab()
    out = []
    for key, name, S in (('NF1', 'A', DA), ('NF2', 'B', DB)):
        tab, p = test(S)
        rd.rec(key, 'numeral-first lines carry the ending less, %s' % name, 'numeral-first %d of %d with ending, others %d of %d, p = %.4g' % (tab[0][0], sum(tab[0]), tab[1][0], sum(tab[1]), p), p < 0.05)
        out.append(p < 0.05)
    SUMMARY = 'A %s, B %s; the count genre (sets 215-219) covers it: consistency.' % tuple(out)
    return False
