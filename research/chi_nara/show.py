"""Print the harvest as a review table: naId, level, RG, years, objects, queries, title, series, scope snippet."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
rows = [json.loads(l) for l in open(os.path.join(HERE, 'raw', 'hits.jsonl'), encoding='utf-8')]
filt = sys.argv[1:]
for o in sorted(rows, key=lambda o: (o['rg'] or 0, o['naId'])):
    if filt and not any(f in o['queries'] for f in filt): continue
    print(f"{o['naId']} {o['level']} RG{o['rg']} {o['years'][:2]} obj={o['nObjects']} q={','.join(o['queries'])}")
    print('   T:', (o['title'] or '')[:200]); print('   S:', (o['series'] or '')[:120], '| FU:', (o.get('fileUnit') or '')[:80])
    if o['scope']: print('   C:', o['scope'][:400].replace('\n', ' '))
