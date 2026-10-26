"""Session-2 loops from set 599 (third series: signs ranked 121-280, numeral contexts dropped): do two frequent signs of different graphic families fill the same slots?
Pairs fixed in advance: the 60 commonest A signs (numerals, 740, 520 left out) in rank order, paired 1-2, 3-4, ...; pair
k of loop L = pairs 2L-1, 2L of that list, skipping same-family pairs."""
import math
import random
from collections import Counter, defaultdict

import rtools as R
import s2kit as K

LOOP = 17
TITLE = 'substitution pairs'
SUMMARY = ''


def pairlist():
    DA, DB = K.ab()
    c = Counter(g for t in DA for g in t if g not in R.NUMS and g not in R.END)
    top = [g for g, n in c.most_common(280)][120:]
    ps = [(top[i], top[i + 1]) for i in range(0, len(top) - 1, 2)]
    return [(a, b) for a, b in ps if int(a) // 10 != int(b) // 10]


PAIRS = pairlist()[2 * LOOP:2 * LOOP + 2]
REG = '''Pairs %s (`hyp_s2_subst.py`, pair list fixed by A frequency rank before testing). Context = (previous sign, next sign);
contexts whose previous sign is a numeral dropped (set 598); cosine of the two signs' context counts against 500 random partner signs of similar frequency (+-5 ranks).

- **SB1** Pair 1 shares contexts beyond random partners on A and on B (p < 0.05 each).
- **SB2** Pair 2 the same.
- Progress rule: either holds (two signs of different families fill the same slots: a substitution class).''' % ', '.join('%s/%s' % p for p in PAIRS)


def ctx(S):
    d = defaultdict(Counter)
    for t in S:
        s = ('^',) + t + ('$',)
        for i in range(1, len(s) - 1):
            if s[i - 1] not in R.NUMS:
                d[s[i]][(s[i - 1], s[i + 1])] += 1
    return d


def cos(a, b):
    num = sum(a[k] * b[k] for k in a)
    den = math.sqrt(sum(v * v for v in a.values())) * math.sqrt(sum(v * v for v in b.values()))
    return num / den if den else 0.0


def test(S, a, b, rnd):
    d = ctx(S)
    occ = sorted(d, key=lambda g: -sum(d[g].values()))
    obs = cos(d[a], d[b])
    k = occ.index(b) if b in occ else 0
    pool = [g for g in occ[max(0, k - 5):k + 6] if g not in (a, b)]
    ge = sum(cos(d[a], d[rnd.choice(pool)]) >= obs for _ in range(500)) if pool else 500
    return obs, (ge + 1) / 501


def run(rd):
    global SUMMARY
    rnd = random.Random(615 + LOOP)
    DA, DB = K.ab()
    res = []
    for key, (a, b) in zip(('SB1', 'SB2'), PAIRS):
        ca, pa = test(DA, a, b, rnd)
        cb, pb = test(DB, a, b, rnd)
        ok = pa < 0.05 and pb < 0.05
        rd.rec(key, '%s and %s share slots' % (a, b), 'A cosine %.3f p %.3f; B cosine %.3f p %.3f' % (ca, pa, cb, pb), ok)
        res.append(ok)
    SUMMARY = '; '.join('%s/%s %s' % (a, b, o) for (a, b), o in zip(PAIRS, res)) + '.'
    return any(res)
