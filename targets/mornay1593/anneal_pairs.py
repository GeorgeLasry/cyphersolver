"""Hypothesis A: each printed group is two letter-numbers (2210 = 22|10); anneal number->letter onto fr-1600-letters."""
import os, sys, random, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
M = lm.load('fr-1600-letters', order=4, spaces=False)

def split(t, amb):
    opts = [(int(t[:i]), int(t[i:])) for i in range(1, len(t)) if t[i] != '0' and 1 <= int(t[:i]) <= 24 and 1 <= int(t[i:]) <= 24]
    return opts[amb % len(opts)] if opts else None

L = [l.split('|') for l in open('ciphertext.txt', encoding='utf8') if l[0] in 'PS']
pas = [l[4].split() for l in L]
seqs = []
for p in pas:
    s = []
    for t in p:
        a = split(t, 0); s += list(a)
    seqs.append(s)
syms = sorted({x for s in seqs for x in s})
ALPH = 'abcdefghilmnopqrstuxyz'
FR = dict(zip('esaitnrulodcmpvqfbghxyz', [15.7,8.4,8.0,7.5,7.2,7.1,6.6,6.3,5.8,5.3,4.0,3.3,2.9,2.8,1.6,1.3,1.1,0.9,1.0,0.7,0.4,0.3,0.1]))
FR = {k: v / 100 for k, v in FR.items()}
def score(key):
    lmv = sum(M.per_char(''.join(key[x] for x in s)) * len(s) for s in seqs)
    n = sum(len(s) for s in seqs); cnt = {}
    for s in seqs:
        for x in s: cnt[key[x]] = cnt.get(key[x], 0) + 1
    pen = sum(c * math.log((c / n) / FR.get(k, 0.001)) for k, c in cnt.items())
    return lmv - 1.5 * pen
best_all = None
for restart in range(int(sys.argv[1]) if len(sys.argv) > 1 else 20):
    key = {x: random.choice(ALPH) for x in syms}
    cur = score(key); T = 2.0
    for it in range(20000):
        x = random.choice(syms); old = key[x]; key[x] = random.choice(ALPH)
        new = score(key)
        if new >= cur or random.random() < math.exp((new - cur) / T): cur = new
        else: key[x] = old
        T *= 0.9997
    n = sum(len(s) for s in seqs)
    if best_all is None or cur > best_all[0]: best_all = (cur, dict(key))
    print(restart, round(cur / n, 3), ' | '.join(''.join(key[x] for x in s) for s in seqs))
print('BEST', round(best_all[0] / sum(len(s) for s in seqs), 3))
