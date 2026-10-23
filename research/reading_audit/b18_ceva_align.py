"""b18 (ceva1632): align a letter's decoded token stream (Lasry's key + cipher.NOMEN) with the contemporary
decipherment, unit by unit (dynamic programming over the whole letter), and print per manuscript line the
decode, the decipherment's matching stretch, and every disagreement.

    python research/reading_audit/b18_ceva_align.py r75|r84 <decifrato.txt> [tokens-file]
Normalisation of both sides: lower case, u->v, j->i, accents off, doubled letters single (the clerk's habit),
abbreviation brackets kept as letters. Unvalued codes match any 0-16 letters (cost 0.6).
"""
import json, re, sys, pathlib, unicodedata
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'ceva1632'
sys.path.insert(0, str(T))
import cipher

def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if c.isalpha() and c.isascii())
    s = s.replace('u', 'v').replace('j', 'i')
    return re.sub(r'(.)\1+', r'\1', s)

doc, decf = sys.argv[1], sys.argv[2]
toks = json.load(open(T / (sys.argv[3] if len(sys.argv) > 3 else f'{doc}.tokens2.json')))
raw = [l for l in open(T / decf, encoding='utf-8') if not l.startswith('#')]
D = norm(' '.join(raw))
units = []          # (line, token, string or None for wildcard)
for li, line in enumerate(toks, 1):
    for t in line:
        if t == '6' or cipher.is_null(t): continue
        if t.startswith('?'):
            units.append((li, t, '')); continue
        if t.startswith('#'):
            v = cipher.NOMEN.get(t[1:]); units.append((li, t, norm(v) if v else None)); continue
        units.append((li, t, norm(cipher.units(t) or '')))
n, m = len(units), len(D)
INF = 1e9
cost = [[INF] * (m + 1) for _ in range(n + 1)]
back = [[None] * (m + 1) for _ in range(n + 1)]
cost[0][0] = 0
for j in range(1, m + 1): cost[0][j] = j * 1.0; back[0][j] = ('ins',)
for i in range(1, n + 1):
    s = units[i - 1][2]
    ci, cp = cost[i], cost[i - 1]
    for j in range(0, m + 1):
        best, bk = cp[j] + 1.0, ('del',)                 # unit not in decifrato
        if j and ci[j - 1] + 1.0 < best: best, bk = ci[j - 1] + 1.0, ('ins',)
        if s is None:
            for k in range(0, min(16, j) + 1):
                c = cp[j - k] + 0.6
                if c < best: best, bk = c, ('code', k)
        elif s == '':
            if cp[j] + 0.2 < best: best, bk = cp[j] + 0.2, ('noise', 0)
        else:
            L = len(s)
            if j >= L:
                c = cp[j - L] + (0 if D[j - L:j] == s else 0.9 if L > 1 and sum(a != b for a, b in zip(D[j-L:j], s)) <= 1 else 1.0 * L)
                if c < best: best, bk = c, ('match', L)
        ci[j] = best; back[i][j] = bk
# traceback
i, j, al = n, m, {}
while i > 0 or j > 0:
    bk = back[i][j]
    if bk[0] == 'ins': j -= 1; continue
    if bk[0] == 'del': al[i - 1] = ('', 'del'); i -= 1; continue
    k = bk[1]; al[i - 1] = (D[j - k:j], bk[0]); i -= 1; j -= k
cur = None
for idx, (li, t, s) in enumerate(units):
    if li != cur:
        if cur is not None: print('   D:', ''.join(dl)); print('   !', '  '.join(bad) or '-')
        cur = li; dl, bad = [], []; print(f'L{li}')
    got, kind = al.get(idx, ('', 'del'))
    dl.append(got)
    if kind == 'code' or (s is None):
        bad.append(f'{t}={got or "∅"}')
    elif kind == 'del' or got != s:
        bad.append(f'{t}({s})≠{got or "∅"}')
print('   D:', ''.join(dl)); print('   !', '  '.join(bad) or '-')
print('total cost', round(cost[n][m], 1))
