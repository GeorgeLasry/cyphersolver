"""b35 (sp106r924): decode a section of Lasry's SP106-8 interlinear file (Pettersson's rows) with his key, letters
lower case, word codes upper case, unvalued figures below 100 as '.', unvalued codes as <n>; optional overrides
code=value. Optionally list the context of given codes.

    python b35_r924dec.py <section> [--ctx 116,168] [--set 168=HOPE,...] [--signs file]
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'sp106r787'))
from apply_key import load_key
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'sp106r924'
k = load_key(T / 'decode' / 'DOC_R924_D3089_3089.txt')
a = sys.argv
if '--set' in a:
    for kv in a[a.index('--set') + 1].split(','):
        c, v = kv.split('='); k[c] = v
sec = a[1]
if '--signs' in a:
    rows = [l.split() for l in open(a[a.index('--signs') + 1], encoding='utf-8') if l.strip() and not l.startswith('#')]
else:
    import re
    cur, body = None, []
    for l in (T / 'decode' / 'DOC_R924_D3091_3091.txt').read_text(encoding='utf-8', errors='replace').splitlines():
        m = re.match(r'#{6,}\s*tna[ _]sp106.(\S+?)(\.txt)?\s*$', l)
        if m: cur = m.group(1); continue
        if l.startswith('#KEY'): cur = None; continue
        if cur == sec and l.strip() and not l.lstrip().startswith('#'): body.append(l)
    rows = [body[i].rstrip().rstrip('|').split() for i in range(0, len(body) - 1, 2)]
def d(g):
    v = k.get(g)
    if v is None: return '.' if g.isdigit() and int(g) < 100 else '<%s>' % g
    return v.lower() if len(v) == 1 else ' %s ' % v.split(' - ')[-1].strip('<>?')
lines = [' '.join(''.join(d(g) for g in r).split()) for r in rows]
if '--ctx' in a:
    flat = [g for r in rows for g in r]
    for c in a[a.index('--ctx') + 1].split(','):
        for i, g in enumerate(flat):
            if g == c:
                print(c, '|', ' '.join(''.join(d(x) if x != c else ' [%s] ' % c for x in flat[max(0, i - 14):i + 10]).split()))
else:
    for i, l in enumerate(lines): print(i, l)
