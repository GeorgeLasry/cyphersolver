"""b18: word-by-word alignment of a reading body (## Reading section) with a source text (decipherment transcription
or decode). Prints the share of reading words carried and every reading word the source does not carry, so that
each can be bracketed or justified.

    python research/reading_audit/b18_align.py <reading.md> <source.txt> [<source2.txt> ...]
Source lines starting with '#' are skipped; {{struck}} words dropped, ^interlined^ kept, '|' line ends removed.
"""
import re, sys, difflib, unicodedata
EXP = {'nro': 'nuestro', 'nra': 'nuestra', 'nros': 'nuestros', 'nras': 'nuestras'}

def norm(w):
    w = unicodedata.normalize('NFD', w.lower())
    w = ''.join(c for c in w if unicodedata.category(c) != 'Mn')
    w = w.replace('j', 'i').replace('v', 'u').replace('ç', 'c').replace('ss', 's')
    return EXP.get(w, w)

def words(t, reading=False):
    if reading:
        m = re.search(r'^## (Reading|Lectura)[^\n]*\n(.*?)(?=^## |\Z)', t, re.S | re.M)
        t = m.group(2)
        t = re.sub(r'^###.*$', '', t, flags=re.M)
    else:
        t = '\n'.join(l for l in t.split('\n') if not l.startswith('#'))
        t = re.sub(r'\{\{[^}]*\}\}', ' ', t); t = t.replace('^', ' ')
        t = re.sub(r'(\w)\|(\w)', r'\1\2', t).replace('|', ' ')
    out = []
    for tok in re.findall(r'\[[^\]]*\]|[^\W\d_]+(?:\[[^\]]*\][^\W\d_]*)*', t):
        if tok.startswith('['):
            out.append(('BR', tok)); continue
        out.append(('W', tok))
    return out

r = words(open(sys.argv[1], encoding='utf8').read(), True)
src = []
for f in sys.argv[2:]:
    src += words(open(f, encoding='utf8').read())
rn = [norm(re.sub(r'[\[\]]', '', w)) for k, w in r if k == 'W']
rw = [w for k, w in r if k == 'W']
sn = [norm(re.sub(r'[\[\]]', '', w)) for k, w in src if k == 'W']
sm = difflib.SequenceMatcher(None, rn, sn, autojunk=False)
carried = sum(b.size for b in sm.get_matching_blocks())
print(f'reading words {len(rn)}, carried by source {carried} ({carried/len(rn):.3f}); bracketed items {sum(1 for k,_ in r if k=="BR")}')
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == 'equal': continue
    print(f'{op:8s} reading: {" ".join(rw[i1:i2])!r:50s} source: {" ".join(w for _,w in src if _=="W")[0:0]}{" ".join(sn[j1:j2])!r}')
