"""Solve the cipher runs of scan 027 (Willem Lodewijk, 1594) as a substitution against Dutch.

Input: cipher_027.txt (one run per line: [clear before] S01 S02 | S03 ... [clear after]) and signs_027.md (legend,
with the 028-key letter each sign resembles). Output: the 028-key reading and the best annealed key.
Usage: python solve027.py [restarts] [iters]
"""
import math, os, random, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm

HERE = os.path.dirname(os.path.abspath(__file__))
runs = []
for line in open(os.path.join(HERE, os.environ.get('SRC', 'cipher_027.txt')), encoding='utf8'):
    body = re.sub(r'\[[^\]]*\]', ' ', line).replace('|', ' ')
    toks = [t for t in body.split() if re.fullmatch(r'S\d+|\?', t)]
    if toks:
        runs.append(toks)
legend = {}
for line in open(os.path.join(HERE, 'signs_027.md'), encoding='utf8'):
    m = re.match(r'\W*(S\d+)\W.*?028:.*?sign under ([a-z])\b', line)
    if m:
        legend[m.group(1)] = m.group(2)

seq = [t for r in runs for t in r + ['#']]
signs = sorted({t for t in seq if t.startswith('S')})
print(len(runs), 'runs', sum(len(r) for r in runs), 'signs', len(signs), 'distinct')

model = lm.load(os.environ.get('LM', 'nl-1600'), order=4, spaces=False)


def text(key, sep=' / '):
    return sep.join(''.join(key.get(t, '?') for t in r) for r in runs)


def score(key):
    return sum(model.per_char(''.join(key.get(t, 'x') for t in r)) * len(r) for r in runs) / sum(len(r) for r in runs)


if legend:
    k028 = {s: legend.get(s, '?') for s in signs}
    print('028 key reading:', text(k028)[:400])
    print('028 key score', round(score(k028), 3))

letters = 'abcdefghijklmnoprstuvwz'
CAP = 2  # at most this many signs per letter (homophones), so the anneal cannot collapse onto e/n
restarts = int(sys.argv[1]) if len(sys.argv) > 1 else 20
iters = int(sys.argv[2]) if len(sys.argv) > 2 else 20000


def ok(key, letter):
    return sum(1 for v in key.values() if v == letter) < CAP


best = (-99, None)
for r in range(restarts):
    pool = list(letters) * CAP; random.shuffle(pool)
    key = {s: pool[i] for i, s in enumerate(signs)}
    cur = score(key); T = 0.5
    for i in range(iters):
        if random.random() < 0.5:
            a, b = random.sample(signs, 2); key[a], key[b] = key[b], key[a]; undo = ('swap', a, b)
        else:
            s = random.choice(signs); l = random.choice(letters)
            if not ok(key, l):
                continue
            undo = ('set', s, key[s]); key[s] = l
        new = score(key)
        if new >= cur or random.random() < math.exp((new - cur) / T):
            cur = new
        elif undo[0] == 'swap':
            key[undo[1]], key[undo[2]] = key[undo[2]], key[undo[1]]
        else:
            key[undo[1]] = undo[2]
        T = max(0.005, T * 0.9996)
    if cur > best[0]:
        best = (cur, dict(key))
    print('restart', r, round(cur, 3), text(key)[:100], flush=True)
print('BEST', round(best[0], 3))
print(text(best[1], '\n'))
print(' '.join(f'{s}={best[1][s]}' for s in signs))
