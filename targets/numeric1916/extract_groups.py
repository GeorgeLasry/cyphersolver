"""Copy Brice Dudout's re-read digit streams out of his repository into groups.tsv.

  python -I extract_groups.py <path to wenmi/solver/numeric1916/data/messages.json>

Only the digits, the family named by the clear prefix, the direction and date, and his published raw text
(for the comparison in decode.py) are kept. Source: github.com/bdudout/wenmi, solver/numeric1916, CC BY 4.0.
The prefix groups (0364 1378, 1369 1378, 6591 1378) are not in the stream: his file strips them.
"""
import json, sys
from pathlib import Path

src = Path(sys.argv[1])
out = Path(__file__).resolve().parent / 'groups.tsv'
d = json.loads(src.read_text(encoding='utf-8'))['messages']
rows = ['# id\tfamily\tprefix\tdirection\tday\tsheets\tgroups\traw_published']
for mid, m in d.items():
    if m['family'] in ('open',):
        continue
    sheets = ';'.join(f'{a} p{b}{c}' for a, b, c in m['sheets'])
    groups = ' '.join(g['cipher'] for g in m['groups'])
    rows.append('\t'.join([mid, m['family'], m['prefix'] or '-', m['dir'] or '-', str(m['date'] or '-'),
                           sheets, groups, m['raw_published'] or '-']))
out.write_text('\n'.join(rows) + '\n', encoding='utf-8')
print(f'{len(rows) - 1} telegrams -> {out}')
