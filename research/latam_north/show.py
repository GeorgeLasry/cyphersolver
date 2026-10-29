"""Print DataViva hits: python show.py term [term...]"""
import json, os, sys
d = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dataviva_hits.json'), encoding='utf-8'))
for t in sys.argv[1:] or d:
    print('##', t, d[t]['total'])
    for r in d[t]['resources']:
        m = r.get('metadata', {}).get('firstLevel', {})
        print(' ', r['id'], r.get('ident'), '|', (m.get('temporalCoverage') or {}).get('start', '')[:10], '|', m.get('extent', ''), '|', (m.get('title') or '')[:150], '| files', r.get('files'))
