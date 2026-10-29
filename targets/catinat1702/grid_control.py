"""Control for grid_test.py: encipher French in a simulated Item-4-style code (low numbers = single letters,
alphabetical; numbers 110-464 = consonant+vowel syllables in a grid of k columns, column = initial consonant),
take 591 tokens, and save them so grid_test.py can be run on them."""
import os, sys, json, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
k = int(sys.argv[1]); seed = int(sys.argv[2])
rnd = random.Random(seed)
raw = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'lang', 'corpora', 'fr-gutenberg.txt'),
           encoding='utf8', errors='ignore').read()[2000000:2400000]
txt = lm.norm(raw, 'modern', spaces=False)
V = 'aeiou'; C = [c for c in 'bcdfghlmnpqrstvxyz']
cols = {c: i % k for i, c in enumerate(C)}               # consonant -> column (several per column when k < 18)
rows_used = {i: 0 for i in range(k)}; grid = {}
for c in C:
    for v in V:
        col = cols[c]; r = rows_used[col]; rows_used[col] += 1
        n = 110 + r * k + col
        if n <= 464: grid[c + v] = n
low = {}
letters = 'abcdefghijlmnopqrstuvxyz'; n = 1
for ch in letters:                                       # 1-99 alphabetical, about four per letter
    low[ch] = list(range(n, n + 4)); n += 4
pos = rnd.randrange(0, len(txt) - 5000); out = []; i = pos
while len(out) < 591:
    s = txt[i:i + 2]
    if s in grid and rnd.random() < 0.85:
        out.append(grid[s]); i += 2
    else:
        ch = txt[i] if txt[i] in low else 'e'
        out.append(rnd.choice(low[ch])); i += 1
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'control_grid.json'), 'w'))
print('high share', sum(x >= 100 for x in out) / len(out))
