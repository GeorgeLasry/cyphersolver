"""Anchored solve of scan 027: place likely words (cribs), fix their sign values, anneal the rest against nl-1600.

Usage: python solve027b.py cipher_027_v2.txt [iters_per_placement] [top]
Word signs listed under "word signs" in recheck_027.md are taken out of the letter stream (they stand for whole words).
"""
import math, os, random, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = sys.argv[1] if len(sys.argv) > 1 else 'cipher_027_v2.txt'
ITERS = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
TOP = int(sys.argv[3]) if len(sys.argv) > 3 else 12
CRIBS = ['staten', 'soldaten', 'soldaet', 'groningen', 'verdugo', 'coevorden', 'steenwijck', 'vyant', 'leger',
         'oorloch', 'graef', 'excellentie', 'geschut']
CAP = 2
LETTERS = 'abcdefghiklmnoprstuvwyz'

word_signs = set()
rc = os.path.join(HERE, 'recheck_027.md')
if os.path.exists(rc):
    sec = None
    for line in open(rc, encoding='utf8'):
        if re.match(r'#+.*word sign', line, re.I):
            sec = 'w'
        elif line.startswith('#'):
            sec = None
        elif sec == 'w':
            word_signs |= set(re.findall(r'S\d+', line))

runs = []
for line in open(os.path.join(HERE, SRC), encoding='utf8'):
    body = re.sub(r'\[[^\]]*\]', ' ', line).replace('|', ' ')
    toks = [t for t in body.split() if re.fullmatch(r'S\d+', t)]
    # a word sign splits the run into letter stretches
    cur = []
    for t in toks:
        if t in word_signs:
            if cur: runs.append(cur)
            cur = []
        else:
            cur.append(t)
    if cur: runs.append(cur)
signs = sorted({t for r in runs for t in r})
model = lm.load('nl-1600', order=4, spaces=False)
N = sum(len(r) for r in runs)


def score(key):
    return sum(model.per_char(''.join(key.get(t, 'x') for t in r)) * len(r) for r in runs) / N


def show(key):
    return ' / '.join(''.join(key.get(t, '?') for t in r) for r in runs)


def placements():
    out = []
    for w in CRIBS:
        for ri, r in enumerate(runs):
            for i in range(len(r) - len(w) + 1):
                seg = r[i:i + len(w)]
                fix, ok = {}, True
                for s, ch in zip(seg, w):
                    if fix.get(s, ch) != ch:
                        ok = False; break
                    fix[s] = ch
                if ok and sum(1 for c in set(w) if list(fix.values()).count(c) > CAP) == 0:
                    out.append((w, ri, i, fix))
    return out


def anneal(fixed, iters):
    free = [s for s in signs if s not in fixed]
    pool = [c for c in LETTERS * CAP]
    for c in fixed.values():
        if c in pool: pool.remove(c)
    random.shuffle(pool)
    key = dict(fixed); key.update({s: pool[i % len(pool)] for i, s in enumerate(free)})
    cur = score(key); T = 0.4
    for _ in range(iters):
        s = random.choice(free); old = key[s]; key[s] = random.choice(LETTERS)
        if list(key.values()).count(key[s]) > CAP:
            key[s] = old; continue
        new = score(key)
        if new >= cur or random.random() < math.exp((new - cur) / T):
            cur = new
        else:
            key[s] = old
        T = max(0.005, T * 0.999)
    return cur, key


P = placements()
print(len(runs), 'letter stretches', N, 'signs', len(signs), 'distinct;', len(word_signs), 'word signs;', len(P), 'placements')
res = []
for w, ri, i, fix in P:
    sc, key = anneal(fix, ITERS)
    res.append((sc, w, ri, i, key))
res.sort(key=lambda x: -x[0])
for sc, w, ri, i, key in res[:TOP]:
    print(round(sc, 3), w, 'run', ri, 'pos', i, '|', show(key)[:160])
best = res[0]
sc, key = anneal({s: best[4][s] for s in best[4]}, 0)
print('BEST', round(best[0], 3), best[1], best[2], best[3])
print(show(best[4]).replace(' / ', '\n'))
