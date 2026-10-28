"""Hypothesis: each sign is the initial letter of a word.

(a) Language model of English word initials (en-gutenberg + KJV + Shakespeare + verse anthology),
    order 3; Dorabella solved as a strict substitution against it, with controls (initials of random
    87-word windows, enciphered at random) and shuffled nulls.
(b) Acrostic of a known text: every 87-word window of those texts. Screen: number of Dorabella's
    equal-symbol pairs whose initials are also equal. Top windows rescored by the best one-to-one
    symbol -> letter assignment (Hungarian): positions explained. Same search for shuffled Dorabella.

python targets/dorabella/initials.py <dir with pg10.txt pg100.txt pg1304.txt> [nulls]
"""
import os, sys, re, random
import numpy as np
from scipy.optimize import linear_sum_assignment
from numpy.lib.stride_tricks import sliding_window_view
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm, corpora
from solve import anneal, text_of

HERE = os.path.dirname(os.path.abspath(__file__))
DL = sys.argv[1]
NN = int(sys.argv[2]) if len(sys.argv) > 2 else 3
AZ = 'abcdefghijklmnopqrstuvwxyz'
toks = open(os.path.join(HERE, 'ct.txt')).read().split()
syms = sorted(set(toks))
ct = np.array([syms.index(t) for t in toks])
n = len(ct)

texts = {'gutenberg': corpora.text(['en-gutenberg'])}
for g, name in (('10', 'KJV'), ('100', 'Shakespeare'), ('1304', 'verse')):
    texts[name] = corpora.strip_gutenberg(open(os.path.join(DL, f'pg{g}.txt'), encoding='utf-8', errors='replace').read())
words = {k: re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", v) for k, v in texts.items()}
init = {k: np.array([AZ.index(w[0].lower()) for w in ws], dtype=np.uint8) for k, ws in words.items()}
print({k: len(v) for k, v in init.items()}, 'words', flush=True)

# ---- (a) initials language model
allinit = ''.join(AZ[i] for v in init.values() for i in v)
m = lm.DenseLM.build(allinit, 3, AZ)
c = np.bincount(np.concatenate(list(init.values())), minlength=26).astype(float)
print(f'IoC of English word initials {((c * (c - 1)).sum() / (c.sum() * (c.sum() - 1))):.4f}; Dorabella 0.0585')
sc, key = anneal(ct, len(syms), m, restarts=20, iters=20000, injective=True)
print(f'(a) DORABELLA {sc / n:.3f} {text_of(m, key, ct)}', flush=True)
rng = random.Random(2)
for j in range(5):
    k = rng.choice(list(init)); v = init[k]; p = rng.randrange(len(v) - n)
    pt = v[p:p + n]; lets = sorted(set(pt.tolist())); cx = np.array([lets.index(x) for x in pt])
    s2, k2 = anneal(cx, len(lets), m, restarts=20, iters=20000, seed=10 + j, injective=True)
    print(f'   control {s2 / n:.3f} acc={np.mean(k2[cx] == pt):.2f}', flush=True)
for j in range(NN):
    sh = np.random.default_rng(j).permutation(ct)
    s3, _ = anneal(sh, len(syms), m, restarts=20, iters=20000, seed=100 + j, injective=True)
    print(f'   null {s3 / n:.3f}', flush=True)


# ---- (b) acrostic window search
def acrostic(seq, tag, top=300):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n) if seq[i] == seq[j]]
    I = np.array([p[0] for p in pairs]); J = np.array([p[1] for p in pairs])
    best = []
    for k, v in init.items():
        W = sliding_window_view(v, n)
        for s in range(0, len(W), 200000):
            Wc = W[s:s + 200000]
            score = (Wc[:, I] == Wc[:, J]).sum(1)
            idx = np.argpartition(-score, min(top, len(score) - 1))[:top]
            best += [(int(score[i]), k, s + int(i)) for i in idx]
    best.sort(reverse=True)
    best = best[:top]
    res = []
    for scr, k, start in best:
        w = init[k][start:start + n]
        M = np.zeros((len(syms), 26))
        for a, b in zip(seq, w):
            M[a, b] += 1
        r_, c_ = linear_sum_assignment(-M)
        res.append((int(M[r_, c_].sum()), scr, k, start))
    res.sort(reverse=True)
    print(f'(b) {tag}: {len(pairs)} equal pairs; best screen {best[0][0]}; best one-to-one fit {res[0][0]}/87', flush=True)
    return res


r = acrostic(ct, 'DORABELLA')
for fit, scr, k, start in r[:3]:
    print(f'   {fit}/87 pairs={scr} {k} word {start}: {" ".join(words[k][start:start + 20])} ...', flush=True)
for j in range(NN):
    acrostic(np.random.default_rng(j).permutation(ct), f'null{j}')
