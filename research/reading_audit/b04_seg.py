"""b04: re-segment the DECODE transcriptions (decode/keep/DOC_R*.txt) of Spagna 423 with Lasry's rules
(7 = null outside groups; 1xxx = nomenclator; else 2-digit), independently of Lasry's segmented file."""
import re, os, sys
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'targets', 'nunzio1736')
DOC = {1: 'R26_D1635_1635', 2: 'R179_D1621_1621', 3: 'R180_D1613_1613', 4: 'R181_D1615_1615', 5: 'R182_D1620_1620', 6: 'R183_D1622_1622',
       7: 'R184_D1617_1617', 8: 'R185_D1618_1618', 9: 'R186_D1623_1623', 10: 'R187_D1619_1619', 11: 'R188_D1637_1637'}
def digits(item):
    t = open(os.path.join(T, 'decode', 'keep', 'DOC_%s.txt' % DOC[item]), encoding='utf8', errors='replace').read()
    t = re.sub(r'<[^>]*>', ' ', t); t = re.sub(r'#[^\n]*', ' ', t)
    # keep digits and '?' (unread digit)
    out = []
    for tok in t.split():
        d = re.sub(r'[^0-9?]', '', tok)
        if d:
            c = d[0]
            if c == '?' and item == 1: c = '2'  # R26 transcriber: '?' marks the digit 2
            out.append(c)
    # transcription corrections checked on the images (texts/423_b04_corrections.tsv): item, digit index, old, new
    p = os.path.join(T, 'texts', '423_b04_corrections.tsv')
    if os.path.exists(p):
        rows = [l.rstrip('\n').split('\t') for l in open(p, encoding='utf8') if l.strip() and not l.startswith('item')]
        for r in sorted((r for r in rows if int(r[0]) == item), key=lambda r: -int(r[1])):
            i = int(r[1]); assert ''.join(out[i:i + len(r[2])]) == r[2], r
            out[i:i + len(r[2])] = list(r[3])
    return out
def segment(ds):
    toks = []; i = 0
    while i < len(ds):
        d = ds[i]
        if d == '7': toks.append('7'); i += 1; continue
        if d == '1': toks.append(''.join(ds[i:i + 4])); i += 4; continue
        toks.append(''.join(ds[i:i + 2])); i += 2
    return toks
if __name__ == '__main__':
    for it in DOC:
        ds = digits(it); tk = segment(ds)
        las = open(os.path.join(T, 'lasry', '423-%d.txt' % it)).read().split()
        print(it, 'digits', len(ds), 'seg tokens', len(tk), 'lasry tokens', len(las))

KEY = {}
for l in open(os.path.join(T, 'decode', 'keep', 'lasry_key_S423.txt'), encoding='utf8'):
    m = re.match(r'^([\d|]+) - (.+)$', l.strip())
    if m:
        for c in m.group(1).split('|'): KEY[c] = m.group(2).split('|')[0]
KEY.update({'25': '(che)', '30': 'ta', '93': 'nel', '69': 'z', '09': 'u', '35': 'u', '55': 'ti'})
EXTRA = {}
for l in open(os.path.join(T, 'key_extra.txt'), encoding='utf8').read().strip().splitlines():
    a, b = l.split(' = '); EXTRA.setdefault(a, b)
B04 = {}  # values added in this re-read (b04), kept apart
p = os.path.join(T, 'texts', 'b04_key_additions.txt')
if os.path.exists(p):
    for l in open(p, encoding='utf8'):
        l = l.split('#')[0].strip()
        if ' = ' in l: a, b = l.split(' = '); B04[a.strip()] = b.strip()
for _c in [c for c in B04 if len(c) == 2]:  # two-digit corrections (r2d, 23 Oct 2026: 26 = del)
    KEY[_c] = B04.pop(_c)
def lab(c):
    if c == '7': return ''
    if len(c) == 4 and c[0] == '1':
        if c in B04:
            v = B04[c]
            return ('[?' + v[1:] + ']') if v.startswith('?') else ('{' + v + '}')
        return '{' + EXTRA.get(c, c) + '}'
    if c in KEY: return KEY[c]
    return '<' + c + '>'
def render(it, width=110):
    tk = segment(digits(it)); out = ''.join(lab(c) for c in tk)
    return tk, out

def write_decodes():
    """texts/423-<n>_decode_b04.txt: the re-segmented digit stream and its decode, 12 tokens a line."""
    for it in DOC:
        tk = segment(digits(it))
        L = ['Spagna 423/%d: DECODE transcription (decode/keep/DOC_%s.txt) re-segmented by research/reading_audit/b04_seg.py '
             '(7 = null; 1xxx = nomenclator; else pairs), decoded with Lasry\'s key + 25=che, 30=ta, 69=z + key_extra.txt + '
             'texts/b04_key_additions.txt. {x} = nomenclator value; [?x] = probable value; {1234} = open group; <..> = no value. '
             '%d tokens (%d without nulls).' % (it, DOC[it], len(tk), sum(1 for t in tk if t != '7')), '']
        nn = [c for c in tk if c != '7']
        for k in range(0, len(nn), 12):
            ch = nn[k:k + 12]
            L.append(' '.join(ch)); L.append(' '.join(lab(c) for c in ch)); L.append('')
        tk2, o = render(it)
        L.append('Running decode:'); L += [o[k:k + 120] for k in range(0, len(o), 120)]
        open(os.path.join(T, 'texts', '423-%d_decode_b04.txt' % it), 'w', encoding='utf8').write('\n'.join(L) + '\n')
if __name__ == '__main__' and '--write' in sys.argv:
    write_decodes()

def where(item, ctx):
    d = ''.join(digits(item)); return [m.start() for m in re.finditer(re.escape(ctx), d)]
