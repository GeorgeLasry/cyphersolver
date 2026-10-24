"""Add inventory number, availability and scan count to hits.jsonl -> enriched.jsonl.

The item path in title_id is '~'-separated; the inventory number is the deepest segment the clevel API
answers with a non-empty unitid. Rows found only by 'cijfers' (statistics) are dropped.
"""
import json, time, urllib.parse, urllib.request

API = 'https://zvt.nationaalarchief.nl/api/eads/{}/clevels/{}'
cache = {}


def clevel(ead, unit):
    if (ead, unit) not in cache:
        url = API.format(urllib.parse.quote(ead), urllib.parse.quote(unit, safe=''))
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (cyphersolver research)'})
            with urllib.request.urlopen(req, timeout=60) as r:
                cache[(ead, unit)] = json.load(r)
        except Exception:
            cache[(ead, unit)] = {}
        time.sleep(0.25)
    return cache[(ead, unit)]


rows = [json.loads(l) for l in open('hits.jsonl', encoding='utf8')]
rows = [r for r in rows if r['terms'] != ['cijfers']]
with open('enriched.jsonl', 'w', encoding='utf8') as out:
    for i, r in enumerate(rows):
        leaf = clevel(r['ead'], r['title_id'])
        r['scans'] = len(leaf.get('scans') or [])
        segs = [s for s in r['title_id'].split('~') if s]
        for seg in reversed(segs):
            for unit in reversed(seg.split('-')):
                d = clevel(r['ead'], unit)
                if d.get('unitid'):
                    r['inv'] = d['unitid']
                    r['inv_title'] = d.get('unittitle')
                    r['availability'] = d.get('availability')
                    r['scans'] = max(r['scans'], len(d.get('scans') or []))
                    break
            if 'inv' in r:
                break
        out.write(json.dumps(r, ensure_ascii=False) + '\n')
        if i % 100 == 0:
            print(i, flush=True)
