"""Second criterion for a decode: does it split into real words of its language?

Vocabulary: the 30,000 commonest words of the model's corpus (lang/ registry, its own normalisation), with log
frequencies. Viterbi segmentation; an unmatched letter costs UNK nats. Reports per decoded line of a bigsolve output:
share of letters inside dictionary words of 3+ letters, and the segmentation score per letter.

python targets/dorabella/wordseg.py <model id> <bigsolve output file> [section header to start at]
"""
import os, sys, re, math
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm, corpora

UNK = -14.0
mid = sys.argv[1]
spec = lm.registry()[0][mid]
words = Counter(lm.norm(corpora.text(spec['sources'])[:8_000_000], spec['norm'], True).split())
top = words.most_common(30000); tot = sum(c for _, c in top)
LP = {w: math.log(c / tot) for w, c in top}
MAXL = max(len(w) for w in LP)


def segment(x):
    n = len(x); best = [(-1e18, 0, None)] * (n + 1); best[0] = (0.0, 0, None)
    for i in range(1, n + 1):
        cand = [(best[i - 1][0] + UNK, best[i - 1][1], (i - 1, None))]
        for L in range(1, min(MAXL, i) + 1):
            w = x[i - L:i]
            if w in LP:
                cand.append((best[i - L][0] + LP[w], best[i - L][1] + (L if L >= 3 else 0), (i - L, w)))
        best[i] = max(cand, key=lambda c: c[0])
    seg, i = [], n
    while i > 0:
        j, w = best[i][2]
        seg.append(w or x[j:i].upper()); i = j
    return best[n][0] / n, best[n][1] / n, ' '.join(reversed(seg))


start = sys.argv[3] if len(sys.argv) > 3 else None
on = start is None
for line in open(sys.argv[2], encoding='utf-8'):
    if start and line.startswith('=='):
        on = start in line
        continue
    if not on:
        continue
    m = re.match(r'(?:misread|homo) K=\d+ (.+?)\s+best (-?[\d.]+).*?\s([a-z]{40,})\s*$', line.strip())
    if not m:
        continue
    name, sc, txt = m.group(1), float(m.group(2)), m.group(3)
    per, cov, seg = segment(txt)
    acc = re.search(r'acc ([\d.]+)', line)
    print(f'{name:22s} solver {sc:7.3f} {("acc " + acc.group(1)) if acc else "        "}  words {cov:.2f}  seg/letter {per:6.2f}  {seg[:100]}')
