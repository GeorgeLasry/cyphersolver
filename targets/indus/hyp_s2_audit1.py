"""Session-2 loop 18: audits of sets 551 (short-line heads) and 552 (number size and counted sign)."""
import math
import random
from collections import Counter

import loopkit as L
import rtools as R
import s2kit as K
from numerals import NUMS
from scipy.stats import binomtest, fisher_exact
from hyp_s2_shortheads import cos

TITLE = 'audits of short-line heads and number size'
REG = '''Audits (`hyp_s2_audit1.py`); a failure withdraws the finding and recounts the streak.

- **AU1** Set 551 within square seals only (A lines whose subtype is SEAL:S): short and long heads still differ (random
  splits, p < 0.05). Otherwise short labels are another object kind.
- **AU2** Set 552 within short-stroke numerals only (numerals.NUMS kind 'short'): 2+ of the A-skewed signs keep their
  small / large direction at p < 0.1 on A, and 75%+ of testable ones lean the same way on B. Otherwise the effect is the
  numeral series, not the number.
- Progress rule: none (audits).'''
SUMMARY = ''


def run(rd):
    global SUMMARY
    rnd = random.Random(553)
    DA, DB = K.ab()
    S = [t for t in DA if L.SUBTYPE.get(t) == 'SEAL:S']
    sh = [t[0] for t in S if len(t) == 2 and t[1] in R.END]
    lo = [t[i] for t in S if len(t) >= 5 for i in range(len(t) - 1) if t[i + 1] in R.END]
    obs = cos(Counter(sh), Counter(lo))
    allh = sh + lo
    le = 0
    for _ in range(500):
        rnd.shuffle(allh)
        le += cos(Counter(allh[:len(sh)]), Counter(allh[len(sh):])) <= obs
    p1 = (le + 1) / 501
    rd.rec('AU1', 'short-line heads differ within square seals', 'cosine %.3f (%d short, %d long), p = %.4f' % (obs, len(sh), len(lo), p1), p1 < 0.05)

    def cnt(T):
        c = {'s': Counter(), 'l': Counter()}
        for t in T:
            for i in range(1, len(t)):
                if t[i - 1] in NUMS and NUMS[t[i - 1]][1] == 'short' and t[i] not in NUMS:
                    c['s' if NUMS[t[i - 1]][0] <= 3 else 'l'][t[i]] += 1
        return c
    SK = {'176': 1, '233': 1, '235': 1, '240': 1, '520': 1, '61': 1, '803': 1, '806': 1, '368': 0, '390': 0, '405': 0, '407': 0, '575': 0, '585': 0, '740': 0, '900': 0}
    ca, cb = cnt(DA), cnt(DB)
    ns, nl = max(1, sum(ca['s'].values())), max(1, sum(ca['l'].values()))
    keep = []
    for g, d in SK.items():
        a, b = ca['s'][g], ca['l'][g]
        if a + b >= 4 and (a / ns > b / nl) == bool(d) and fisher_exact([[a, ns - a], [b, nl - b]])[1] < 0.1:
            keep.append(g)
    nbs, nbl = max(1, sum(cb['s'].values())), max(1, sum(cb['l'].values()))
    rep = [g for g in SK if cb['s'][g] + cb['l'][g] >= 3]
    same = sum((cb['s'][g] / nbs > cb['l'][g] / nbl) == bool(SK[g]) for g in rep)
    ok2 = len(keep) >= 2 and rep and same / len(rep) >= 0.75
    rd.rec('AU2', 'number size within short strokes', 'kept on A: %s; B same way %d of %d' % (' '.join(keep), same, len(rep)), ok2)
    SUMMARY = 'AU1 %s (p %.3f); AU2 %s (kept %d, B %d/%d).' % (p1 < 0.05, p1, ok2, len(keep), same, len(rep))
    return False
