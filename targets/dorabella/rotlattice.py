"""Elgar's notebook key with signs drawn turned round.

Each sign may have been written in its own orientation or turned: by 180 degrees (V180), by any multiple of 90 (V90),
mirrored left-right (MLR) or top-bottom (MTB), or any of rotate-180 / both mirrors (KLEIN). Every sign then stands for
a small set of letters (I/J and U/V both allowed); an exact Viterbi search under an order-4 model picks the best English
path. The excess of 180-degree flips (27 against 12.6) is the motivation: if Elgar sometimes reversed a sign, the
notebook key would read through the reversals.

Nulls: the same flexibility under random bijective keys on the real sign order, and the notebook key on shuffled signs.
Power: English passages enciphered with the notebook key, a fraction of signs turned at random, decoded the same way.

python targets/dorabella/rotlattice.py [model] [N]
"""
import os, sys, random
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm, corpora

HERE = os.path.dirname(os.path.abspath(__file__))
toks = open(os.path.join(HERE, 'ct.txt')).read().split()
SEQ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'ij', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'uv', 'w', 'x', 'y', 'z']
SIGNS = [o + str(a) for o in 'ABCDEFGH' for a in (1, 2, 3)]
NOTEBOOK = {s: SEQ[i] for i, s in enumerate(SIGNS)}
VARIANTS = {
    'NONE': lambda o: {o},
    'V180': lambda o: {o, (o + 4) % 8},
    'V90': lambda o: {o, (o + 2) % 8, (o + 4) % 8, (o + 6) % 8},
    'MLR': lambda o: {o, (4 - o) % 8},
    'MTB': lambda o: {o, (8 - o) % 8},
    'KLEIN': lambda o: {o, (o + 4) % 8, (4 - o) % 8, (8 - o) % 8},
}


def cands(tk, key, var, m):
    out = []
    for t in tk:
        o, a = ord(t[0]) - 65, t[1]
        letters = set()
        for o2 in VARIANTS[var](o):
            letters |= set(key[chr(65 + o2) + a])
        out.append(sorted(m.index[c] for c in letters))
    return out


def viterbi(cs, m):
    """Exact best path for an order-4 DenseLM; state = indices chosen at the last three positions."""
    A, lp = m.A, m.lp
    states = {}
    for i0 in cs[0]:
        for i1 in cs[1]:
            for i2 in cs[2]:
                states[(i0, i1, i2)] = (0.0, (i0, i1, i2))
    for p in range(3, len(cs)):
        new = {}
        for (a, b, c), (sc, path) in states.items():
            base = ((a * A + b) * A + c) * A
            for d in cs[p]:
                v = sc + float(lp[base + d])
                k = (b, c, d)
                if k not in new or v > new[k][0]:
                    new[k] = (v, path + (d,))
        states = new
    sc, path = max(states.values())
    return sc / (len(cs) - 3), ''.join(m.alpha[i] for i in path)


def turn(tk, var, frac, rng):
    """Turn a fraction of signs to another orientation allowed by the variant (for controls)."""
    out = []
    for t in tk:
        o = ord(t[0]) - 65
        alts = sorted(VARIANTS[var](o) - {o})
        if alts and rng.random() < frac:
            o = rng.choice(alts)
        out.append(chr(65 + o) + t[1])
    return out


def main():
    model = sys.argv[1] if len(sys.argv) > 1 else 'en-modern'
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    m = lm.load(model, order=4, spaces=False)
    norm = lm.registry()[0][model]['norm']
    corpus = lm.norm(corpora.text(lm.registry()[0][model]['sources'])[:3_000_000], norm, False)
    rng = random.Random(11)
    inv = {}
    for s, ls in NOTEBOOK.items():
        for c in ls:
            inv[c] = s
    print(f'model {model}; nulls {N} random keys, {N} shuffles; controls 8 per variant (35% of signs turned)')
    for var in VARIANTS:
        real, txt = viterbi(cands(toks, NOTEBOOK, var, m), m)
        rk = []
        for _ in range(N):
            p = SEQ[:]; rng.shuffle(p)
            rk.append(viterbi(cands(toks, dict(zip(SIGNS, p)), var, m), m)[0])
        sh = []
        for _ in range(N):
            t = toks[:]; rng.shuffle(t)
            sh.append(viterbi(cands(t, NOTEBOOK, var, m), m)[0])
        ctl = []
        for j in range(8):
            q = rng.randrange(len(corpus) - 87)
            pt = corpus[q:q + 87]
            tk = turn([inv[c] for c in pt], var, 0.35 if var != 'NONE' else 0.0, rng)
            s2, t2 = viterbi(cands(tk, NOTEBOOK, var, m), m)
            ctl.append((s2, sum(x == y for x, y in zip(t2, pt)) / 87))
        prk = sum(x >= real for x in rk) / N
        psh = sum(x >= real for x in sh) / N
        cs = ' '.join(f'{s:.2f}/{a:.2f}' for s, a in ctl)
        print(f'{var:5s} note {real:.3f} | random keys max {max(rk):.3f} mean {np.mean(rk):.3f} P {prk:.3f} | '
              f'shuffles max {max(sh):.3f} P {psh:.3f} | controls score/acc {cs}', flush=True)
        print(f'       {txt}', flush=True)


if __name__ == '__main__':
    main()
