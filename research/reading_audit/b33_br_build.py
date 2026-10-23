"""b33 riksarkivet1628 (Bremen 1631): check bremen1631_aligned.txt word by word against the band-key decode and
write the reading body and the alignment table.

    python b33_br_build.py <target dir>
writes <dir>/bremen1631_body.txt (reading body, one paragraph per line) and <dir>/bremen1631_alignment.tsv;
prints every cipher word whose decode differs from its reading word, and the counts.
"""
import re, sys, os, unicodedata
sys.path.insert(0, os.path.dirname(__file__))
from b33_br_dec import dec

D = sys.argv[1]
src = open(os.path.join(D, 'bremen1631_aligned.txt'), encoding='utf8').read()
TOK = re.compile(r'\{([^|}]*)\|([^|}]*)(?:\|(g))?\}')


def norm(w):
    w = unicodedata.normalize('NFD', w.lower())
    w = ''.join(c for c in w if not unicodedata.combining(c))
    return re.sub(r'[^a-z]', '', w).replace('v', 'u').replace('j', 'i')


def edits(a, b):
    p = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        c = [i]
        for j, y in enumerate(b, 1):
            c.append(min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (x != y)))
        p = c
    return p[-1]


rows, out, stats = [], [], dict(words=0, exact=0, gloss=0, hole=0, code=0, groups=0, bad=0)
for line in src.splitlines():
    if line.startswith('#') or not line.strip():
        continue
    if line.startswith('='):
        out.append('### ' + line[1:].strip()); continue
    for m in TOK.finditer(line):
        g, w, flag = m.group(1).strip(), m.group(2).strip(), m.group(3)
        if g.startswith('#'):
            stats['code'] += 1
            rows.append((g, '(code)', w, 'nomenclator')); continue
        nums = g.split(); stats['groups'] += len(nums); stats['words'] += 1
        d = ''.join(dec(n) for n in nums)
        if w.startswith('['):
            stats['hole'] += 1; rows.append((g, d, w, 'hole')); continue
        e = edits(d, norm(w))
        if e == 0:
            stats['exact'] += 1; st = 'exact'
        elif flag == 'g':
            stats['gloss'] += 1; st = 'gloss (%d edits)' % e
        else:
            stats['bad'] += 1; st = 'MISMATCH (%d edits)' % e
            print('MISMATCH', g, d, w)
        rows.append((g, d, w, st))
    out.append(TOK.sub(lambda m: m.group(2), line))
open(os.path.join(D, 'bremen1631_body.txt'), 'w', encoding='utf8').write('\n\n'.join(out) + '\n')
with open(os.path.join(D, 'bremen1631_alignment.tsv'), 'w', encoding='utf8') as f:
    f.write('groups\tdecode\treading\tstatus\n')
    for r in rows:
        f.write('\t'.join(r) + '\n')
print(stats)
