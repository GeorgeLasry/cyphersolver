"""Fetch DataViva public details for resource ids and print the descriptive text around a term.
    python details.py TERM id [id ...]"""
import json, re, sys, time, urllib.request
term = sys.argv[1]
for i in sys.argv[2:]:
    u = f'https://dataviva.archivogeneral.gov.co/api/resources/public/details/{i}'
    with urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60) as r:
        d = json.load(r)
    s = json.dumps(d, ensure_ascii=False)
    md = d.get('metadata', d.get('data', {}).get('metadata', {})) if isinstance(d, dict) else {}
    print('==', i, d.get('ident') or d.get('data', {}).get('ident'))
    for m in re.finditer(term, s, re.I):
        print('   ...', s[max(0, m.start()-400):m.end()+300].replace('\n', ' '))
    if not re.search(term, s, re.I):
        print('   (term not in details) ', s[:600])
    time.sleep(1)
