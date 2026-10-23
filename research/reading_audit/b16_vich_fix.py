"""b16: apply a corrections tsv (line, old, new, nth, evidence) to a vich1511 transcription.
new '-' deletes the token. nth counts occurrences of `old` in the line as it stands when the row is applied.
python b16_vich_fix.py <transcription> <corrections.tsv> <out>"""
import sys, csv
src, tsv, out = sys.argv[1:4]
rows = list(csv.DictReader(open(tsv, encoding='utf-8'), delimiter='\t'))
lines = open(src, encoding='utf-8').read().split('\n')
idx = {l.split(':', 1)[0]: i for i, l in enumerate(lines) if l.startswith('L') and ':' in l}
for r in rows:
    i = idx[r['line']]; tag, body = lines[i].split(':', 1); toks = body.split()
    n = int(r['nth']); k = [j for j, t in enumerate(toks) if t == r['old']]
    if len(k) < n: raise SystemExit(f"{r['line']}: no occurrence {n} of {r['old']}")
    j = k[n - 1]
    if r['new'] == '-': del toks[j]
    else: toks[j] = r['new']
    lines[i] = tag + ': ' + ' '.join(toks)
hdr = f'# b16 (22 Oct 2026): {len(rows)} label corrections from {tsv.split("/")[-1]} applied to {src.split("/")[-1]}'
open(out, 'w', encoding='utf-8').write(hdr + '\n' + '\n'.join(lines))
print(out, len(rows), 'corrections')
