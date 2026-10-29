"""Build texts/f<folio>_tokens.tsv from the line rows of texts/f<folio>.md and print read shares.
Row format in the md: L<n> `sign=value | sign=value ...`. A cell without '=' (e.g. a run of padding signs) is
expanded into one token per space-separated sign with value [..]."""
import re, sys, pathlib
f = sys.argv[1]
d = pathlib.Path(__file__).parent
rows = []
for line in (d / f'f{f}.md').read_text(encoding='utf-8').splitlines():
    m = re.match(r'L(\d+) `(.*)`', line)
    if not m: continue
    ln = m.group(1)
    for cell in m.group(2).split(' | '):
        cell = cell.strip()
        if cell.startswith('then ') and ':' in cell:
            for s in cell.split(':', 1)[1].split():
                rows.append((ln, s, '[..]'))
            continue
        if '=' in cell:
            s, v = cell.split('=', 1)
            v = v.split(' (')[0].strip()
            rows.append((ln, s.strip(), v))
        else:
            rows.append((ln, cell, '[..]'))
with open(d / f'f{f}_tokens.tsv', 'w', encoding='utf-8') as o:
    o.write('line\tsign\tvalue\n')
    for r in rows: o.write('\t'.join(r) + '\n')
n = len(rows); nul = sum(1 for r in rows if r[2] == '{null}' or r[2] == '{null?}')
unr = sum(1 for r in rows if '[..]' in r[2]); unc = sum(1 for r in rows if '[?]' in r[2])
print(f'f{f}: lines {len(set(r[0] for r in rows))} tokens {n} nulls {nul} unread {unr} uncertain {unc} '
      f'read(non-null) {n-nul-unr}/{n-nul} = {(n-nul-unr)/(n-nul):.1%}')
