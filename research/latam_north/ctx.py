"""python ctx.py REGEX id...: print the scopeContent of DataViva records with REGEX matches marked."""
import json, re, sys, time, urllib.request
rx = re.compile(sys.argv[1], re.I)
for i in sys.argv[2:]:
    u = f'https://dataviva.archivogeneral.gov.co/api/resources/public/details/{i}'
    d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60))
    fl = d.get('metadata', {}).get('firstLevel', {})
    sc = fl.get('scopeContent', '') or ''
    print('==', i, d.get('ident'), (fl.get('temporalCoverage') or {}), fl.get('title'), '| files', len(d.get('filesObj') or []))
    hits = [m.start() for m in rx.finditer(sc)]
    for h in hits[:4]:
        print('   ...', sc[max(0, h-300):h+250].replace('\n', ' '))
    if not hits:
        print('   [no match in scope]', sc[:300].replace('\n', ' '))
    time.sleep(1)
