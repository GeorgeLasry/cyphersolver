"""Session-2 loop 7: the same sign twice in a line, not adjacent (a x a), against within-line shuffles."""
import random

import rtools as R
import s2kit as K

TITLE = 'non-adjacent repeats in a line'
REG = '''Lines in which a non-numeral sign occurs twice, not adjacent (`hyp_s2_repeat.py`). Null: each line's signs shuffled
(500 times), which keeps the line's sign counts; a repeat then lands adjacent or not by chance.

- **RP1** On A, repeated signs stand apart (not adjacent) more often than in shuffles, p < 0.05 (repetition is a
  frame, e.g. a x a, rather than doubling).
- **RP2** The same on B.
- Progress rule: RP1 and RP2.'''
SUMMARY = ''


def stat(S):
    tot = 0
    for t in S:
        for i in range(len(t)):
            for j in range(i + 2, len(t)):
                if t[i] == t[j] and t[i] not in R.NUMS:
                    tot += 1
    return tot


def run(rd):
    global SUMMARY
    rnd = random.Random(542)
    DA, DB = K.ab()
    out = []
    for key, name, S in (('RP1', 'A', DA), ('RP2', 'B', DB)):
        S2 = [t for t in S if len(t) >= 3 and len(set(g for g in t if g not in R.NUMS)) < len([g for g in t if g not in R.NUMS])]
        obs = stat(S2)
        ge = 0
        for _ in range(500):
            sh = []
            for t in S2:
                u = list(t)
                rnd.shuffle(u)
                sh.append(u)
            ge += stat(sh) >= obs
        p = (ge + 1) / 501
        rd.rec(key, 'repeats stand apart more than chance, %s' % name, '%d apart-pairs in %d lines with a repeat; shuffles as many or more %d of 500, p = %.4f' % (obs, len(S2), ge, p), p < 0.05)
        out.append(p < 0.05)
    SUMMARY = 'A %s, B %s.' % tuple(out)
    return all(out)
