import requests, json, time, sys
Q = sys.argv[1:]
out = {}
for q in Q:
    full = f'({q}) AND date:[1350-01-01 TO 1950-12-31] AND mediatype:(texts)'
    try:
        r = requests.get('https://archive.org/advancedsearch.php', params={'q': full, 'fl[]': ['identifier','title','date','creator','collection','description'], 'rows': 40, 'output': 'json'}, timeout=60)
        d = r.json()['response']
    except Exception as e:
        print('ERR', q, e); continue
    print('##', q, d['numFound'])
    for x in d['docs']:
        desc = x.get('description', '')
        if isinstance(desc, list): desc = ' '.join(desc)
        print(x['identifier'], '|', x.get('date','')[:10], '|', str(x.get('title',''))[:90], '|', str(x.get('creator',''))[:40], '|', desc[:160].replace('\n',' '))
    time.sleep(0.6)
