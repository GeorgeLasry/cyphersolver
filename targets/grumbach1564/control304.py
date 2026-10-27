"""Control for solve304: encipher a 16th-c. German passage of the f. 304r size (63 words, ~273 letters)
in a one-to-one word-divided substitution and see whether the same annealer recovers it.

python targets/grumbach1564/control304.py [seed] [homophones]
homophones = number of letters given a second sign (f. 304r may have some).
"""
import random, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lang import lm, corpora
from solve304 import run, ALPHA
from homo304 import run_cap

seed = int(sys.argv[1]) if len(sys.argv) > 1 else 7
homo = int(sys.argv[2]) if len(sys.argv) > 2 else 0
rnd = random.Random(seed)
raw = lm.norm(corpora.text(['de-dta-1470-1610']), 'early')
words = [w for w in raw.split() if w]
start = rnd.randrange(len(words) - 200)
pt, n0 = [], 0
for w in words[start:]:
    if n0 >= 273: break
    pt.append(w); n0 += len(w)
signs = [f'S{i}' for i in range(40)]
rnd.shuffle(signs)
key = {a: [signs[i]] for i, a in enumerate(ALPHA + 'xy')}
for a in rnd.sample('enrstidahu', homo):
    key[a].append(signs.pop())
ct = [[rnd.choice(key[c]) for c in w if c in key] for w in pt]
ct = [w for w in ct if w]
model = lm.load('de-1500s')
(score, m), t = run_cap(ct, model, restarts=10)
truth = ' '.join(pt)
ok = sum(a == b for a, b in zip(t.replace(' ', ''), ''.join(''.join(c for c in w if c in key) for w in pt)))
n = sum(len(w) for w in ct)
print('TRUTH', truth)
print('GOT  ', t)
print(f'letters right {ok}/{n} = {ok/n:.0%}; per-char {model.score(t)/len(t):.3f} truth {model.score(truth)/len(truth):.3f}')
