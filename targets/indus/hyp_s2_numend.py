"""Session-2 loop 9: a numeral directly before an ending, against within-line shuffles."""
import random

import rtools as R
import s2kit as K

TITLE = 'numeral directly before an ending'
REG = '''How often a numeral stands directly before 740 / 520, against 500 within-line shuffles (`hyp_s2_numend.py`).

- **NE1** On A numerals stand before an ending less often than in shuffles (p < 0.05): a count does not take the
  ending; the ending attaches to a word.
- **NE2** The same on B.
- Progress rule: NE1 and NE2, unless a past set already established it (then consistency).'''
SUMMARY = ''


def stat(S):
    return sum(1 for t in S for i in range(len(t) - 1) if t[i] in R.NUMS and t[i + 1] in R.END)


def run(rd):
    global SUMMARY
    rnd = random.Random(544)
    DA, DB = K.ab()
    out = []
    for key, name, S in (('NE1', 'A', DA), ('NE2', 'B', DB)):
        S2 = [t for t in S if any(g in R.NUMS for g in t) and any(g in R.END for g in t)]
        obs = stat(S2)
        le = 0
        for _ in range(500):
            sh = []
            for t in S2:
                u = list(t)
                rnd.shuffle(u)
                sh.append(u)
            le += stat(sh) <= obs
        p = (le + 1) / 501
        rd.rec(key, 'numerals avoid the slot before the ending, %s' % name, '%d observed in %d lines; shuffles as few %d of 500, p = %.4f' % (obs, len(S2), le, p), p < 0.05)
        out.append(p < 0.05)
    SUMMARY = 'A %s, B %s; the name grammar (head before the ending, sets 176-177) implies it: consistency.' % tuple(out)
    return False
