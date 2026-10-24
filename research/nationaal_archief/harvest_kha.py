"""Harvest cipher-related items from the Koninklijk Huisarchief catalogue (Koninklijke Verzamelingen).

API (found from the site's Next.js client, Oct 2026):
  GET https://cms.koninklijkeverzamelingen.nl/api/archive/?format=json&query=<term>&limit=50&start=<n>
Writes kha_hits.jsonl (one row per item, with the terms that found it).
"""
import json, sys, time, urllib.parse, urllib.request

TERMS = ['cijfer', 'cijfers', 'gecijferd', 'ontcijferd', 'ontcijfering', 'ontcijferingen', 'dechiffrement',
         'dechiffrementen', 'déchiffrement', 'chiffre', 'chiffres', 'chiffré', 'cijferschrift', 'geheimschrift',
         'sleutel', 'sleutels', 'cifra', 'nomenclator', 'onderschepte', 'onderschept', 'intercepted', 'chiffrant',
         'déchiffrant', 'code']
API = 'https://cms.koninklijkeverzamelingen.nl/api/archive/?'


def get(**params):
    url = API + urllib.parse.urlencode(dict(format='json', limit=50, **params))
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (cyphersolver research)'})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception as e:
            print('retry', url, e, file=sys.stderr)
            time.sleep(4 * (attempt + 1))
    return {'meta': {'total_count': 0}, 'results': []}


seen = {}
for term in TERMS:
    start, total = 1, None
    while True:
        d = get(query=term, start=start)
        total = d['meta']['total_count']
        for r in d['results']:
            row = seen.setdefault(r['name'], dict(r, terms=[]))
            row['terms'].append(term)
        start += 50
        if start > total or not d['results'] or start > 2000:
            break
        time.sleep(0.3)
    print(term, total, len(seen), file=sys.stderr, flush=True)

with open('kha_hits.jsonl', 'w', encoding='utf8') as f:
    for row in seen.values():
        f.write(json.dumps(row, ensure_ascii=False) + '\n')
