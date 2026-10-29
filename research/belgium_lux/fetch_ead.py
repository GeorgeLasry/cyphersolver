"""Download the EAD XML of every inventory listed in inventories.json / inv_free.json into ead/ (cached, git-ignored)."""
import json, os, sys, time, urllib.request

ids = {}
for f in ('inventories.json', 'inv_free.json'):
    for spec, docs in json.load(open(f, encoding='utf8')).items():
        for d in docs:
            if spec.startswith('free:') and (d['start_year'] or 9999) >= 1900:
                continue
            ids[d['id']] = d
print(len(ids), 'inventories', file=sys.stderr)
os.makedirs('ead', exist_ok=True)
for i, eid in enumerate(sorted(ids)):
    path = f'ead/{eid}.xml'
    if os.path.exists(path) and os.path.getsize(path) > 500:
        continue
    url = f'https://agatha.arch.be/en/data/ead/{eid}.ead.xml'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (cyphersolver research sweep)'})
        data = urllib.request.urlopen(req, timeout=180).read()
        open(path, 'wb').write(data)
        print(i, eid, len(data), file=sys.stderr, flush=True)
    except Exception as e:
        print(i, eid, 'ERR', e, file=sys.stderr, flush=True)
    time.sleep(1)
json.dump(ids, open('inventory_index.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
