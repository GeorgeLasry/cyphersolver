"""r2p (23 Oct 2026), morosini1588: run the r2d_mparse.py enumeration on every hole listed by r2p_holes.py.

    python research/reading_audit/r2p_parseall.py <holes.txt> [it|es] [top]  > parses.txt
Lines of figures with '|' (line breaks) are joined; holes with more than 40 figures are parsed as given but marked.
"""
import heapq, re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / 'research' / 'reading_audit'))
from lang import lm
from reread_b00_decode import CODES, NOM

lang = sys.argv[2] if len(sys.argv) > 2 else 'it'
top = int(sys.argv[3]) if len(sys.argv) > 3 else 6
M = lm.load('it-cinquecento' if lang == 'it' else 'es-golden-age', spaces=False)


def sc(t):
    return M.score(re.sub(r'\[[^]]*\]', '', t) or 'a')


def parses(figs):
    dotted, d = set(), ''
    for tok in figs.split():
        if tok == '|':
            continue
        t = tok.replace('^.', '')
        dd = re.sub(r'\D', '', t)
        if '^' in tok:
            dotted.add(len(d) + len(dd) - 1)
            d += dd
            continue
        d += dd
    n = len(d)
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
                if L == 3 and c in NOM and (i + 2) in dotted: opts.append(('[' + NOM[c] + ']', c + '.'))
                for pt, cc in opts:
                    beams.setdefault(i + L, []).append((txt + pt, path + [cc]))
        if i + 1 in beams:
            beams[i + 1] = heapq.nlargest(300, beams[i + 1], key=lambda x: sc(x[0]))
    res, seen, out = beams.get(n, []), set(), []
    for txt, path in sorted(res, key=lambda x: -sc(x[0])):
        if txt in seen: continue
        seen.add(txt); out.append(f'{sc(txt):7.1f}  {txt:34s} {" ".join(path)}')
        if len(out) >= top: break
    return out


lines = open(sys.argv[1], encoding='utf8').read().split('\n')
for k, ln in enumerate(lines):
    if ln.strip().startswith('figs:'):
        print(lines[k - 1]); print(ln)
        f = ln.split('figs:', 1)[1].strip()
        if f.startswith('('):
            continue
        for p in parses(f) or ['      (no parse)']:
            print('        ' + p)
