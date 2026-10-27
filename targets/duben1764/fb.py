"""Soft-EM (forward-backward) aligner: cipher groups -> plaintext substrings of 0..MAXL letters.

Monotone: groups emit consecutive substrings of the plaintext in order; length 0 = null.
Plaintext letters may be skipped at a cost (passages not in the cipher).
Usage: python fb.py <cipher tx> <plain file> [iters] [skip_logp]
Writes fb_key.json (top values per group) and fb_path.txt (Viterbi segmentation).
"""
import sys, json, collections, unicodedata
import numpy as np
sys.stdout.reconfigure(encoding='utf-8')
from wem import load_cipher

import os
MAXL = int(os.environ.get('MAXL', '4'))
if MAXL == 4:
    LPRIOR = np.log(np.array([.06, .35, .35, .18, .06]))
    BIAS = np.array([-3.0, 0.0, 0.0, -1.0, -3.0])  # fixed per-length penalty in the alignment
else:
    LPRIOR = np.log(np.array([.05, .25, .3, .18, .09, .05, .04, .02, .02][:MAXL + 1]))
    BIAS = np.array([-3.0, 0.0, 0.0, -0.5, -1.0, -1.5, -2.0, -2.5, -3.0][:MAXL + 1])


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(ch for ch in s if 'a' <= ch <= 'z')


def lse(a, axis=None):
    m = np.max(a, axis=axis, keepdims=True)
    m = np.where(np.isfinite(m), m, 0)
    r = np.log(np.sum(np.exp(a - m), axis=axis, keepdims=True)) + m
    return np.squeeze(r, axis=axis) if axis is not None else r.item()


def run(t, s, iters=30, skip=-9.0):
    I, J = len(t), len(s)
    toks = sorted(set(t)); ti = {x: k for k, x in enumerate(toks)}
    T = np.array([ti[x] for x in t])
    subs = {'': 0}
    sid = np.full((MAXL + 1, J + 1), -1)
    for L in range(MAXL + 1):
        for j in range(J - L + 1):
            u = s[j:j + L]
            if u not in subs:
                subs[u] = len(subs)
            sid[L, j] = subs[u]
    S = len(subs)
    sublen = np.zeros(S, int)
    for u, k in subs.items():
        sublen[k] = len(u)
    # base distribution over substrings: length prior, uniform within length
    base = np.zeros(S)
    for L in range(MAXL + 1):
        m = sublen == L
        base[m] = LPRIOR[L] - np.log(m.sum())
    logE = np.tile(base, (len(toks), 1))
    NEG = -1e30
    for it in range(iters):
        A = np.full((I + 1, J + 1), NEG); A[0, 0] = 0
        for i in range(I + 1):
            # skips within row i (left to right)
            row = A[i]
            for j in range(1, J + 1):
                row[j] = np.logaddexp(row[j], row[j - 1] + skip)
            if i == I:
                break
            e = logE[T[i]] + BIAS[sublen]
            for L in range(MAXL + 1):
                js = np.arange(0, J - L + 1)
                v = row[js] + e[sid[L, js]]
                A[i + 1, js + L] = np.logaddexp(A[i + 1, js + L], v)
        Bt = np.full((I + 1, J + 1), NEG); Bt[I, J] = 0
        for i in range(I, -1, -1):
            if i < I:
                e = logE[T[i]] + BIAS[sublen]
                for L in range(MAXL + 1):
                    js = np.arange(0, J - L + 1)
                    Bt[i, js] = np.logaddexp(Bt[i, js], Bt[i + 1, js + L] + e[sid[L, js]])
            row = Bt[i]
            for j in range(J - 1, -1, -1):
                row[j] = np.logaddexp(row[j], row[j + 1] + skip)
        Z = A[I, J]
        C = np.zeros((len(toks), S))
        for i in range(I):
            e = logE[T[i]] + BIAS[sublen]
            for L in range(MAXL + 1):
                js = np.arange(0, J - L + 1)
                p = np.exp(A[i, js] + e[sid[L, js]] + Bt[i + 1, js + L] - Z)
                np.add.at(C[T[i]], sid[L, js], p)
        alpha = 0.5
        P = C + alpha * np.exp(base)[None, :] * 5
        logE = np.log(P / P.sum(1, keepdims=True))
        top = C.max(1).sum() / C.sum()
        print('iter', it, 'logZ', round(Z, 1), 'top-share', round(top, 3), flush=True)
    inv = {k: u for u, k in subs.items()}
    key = {}
    for x, k in ti.items():
        order = np.argsort(-C[k])[:3]
        key[x] = [(inv[o] or '_', round(float(C[k, o]), 2)) for o in order if C[k, o] > 0.05]
    return key, logE, T, sid, subs


if __name__ == '__main__':
    t = load_cipher(sys.argv[1])
    s = norm(open(sys.argv[2], encoding='utf-8').read())
    iters = int(sys.argv[3]) if len(sys.argv) > 3 else 30
    skip = float(sys.argv[4]) if len(sys.argv) > 4 else -9.0
    key, *_ = run(t, s, iters, skip)
    json.dump(key, open(sys.argv[5] if len(sys.argv) > 5 else 'fb_key.json', 'w', encoding='utf-8'), indent=0)
    cnt = collections.Counter(t)
    for x, _ in cnt.most_common(40):
        print(x, cnt[x], key[x])
