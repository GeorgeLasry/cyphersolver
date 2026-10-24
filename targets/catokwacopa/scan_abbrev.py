"""Cotegr-style test: W. wrote Od. 1.6.9 'conamur tenues grandia' as CO TE GR, the first two letters of each word.
Scan a corpus for runs of consecutive words whose initial pairs (one letter for one-letter words) merge EXACTLY,
with no omissions, into the two halves of a line."""
import re, sys
from functools import lru_cache
import ads2 as ads
def merges(A, B, P):
    la, lb = len(A), len(B)
    if la + lb != len(P): return False
    @lru_cache(maxsize=None)
    def f(i, j):
        k = i + j
        if k == len(P): return True
        return (i < la and A[i] == P[k] and f(i+1, j)) or (j < lb and B[j] == P[k] and f(i, j+1))
    return f(0, 0)
corpus = sys.argv[1]; lines = [int(x) for x in sys.argv[2].split(",")]
text = open(corpus, encoding="utf-8", errors="replace").read().lower()
text = re.sub(r"[àáâä]", "a", text); text = re.sub(r"[èéêë]", "e", text); text = re.sub(r"[ìíîï]", "i", text); text = re.sub(r"[òóôö]", "o", text); text = re.sub(r"[ùúûü]", "u", text)
words = re.findall(r"[a-z]+", text)
pairs = [w[:2] for w in words]
for ln in lines:
    A, B = ads.BNA[ln]; A, B = A.lower(), B.lower(); target = sorted(A + B); L = len(A) + len(B)
    seen = set(); hits = 0
    for start in range(len(words)):
        s = ""; n = 0; k = start
        while len(s) < L and k < len(words):
            s += pairs[k]; k += 1
        if len(s) != L or sorted(s) != target: continue
        if merges(A, B, s):
            phrase = " ".join(words[start:k])
            if phrase in seen: continue
            seen.add(phrase); hits += 1
            if hits <= 40: print(f"line {ln}: {s}  <-  {phrase}")
    print(f"line {ln}: {hits} distinct hits in {corpus.split('/')[-1]}")
