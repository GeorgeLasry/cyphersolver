"""Polona (polona.pl) search sweep for cipher manuscripts.

    python research/polish_archives/polona.py            # writes polona_hits.jsonl next to this file

Uses the public search endpoint the site's own JS calls:
    POST https://polona.pl/api/search-service/search/simple?query=<q>&page=<n>&pageSize=<k>&sort=RELEVANCE  (body {})
"""
import json, os, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
TERMS = ['szyfr', 'szyfrem', 'szyfrowany', 'szyfrowana', 'szyfrowane', 'szyfrowanych', 'zaszyfrowany', 'zaszyfrowana',
         'cyfra', 'cyfrą', 'pisane szyfrem', 'pisany szyfrem', 'pisana szyfrem', 'klucz szyfrowy', 'klucz do szyfru',
         'Chiffre', 'Ziffer', 'Geheimschrift', 'chiffre', 'chiffré', 'en chiffres', 'cifra', 'cifrario', 'kryptogram',
         'zifra', 'ciffra', 'deszyfr', 'rozszyfrowanie', 'tajnopis', 'szyfrowy', 'nomenklator']


def search(q, page, size=100):
    url = ('https://polona.pl/api/search-service/search/simple?' +
           urllib.parse.urlencode({'query': q, 'page': page, 'pageSize': size, 'sort': 'RELEVANCE'}))
    req = urllib.request.Request(url, data=b'{}', headers={'Content-Type': 'application/json',
                                                           'User-Agent': 'cyphersolver research sweep'})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def flat(h):
    out = {}
    for grp in ('basicFields', 'expandedFields', 'hiddenFields'):
        for k, v in (h.get(grp) or {}).items():
            out[k] = v.get('values')
    out['id'] = h.get('objectId')
    for k, v in (h.get('attributes') or {}).items():
        if isinstance(v, dict) and v.get('stringValue') and k not in out:
            out['attr_' + k] = v['stringValue']
    return out


def main():
    seen = {}
    for t in TERMS:
        page = 0
        while True:
            try:
                d = search(t, page)
            except Exception as e:
                print('ERR', t, page, e, file=sys.stderr); break
            for h in d.get('hits', []):
                f = flat(h)
                key = f.get('id') or json.dumps(f.get('title'))
                if key not in seen:
                    f['terms'] = [t]
                    seen[key] = f
                elif t not in seen[key]['terms']:
                    seen[key]['terms'].append(t)
            print(t, page, d.get('totalElements'), file=sys.stderr)
            if d.get('last', True) or page >= 9:
                break
            page += 1
            time.sleep(0.5)
    with open(os.path.join(HERE, 'polona_hits.jsonl'), 'w', encoding='utf-8') as fh:
        for f in seen.values():
            fh.write(json.dumps(f, ensure_ascii=False) + '\n')
    print(len(seen), 'unique hits', file=sys.stderr)


if __name__ == '__main__':
    main()
