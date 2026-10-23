"""b37: as b37_wals_crib.py, but the crib is one letter string and Tomokiyo's word signs (and have in of the to your be
he me that you) may stand for that string anywhere, inside words too (servAND, doMEstik).
python b37_wals_crib2.py <letter homophone limit> <max nulls> [crib]"""
import sys, pathlib
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'walsingham1581' / 'SP53_11_50b.txt'
toks = [t for line in T.read_text().splitlines()[1:] for t in line.strip().split(';') if t]
LIM = int(sys.argv[1]); MAXN = int(sys.argv[2])
crib = (sys.argv[3] if len(sys.argv) > 3 else 'the beirar is domestik servand to the erle of shrevisbvry').replace(' ', '')
SIGNS = ['and', 'have', 'in', 'of', 'the', 'to', 'your', 'be', 'he', 'me', 'that', 'you']
sys.setrecursionlimit(10000)
best = []
def dfs(i, p, m, nulls, nn, signs):
    if nn > MAXN or len(best) > 2000: return
    if p == len(crib): best.append((nn, dict(m), set(nulls), dict(signs), i)); return
    if i >= len(toks): return
    t = toks[i]
    if t in nulls: dfs(i + 1, p, m, nulls, nn + 1, signs); return
    if t in signs:
        s = signs[t]
        if crib.startswith(s, p): dfs(i + 1, p + len(s), m, nulls, nn, signs)
        return
    if t in m:
        if crib[p] == m[t]: dfs(i + 1, p + 1, m, nulls, nn, signs)
        return
    ch = crib[p]
    cnt = sum(1 for v in m.values() if v == ch)
    if cnt < (4 if ch in 'maeiv' else LIM):
        m2 = dict(m); m2[t] = ch; dfs(i + 1, p + 1, m2, nulls, nn, signs)
    for s in SIGNS:
        if s not in signs.values() and crib.startswith(s, p):
            s2 = dict(signs); s2[t] = s; dfs(i + 1, p + len(s), m, nulls, nn, s2)
    n2 = set(nulls); n2.add(t); dfs(i + 1, p, m, n2, nn + 1, signs)
for start in range(0, int(sys.argv[4]) if len(sys.argv) > 4 else 4):
    dfs(start, 0, {}, set(), 0, {})
best.sort(key=lambda x: (x[0] + len(x[3]), -x[4]))
for nn, m, nulls, signs, end in best[:6]:
    print('nulls', nn, sorted(nulls), 'signs', signs, 'end', end)
    print('   ', ' '.join(f'{k}={v}' for k, v in sorted(m.items(), key=lambda kv: kv[1])))
print(len(best), 'solutions')
