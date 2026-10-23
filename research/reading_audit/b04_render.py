"""b04: render Spagna 423 items from Lasry's segmented decipherment (targets/nunzio1736/seq.json, built by corpus.py)
with the key corrections of the 22 Oct 2026 re-read (30 = ta) and key_extra.txt nomenclator values.
Usage: python b04_render.py <item> [--ctx GROUP]"""
import json, re, sys, os
T = os.path.join(os.path.dirname(__file__), '..', '..', 'targets', 'nunzio1736')
seq = json.load(open(os.path.join(T, 'seq.json')))
extra = {}
for l in open(os.path.join(T, 'key_extra.txt'), encoding='utf8').read().strip().splitlines():
    a, b = l.split(' = '); extra[a] = b
FIX = {'30': 'ta', '55': 'ti', '69': 'z'}
def lab(c, p, raw=False):
    if re.fullmatch(r'1\d{3}', c):
        return '{' + (extra.get(c, c) if not raw else c) + '}'
    if c in ('7', '77'): return ''
    if c in FIX: return FIX[c]
    if p.endswith('?') or not p: return '<' + c + '>'
    return p.replace('u/v', 'u')
if __name__ == '__main__':
    if '--ctx' in sys.argv:
        g = sys.argv[sys.argv.index('--ctx') + 1]
        for i, (it, c, p) in enumerate(seq):
            if c == g:
                print(it, ''.join(lab(*x[1:]) for x in seq[max(0, i - 14):i]) + ' [' + g + '] ' + ''.join(lab(*x[1:]) for x in seq[i + 1:i + 14]))
        sys.exit()
    it = int(sys.argv[1])
    toks = [(c, p) for (i, c, p) in seq if i == it]
    out = ''.join(lab(c, p) for c, p in toks)
    print(len(toks), 'tokens')
    for k in range(0, len(out), 110): print(out[k:k + 110])

def show(it, a, b):
    """print tokens a..b of item it as code=label"""
    toks = [(c, p) for (i, c, p) in seq if i == it]
    print(' '.join('%s=%s' % (c, lab(c, p)) for c, p in toks[a:b]))

def find(it, s):
    toks = [(c, p) for (i, c, p) in seq if i == it]
    out = ''; pos = []
    for k, (c, p) in enumerate(toks):
        l = lab(c, p); pos += [k] * len(l); out += l
    j = out.find(s)
    return pos[j] if j >= 0 else None
