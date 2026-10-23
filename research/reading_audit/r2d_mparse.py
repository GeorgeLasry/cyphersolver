"""r2d (23 Oct 2026), morosini1588: enumerate the readings of a run of figures under Meister no. 40 (letters, word
signs, three-figure codes, 8x nulls), ranked by a character model of the period language, to test a hole.

    python research/reading_audit/r2d_mparse.py "<figures>" [it|es] [top]      dots: write 1^.9 or 19^. as in DECODE
"""
import heapq, re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / 'research' / 'reading_audit'))
from lang import lm
from reread_b00_decode import CODES, NOM

figs, lang = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else 'it')
top = int(sys.argv[3]) if len(sys.argv) > 3 else 15
dotted = set()
d = ''
for tok in figs.split():
    t = tok.replace('^.', '').replace('.', '')
    dd = re.sub(r'\D', '', t)
    if '^' in tok or tok.endswith('.'):
        dotted.add(len(d) + len(dd) - 1)          # the dot stands on the last figure written before it
    d += dd
M = lm.load('it-cinquecento' if lang == 'it' else 'es-golden-age', spaces=False)
n = len(d)
# DP over positions: keep up to K partial texts per position
K = 400
beams = {0: [('', [])]}
for i in range(n):
    for txt, path in beams.get(i, []):
        for L in (1, 2, 3):
            c = d[i:i + L]
            if len(c) < L: break
            opts = []
            if L == 2 and c[0] == '8': opts.append(('', '8' + c[1]))
            if L == 1 and c == '8': opts.append(('', '8'))
            for pt, pen in CODES.get(c, []):
                opts.append((pt, c))
            if L == 3 and c in NOM and (i + 1) in dotted: opts.append(('[' + NOM[c] + ']', c))
            for pt, cc in opts:
                beams.setdefault(i + L, []).append((txt + pt, path + [cc]))
    if i + 1 in beams:
        beams[i + 1] = heapq.nlargest(K, beams[i + 1], key=lambda x: M.score(re.sub(r'\[[^]]*\]', '', x[0]) or 'a') / max(1, len(x[0])) * 0 + M.score(re.sub(r'\[[^]]*\]', '', x[0]) or 'a'))
res = beams.get(n, [])
seen = set()
for txt, path in sorted(res, key=lambda x: -M.score(re.sub(r'\[[^]]*\]', '', x[0]) or 'a'))[:top * 3]:
    if txt in seen: continue
    seen.add(txt)
    print(f'{M.score(re.sub(r"[^a-z]", "", txt) or "a"):8.1f}  {txt:40s} {" ".join(path)}')
    if len(seen) >= top: break
