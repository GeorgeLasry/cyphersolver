"""v5 (b): show one outcome.texts entry (by index) of a target, without long summary fields.
    python research/reading_audit/v5b_show.py <folder> <idx> [<idx> ...]"""
import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
p = json.loads((ROOT / 'targets' / sys.argv[1] / 'profile.json').read_text(encoding='utf8'))
for i in sys.argv[2:]:
    e = p['outcome']['texts'][int(i)]
    print(f'--- #{i}', json.dumps({k: v for k, v in e.items() if k not in ('summary',)}, ensure_ascii=False, indent=1))
print('class', p['outcome'].get('class'), 'fraction', p['outcome'].get('fraction_read'), 'n texts', len(p['outcome']['texts']))
