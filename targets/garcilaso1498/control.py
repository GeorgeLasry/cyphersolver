"""Control for solve.py: encipher 315 letters of Spanish (es-gutenberg, not in the model) with a 57-symbol
homophonic key (frequency-proportional homophones) and attack it with the same annealer.
Usage: python control.py [restarts] [iters]"""
import os, sys, random
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
from lang import lm
import solve

rng = np.random.default_rng(3)
txt = open(os.path.join(HERE, '..', '..', 'lang', 'corpora', 'es-gutenberg.txt'), encoding='utf8', errors='ignore').read()
pt = lm.norm(txt[2_000_000:2_003000], 'early', spaces=False)[:315]
letters = sorted(set(pt))
cnt = {c: pt.count(c) for c in letters}
nsym, homs = 57, {c: 1 for c in letters}
while sum(homs.values()) < nsym:
    c = max(letters, key=lambda c: cnt[c] / homs[c]); homs[c] += 1
sym, k = {}, 0
for c in letters:
    sym[c] = [f's{k + i}' for i in range(homs[c])]; k += homs[c]
ct = [random.Random(i).choice(sym[c]) for i, c in enumerate(pt)]
m = solve.build_model()
syms = sorted(set(ct))
restarts = int(sys.argv[1]) if len(sys.argv) > 1 else 6
iters = int(sys.argv[2]) if len(sys.argv) > 2 else 250000
best = None
for r in range(restarts):
    b, key = solve.anneal(m, [ct], syms, iters, rng)
    out = ''.join(solve.ALPHA[key[syms.index(t)]] for t in ct)
    acc = sum(a == b for a, b in zip(out, pt)) / len(pt)
    print(f'{r} {b / len(ct):.3f} acc={acc:.2f} {out[:120]}', flush=True)
print('PLAIN', pt[:120])
