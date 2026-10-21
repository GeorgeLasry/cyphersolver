"""Step 2: rebuild the code from (cipher run, plaintext span) pairs by hard EM.
Each code group (number + mark type, or number only with --nomarks) stands for one plaintext piece: a word, a part
of a word (syllable/letters), several words, or nothing (null).  The plaintext span of each run is segmented into as
many pieces as the run has groups (Viterbi), pieces are counted, and the counts become the code for the next round.
Library use:  model = fit(runs, keyf, iters)  ;  decode(model, groups, keyf)  ;  segment(model, run, keyf)
"""
import json, math, os, sys, collections
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
MAXL = 22
ALPHA = 1.0


def key_marks(t):
    return t['n'] + (t['m'] or '')


def key_nomarks(t):
    return t['n']


class Run:
    def __init__(self, r):
        self.r = r
        words = r['plain']
        self.s = ''.join(words)
        self.A = len(self.s)
        bset = set([0])
        p = 0
        for w in words:
            p += len(w); bset.add(p)
        self.bset = bset
        A = self.A
        # log prior of a piece starting at a with length L
        lp = np.full((A + 1, MAXL + 1), -np.inf)
        isb = np.array([i in bset for i in range(A + 1)])
        nb = np.cumsum(isb)  # number of boundaries in [0..i]
        for L in range(0, MAXL + 1):
            for a in range(0, A + 1 - L):
                b = a + L
                if L == 0:
                    lp[a, 0] = math.log(0.003); continue
                inner = nb[b - 1] - nb[a]  # boundaries strictly inside (a, b)
                sa, sb = isb[a], isb[b]
                if inner > 2:
                    continue
                if sa and sb:
                    f = 1.0
                elif sa or sb:
                    f = 0.25
                else:
                    f = 0.08
                if not (sa and sb):
                    f *= 0.5 if L == 1 else (1.0 if L <= 4 else (0.5 if L <= 6 else 0.15))
                f *= 0.05 ** inner
                lp[a, L] = math.log(f)
        self.lp = lp
        self.pieces = {}
        for a in range(A + 1):
            for L in range(1, min(MAXL, A - a) + 1):
                self.pieces.setdefault(self.s[a:a + L], []).append(a)

    def viterbi(self, keys, counts, tot):
        A, n = self.A, len(keys)
        dp = np.full(A + 1, -np.inf); dp[0] = 0.0
        back = np.zeros((n, A + 1), dtype=np.int16)
        for i, g in enumerate(keys):
            cg = tot.get(g, 0)
            base = -math.log(cg + ALPHA) + math.log(ALPHA)
            new = np.full(A + 1, -np.inf); bl = np.zeros(A + 1, dtype=np.int16)
            for L in range(0, MAXL + 1):
                if L > A:
                    break
                cand = dp[:A + 1 - L] + self.lp[:A + 1 - L, L] + base
                tgt = new[L:]
                m = cand > tgt
                tgt[m] = cand[m]; bl[L:][m] = L
            for piece, c in counts.get(g, {}).items():
                occ = self.pieces.get(piece)
                if not occ:
                    continue
                L = len(piece)
                a = np.array(occ)
                v = dp[a] + np.log(c + ALPHA * np.exp(self.lp[a, L])) - math.log(cg + ALPHA)
                for aa, vv in zip(a, v):
                    if vv > new[aa + L]:
                        new[aa + L] = vv; bl[aa + L] = L
            dp = new; back[i] = bl
        # backtrack
        segs = []
        b = A
        if not np.isfinite(dp[A]):
            return None, -np.inf
        for i in range(n - 1, -1, -1):
            L = int(back[i][b]); segs.append((b - L, b)); b -= L
        segs = segs[::-1]
        return [self.s[a:b] for a, b in segs], float(dp[A])


def fit(runs, keyf, iters=12, verbose=False, init=None, seed=0):
    """collapsed hard EM: each run is re-segmented with the counts of all OTHER runs (its own removed)"""
    import random
    rnd = random.Random(seed)
    R = [Run(r) for r in runs]
    keys = [[keyf(t) for t in r['groups']] for r in runs]
    base_c, base_t = (init or ({}, {}))
    counts = collections.defaultdict(collections.Counter)
    for g, c in base_c.items():
        counts[g].update(c)
    segs = [None] * len(R)

    def add(k, sign):
        sg = segs[k][0]
        if sg is None:
            return
        for g, p in zip(keys[k], sg):
            counts[g][p] += sign
            if counts[g][p] <= 0:
                del counts[g][p]

    for it in range(iters):
        order = list(range(len(R)))
        rnd.shuffle(order)
        ll = 0; changed = 0
        for k in order:
            if segs[k] is not None:
                add(k, -1)
            tot = {}
            sg, l = R[k].viterbi(keys[k], counts, _Tot(counts))
            if segs[k] is None or segs[k][0] != sg:
                changed += 1
            segs[k] = (sg, l)
            add(k, +1)
            ll += l if sg is not None else 0
        if verbose:
            print('iter', it, 'll %.1f' % ll, 'changed', changed, file=sys.stderr)
        if changed == 0:
            break
    cnt = {g: dict(c) for g, c in counts.items() if c}
    return {'counts': cnt, 'tot': {g: sum(c.values()) for g, c in cnt.items()}, 'segs': segs}


class _Tot(dict):
    def __init__(self, counts):
        self.c = counts

    def get(self, g, d=0):
        c = self.c.get(g)
        return sum(c.values()) if c else d


def best(model, g):
    c = model['counts'].get(g)
    if not c:
        return None
    return max(c.items(), key=lambda x: (x[1], len(x[0])))[0]


def decode(model, groups, keyf):
    return [best(model, keyf(t)) for t in groups]


def score(dec, true_str):
    """character similarity of a decode (unknown groups count as '?') against the true plaintext (no spaces)"""
    import difflib
    d = ''.join(x if x is not None else '?' for x in dec)
    sm = difflib.SequenceMatcher(None, d, true_str, autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks()) / max(len(true_str), 1)
