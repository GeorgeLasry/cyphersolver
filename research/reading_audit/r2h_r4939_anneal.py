"""r2h: homophonic-substitution annealer for R4939 (transylvania1645), word divisions kept, hu-modern model.
usage: python r2h_r4939_anneal.py <transcription> [restarts] [fix=c:p,...]
Cipher letters map many-to-one onto plain letters; Y merged with y. Prints the best key and decode."""
import sys, re, random, math, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from lang import lm
m = lm.load('hu-modern', order=5, spaces=True)
AL = m.alphabet if hasattr(m, 'alphabet') else None
lines = [l[3:].rstrip('\n') for l in open(sys.argv[1], encoding='utf-8') if re.match(r'\d\d ', l)]
txt = ' '.join(lines).replace('Y', 'y')
txt = re.sub(r'[^a-z ]', '', txt); txt = re.sub(' +', ' ', txt)
restarts = int(sys.argv[2]) if len(sys.argv) > 2 else 20
fix = {}
if len(sys.argv) > 3:
    for kv in sys.argv[3].split(','):
        a, b = kv.split(':'); fix[a] = b
cl = sorted(set(txt) - {' '})
plain = 'abcdefghijklmnopqrstuvwxyz'
def dec(key): return ''.join(key.get(c, c) for c in txt)
def score(s): return m.score(s) if hasattr(m, 'score') else m.logprob(s)
random.seed(4939)
best = (-1e99, None)
free = [c for c in cl if c not in fix]
for r in range(restarts):
    pool = [p for p in plain if p not in fix.values()]
    random.shuffle(pool)
    key = dict(fix); key.update({c: pool[i] for i, c in enumerate(free)})
    spare = pool[len(free):]
    s = score(dec(key)); T0 = 4.0; N = 8000
    for it in range(N):
        a = random.choice(free)
        if spare and random.random() < 0.3:
            j = random.randrange(len(spare)); old = key[a]; key[a], spare[j] = spare[j], old
            ns = score(dec(key)); T = T0 * (1 - it / N) + 0.05
            if ns >= s or random.random() < math.exp((ns - s) / T): s = ns
            else: spare[j] = key[a]; key[a] = old
        else:
            b = random.choice(free)
            key[a], key[b] = key[b], key[a]
            ns = score(dec(key)); T = T0 * (1 - it / N) + 0.05
            if ns >= s or random.random() < math.exp((ns - s) / T): s = ns
            else: key[a], key[b] = key[b], key[a]
    if s > best[0]: best = (s, dict(key)); print(r, round(s, 1), dec(key)[:200], flush=True)
s, key = best
print('KEY', ' '.join(f'{c}={key[c]}' for c in cl))
print(dec(key))
