"""v5a: show one outcome.texts entry (by index) and the head of its scored file.
    python research/reading_audit/v5a_show.py <folder> <idx> [nlines]"""
import json, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
T, i = sys.argv[1], int(sys.argv[2]); n = int(sys.argv[3]) if len(sys.argv) > 3 else 40
p = json.loads((ROOT / 'targets' / T / 'profile.json').read_text(encoding='utf-8'))
e = p['outcome']['texts'][i]
print(json.dumps(e, ensure_ascii=False, indent=1)[:3000])
print('class', p['outcome'].get('class'), 'fraction', p['outcome'].get('fraction_read'), 'ntexts', len(p['outcome']['texts']))
