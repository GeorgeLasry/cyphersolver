"""Session-2 loop 22: lines with two counts: same counted sign or different?"""
import random

import s2kit as K
from numerals import NUMS

TITLE = 'two counts in one line'
REG = '''Lines with two 'numeral + sign' units (sign not a numeral). Share where both units count the same sign, against 1,000
shuffles of counted signs among all such units (`hyp_s2_twocounts.py`).

- **TC1** On A the same-sign share differs from the shuffles (two-sided p < 0.05); direction is B's prediction.
- **TC2** B shows the same direction (p < 0.05 one-sided).
- Progress rule: TC1 and TC2.'''
SUMMARY = ''


def pairs(S):
    out = []
    for t in S:
        u = [t[i] for i in range(1, len(t)) if t[i - 1] in NUMS and t[i] not in NUMS]
        if len(u) >= 2:
            out.append(u[:2])
    return out


def test(P, rnd):
    obs = sum(a == b for a, b in P)
    flat = [x for p in P for x in p]
    null = []
    for _ in range(1000):
        rnd.shuffle(flat)
        null.append(sum(flat[2 * i] == flat[2 * i + 1] for i in range(len(P))))
    return obs, sum(null) / 1000, (sum(x >= obs for x in null) + 1) / 1001, (sum(x <= obs for x in null) + 1) / 1001


def run(rd):
    global SUMMARY
    rnd = random.Random(557)
    DA, DB = K.ab()
    pa = pairs(DA)
    o, m, hi, lo = test(pa, rnd)
    up = o > m
    p1 = min(1, 2 * min(hi, lo))
    rd.rec('TC1', 'same-sign share differs on A', '%d of %d same; shuffles %.1f; p = %.4f' % (o, len(pa), m, p1), p1 < 0.05)
    pb = pairs(DB)
    o2, m2, hi2, lo2 = test(pb, rnd)
    p2 = hi2 if up else lo2
    rd.rec('TC2', 'same direction on B', '%d of %d same; shuffles %.1f; p = %.4f' % (o2, len(pb), m2, p2), p2 < 0.05)
    SUMMARY = 'A %d/%d same (null %.1f); B %d/%d (null %.1f).' % (o, len(pa), m, o2, len(pb), m2)
    return p1 < 0.05 and p2 < 0.05
