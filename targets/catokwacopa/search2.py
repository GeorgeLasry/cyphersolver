"""Open-vocabulary exact-merge search for one Catokwacopa line pair (A, B).
Every cipher letter of A and B must be consumed, in order; plaintext letters W. dropped are 'omitted' at a cost.
Scoring = bigram LM (stupid backoff) - omission penalties - onset prior.  Dynamic programme over (i, j) with k-best lists."""
import sys, math, pickle, re, heapq, collections
import ads2 as ads

VOW = set("AEIOUY")
P_VOW, P_DBL, P_CONS, P_FINAL, P_ONSET_B = 1.6, 1.6, 3.2, 1.0, 1.5
import os
MAXOM = int(os.environ.get("MAXOM", "4")); MAXCONSEC = int(os.environ.get("MAXCONSEC", "2"))
RUNPEN = [0.0, 0.0, 0.4, 1.5, 3.0, 5.0, 8.0, 12.0]
USE_RUNS = os.environ.get("RUNS", "1") == "1"
FIRSTOM = os.environ.get("FIRSTOM") == "1"
P_FIRST = 2.5
NBEST = int(os.environ.get("NBEST", "25"))
KBEST = int(os.environ.get("KBEST", "40"))

def load_lm(path=None, mincount=2):
    if path is None: path = os.environ.get("LM", "lm.pkl")
    uni, bi = pickle.load(open(path, "rb"))
    N = sum(uni.values()); V = len(uni)
    vocab = {w.upper(): c for w, c in uni.items() if c >= mincount and (len(w) > 1 or w in ("i", "a", "o"))}
    lp = {w: math.log((c + 0.5) / (N + 0.5 * V)) for w, c in vocab.items()}
    uniU = {w.upper(): c for w, c in uni.items()}
    biU = {}
    for (a, b), c in bi.items():
        if c >= 2: biU[(a.upper(), b.upper())] = c
    return vocab, lp, uniU, biU

def build_trie(vocab):
    root = {}
    for w in vocab:
        node = root
        for ch in w: node = node.setdefault(ch, {})
        node['$'] = w
    return root

class Searcher:
    def __init__(self, A, B, vocab, lp, uniU, biU, trie, names_boost=None):
        self.A, self.B = A.upper(), B.upper(); self.la, self.lb = len(A), len(B)
        self.vocab, self.lp, self.uniU, self.biU, self.trie = vocab, lp, uniU, biU, trie
        self.tcache = {}
    def lm(self, prev, w):
        if prev is not None:
            c = self.biU.get((prev, w))
            if c: return math.log(c / self.uniU[prev])
            return math.log(0.4) + self.lp[w]
        return self.lp[w]
    def transitions(self, i, j):
        if (i, j) in self.tcache: return self.tcache[(i, j)]
        out = []
        A, B, la, lb = self.A, self.B, self.la, self.lb
        def rec(node, i2, j2, om, consec, pen, prev, depth, src0, lastom, lastsrc=None, runs1=0):
            if '$' in node:
                w = node['$']
                if len(w) == 1 or len(w) - om >= 2:
                    p = pen + (P_FINAL if lastom else 0.0)
                    if USE_RUNS: p += RUNPEN[min(runs1, 7)]
                    if src0 == 'B' and w[0] not in VOW: p += P_ONSET_B
                    out.append((w, i2, j2, om, p))
            for ch, child in node.items():
                if ch == '$': continue
                s0 = src0
                if i2 < la and A[i2] == ch:
                    rec(child, i2 + 1, j2, om, 0, pen, ch, depth + 1, s0 or 'A', False, 'A', runs1 + (1 if lastsrc != 'A' else 0))
                if j2 < lb and B[j2] == ch:
                    rec(child, i2, j2 + 1, om, 0, pen, ch, depth + 1, s0 or 'B', False, 'B', runs1)
                if (depth > 0 or (FIRSTOM and ch in VOW)) and om < MAXOM and consec < MAXCONSEC:
                    if depth == 0: c = P_FIRST
                    elif ch in VOW: c = P_VOW
                    elif ch == prev: c = P_DBL
                    else: c = P_CONS
                    rec(child, i2, j2, om + 1, consec + 1, pen + c, ch, depth + 1, s0, True, lastsrc, runs1)
        rec(self.trie, i, j, 0, 0, 0.0, '', 0, None, False)
        self.tcache[(i, j)] = out
        return out
    def run(self, K=None, N=None):
        if N is None: N = NBEST
        if K is None: K = KBEST
        la, lb = self.la, self.lb
        # dp[(i,j)] = list of (score, words_tuple)
        dp = collections.defaultdict(list)
        dp[(0, 0)] = [(0.0, ())]
        order = sorted(((i, j) for i in range(la + 1) for j in range(lb + 1)), key=lambda t: (t[0] + t[1], t[0]))
        for (i, j) in order:
            hyps = dp.get((i, j))
            if not hyps: continue
            # keep best K, diverse in last word
            hyps.sort(key=lambda h: -h[0])
            seen = set(); kept = []
            for h in hyps:
                last = h[1][-1] if h[1] else None
                key = (last,)
                if key in seen and len(kept) >= 8: continue
                seen.add(key); kept.append(h)
                if len(kept) >= K: break
            dp[(i, j)] = kept
            if i == la and j == lb: continue
            for (w, i2, j2, om, pen) in self.transitions(i, j):
                for (sc, words) in kept:
                    prev = words[-1] if words else None
                    s2 = sc + self.lm(prev, w) - pen
                    lst = dp[(i2, j2)]
                    lst.append((s2, words + (w,)))
                    if len(lst) > 8 * K:
                        lst.sort(key=lambda h: -h[0]); del lst[4 * K:]
        final = dp.get((la, lb), [])
        final.sort(key=lambda h: -h[0])
        return final[:N]

def main():
    vocab, lp, uniU, biU = load_lm()
    trie = build_trie(vocab)
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    import os; T = ads.OLD if os.environ.get("TRANS") == "OLD" else ads.BNA
    lines = [int(x) for x in which.split(",")] if which != "all" else sorted(k for k in T if T[k][0])
    for ln in lines:
        A, B = T[ln]
        print(f"=== line {ln}: {A} / {B}")
        s = Searcher(A, B, vocab, lp, uniU, biU, trie)
        for sc, words in s.run():
            print(f"  {sc:8.2f}  {' '.join(words)}")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
