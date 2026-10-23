"""b37: place Tomokiyo's published opening of SP 53/11 no. 50I on the numeric labels (targets/walsingham1581/SP53_11_50b.txt).
DFS over the token stream: each token is a letter of the crib (consistent label->letter, letter->labels at most 2 except
m/a/e/i/v up to 4), a null/space label (consistent: once a label is null it is always null), or a word sign for
the/to/of/and (consistent). Prints the assignments with fewest nulls."""
import sys, pathlib
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'walsingham1581' / 'SP53_11_50b.txt'
toks = [t for line in T.read_text().splitlines()[1:] for t in line.strip().split(';') if t]
crib = 'the beirar is domestik servand to the erle of shrevisbvry'.split()
LIM = int(sys.argv[1]) if len(sys.argv) > 1 else 1
MAXN = int(sys.argv[2]) if len(sys.argv) > 2 else 14
SIGNS = {'the', 'to', 'of', 'and'}
best = []
sys.setrecursionlimit(10000)
def dfs(i, w, c, m, nulls, nn, signs):
    # i token index, w word index, c char index in word
    if nn > MAXN: return
    if w == len(crib):
        best.append((nn, dict(m), set(nulls), dict(signs), i)); return
    if i >= len(toks): return
    t = toks[i]; word = crib[w]
    if t in nulls:
        dfs(i + 1, w, c, m, nulls, nn + 1, signs); return
    # word sign at word start
    if c == 0 and word in SIGNS:
        if signs.get(t) == word or (t not in signs and t not in m and t not in nulls):
            s2 = dict(signs); s2[t] = word
            dfs(i + 1, w + 1, 0, m, nulls, nn, s2)
    # letter
    ch = word[c]
    if t not in signs:
        if m.get(t) == ch or (t not in m):
            cnt = sum(1 for v in m.values() if v == ch)
            lim = 4 if ch in 'maeiv' else LIM
            if m.get(t) == ch or cnt < lim:
                m2 = dict(m); m2[t] = ch
                if c + 1 == len(word): dfs(i + 1, w + 1, 0, m2, nulls, nn, signs)
                else: dfs(i + 1, w, c + 1, m2, nulls, nn, signs)
    # null
    if t not in m and t not in signs:
        n2 = set(nulls); n2.add(t)
        dfs(i + 1, w, c, m, n2, nn + 1, signs)
for start in range(0, 4):
    dfs(start, 0, 0, {}, set(), 0, {})
best.sort(key=lambda x: (x[0], len(x[2])))
for nn, m, nulls, signs, end in best[:8]:
    print('nulls', nn, sorted(nulls), 'signs', signs, 'end', end)
    print('   ', ' '.join(f'{k}={v}' for k, v in sorted(m.items(), key=lambda kv: kv[1])))
print(len(best), 'solutions')
