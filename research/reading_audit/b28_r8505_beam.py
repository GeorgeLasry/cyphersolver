"""b28: beam decode of harley1582r8505 runs with key.json, allowing the documented look-alike alternates per token
(each at a penalty), scored by the fr-1530-despatches 5-gram (no spaces) with the clear text before the run as context.
Output per line: tokens, chosen letters, alternates used (token:primary->alt), and a word segmentation.
    python research/reading_audit/b28_r8505_beam.py [files]   (PEN=3.0 BEAM=400)"""
import sys, os, re, glob, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lang import lm
_argv = sys.argv; sys.argv = ['x']
import b28_r8505_decode as D
sys.argv = _argv
M = lm.load('fr-1530-despatches', order=5, spaces=False)
K = D.key; PEN = float(os.environ.get('PEN', 3.0)); BEAM = int(os.environ.get('BEAM', 400))
# look-alike alternates: shapes the second reading (signs.md, NOTES) and this pass showed to be confusable
ALT = {
    'd': ['t'],            # crossed delta (a) vs crossed epsilon Eb (t): the first transcription of the rectos merged them
    'Eb': ['a'],
    'wf': ['qu'],          # omega+long-s ligature (t) vs omega (q) followed by long-s f (u)
    'phi': ['u'], 'f': ['b'],
    'E3': ['a'], 'E': ['s'],
    'b': ['u'], 'T': ['n'],
    'X': ['p'], 'hg': ['l'],
    '#': ['d'], 'H': ['d'], 'ne': ['d'], 'F': ['t'],
    'Pi': ['o'], 'PiG': ['o'],
    'DOT': ['f'], 'eq': ['m'],
    'q': ['q'], 'cy': ['u'], 'Xo': ['l'],
}
NULLPEN = float(os.environ.get('NULLPEN', 99))
def opts(t):
    t = t.rstrip('?')
    if re.fullmatch(r'[:.]+|:[234]', t): t = 'DOT'
    prim = 'm' if t == 'DOT' else K.get(t)
    if prim is None: return [('', 0.0, t + '?')]
    o = [(prim, 0.0, None)]
    for a in ALT.get(t, []):
        if a != prim: o.append((a, PEN, '%s:%s>%s' % (t, prim, a)))
    if NULLPEN < 90: o.append(('', NULLPEN, '%s:%s>0' % (t, prim)))
    return o
def inc(ctx, s):
    tot = 0.0; c = ctx
    for ch in s:
        if ch not in M.index: continue
        c = (c + ch)[-5:]
        if len(c) == 5:
            x = M.encode(c); tot += M.score_idx(x)
    return tot, c
def beam(tokens, ctx):
    B = [(0.0, ctx[-4:], '', ())]
    for t in tokens:
        if re.fullmatch(r'#\d+', t):
            B = [(s, c, out + ' [%s] ' % t[1:], al) for s, c, out, al in B]; continue
        if t in ('-', '/'): continue
        nb = []
        for s, c, out, al in B:
            for letters, pen, tag in opts(t):
                d, c2 = inc(c, letters)
                nb.append((s + d - pen, c2, out + letters, al + ((tag,) if tag else ())))
        nb.sort(key=lambda z: -z[0]); seen = set(); B = []
        for z in nb:
            key = (z[1], z[2][-6:])
            if key in seen: continue
            seen.add(key); B.append(z)
            if len(B) >= BEAM: break
    return B[0]
if __name__ == '__main__':
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(os.path.dirname(D.T.__str__()), 'harley1582r8505', 'final', 'f*.txt')))
    nalt = 0
    for fn in files:
        for line in open(fn, encoding='utf-8'):
            p = [x.strip() for x in line.rstrip('\n').split('|')]
            if len(p) < 3: continue
            out = ''; al = ()
            for fi in range(2, len(p), 2):                     # every cipher field, with the clear text before it as context
                toks = p[fi].replace('/', ' ').split()
                ctx = lm.norm(p[fi - 1], 'early').replace(' ', '')
                s, c, o1, a1 = beam(toks, 'xxxx' + ctx)
                out += (' | ' if out else '') + o1; al += a1
            nalt += sum(len(a.split('>')[1]) for a in al)
            seg = ' '.join(x if (x.startswith('[') or x == '|') else D.segment(x) for x in out.split())
            print('%s\t%s\t||\t%s\t||\t%s' % (p[0], out, seg, ' '.join(al)))
    print('alternate letters', nalt, file=sys.stderr)
