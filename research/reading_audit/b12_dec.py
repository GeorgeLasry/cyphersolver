"""b12: decode the Acciaiuoli (Portogallo 117) digit transcriptions with Lasry's key (decode/DOC_R25_D3232).
Deterministic parse: 6 null; 2xxx nomenclator code; a lone digit followed by 6 = marker; else a 2-digit element.
Key change found 22 Oct 2026 against the Secretariat's decipherments: 03 = per (Lasry: nel).
usage: b12_dec.py <DOC transcription> [--tokens]"""
import re, sys
KEYF = r'C:\Users\dbour\cypher\.worktrees\reading-gate\targets\acciaiuoli1757\decode\DOC_R25_D3232_3232.txt'
KEY = {}
for l in open(KEYF, encoding='utf8', errors='replace'):
    m = re.match(r'^([\d|]+) - (.+)$', l.strip())
    if m:
        for g in m.group(1).split('|'):
            KEY[g] = m.group(2).split('|')[0]
KEY['03'] = 'per'
def tokens(path):
    out = []
    for l in open(path, encoding='utf8', errors='replace'):
        if l.startswith('#'):
            if l.startswith('#IMAGE NAME') and out: out.append(('|', '|'))
            continue
        out += [(d.rstrip('?'), '?' in d) for d in l.split() if re.match(r'^\d\??$', d)]
    return out
def parse(path):
    ds = tokens(path); res = []; i = 0
    while i < len(ds):
        d, q = ds[i]
        if d == '|': res.append(('|', '|')); i += 1; continue
        if d == '6': i += 1; continue
        if d == '2':
            g = ''.join(x[0] for x in ds[i:i+4]); res.append((g, '<%s>' % g)); i += 4; continue
        if i + 1 >= len(ds) or ds[i+1][0] in ('6', '|'):
            res.append((d, '·')); i += 1; continue
        g = d + ds[i+1][0]
        res.append((g, KEY.get(g, '[%s?]' % g))); i += 2
    return res
if __name__ == '__main__':
    r = parse(sys.argv[1])
    if '--tokens' in sys.argv:
        print(' '.join('%s=%s' % t for t in r))
    else:
        print(''.join(p if p.startswith('<') or p.startswith('[') else p for g, p in r).replace('<', ' <').replace('>', '> '))

LASRY = r'C:\Users\dbour\cypher\.worktrees\reading-gate\targets\acciaiuoli1757\decode\DOC_R25_D3231_3231.txt'
ORDER = ['R25', 'R195', 'R196', 'R197', 'R198', 'R199', 'R200', 'R201']
def parse_lasry(rec):
    """the digit groups of Lasry's decryption file (one block per letter, in ORDER), keyed as parse()."""
    t = open(LASRY, encoding='utf8', errors='replace').read()
    blocks = re.split(r'^#{5,}.*$', t, flags=re.M)[1:]
    b = blocks[ORDER.index(rec)]
    res = []
    for l in b.split('\n'):
        if l.startswith('#IMAGE NAME') and res: res.append(('|', '|'))
        if l.startswith('#') or not l.strip(): continue
        toks = l.replace('|', ' ').split()
        if not toks or not all(re.match(r'^\d+\??$', x) for x in toks): continue
        for x in toks:
            x = x.rstrip('?')
            if x == '6': continue
            if len(x) == 1: res.append((x, '·'))
            elif len(x) == 4: res.append((x, '<%s>' % x))
            else: res.append((x, KEY.get(x, '[%s?]' % x)))
    return res
