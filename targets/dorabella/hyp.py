"""Hypothesis harness for the Dorabella loop (28 Oct 2026 onward).

Every hypothesis is calibrated the same way and logged to runs/ledger.tsv:
  D       Dorabella's best score under the hypothesis
  nulls   the same procedure on shuffles of Dorabella's signs (order destroyed, symbols kept)
  ctl     the same procedure on English that was put through the hypothesised system (when an encoder exists)
Verdict: 'READING?' if D reaches the control range and clears every null; 'above nulls' if D beats every
null only; 'negative' otherwise; 'no power' if controls do not separate from nulls.

Two kinds:
  solver(name, transform, encoder)  transform(signs) -> token list, solved as a substitution by annealing
  direct(name, family, encoder)     family(signs) -> candidate plaintexts (fully determined systems), best scored

signs are (orientation 0-7, arcs 0-2) in ct.txt notation: A=0 opens right, then clockwise B..H.
"""
import os, sys, random, math, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm, corpora
from solve import anneal

HERE = os.path.dirname(os.path.abspath(__file__))
TOK = [o + c for o in 'ABCDEFGH' for c in '123']
LINES = [[(TOK.index(t) // 3, TOK.index(t) % 3) for t in l.split()]
         for l in open(os.path.join(HERE, 'ct.txt')).read().strip().splitlines()]
SIGNS = sum(LINES, [])
N = len(SIGNS)
M4 = lm.load('en-modern', order=4, spaces=False)
AZ = 'abcdefghijklmnopqrstuvwxyz'
_corpus = None
LEDGER = os.path.join(HERE, 'runs', 'ledger.tsv')


def corpus():
    global _corpus
    if _corpus is None:
        _corpus = lm.norm(corpora.text(['en-gutenberg'])[:4_000_000], 'modern', False)
    return _corpus


def english(n, rng):
    c = corpus(); p = rng.randrange(len(c) - n - 1)
    return c[p:p + n]


def shuffles(k):
    return [[tuple(x) for x in np.random.default_rng(j).permutation(np.array(SIGNS)).tolist()] for j in range(k)]


def doublet_shuffles(k):
    """Random sequences with exactly Dorabella's multiset of adjacent sign pairs (random Eulerian
    walks over its transition multigraph from the same first sign): keeps bigram structure, including
    the opposite-orientation flips, and destroys everything longer."""
    out = []
    for j in range(k):
        rng = random.Random(1000 + j)
        while True:
            edges = {}
            for a, b in zip(SIGNS, SIGNS[1:]):
                edges.setdefault(a, []).append(b)
            for v in edges.values():
                rng.shuffle(v)
            # Hierholzer: random Eulerian trail from SIGNS[0]
            stack, path = [SIGNS[0]], []
            while stack:
                v = stack[-1]
                if edges.get(v):
                    stack.append(edges[v].pop())
                else:
                    path.append(stack.pop())
            path = path[::-1]
            if len(path) == N:
                break
        out.append([tuple(s) for s in path])
    return out


NULLS = 'shuffle'          # or 'doublet'


def lines_of(signs):
    out, i = [], 0
    for l in LINES:
        out.append([tuple(s) for s in signs[i:i + len(l)]]); i += len(l)
    return out


def per_char(text, m=M4):
    return m.per_char(text)


def solve_tokens(tokens, m=M4, R=8, iters=12000, seed=0, injective=True, fixed=None):
    syms = sorted(set(tokens), key=str)
    ct = np.array([syms.index(t) for t in tokens])
    if len(syms) > m.A - (1 if ' ' in m.alpha else 0):
        injective = False
    sc, key = anneal(ct, len(syms), m, restarts=R, iters=iters, seed=seed, injective=injective)
    txt = ''.join(m.alpha[i] for i in key[ct])
    return sc / len(ct), txt, key, syms


def verdict(D, nulls, ctl, acc=None):
    if (ctl and max(ctl) <= max(nulls)) or (acc is not None and np.median(acc) < 0.5):
        return 'no power'
    if D > max(nulls) and ctl and D >= min(ctl):
        return 'READING?'
    if D > max(nulls):
        return 'above nulls'
    return 'negative'


def log(rnd, name, D, nulls, ctl, txt, extra='', acc=None):
    v = verdict(D, nulls, ctl, acc)
    os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
    new = not os.path.exists(LEDGER)
    with open(LEDGER, 'a', encoding='utf-8') as f:
        if new:
            f.write('round\thypothesis\tD\tnulls\tcontrols\tverdict\tbest text\tnote\n')
        nr = f'{min(nulls):.3f}..{max(nulls):.3f}'
        cr = f'{min(ctl):.3f}..{max(ctl):.3f}' if ctl else '-'
        f.write(f'{rnd}\t{name}\t{D:.3f}\t{nr}\t{cr}\t{v}\t{txt[:90]}\t{extra}\n')
    print(f'[R{rnd}] {name:44s} D {D:7.3f} | nulls {min(nulls):.3f}..{max(nulls):.3f} | '
          f'ctl {"-" if not ctl else f"{min(ctl):.3f}..{max(ctl):.3f}"} | {v:11s} | {txt[:60]} {extra}', flush=True)
    return v


def solver(rnd, name, transform, encoder=None, m=M4, nn=3, nc=3, R=8, iters=12000, injective=True):
    """transform(signs)->tokens; encoder(english_text, rng)->signs (a random instance of the system)."""
    D, txt, _, _ = solve_tokens(transform(SIGNS), m, R, iters, 0, injective)
    pool = doublet_shuffles(nn) if NULLS == 'doublet' else shuffles(nn)
    nulls = [solve_tokens(transform(s), m, R, iters, 100 + j, injective)[0] for j, s in enumerate(pool)]
    ctl, accs = [], []
    if encoder:
        rng = random.Random(7)
        for j in range(nc):
            eng = english(N, rng)
            sc, t2, _, _ = solve_tokens(transform(encoder(eng, rng)), m, R, iters, 200 + j, injective)
            ctl.append(sc)
            accs.append(np.mean([a == b for a, b in zip(t2, eng)]))   # one token per letter, aligned
    extra = f'ctl acc {min(accs):.2f}..{max(accs):.2f}' if accs else ''
    return log(rnd, name, D, nulls, ctl, txt, extra + f' [{NULLS} nulls]', accs or None)


def direct(rnd, name, family, encoder=None, m=M4, nn=5, nc=3):
    """family(signs) -> iterable of (plaintext, label); best per-char score wins."""
    def best(signs):
        b = (-1e9, '', '')
        for txt, lab in family(signs):
            if len(txt) < 8:
                continue
            s = m.per_char(txt)
            if s > b[0]:
                b = (s, txt, lab)
        return b
    D = best(SIGNS)
    nulls = [best(s)[0] for s in (doublet_shuffles(nn) if NULLS == 'doublet' else shuffles(nn))]
    ctl = []
    if encoder:
        rng = random.Random(7)
        for j in range(nc):
            ctl.append(best(encoder(english(N, rng), rng))[0])
    return log(rnd, name, D[0], nulls, ctl, D[1], D[2])


def mono_encoder(order_fn=None):
    """English -> signs by a random one-to-one key (letters folded to 24 if needed), then order_fn."""
    def enc(text, rng):
        letters = sorted(set(text))
        cells = rng.sample([(o, a) for o in range(8) for a in range(3)], 24)
        key = {ch: cells[i % 24] for i, ch in enumerate(letters)}
        s = [key[ch] for ch in text]
        return order_fn(s) if order_fn else s
    return enc
