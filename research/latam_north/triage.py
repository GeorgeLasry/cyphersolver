"""Fetch details for every DataViva hit under the given query keys (default: all keys containing a space)
and print the scope-content snippets that match the cipher regex. Caches details in details_cache.json."""
import json, os, re, sys, time, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
hits = json.load(open(os.path.join(HERE, 'dataviva_hits.json'), encoding='utf-8'))
cache_p = os.path.join(HERE, 'details_cache.json')
cache = json.load(open(cache_p, encoding='utf-8')) if os.path.exists(cache_p) else {}
RX = re.compile(r'cifr\w*|en clave|clave secreta|clave (?:de|para|telegr)|claves|tinta simp\w*|jerogl\w*|criptogr\w*|signos convencionales|descifr\w*', re.I)
keys = sys.argv[1:] or [k for k in hits if ' ' in k]
ids = []
for k in keys:
    for r in hits[k]['resources']:
        if r['id'] not in ids:
            ids.append(r['id'])
print(len(ids), 'ids')
for i in ids:
    if i not in cache:
        u = f'https://dataviva.archivogeneral.gov.co/api/resources/public/details/{i}'
        try:
            cache[i] = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60))
        except Exception as e:
            print('err', i, e); continue
        time.sleep(0.7)
        json.dump(cache, open(cache_p, 'w', encoding='utf-8'), ensure_ascii=False)
    d = cache[i]
    fl = d.get('metadata', {}).get('firstLevel', {})
    sc = ' '.join(str(f.get('value')) for f in d.get('fields', []) if f.get('label') in ('Título', 'Alcance y contenido'))
    ms = list(RX.finditer(sc))
    if not ms:
        continue
    print('==', i, d.get('ident'), (fl.get('temporalCoverage') or {}).get('start', '')[:4], '| files', len(d.get('filesObj') or []), '|', (fl.get('title') or '')[:80])
    for m in ms[:3]:
        print('    ...', sc[max(0, m.start()-220):m.end()+180].replace('\n', ' '))
