"""Ciphertext-only homophonic attack on the Garcilaso-cipher passages of R10180 (ct.txt).

Each token type is mapped to one plaintext letter; the score is a 5-gram Spanish model (no spaces) built from
es-golden-age plus Parisi's printed Ferdinand-Escrivà decipherments of 1495-98 (lit/parisi2004.txt), weighted x5.
Usage: python solve.py [restarts] [iters] [--merge]   (--merge folds superscript variants into their base sign)
"""
import os, re, sys, random, math
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
from lang import lm

ALPHA = lm.alphabet('early', spaces=False)


def read_ct(merge=False):
    segs, cur = [], []
    for line in open(os.path.join(HERE, 'ct.txt'), encoding='utf8'):
        if not re.match(r'^(H0|H0b|L\d+) ', line):
            continue
        for t in line.split()[1:]:
            if t == '[gap]':
                if cur: segs.append(cur); cur = []
                continue
            if merge and '^' in t:
                t = t.split('^')[0]
            cur.append(t)
    if cur: segs.append(cur)
    return segs


def build_model():
    cache = os.path.join(HERE, 'lm_es1498.npz')
    if os.path.exists(cache):
        d = np.load(cache)
        return lm.DenseLM(d['lp'], 5, ALPHA)
    corp = ''
    for f in ('es-quijote.txt', 'es-vasto-memorias.txt'):
        p = os.path.join(HERE, '..', '..', 'lang', 'corpora', f)
        corp += open(p, encoding='utf8', errors='ignore').read()
    par = open(os.path.join(HERE, 'lit', 'parisi2004.txt'), encoding='utf8').read()
    i = par.find('=====PAGE 20')
    par = re.sub(r'\n\d+\. \[A\].*', '', par[i:])           # footnotes on readings
    corp = lm.norm(corp, 'early', spaces=False) + lm.norm(par, 'early', spaces=False) * 5
    m = lm.DenseLM.build(corp, 5, ALPHA)
    np.savez_compressed(cache, lp=m.lp)
    return m


def anneal(m, segs, syms, iters, rng, fixed=None):
    S = len(syms)
    sid = {s: i for i, s in enumerate(syms)}
    segidx = [np.array([sid[t] for t in s]) for s in segs]
    freq = np.array([.125, .015, .045, .055, .135, .007, .01, .007, .06, .05, .028, .067, .087, .025, .015, .068,
                     .075, .045, .04, .002, .009, .004])  # a..z early, no j/v/k/w
    letters = [c for c in ALPHA]
    p = np.array([freq[letters.index(c)] if c in letters[:len(freq)] else .005 for c in letters]); p /= p.sum()
    key = rng.choice(len(letters), size=S, p=p)
    if fixed:
        for s, c in fixed.items():
            if s in sid: key[sid[s]] = letters.index(c)
    lock = set(sid[s] for s in (fixed or {}) if s in sid)

    allidx = np.concatenate(segidx)
    W = float(os.environ.get('KLW', 1.0))
    def score(k):
        lp = sum(m.score_idx(k[x]) for x in segidx)
        q = np.bincount(k[allidx], minlength=len(letters)) / len(allidx)
        kl = float(np.sum(np.where(q > 0, q * np.log(np.maximum(q, 1e-9) / p), 0)))
        return lp - W * len(allidx) * kl
    cur = score(key); best, bkey = cur, key.copy()
    T0, T1 = 3.0, 0.05
    free = [i for i in range(S) if i not in lock]
    for it in range(iters):
        T = T0 * (T1 / T0) ** (it / iters)
        i = rng.choice(free); old = key[i]
        if rng.random() < .2:
            j = rng.choice(free); key[i], key[j] = key[j], key[i]
        else:
            j = None; key[i] = rng.integers(len(letters))
        new = score(key)
        if new >= cur or rng.random() < math.exp((new - cur) / T):
            cur = new
            if cur > best: best, bkey = cur, key.copy()
        else:
            if j is None: key[i] = old
            else: key[i], key[j] = key[j], key[i]
    return best, bkey


def main():
    restarts = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    iters = int(sys.argv[2]) if len(sys.argv) > 2 else 40000
    merge = '--merge' in sys.argv
    m = build_model()
    segs = read_ct(merge)
    syms = sorted(set(t for s in segs for t in s))
    n = sum(len(s) for s in segs)
    print(f'{n} tokens, {len(syms)} types, merge={merge}')
    rng = np.random.default_rng(int(os.environ.get('SEED', 1)))
    res = []
    for r in range(restarts):
        b, k = anneal(m, segs, syms, iters, rng)
        txt = ' | '.join(''.join(ALPHA[k[syms.index(t)]] for t in s) for s in segs)
        res.append((b / n, txt, {syms[i]: ALPHA[k[i]] for i in range(len(syms))}))
        print(f'{r:2d} {b / n:7.3f} {txt}', flush=True)
    res.sort(key=lambda x: -x[0])
    print('\nBEST', res[0][0]); print(res[0][1]); print(res[0][2])


if __name__ == '__main__':
    main()
