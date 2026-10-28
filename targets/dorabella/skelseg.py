"""Round 39, second criterion: can a decoded consonant string be split into skeletons of real English words?

Dictionary: consonant skeletons (vowels a e i o u removed) of the 20,000 commonest words in en-gutenberg, with
log-frequencies summed over words sharing a skeleton. Viterbi segmentation; an unmatched letter costs UNK nats.
Reports, per decoded string in a bigsolve output file: share of letters covered by dictionary skeletons of length
>= 2, and the segmentation score per letter.

python targets/dorabella/skelseg.py runs/r39_skeleton.txt
"""
import os, sys, re, math
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import corpora

UNK = -14.0
words = Counter(re.findall(r'[a-z]+', corpora.text(['en-gutenberg'])[:8_000_000].lower()))
top = words.most_common(20000)
tot = sum(c for _, c in top)
sk = Counter()
for w, c in top:
    s = re.sub('[aeiou]', '', w)
    if len(s) >= 1:
        sk[s] += c
LP = {s: math.log(c / tot) for s, c in sk.items()}
MAXL = max(len(s) for s in LP)


def segment(x):
    n = len(x); best = [(-1e18, 0, None)] * (n + 1); best[0] = (0.0, 0, None)
    for i in range(1, n + 1):
        cand = [(best[i - 1][0] + UNK, best[i - 1][1], (i - 1, None))]
        for L in range(1, min(MAXL, i) + 1):
            w = x[i - L:i]
            if w in LP:
                cand.append((best[i - L][0] + LP[w], best[i - L][1] + (L if L >= 2 else 0), (i - L, w)))
        best[i] = max(cand, key=lambda c: c[0])
    seg, i = [], n
    while i > 0:
        j, w = best[i][2]
        seg.append(w or x[j:i].upper()); i = j
    return best[n][0] / n, best[n][1] / n, ' '.join(reversed(seg))


for line in open(sys.argv[1], encoding='utf-8'):
    m = re.match(r'misread K=\d+ (.+?)\s+best (-?[\d.]+).*?\s([a-z]{40,})\s*$', line.strip())
    if not m:
        continue
    name, sc, txt = m.group(1), float(m.group(2)), m.group(3)
    per, cov, seg = segment(txt)
    acc = re.search(r'acc ([\d.]+)', line)
    print(f'{name:22s} solver {sc:7.3f}  {"acc " + acc.group(1) if acc else "        "}  covered {cov:.2f}  seg/letter {per:6.2f}  {seg[:110]}')
