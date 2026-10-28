"""Dorabella: substitution attack with calibration.

python targets/dorabella/solve.py <model> [--reverse] [--restarts N] [--controls N]

Solves ct.txt (Hauer et al. 2025 consensus transcription) as a simple substitution
(each of the 24 symbols -> one letter, letters may repeat so homophones are allowed)
by simulated annealing on a no-space n-gram model. Then the same solver is run on
N random 87-letter passages of the model's own corpus, enciphered with a random key
using Dorabella's 24-symbol alphabet (controls), and on N shuffles of Dorabella (nulls).
A real solution should score like the controls, not like the nulls.
"""
import os, sys, random, math
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm, corpora

HERE = os.path.dirname(os.path.abspath(__file__))
NOISE = 0.0


CT = 'ct.txt'


def load_ct(reverse=False):
    toks = open(os.path.join(HERE, CT)).read().split()
    if reverse:
        toks = toks[::-1]
    syms = sorted(set(toks))
    return np.array([syms.index(t) for t in toks]), syms


def anneal(ct, nsym, m, restarts=20, iters=20000, seed=0, injective=False, maxper=2):
    """maxper caps how many symbols may share one letter; without a cap the search
    collapses to 'eeee...', which a backed-off n-gram model scores spuriously well."""
    rng = random.Random(seed)
    A = m.A
    letters = [i for i, c in enumerate(m.alpha) if c != ' ']
    best = (-1e18, None)
    for r in range(restarts):
        key = np.array(rng.sample(range(A), nsym) if nsym <= A else
                       [rng.randrange(A) for _ in range(nsym)])
        if not injective:          # start one symbol per letter where possible, then cap
            key = np.array([letters[i % len(letters)] for i in rng.sample(range(nsym), nsym)])
        cur = m.score_idx(key[ct])
        T0 = 3.0
        for i in range(iters):
            T = T0 * (1 - i / iters) + 0.05
            k2 = key.copy()
            s = rng.randrange(nsym)
            if injective and rng.random() < 0.3:   # bring in a letter no symbol uses yet
                free = [a for a in range(A) if a not in set(k2.tolist())]
                if not free:
                    continue
                k2[s] = rng.choice(free)
            elif injective or rng.random() < 0.5:
                t = rng.randrange(nsym)
                k2[s], k2[t] = k2[t], k2[s]
            else:
                k2[s] = rng.randrange(A)
                if (k2 == k2[s]).sum() > maxper:
                    continue
            sc = m.score_idx(k2[ct])
            if sc >= cur or rng.random() < math.exp((sc - cur) / T):
                key, cur = k2, sc
        if cur > best[0]:
            best = (cur, key.copy())
    return best


def text_of(m, key, ct):
    return ''.join(m.alpha[i] for i in key[ct])


def main():
    model = sys.argv[1] if len(sys.argv) > 1 else 'en-modern'
    rev = '--reverse' in sys.argv
    inj = '--injective' in sys.argv
    R = int(sys.argv[sys.argv.index('--restarts') + 1]) if '--restarts' in sys.argv else 20
    C = int(sys.argv[sys.argv.index('--controls') + 1]) if '--controls' in sys.argv else 10
    global NOISE, CT
    if '--ct' in sys.argv:
        CT = sys.argv[sys.argv.index('--ct') + 1]
    NOISE = float(sys.argv[sys.argv.index('--noise') + 1]) if '--noise' in sys.argv else 0.0
    m = lm.load(model, order=4, spaces=False)
    ct, syms = load_ct(rev)
    n = len(ct)
    norm = lm.registry()[0][model]['norm']
    sc, key = anneal(ct, len(syms), m, restarts=R, injective=inj)
    print(f'{model} rev={rev} inj={inj} DORABELLA {sc / n:.3f}  {text_of(m, key, ct)}', flush=True)
    rng = random.Random(1)
    corpus = lm.norm(corpora.text(lm.registry()[0][model]['sources'])[:3_000_000], norm, False)
    for j in range(C):
        p = rng.randrange(len(corpus) - n)
        pt = m.encode(corpus[p:p + n])
        # encipher with Dorabella's own symbol-frequency structure: random homophonic map
        letters = sorted(set(pt.tolist()))
        sym_of = {l: i for i, l in enumerate(letters)}
        cx = np.array([sym_of[l] for l in pt])
        if NOISE:              # misread symbols: replace a fraction with a random other symbol
            for p in rng.sample(range(n), int(round(NOISE * n))):
                cx[p] = rng.randrange(len(letters))
        s2, k2 = anneal(cx, len(letters), m, restarts=R, seed=j + 10, injective=inj)
        acc = np.mean(k2[cx] == pt)
        print(f'  control {j} {s2 / n:.3f} acc={acc:.2f} {text_of(m, k2, cx)}', flush=True)
    for j in range(C):
        sh = ct.copy()
        np.random.default_rng(j).shuffle(sh)
        s3, k3 = anneal(sh, len(syms), m, restarts=R, seed=j + 100, injective=inj)
        print(f'  null {j} {s3 / n:.3f} {text_of(m, k3, sh)}', flush=True)


if __name__ == '__main__':
    main()
