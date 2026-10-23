"""v3 verify (a): show the profile entry for each v3_below_a.txt row (or one folder) and the scored file's head.

    python research/reading_audit/v3a_show.py [folder]
"""
import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
rows = [l.split('\t') for l in (ROOT / 'research/reading_audit/v3_below_a.txt').read_text(encoding='utf8').splitlines() if l.strip()]
want = sys.argv[1] if len(sys.argv) > 1 else None
for folder, idx, doc, lang, f in rows:
    if want and folder != want: continue
    p = json.loads((ROOT / 'targets' / folder / 'profile.json').read_text(encoding='utf8'))
    e = p['outcome']['texts'][int(idx)]
    print('=' * 20, folder, idx, doc, lang, f)
    print(json.dumps(e, ensure_ascii=False, indent=1)[:2500])
    print('class', p['outcome'].get('class'), 'method', p['outcome'].get('method'), 'fraction', p['outcome'].get('fraction_read'))
