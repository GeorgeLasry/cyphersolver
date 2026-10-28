"""Melody crib: the Lullaby Elgar played at Wolverhampton in July 1897 (Powell 1937, p. 9).

From the Bavarian Highlands op. 27 no. 3, alto solo bars 23-38 ("Sleep, my son, oh! slumber softly ...
Sleep, oh! sleep, my son"), read by eye from the SHORCHOR 2019 vocal score (src/music/ELGAR_27_3.pdf,
pp. 2-3; D major, 3/4). Ties merged. Duration classes as Hauer et al.: s shorter than a quarter,
q quarter, l longer. E#4 and F4 are kept as one pitch (enharmonic). (The NWC Scriptorium file is a
different 2005 arrangement whose sections and keys do not match the published score; not used.)

Test: every melody segment of >= MINLEN notes at every Dorabella offset; a fit is consistent when one
mapping explains it throughout. Structured: pitch -> orientation and duration class -> arc count, each
one-to-one. Free: (pitch, duration) -> symbol one-to-one. Score = longest consistent fit. Same search on
shuffles of Dorabella and on random melodies drawn from the tune's own notes.

python targets/dorabella/melody_crib.py
"""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
MEL = ('D l, C# q, B l, C# q, D l, C# q, B l, C# q, D l, F# q, A l, A# q, B q, B q, A q, G l, G q, E q, '
       'E q, F# s, G s, D s, C# s, D q, B q, D q, F l, F q, D q, F# q, G l, C# q, D l')
MEL = [tuple(x.split()) for x in MEL.split(', ')]
import sys
MINLEN = int(sys.argv[1]) if len(sys.argv) > 1 else 12
toks = open(os.path.join(HERE, 'ct.txt')).read().split()


def consistent(seg, ct, structured):
    if structured:
        maps = [({}, {}), ({}, {})]                  # pitch<->orientation, duration<->arcs
        for (p, d), t in zip(seg, ct):
            for (f, g), a, b in ((maps[0], p, t[0]), (maps[1], d, t[1])):
                if f.setdefault(a, b) != b or g.setdefault(b, a) != a:
                    return False
        return True
    f, g = {}, {}
    for x, t in zip(seg, ct):
        if f.setdefault(x, t) != t or g.setdefault(t, x) != x:
            return False
    return True


def longest(mel, ct, structured):
    best = (0, None)
    n, M = len(ct), len(mel)
    for i in range(M):                                # melody segment start
        for k in range(n):                            # Dorabella offset
            L = 0
            lo, hi = MINLEN, min(M - i, n - k)        # binary search the longest consistent length
            if hi < lo or not consistent(mel[i:i + lo], ct[k:k + lo], structured):
                continue
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if consistent(mel[i:i + mid], ct[k:k + mid], structured):
                    lo = mid
                else:
                    hi = mid - 1
            if lo > best[0]:
                best = (lo, (i, k))
    return best


rng = np.random.default_rng(0)
for structured in (True, False):
    tag = 'structured' if structured else 'free'
    d = longest(MEL, toks, structured)
    nulls = [longest(MEL, list(rng.permutation(toks)), structured)[0] for _ in range(200)]
    rmel = [longest([MEL[j] for j in rng.integers(0, len(MEL), len(MEL))], toks, structured)[0] for _ in range(200)]
    print(f'{tag:10s}: Dorabella longest fit {d[0]} (melody note {d[1][0] if d[1] else "-"}, offset {d[1][1] if d[1] else "-"}); '
          f'shuffles mean {np.mean(nulls):.1f}, P(>=) {np.mean(np.array(nulls) >= d[0]):.3f}; '
          f'random melodies mean {np.mean(rmel):.1f}, P(>=) {np.mean(np.array(rmel) >= d[0]):.3f}')
