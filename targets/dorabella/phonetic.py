"""Phonetic English: each sign a speech sound, not a letter (Sams 1970 thought the note partly
phonetic; Elgar's letters spell by sound). en-gutenberg is converted word by word to ARPAbet with the
CMU Pronouncing Dictionary (stress removed; 39 phonemes; words not in the dictionary dropped), no word
breaks. Order-4 model on the phoneme string. Dorabella solved as a strict substitution of its 20 signs
onto phonemes; controls = phoneme strings of random passages, enciphered; nulls = shuffles.
A merged variant folds the 39 phonemes into 24 (the vowel sets AA/AO/AH, IH/IY, UH/UW, ER/R, Z/S, DH/TH,
ZH/SH, NG/N, JH/CH ... see MERGE), the size of Dorabella's sign set.

python targets/dorabella/phonetic.py <cmudict.dict> [merged]
"""
import os, sys, re, random
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm, corpora
from solve import anneal

HERE = os.path.dirname(os.path.abspath(__file__))
PH = 'AA AE AH AO AW AY B CH D DH EH ER EY F G HH IH IY JH K L M N NG OW OY P R S SH T TH UH UW V W Y Z ZH'.split()
MERGE = {'AO': 'AA', 'AH': 'AA', 'IY': 'IH', 'UW': 'UH', 'ER': 'R', 'Z': 'S', 'DH': 'TH', 'ZH': 'SH', 'NG': 'N',
         'JH': 'CH', 'OY': 'OW', 'AW': 'AY', 'Y': 'IH', 'HH': 'HH', 'V': 'F'}
merged = len(sys.argv) > 2 and sys.argv[2] == 'merged'
cmu = {}
for line in open(sys.argv[1], encoding='utf-8', errors='replace'):
    w, *ph = line.split('#')[0].split()                # drop trailing '# comment' words
    if '(' in w or w in cmu:
        continue
    ph = [re.sub(r'\d', '', p) for p in ph]
    cmu[w] = [MERGE.get(p, p) if merged else p for p in ph]
inv = sorted({p for v in cmu.values() for p in v})
ALPHA = ''.join(chr(0x41 + i) if i < 26 else chr(0x61 + i - 26) for i in range(len(inv)))
code = {p: ALPHA[i] for i, p in enumerate(inv)}
words = re.findall(r"[a-z']+", corpora.text(['en-gutenberg'])[:6_000_000].lower())
seq = ''.join(''.join(code[p] for p in cmu[w]) for w in words if w in cmu)
print(f'{len(inv)} phonemes; {len(seq)} phoneme tokens from {len(words)} words', flush=True)
m = lm.DenseLM.build(seq, 4, ALPHA)


def show(key, ct):
    return ' '.join(inv[ALPHA.index(m.alpha[i])] for i in key[ct])


toks = open(os.path.join(HERE, 'ct.txt')).read().split()
syms = sorted(set(toks)); ct = np.array([syms.index(t) for t in toks]); n = len(ct)
sc, key = anneal(ct, len(syms), m, restarts=30, iters=20000, injective=True)
print(f'DORABELLA {sc / n:.3f} {show(key, ct)}', flush=True)
rng = random.Random(6)
for j in range(6):
    p = rng.randrange(len(seq) - n); pt = m.encode(seq[p:p + n])
    lets = sorted(set(pt.tolist())); cx = np.array([lets.index(x) for x in pt])
    s2, k2 = anneal(cx, len(lets), m, restarts=30, iters=20000, seed=10 + j, injective=True)
    print(f'  control {s2 / n:.3f} acc={np.mean(k2[cx] == pt):.2f}', flush=True)
for j in range(6):
    sh = np.random.default_rng(j).permutation(ct)
    s3, _ = anneal(sh, len(syms), m, restarts=30, iters=20000, seed=100 + j, injective=True)
    print(f'  null {s3 / n:.3f}', flush=True)
