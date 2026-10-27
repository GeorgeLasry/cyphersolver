"""rec.py <naId> [...]: fetch (cached, via nara_reels/reels.get, 4 s spacing) and summarise a NARA catalogue record:
title, level, dates, scope note, extent, digital-object count, ancestors."""
import json, os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'nara_reels'))
import reels

for naid in sys.argv[1:]:
    p = os.path.join(reels.CACHE, f'{naid}.rec.json')
    if os.path.exists(p):
        rec = json.load(open(p, encoding='utf-8'))
    else:
        os.makedirs(reels.CACHE, exist_ok=True)
        d = reels.get(f'records/search?naId={naid}')
        hits = d['body']['hits']['hits']
        if not hits:
            print(naid, 'NO RECORD'); continue
        rec = hits[0]['_source']['record']
        json.dump(rec, open(p, 'w', encoding='utf-8'), ensure_ascii=False)
    anc = ' > '.join(a.get('title', '')[:50] for a in (rec.get('ancestors') or []))
    print('=' * 8, naid, rec.get('levelOfDescription'), '|', rec.get('title'))
    print('  ancestors:', anc)
    for k in ('inclusiveDates', 'coverageDates', 'productionDates'):
        if rec.get(k): print(' ', k, json.dumps(rec[k])[:200])
    for k in ('scopeAndContentNote', 'generalNotes', 'physicalOccurrences', 'microformPublications'):
        if rec.get(k): print(' ', k, re.sub(r'\s+', ' ', json.dumps(rec[k], ensure_ascii=False))[:900])
    dobj = rec.get('digitalObjects') or []
    print('  digitalObjects:', len(dobj), [o.get('objectFilename') for o in dobj[:3]])
