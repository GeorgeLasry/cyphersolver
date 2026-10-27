"""Seeded anneal for f. 304r: crib-fixed signs held, the rest free (homophones allowed, small penalty)."""
import math, random, sys
from collections import Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lang import lm
from solve304 import words_of, ALPHA

FIX = dict(V='e', S='n', G='d', P='m', L='c', H='k', T='t', **{'6': 'u', '3': 'h'})
words = words_of(Path(__file__).with_name('f304r_transcription.txt'))
model = lm.load('de-1500s')
signs = sorted({t for w in words for t in w})
free = [s for s in signs if s not in FIX]
def text(m): return ' '.join(''.join(m[t] for t in w) for w in words)
def sc(m):
    c = Counter(m.values())
    return model.score(text(m)) - 3.0 * sum(v - 1 for v in c.values())
rnd = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
best = (-1e9, None)
for r in range(12):
    m = dict(FIX); m.update({s: rnd.choice(ALPHA) for s in free})
    cur = sc(m)
    for i in range(6000):
        T = max(0.05, 2.0 * (1 - i / 6000))
        a = rnd.choice(free); old = m[a]; m[a] = rnd.choice(ALPHA)
        new = sc(m)
        if new >= cur or rnd.random() < math.exp((new - cur) / T): cur = new
        else: m[a] = old
    if cur > best[0]: best = (cur, dict(m))
t = text(best[1])
print(round(best[0], 1), round(model.score(t) / len(t), 3))
print(' '.join(f'{k}={best[1][k]}' for k in free))
print(t)
