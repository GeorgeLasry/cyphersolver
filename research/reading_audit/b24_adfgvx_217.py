"""b24 (adfgvx): test the reported 2026 decipherment of Childs p. 217 ('prinz', Sept 2026: keyword TRUPPENVERSCHIEBUNG,
plaintext EIN ENGLISCHER KREUZER ...) as a known-plaintext check: undo the transposition with the keyword and see whether
every ADFGVX pair maps to one plaintext letter and every letter to one pair (a consistent substitution square).
    python b24_adfgvx_217.py"""
import sys, pathlib, os
A = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'adfgvx'
sys.path.insert(0, str(A)); os.chdir(A)
import gaps
from repair import untranspose
from collections import defaultdict
KW = 'TRUPPENVERSCHIEBUNG'
PT = 'EINENGLISCHERKREUZEREINLIEGXSEWASTOPOLXS4STENXEINGESCHWADERDERXALLIIERTENFOLGT26STENX'
rank = sorted(range(len(KW)), key=lambda i: (KW[i], i))
perm_B = [0] * len(KW)
for r, i in enumerate(rank): perm_B[i] = r + 1          # column i is emitted perm_B[i]-th
perm_A = [i + 1 for i in rank]                          # the column emitted i-th
m = [m for m in gaps.parse() if m['page'].startswith('217')][0]
ct = m['ct']; print('cells', len(ct), 'plaintext letters', len(PT))
for name, perm, conv in (('B', perm_B, 'B'), ('A', perm_A, 'A')):
    s = untranspose(ct, perm, len(KW), conv)
    pairs = [s[i:i + 2] for i in range(0, len(s), 2)]
    p2l, l2p = defaultdict(set), defaultdict(set)
    for p, l in zip(pairs, PT): p2l[p].add(l); l2p[l].add(p)
    bad1 = {p: v for p, v in p2l.items() if len(v) > 1}; bad2 = {l: v for l, v in l2p.items() if len(v) > 1}
    print(name, 'pairs', len(p2l), 'letters', len(l2p), 'pair->2+ letters', len(bad1), 'letter->2+ pairs', len(bad2))
    if len(bad1) + len(bad2) < 5:
        print('  conflicts', bad1, bad2)
        SYM = 'ADFGVX'; sq = ['-'] * 36
        for p, v in p2l.items(): sq[SYM.index(p[0]) * 6 + SYM.index(p[1])] = next(iter(v))
        for r in range(6): print('  ', SYM[r], ' '.join(sq[r * 6:r * 6 + 6]))

# the other open messages under the same transposition and the 23 recovered cells
s = untranspose(ct, perm_B, len(KW), 'B'); SYM = 'ADFGVX'; sq = {}
for i in range(0, len(s), 2): sq[s[i:i + 2]] = PT[i // 2]
for m in gaps.parse():
    if m['page'].split()[0] in ('73', '152', '153', '158', '170', '176', '189', '198'):
        c = m['ct'].replace('#', '')
        if len(c) % 2: c = c[:-1]
        t = untranspose(c, perm_B, len(KW), 'B')
        out = ''.join(sq.get(t[i:i + 2], '.') for i in range(0, len(t), 2))
        print('%-10s %3d cells  known %.2f  %s' % (m['page'][:10], len(c), 1 - out.count('.') / len(out), out[:80]))
