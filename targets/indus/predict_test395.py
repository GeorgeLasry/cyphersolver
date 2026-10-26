"""Set 395 (goal run loop 41): two claims of Wells 1998 through the concordance (set 394): markers 193 / 196 / 231
(ICIT 2, 1, 60) as word dividers; 290-292 (ICIT 741, 742, 745) as case endings like 288 (740). A, replicated on B.
Writes results/predict_test395.md."""
import math
import random
from collections import Counter

import rtools as R
from signs import load

DIV = {'2', '1', '60'}
STROKED = {'741', '742', '745'}


def cos(a, b):
    num = sum(a[k] * b[k] for k in a)
    den = math.sqrt(sum(v * v for v in a.values())) * math.sqrt(sum(v * v for v in b.values()))
    return num / den if den else 0.0


def divider_test(L, rnd):
    openers = Counter(t[0] for t in L)
    after = Counter(t[i + 1] for t in L for i in range(1, len(t) - 1) if t[i] in DIV and t[i - 1] not in R.NUMS and t[i + 1] not in R.NUMS)
    n = sum(after.values())
    obs = cos(after, openers)
    mids = [(t, i) for t in L for i in range(1, len(t) - 1)]
    ge = 0
    for _ in range(1000):
        c = Counter(t[i + 1] for t, i in rnd.sample(mids, n))
        ge += cos(c, openers) >= obs
    return obs, n, (ge + 1) / 1001


def final(t, i):
    return all(g in ('400', '90') for g in t[i + 1:])


def ending_rate(L, S):
    x = [final(t, i) for t in L for i, g in enumerate(t) if g in S]
    return sum(x) / max(1, len(x)), len(x)


def main():
    rnd = random.Random(395)
    rd = R.Round('Three-hundred-and-ninety-fifth registered predictions: goal loop 41, two claims of Wells 1998', 'predict_test395')
    A, B, *_ = R.load_all()
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    res = [divider_test(L, rnd) for L in (DA, DB)]
    rd.rec('WD1', 'what follows 2 / 1 / 60 (not in a numeral run) resembles line openers, A and B',
           ['A: cosine %.3f over %d tokens, p = %.4f' % res[0], 'B: cosine %.3f over %d tokens, p = %.4f' % res[1]], all(r[2] < 0.05 for r in res))
    out = []
    for L in (DA, DB):
        s, ns = ending_rate(L, STROKED)
        j, nj = ending_rate(L, {'740'})
        out.append((s, ns, j, nj))
    ok = all(s >= 0.5 * j for s, ns, j, nj in out)
    rd.rec('WE1', 'stroked jars close lines at least half as often as 740, A and B',
           ['%s: stroked %.1f%% of %d, 740 %.1f%% of %d' % (k, 100 * s, ns, 100 * j, nj) for k, (s, ns, j, nj) in zip('AB', out)], ok)
    rd.rec('P', 'progress rule: either holds', 'WD1 %s, WE1 %s' % (all(r[2] < 0.05 for r in res), ok), all(r[2] < 0.05 for r in res) or ok)
    rd.finish()


if __name__ == '__main__':
    main()
