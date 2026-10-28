"""Every 'alphabet in order around the 8 orientations x 3 arc counts' key, with Caesar shift
and reversal, scored by en-modern order 4 (no spaces). Elgar's own notebook table is one of these
layouts, so this family contains a direct reading with his key and its simple variants."""
import os, sys, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm

HERE = os.path.dirname(os.path.abspath(__file__))
toks = open(os.path.join(HERE, 'ct.txt')).read().split()
m = lm.load('en-modern', order=4, spaces=False)
AZ = 'abcdefghijklmnopqrstuvwxyz'
res = []
for drop in itertools.combinations(AZ, 2):
    alpha = ''.join(c for c in AZ if c not in drop)
    for start in range(8):
        for step in (1, -1):
            orient = {chr(65 + (start + step * i) % 8): i for i in range(8)}
            for major in ('orient', 'count'):
                for crev in (False, True):
                    def letter(t):
                        o, c = orient[t[0]], int(t[1]) - 1
                        if crev: c = 2 - c
                        return alpha[o * 3 + c] if major == 'orient' else alpha[c * 8 + o]
                    base = ''.join(letter(t) for t in toks)
                    for sh in range(26):
                        s = ''.join(AZ[(AZ.index(ch) + sh) % 26] for ch in base)
                        for rv in (s, s[::-1]):
                            res.append((m.per_char(rv), rv, drop, start, step, major, crev, sh))
res.sort(reverse=True)
print(len(res), 'candidates')
for r in res[:15]:
    print(f'{r[0]:.3f} {r[1]} drop={"".join(r[2])} start={r[3]} step={r[4]} {r[5]} crev={r[6]} shift={r[7]}')
