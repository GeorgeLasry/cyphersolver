"""Audit of set 351 (not registered): the summed chi-square for 300 draws of random sign pairs matched to each marked/base pair's token counts."""
import random, predict_test351 as T, rtools as R
from collections import Counter
from devices import pairs
rnd = random.Random(7)
A, B, *_ = R.load_all()
for name, L in (('A', sorted({tuple(t) for t in A})), ('B', sorted({tuple(t) for t in B}))):
    P = [p for p in pairs() if p['type'] != 'cage' and not p['gm'] <= T.JAR]
    obs = sum(T.chi(T.toks(L, p['gm']), T.toks(L, p['gb'])) for p in P)
    c = Counter(g for t in L for g in t); gs = sorted(c, key=c.get)
    def near(n):
        k = min(range(len(gs)), key=lambda i: abs(c[gs[i]] - n)); return gs[max(0, min(len(gs) - 1, k + rnd.randint(-3, 3)))]
    null = []
    for _ in range(300):
        s = 0
        for p in P:
            na, nb = len(T.toks(L, p['gm'])), len(T.toks(L, p['gb']))
            s += T.chi(T.toks(L, {near(na)}) if na else [], T.toks(L, {near(nb)}) if nb else [])
        null.append(s)
    null.sort(); print(name, 'marked/base %.1f; random matched pairs median %.1f, share >= obs %.3f' % (obs, null[150], sum(x >= obs for x in null) / 300))
