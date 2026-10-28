"""Newberry Library catalogue (CARLI I-Share Primo VE, view 01CARLI_NBY:CARLI_NBY) search via the public primaws JSON API.
Usage: python primo.py "<query>" [scope] [tab]   -> appends hits to primo_hits.jsonl and prints a summary."""
import json, sys, time, requests
UA = {'User-Agent': 'cyphersolver research (catalogue sweep)'}
BASE = 'https://i-share-nby.primo.exlibrisgroup.com/primaws/rest/pub'
VID = '01CARLI_NBY:CARLI_NBY'
S = requests.Session(); S.headers.update(UA)

def jwt():
    r = S.get(f'{BASE}/institution/01CARLI_NBY/guestJwt', params={'isGuest': 'true', 'lang': 'en', 'viewId': VID,
              'targetUrl': 'https://i-share-nby.primo.exlibrisgroup.com'}, timeout=60)
    return r.json()

def search(q, scope='MyInstitution', tab='LibraryCatalog', offset=0, limit=50, tok=None, inc=''):
    p = dict(blendFacetsSeparately='false', disableCache='false', getMore='0', inst='01CARLI_NBY', lang='en',
             limit=limit, newspapersActive='false', newspapersSearch='false', offset=offset, pcAvailability='false',
             q=q, qExclude='', qInclude=inc, rapido='false', refEntryActive='false', rtaLinks='true', scope=scope,
             searchInFulltextUserSetting='false', skipDelivery='Y', sort='rank', tab=tab, vid=VID)
    h = {'Authorization': 'Bearer ' + tok} if tok else {}
    r = S.get(f'{BASE}/pnxs', params=p, headers=h, timeout=60)
    if r.status_code in (403, 429):
        sys.exit(f'STOP {r.status_code}')
    return r.json()

def brief(doc):
    d = doc['pnx']['display']; c = doc['pnx']['control']
    g = lambda k: ' | '.join(d.get(k, []))
    return dict(id=c.get('recordid', [''])[0], title=g('title'), date=g('creationdate'), type=g('type'),
                creator=g('creator') or g('contributor'), desc=g('description')[:1500], subject=g('subject')[:400],
                notes=' | '.join(v for k in sorted(d) if k.startswith('lds') for v in d[k])[:3000],
                identifier=g('identifier'), format=g('format'))

if __name__ == '__main__':
    q = sys.argv[1]; scope = sys.argv[2] if len(sys.argv) > 2 else 'MyInstitution'
    tab = 'LibraryCatalog'
    inc = sys.argv[3] if len(sys.argv) > 3 else ''
    tok = jwt(); off = 0; out = []
    while True:
        res = search(q, scope, tab, off, 50, tok, inc)
        total = res.get('info', {}).get('total', 0)
        docs = res.get('docs', [])
        out += [brief(x) for x in docs]
        off += 50
        if off >= total or not docs or off >= 500:
            break
        time.sleep(3)
    with open('primo_hits.jsonl', 'a', encoding='utf-8') as fh:
        for o in out:
            o['query'] = q + ' ' + inc; fh.write(json.dumps(o, ensure_ascii=False) + '\n')
    sys.stdout.reconfigure(encoding='utf-8')
    print(f'QUERY {q} inc={inc} scope={scope} total={total} fetched={len(out)}')
    for o in out:
        print('-', o['id'], '|', o['date'], '|', o['type'], '|', o['title'][:150])
