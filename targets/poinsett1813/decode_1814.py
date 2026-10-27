"""Apply key_1814.tsv to transcription_1814.tsv (14 June 1814); write reading_1814.txt and print coverage per copy."""
import re
from pathlib import Path
H = Path(__file__).parent
key = {}
for l in open(H / 'key_1814.tsv', encoding='utf8'):
    if l.startswith(('#', 'group')) or not l.strip(): continue
    g, v = l.split('\t')[:2]; key[int(g)] = v
rows = [l.rstrip('\n').split('\t') for l in open(H / 'transcription_1814.tsv', encoding='utf8')
        if not l.startswith(('#', 'passage'))]


def read(groups):
    out, n, k = [], 0, 0
    for t in groups.split():
        m = re.match(r'(\d+)', t)
        if not m: continue  # '|' and '...' (cut at the gutter)
        if t.endswith('...'): continue
        g = int(m.group(1)); n += 1
        if g in key:
            k += 1; out.append(key[g] + ('s' if '°' in t else '') + ('[?]' if '?' in t else ''))
        else:
            out.append(f'[{g}]')
    return out, n, k


lines, tot = [], {'duplicate_0100': [0, 0], 'rc_0098': [0, 0]}
for r in rows:
    for col, i in (('duplicate_0100', 2), ('rc_0098', 3)):
        out, n, k = read(r[i]); tot[col][0] += n; tot[col][1] += k
        if col == 'duplicate_0100':
            lines.append(f'{r[0]} {r[1]}  {r[i]}\n      {" ".join(out)}\n      clerk: {r[4]}')
for col, (n, k) in tot.items():
    lines.append(f'{col}: {k}/{n} groups with a value = {k / n:.3f}')
(H / 'reading_1814.txt').write_text('\n'.join(lines) + '\n', encoding='utf8')
print('\n'.join(lines))
