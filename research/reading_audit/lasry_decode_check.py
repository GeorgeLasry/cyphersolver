"""24 Oct 2026: for targets whose Lasry text is only an excerpt (lasry_entry.md, from his BnF cipher research report of
10 Oct 2026), record that DECODE holds no record of the document (full record list, 10,606 rows, fetched 24 Oct 2026,
searched by shelfmark), so no full decryption could be imported under his 24 Oct permission. One step, one NOTES line."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save, ROOT  # noqa: E402
TXT = ("George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list "
       "(10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark ({sm}): no record, so DECODE holds no "
       "decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.")
for T in sys.argv[1:]:
    sm = (ROOT / 'targets' / T / 'lasry_entry.md').read_text(encoding='utf8').split('\n')[2].strip()
    p = load(T)
    if any('10,606 records' in s.get('what', '') for s in p['solution']): continue
    p['solution'].append({'date': '2026-10-24', 'kind': 'literature search', 'what': TXT.format(sm=sm), 'result': 'failed'})
    save(T, p)
    n = ROOT / 'targets' / T / 'NOTES.md'
    s = n.read_text(encoding='utf8').split('\n')
    i = 1
    while i < len(s) and (s[i].strip() == '' or s[i].startswith('Status:')): i += 1
    s.insert(i, '**24 Oct 2026, DECODE check** (Claude Opus 5.5): ' + TXT.format(sm=sm) + '\n')
    n.write_text('\n'.join(s), encoding='utf8', newline='')
    print('noted', T)
