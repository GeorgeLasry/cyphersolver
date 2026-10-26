"""Session-2 loop 5: fish signs written next to each other in either order (set 538's free-order pairs)."""
from collections import Counter

import s2kit as K
from scipy.stats import fisher_exact

TITLE = 'fish signs in free order'
REG = '''Set 538 found free-order pairs, many of them two fish signs (220 233 235 240 255 ...). Fish = ICIT 220-259
(`hyp_s2_fishorder.py`). For each unordered pair of distinct signs seen adjacent 3+ times, 'reversible' = both orders
attested.

- **FO1** On A, fish-fish pairs are reversible more often than other pairs (Fisher p < 0.05).
- **FO2** The same on B.
- Progress rule: FO1 and FO2 (the fish signs combine in free order, like stacked modifiers).'''
SUMMARY = ''
FISH = {str(x) for x in range(220, 260)}


def test(S):
    c = Counter()
    for t in S:
        for x in zip(t, t[1:]):
            c[x] += 1
    seen = {}
    for (a, b), n in c.items():
        if a != b:
            k = tuple(sorted((a, b)))
            seen[k] = seen.get(k, 0) + n
    fr = [[0, 0], [0, 0]]
    for (a, b), n in seen.items():
        if n < 3:
            continue
        rev = c[(a, b)] > 0 and c[(b, a)] > 0
        fish = a in FISH and b in FISH
        fr[0 if fish else 1][0 if rev else 1] += 1
    return fr, fisher_exact(fr, alternative='greater')[1]


def run(rd):
    global SUMMARY
    DA, DB = K.ab()
    out = []
    for key, name, S in (('FO1', 'A', DA), ('FO2', 'B', DB)):
        fr, p = test(S)
        ok = p < 0.05 and fr[0][0] / max(1, sum(fr[0])) > fr[1][0] / max(1, sum(fr[1]))
        rd.rec(key, 'fish-fish pairs reversible more often, %s' % name, 'fish %d of %d, others %d of %d, p = %.4f' % (fr[0][0], sum(fr[0]), fr[1][0], sum(fr[1]), p), ok)
        out.append((ok, fr))
    SUMMARY = 'fish pairs reversible A %d/%d vs %d/%d; B %d/%d vs %d/%d.' % (out[0][1][0][0], sum(out[0][1][0]), out[0][1][1][0], sum(out[0][1][1]), out[1][1][0][0], sum(out[1][1][0]), out[1][1][1][0], sum(out[1][1][1]))
    return out[0][0] and out[1][0]
