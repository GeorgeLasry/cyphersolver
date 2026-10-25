"""Test key-sheet alphabets (alpha_XXX.tsv: letter TAB label TAB confidence) against the 1594 letter (cipher_027_v2.txt).

For each sheet: (1) decode with the table as matched and score with nl-1600; (2) keep the high/medium matches fixed
and anneal the rest, to see whether the sheet's values pull the text towards Dutch better than a free solve.
Usage: python test_alpha.py 003 016 029
"""
import math, os, random, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm

HERE = os.path.dirname(os.path.abspath(__file__))
WORD = {'S28', 'S32'}
runs = []
for line in open(os.path.join(HERE, 'cipher_027_v2.txt'), encoding='utf8'):
    body = re.sub(r'\[[^\]]*\]', ' ', line).replace('|', ' ')
    cur = []
    for t in body.split():
        if not re.fullmatch(r'S\d+', t):
            continue
        if t in WORD:
            if cur: runs.append(cur)
            cur = []
        else:
            cur.append(t)
    if cur: runs.append(cur)
signs = sorted({t for r in runs for t in r})
N = sum(len(r) for r in runs)
model = lm.load('nl-1600', order=4, spaces=False)


def score(key):
    return sum(model.per_char(''.join(key.get(t, 'x') for t in r)) * len(r) for r in runs) / N


def show(key):
    return ' / '.join(''.join(key.get(t, '?') for t in r) for r in runs)


def anneal(fixed, iters=20000, cap=3):
    free = [s for s in signs if s not in fixed]
    key = dict(fixed); key.update({s: random.choice('etnadrsoilg') for s in free})
    cur = score(key); T = 0.4
    for _ in range(iters):
        if not free: break
        s = random.choice(free); old = key[s]; key[s] = random.choice('abcdefghiklmnoprstuvwyz')
        if list(key.values()).count(key[s]) > cap:
            key[s] = old; continue
        new = score(key)
        if new >= cur or random.random() < math.exp((new - cur) / T):
            cur = new
        else:
            key[s] = old
        T = max(0.005, T * 0.9996)
    return cur, key


for sheet in sys.argv[1:]:
    path = os.path.join(HERE, f'alpha_{sheet}.tsv')
    table = {}
    for line in open(path, encoding='utf8'):
        if line.startswith('#') or not line.strip():
            continue
        parts = line.rstrip('\n').split('\t')
        if len(parts) >= 2 and re.fullmatch(r'S\d+', parts[1]):
            table.setdefault(parts[1], (parts[0], parts[2] if len(parts) > 2 else 'low'))
    key = {s: v[0] for s, v in table.items()}
    covered = sum(1 for r in runs for t in r if t in key) / N
    print(f'== {sheet}: {len(key)} labels matched, covering {covered:.0%} of the letter signs')
    print('  as matched:', round(score(key), 3), show(key)[:200])
    fixed = {s: v[0] for s, v in table.items() if v[1] in ('high', 'medium')}
    best = max((anneal(fixed) for _ in range(4)), key=lambda x: x[0])
    print('  fixed+anneal:', round(best[0], 3), show(best[1])[:200])
