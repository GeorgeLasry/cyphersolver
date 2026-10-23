"""b24 (vanreede1787): decode R1026/R1027 from the DECODE transcription (or a corrected group file) with key R1024.
The DECODE sign 'J+' is the writer's hooked 1 (b24 finding: J=1 reads 'au Roi le projet', 'à dix heures', 'il n'y a';
J=3 and the LM-picked digits of resolve_j.py do not). Nulls per the key's Nonvaleurs blocks print as '·'.
Marks: the transcriber's bar strings are kept after the word in {} ('^_' bar above, '__' bar below, counts kept).
    python b24_vr_decode.py R1026|R1027 [groups.tsv]
"""
import re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from b24_vr_key import load, is_null, D
DOCS = {'R1026': 'DOC_R1026_D1852_1852.txt', 'R1027': 'DOC_R1027_D2299_2299.txt'}
def parse(chunk):
    o = []
    for part in chunk.split('.'):
        marks = ''.join(re.findall(r'\^?\{?\^?_+\}?', part))
        p = re.sub(r'\{.*?\}|\^', '', part).replace('J+', 'J')
        p = re.sub(r'[^0-9J?/]', '', p)
        if '/' in p: p = p.split('/')[0]
        if p and re.search(r'[0-9J]', p): o.append(['g', p.replace('J', '1'), marks, p])
    return o
def groups(rec):
    out = []
    for line in (D / DOCS[rec]).read_text(encoding='utf8', errors='replace').splitlines():
        if line.startswith('#'): continue
        pos = 0
        for m in re.finditer(r'<(?:CLEAR|PLAIN)TEXT\s+[A-Z?]+\s+(.*?)>', line):
            out += parse(line[pos:m.start()]); out.append(['c', m.group(1)]); pos = m.end()
        out += parse(line[pos:])
    return out
def word(k, g):
    if '?' in g: return '[%s]' % g
    v = int(g)
    if is_null(v): return '·'
    return k.get(v, '[%d]' % v)
if __name__ == '__main__':
    k, _ = load()
    rec = sys.argv[1]
    gs = groups(rec)
    if len(sys.argv) > 2:   # corrected groups: tsv idx \t group \t marks
        gs = [l.split('\t') for l in pathlib.Path(sys.argv[2]).read_text(encoding='utf8').splitlines() if l and not l.startswith('#')]
        gs = [['c', x[2]] if x[1] == 'C' else ['g', x[1], x[2] if len(x) > 2 else '', x[1]] for x in gs]
    i = 0
    for it in gs:
        if it[0] == 'c': print('\n[clear: %s]' % it[1]); continue
        i += 1
        print('%3d %-6s %-9s %s' % (i, it[1], it[2], word(k, it[1])))
