"""Initial-letter abbreviation scan over Horace: each word of a run contributes its first 1-3 letters (uniform k, or mixed),
and the concatenation must be an EXACT merge of the two halves of a line (no omissions)."""
import re, sys
import ads2 as ads
def prefix_states(A, B, s, states):
    # advance the set of (i,j) merge states by string s; return new set (empty if impossible)
    for ch in s:
        nxt = set()
        for (i, j) in states:
            if i < len(A) and A[i] == ch: nxt.add((i+1, j))
            if j < len(B) and B[j] == ch: nxt.add((i, j+1))
        states = nxt
        if not states: break
    return states
text = open(sys.argv[1], encoding="utf-8", errors="replace").read().lower()
text = re.sub(r"##### \S+", " ", text)
words = re.findall(r"[a-z]+", text)
print("words", len(words))
lines = [int(x) for x in sys.argv[2].split(",")]
for ln in lines:
    A, B = ads.BNA[ln]; A, B = A.lower(), B.lower(); L = len(A) + len(B)
    found = {}
    # uniform k
    for k in (1, 2, 3):
        for start in range(len(words)):
            states = {(0, 0)}; s = ""; w = start
            while len(s) < L and w < len(words) and states:
                piece = words[w][:k]; states = prefix_states(A, B, piece, states); s += piece; w += 1
            if states and len(s) == L and (len(A), len(B)) in states:
                found.setdefault(" ".join(words[start:w]), f"k={k}")
    # mixed 1-3 letters per word, words must be >= 3 letters to be abbreviated to 1-2 (avoid trivial matches)
    def rec(w, states, s, path):
        if len(s) == L:
            if (len(A), len(B)) in states: found.setdefault(" ".join(path), "mixed")
            return
        if w >= len(words): return
        word = words[w]
        for k in (1, 2, 3):
            if k > len(word): break
            piece = word[:k]
            if len(s) + len(piece) > L: break
            st = prefix_states(A, B, piece, states)
            if st: rec(w + 1, st, s + piece, path + [word])
    for start in range(len(words)):
        rec(start, {(0, 0)}, "", [])
    print(f"=== line {ln} ({A} / {B}): {len(found)} matches")
    for phrase, how in list(found.items())[:40]:
        print(f"   [{how}] {phrase}")
