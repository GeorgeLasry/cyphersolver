"""Harvest the new Danish Rigsarkivet search (soeg.rigsarkivet.dk, POST /api/v1/Search/arkivalier), which searches
series and creator descriptions in full text (Daisy only matches titles).

    python research/scandinavia/harvest_soeg.py -> soeg_hits.jsonl
"""
import json, os, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
URL = 'https://soeg.rigsarkivet.dk/api/v1/Search/arkivalier'
TERMS = ['ciffre', 'cifre', 'ciffreret', 'cifreret', 'ciffrerede', 'chiffreskrift', 'chifreskrift', 'chifferskrifter', 'chiffrirt', 'chiffrirten', 'dechiffrirt', 'Chiffern', 'chiffrerte', 'chiffreres', 'tallenes', 'hemmelige skrift', 'hemmeligt alfabet', 'geheime', 'kryptografi', 'krypteret', 'chiffer', 'chifferskrift', 'chiffre', 'chiffrer', 'chiffreret', 'chiffrerede', 'chifreret', 'chifrerede', 'chifre',
         'dechiffrering', 'dechiffreret', 'dechiffrerede', 'dechifreret', 'dechifrerede', 'chifferbrev', 'chifferbreve',
         'chiffernøgle', 'chiffernøgler', 'chifferdepeche', 'chifferdepecher', 'ziffer', 'Ziffern', 'Chiffren', 'chiffriert',
         'Geheimschrift', 'cifferskrift', 'ciffer', 'chiffres', 'chiffrées', 'chiffré', 'cipher', 'lønskrift', 'hemmelig skrift',
         'usynligt blæk', 'sympatetisk', 'opsnappede', 'opsnappet', 'intercepterede', 'interciperede', 'intercipierte',
         'kodetelegrammer', 'chiffertelegrammer', 'chiffertelegram', 'kodebog', 'koder', 'chifrering', 'chiffrering',
         'chifferprotokol', 'chiffersystem']


def post(body):
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (cyphersolver research)'})
    with urllib.request.urlopen(req, timeout=120) as f:
        return json.load(f)


def main():
    out = os.path.join(HERE, 'soeg_hits.jsonl')
    seen = set()
    if os.path.exists(out):
        seen = {json.loads(l)['id'] for l in open(out, encoding='utf-8')}
    fh = open(out, 'a', encoding='utf-8')
    for t in TERMS:
        page, n_new, total = 0, 0, None
        while True:
            try:
                d = post({'searchQuery': t, 'pageNumber': page, 'resultsPerPage': 100, 'sortOptions': {'fieldName': 'Dato', 'ascending': True}, 'exactMatch': False})
            except Exception as e:
                print(t, 'ERR', e); break
            total = d.get('totalCount')
            res = d.get('searchResults') or []
            for r in res:
                if r['id'] in seen:
                    continue
                seen.add(r['id']); n_new += 1
                r['term'] = t
                fh.write(json.dumps(r, ensure_ascii=False) + '\n')
            fh.flush()
            page += 1
            if not res or page * 100 >= (total or 0) or page >= 10:
                break
            time.sleep(0.4)
        print(t, total, 'new', n_new, flush=True)


if __name__ == '__main__':
    main()
