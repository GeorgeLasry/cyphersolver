"""v2 verify sweep: mark as holes the reading words that rest on a look-alike alternate (align tsv class_resolved).

    python v2_lookalike_holes.py <reading.md> <align.tsv> <out.md>

Walks the cipher words of the align tsv in order and finds each in the reading body (clear text in *...* is skipped
by the search moving forward); a word with a class_resolved entry is replaced by [?]. Prints how many were marked.
"""
import csv, re, sys
rd, al, out = sys.argv[1:4]
t = open(rd, encoding='utf8').read()
m = re.search(r'^## Reading[^\n]*\n(.*?)(?=^## |\Z)', t, re.S | re.M)
body = m.group(1)
rows = list(csv.DictReader(open(al, encoding='utf8'), delimiter='\t'))
pos, marked, missed, res = 0, 0, 0, []
for r in rows:
    w = r['word'].strip(' .,;:')
    if not w: continue
    i = body.find(w, pos)
    if i < 0: missed += 1; continue
    if r['class_resolved'].strip():
        res.append(body[pos:i]); res.append('[?]'); marked += 1
    else:
        res.append(body[pos:i + len(w)])
    pos = i + len(w)
res.append(body[pos:])
open(out, 'w', encoding='utf8').write('## Reading\n' + ''.join(res))
print('marked', marked, 'missed', missed, 'of', len(rows))
