"""b24 (adfgvx): VGADA (Childs p. 215, 22 Nov 1918) under the Nov 22-24 key, with Norbert's two inserted five-letter
groups (comment 32: after group 6 'D.F..' and after group 43), letter by letter against Max Baertl's corrected text
(comment 39). Each plaintext letter is: full (both ADFGVX cells received), half (one cell received: six candidates),
lost (no cell). Baertl's letter is checked against what the cells allow.
    python b24_adfgvx_vgada.py"""
import sys, pathlib
A = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'adfgvx'
sys.path.insert(0, str(A))
import os; os.chdir(A)
import gaps
from repair import untranspose, load_keys
SYM = 'ADFGVX'
k = load_keys()[11]
m = [m for m in gaps.parse() if m['page'].startswith('??')][0]
g = list(m['groups']); g[5] = 'D#F##'
g = g[:6] + ['#####'] + g[6:43] + ['#####'] + g[43:]
s = untranspose(''.join(g), k['perm'], k['n'], 'B')
sq = k['square']
cells = []
for a, b in zip(s[0::2], s[1::2]):
    if a in SYM and b in SYM: cells.append(('full', {sq[SYM.index(a) * 6 + SYM.index(b)]}))
    elif a in SYM: cells.append(('half', {sq[SYM.index(a) * 6 + j] for j in range(6)}))
    elif b in SYM: cells.append(('half', {sq[i * 6 + SYM.index(b)] for i in range(6)}))
    else: cells.append(('lost', set(sq)))
BAERTL = 'ABSXMIDIV5XEILMELDGX24NX24NXARMADAKERTSCHXBRINGTENTENTEFLOTTEZWODIVISIONENXNEUSEELAENDERXENGLXUXFRANZOXMITXNUROHLXKORPSFRISCHX3Y52'
print('cells', len(cells), 'Baertl', len(BAERTL))
# DP alignment: match cost 0 if letter allowed, 1 if not; gap cost 1
n, mm = len(cells), len(BAERTL)
INF = 9e9
D = [[INF] * (mm + 1) for _ in range(n + 1)]; P = [[None] * (mm + 1) for _ in range(n + 1)]
D[0][0] = 0
for i in range(n + 1):
    for j in range(mm + 1):
        if i < n and j < mm:
            c = 0 if BAERTL[j] in cells[i][1] else 1
            if D[i][j] + c < D[i + 1][j + 1]: D[i + 1][j + 1] = D[i][j] + c; P[i + 1][j + 1] = (i, j, 'm')
        if i < n and D[i][j] + 1 < D[i + 1][j]: D[i + 1][j] = D[i][j] + 1; P[i + 1][j] = (i, j, 'd')
        if j < mm and D[i][j] + 1 < D[i][j + 1]: D[i][j + 1] = D[i][j] + 1; P[i][j + 1] = (i, j, 'i')
i, j, path = n, mm, []
while (i, j) != (0, 0):
    pi, pj, op = P[i][j]; path.append((op, pi, pj)); i, j = pi, pj
path.reverse()
from collections import Counter
st = Counter(); line_f, line_b, line_s = '', '', ''
for op, i, j in path:
    if op == 'm':
        kind, cand = cells[i]
        ok = BAERTL[j] in cand
        tag = {'full': 'F', 'half': 'h', 'lost': 'L'}[kind] if ok else 'E'
        st[tag] += 1
        line_f += (next(iter(cand)) if kind == 'full' else ('.' if kind == 'lost' else '?')); line_b += BAERTL[j]; line_s += tag
    elif op == 'd':
        st['extra cell'] += 1; line_f += (next(iter(cells[i][1])) if cells[i][0] == 'full' else '.'); line_b += '-'; line_s += 'D'
    else:
        st['Baertl only'] += 1; line_f += '-'; line_b += BAERTL[j]; line_s += 'I'
print('F = carried by both cells, h = one cell (Baertl letter among six), L = both cells lost, E = cells give another letter,')
print('D = a cell pair Baertl has no letter for, I = a Baertl letter with no cell pair')
for x in range(0, len(line_b), 70):
    print('figs  ', line_f[x:x + 70]); print('Baertl', line_b[x:x + 70]); print('      ', line_s[x:x + 70]); print()
print(dict(st))

# for each E: does Baertl's letter share a row or a column of the square with the cells' letter (a one-cell error)?
print('\nconflicts (cells letter -> Baertl letter, one-cell error?):')
pos = {c: (i // 6, i % 6) for i, c in enumerate(sq)}
one = 0; out = []
for op, i, j in path:
    if op == 'm' and BAERTL[j] not in cells[i][1]:
        kind, cand = cells[i]
        if kind == 'full':
            f = next(iter(cand)); r1, c1 = pos[f]; r2, c2 = pos[BAERTL[j]]
            o = (r1 == r2) or (c1 == c2); one += o
            out.append('%s->%s%s' % (f, BAERTL[j], '' if o else '*'))
        else:
            out.append('half{%s}->%s*' % (''.join(sorted(cand)), BAERTL[j]))
print(' '.join(out)); print('one-cell explicable:', one, 'of', len(out))
