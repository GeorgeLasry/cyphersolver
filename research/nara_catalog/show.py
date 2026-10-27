"""Print one NARA catalogue record: python show.py <naId> [...]"""
import json, sys, time, urllib.request
for id in sys.argv[1:]:
    for a in range(4):
        try:
            d = json.loads(urllib.request.urlopen(f'https://catalog.archives.gov/proxy/records/search?naId={id}', timeout=60).read().decode('utf-8')); break
        except Exception:
            time.sleep(4)
    r = d['body']['hits']['hits'][0]['_source']['record']
    print('##', r['naId'], r['levelOfDescription'], r['title'])
    print('  anc:', ' > '.join(f"{a.get('title','')[:60]}[{a.get('naId')}]" for a in reversed(r.get('ancestors', []))))
    for k in ('scopeAndContentNote', 'generalNotes', 'productionDates', 'coverageStartDate', 'coverageEndDate', 'inclusiveStartDate', 'microformPublications', 'localIdentifier', 'creators', 'organizationalReferences'):
        if r.get(k): print('  ', k, json.dumps(r[k], ensure_ascii=False)[:900])
    objs = r.get('digitalObjects', []) or []
    print('   objects', len(objs), [o['objectUrl'] for o in objs[:2]])
