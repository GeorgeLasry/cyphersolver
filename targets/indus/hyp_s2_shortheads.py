"""Session-2 loop 16: do two-sign 'X + ending' lines use the same heads as long lines?"""
import math
import random
from collections import Counter

import rtools as R
import s2kit as K

TITLE = 'heads of short and long lines'
REG = '''Head = sign before an ending. Heads in two-sign lines (X + ending) against heads in lines of 5+ signs; cosine of the two
head distributions, against 500 random splits of the same head tokens into groups of the same sizes (`hyp_s2_shortheads.py`).

- **SH1** On A the cosine is lower than the random splits (p < 0.05): short labels name different things than long texts.
- **SH2** The same on B.
- Progress rule: SH1 and SH2.'''
SUMMARY = ''


def cos(a, b):
    num = sum(a[k] * b[k] for k in a)
    return num / (math.sqrt(sum(v * v for v in a.values())) * math.sqrt(sum(v * v for v in b.values())) or 1)


def run(rd):
    global SUMMARY
    rnd = random.Random(551)
    DA, DB = K.ab()
    out = []
    for key, name, S in (('SH1', 'A', DA), ('SH2', 'B', DB)):
        sh = [t[0] for t in S if len(t) == 2 and t[1] in R.END]
        lo = [t[i] for t in S if len(t) >= 5 for i in range(len(t) - 1) if t[i + 1] in R.END]
        obs = cos(Counter(sh), Counter(lo))
        allh = sh + lo
        le = 0
        for _ in range(500):
            rnd.shuffle(allh)
            le += cos(Counter(allh[:len(sh)]), Counter(allh[len(sh):])) <= obs
        p = (le + 1) / 501
        rd.rec(key, 'short and long lines use different heads, %s' % name, 'cosine %.3f (%d short, %d long heads); random as low %d of 500, p = %.4f' % (obs, len(sh), len(lo), le, p), p < 0.05)
        out.append(p < 0.05)
    SUMMARY = 'A %s, B %s.' % tuple(out)
    return all(out)
