"""Strict substitution over every combination of the transcribers' disputed readings.

disputes.json lists, per position, the alternative token another transcription gives
(Schmeh 2017; the Elgar-key reading on Cipher Mysteries) against Hauer's consensus ct.txt.
'?X' alternatives are symbol types that reader holds distinct from every consensus token: they
become new symbols. Key and the 11 binary choices are annealed together (2^11 readings).
Controls: English written in Dorabella's tokens, the same 11 positions disputed, and the
consensus side wrong at a random half of them. Nulls: shuffles carrying their alternatives along.

python targets/dorabella/variants.py [restarts] [controls]
"""
import os, sys, json, random, math
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm, corpora

HERE = os.path.dirname(os.path.abspath(__file__))
TOK = [o + c for o in 'ABCDEFGH' for c in '123']
R = int(sys.argv[1]) if len(sys.argv) > 1 else 20
NC = int(sys.argv[2]) if len(sys.argv) > 2 else 8
m = lm.load('en-modern', order=4, spaces=False)
A = m.A
NS = 24 + 3                                        # 3 slots for '?X' symbol types



def build(ct, disputes):
    """ct: list of token ids; disputes: {pos: alt id}. Returns base array, positions, alternatives."""
    pos = sorted(disputes)
    return np.array(ct), np.array(pos), np.array([disputes[p] for p in pos])


def solve(base, pos, alt, seed, iters=30000):
    rng = random.Random(seed)
    best = (-1e18,)
    for r in range(R):
        key = np.array(rng.sample(range(A), min(NS, A)) + [rng.randrange(A)] * max(0, NS - A))
        ch = np.array([rng.random() < 0.5 for _ in pos])
        def reading(ch):
            c = base.copy(); c[pos[ch]] = alt[ch]; return c
        c = reading(ch)
        cur = m.score_idx(key[c])
        for i in range(iters):
            T = 3.0 * (1 - i / iters) + 0.05
            k2, ch2 = key, ch
            u = rng.random()
            if u < 0.15:
                ch2 = ch.copy(); j = rng.randrange(len(pos)); ch2[j] = not ch2[j]
            elif u < 0.4:
                k2 = key.copy(); s = rng.randrange(NS)
                free = [a for a in range(A) if a not in set(k2.tolist())]
                k2[s] = rng.choice(free) if free else rng.randrange(A)
            else:
                k2 = key.copy(); s, t = rng.randrange(NS), rng.randrange(NS)
                k2[s], k2[t] = k2[t], k2[s]
            c2 = reading(ch2) if ch2 is not ch else c
            sc = m.score_idx(k2[c2])
            if sc >= cur or rng.random() < math.exp((sc - cur) / T):
                key, ch, c, cur = k2, ch2, c2, sc
        if cur > best[0]:
            best = (cur, key.copy(), ch.copy(), c.copy())
    return best


def show(tag, res, truth=None):
    sc, key, ch, c = res
    txt = ''.join(m.alpha[i] for i in key[c])
    extra = f' acc={np.mean(key[c] == truth):.2f}' if truth is not None else ''
    print(f'{tag:10s} {sc / len(c):.3f} alts={int(ch.sum())}/{len(ch)}{extra} {txt}', flush=True)


raw = json.load(open(os.path.join(HERE, sys.argv[3] if len(sys.argv) > 3 else 'disputes.json')))
novel = {}
disp = {}
for p, alts in raw.items():
    a = alts[0]
    if a.startswith('?'):
        a = novel.setdefault(a, 24 + len(novel))
    else:
        a = TOK.index(a)
    disp[int(p)] = a
ct = [TOK.index(t) for t in open(os.path.join(HERE, 'ct.txt')).read().split()]
n = len(ct)
base, pos, alt = build(ct, disp)
print(f'restarts={R} disputed positions={list(pos)}', flush=True)
res = solve(base, pos, alt, 0)
show('DORABELLA', res)
print('  chosen alternatives at:', [int(p) for p, c in zip(pos, res[2]) if c], flush=True)

rng = random.Random(5)
corpus = lm.norm(corpora.text(lm.registry()[0]['en-modern']['sources'])[:3_000_000], 'modern', False)
for j in range(NC):
    p0 = rng.randrange(len(corpus) - n)
    pt = m.encode(corpus[p0:p0 + n])
    tok_of = dict(zip(sorted(set(pt.tolist())), rng.sample(range(24), 24)))
    true_ct = np.array([tok_of[l] for l in pt])
    dpos = sorted(rng.sample(range(n), len(pos)))
    obs, alts = true_ct.copy(), {}
    for q in dpos:                   # each disputed position: one side is the truth, one a neighbour slip
        wrong = ((true_ct[q] // 3 + rng.choice((-1, 1))) % 8) * 3 + true_ct[q] % 3
        if rng.random() < 0.5:
            obs[q], alts[q] = wrong, true_ct[q]      # consensus wrong, alternative right
        else:
            alts[q] = wrong                          # consensus right
    b, pp, aa = build(list(obs), alts)
    show(f'control{j}', solve(b, pp, aa, 10 + j), truth=pt)
for j in range(NC):
    perm = np.random.default_rng(j).permutation(n)
    inv = {int(old): new for new, old in enumerate(perm)}
    b, pp, aa = build([ct[i] for i in perm], {inv[p]: a for p, a in disp.items()})
    show(f'null{j}', solve(b, pp, aa, 100 + j))
