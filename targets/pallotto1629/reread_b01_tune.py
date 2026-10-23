"""Tune the decoder's penalties on R286 against the printed decipherment (crib153.txt) (reread batch b01).
Metric: mean alignment cost per decoded letter, chunks of 110 letters, against the crib's letters."""
import itertools, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import reread_b01_decode as D, reread_b01_align as A
from lang import lm
E = lm.norm(open(os.path.join(HERE, 'crib153.txt'), encoding='utf-8').read(), 'early', False)
segs = D.parse(os.path.join(HERE, 'decode', 'R286.txt'))
runs = [v for k, v in segs if k == 'cipher']
def score():
    tot = 0; nl = 0
    for r in runs:
        toks, _ = D.decode_run(r)
        chunks = []; cur = []; c = 0
        for t in toks:
            cur.append(t); c += len(D.letters(t[2])) if t[0] in 'lw' else 0
            if c >= 110: chunks.append(cur); cur = []; c = 0
        if cur: chunks.append(cur)
        for ch in chunks:
            u = A.tokens_of_run(ch); n = sum(1 for x in u if x[0] == 'L')
            if n < 20: continue
            s, *_ = A.align(u, E); tot += s; nl += n
    return tot / nl
grid = [(-9, -7, -11), (-9, -12, -13), (-9, -99, -13), (-10, -7, -13), (-9, -6, -13)]
for w, p, u in grid:
    D.WORD, D.UNK = w, u
    D.P08 = p
    # P08 is read at parse time: re-parse
    globals()['runs'] = [v for k, v in D.parse(os.path.join(HERE, 'decode', 'R286.txt')) if k == 'cipher']
    print(w, p, u, round(score(), 3), flush=True)
