"""Europeana search API (public demo key) for cipher terms, Italian providers.

    PYTHONUTF8=1 python -I research/milan_archives/europeana_harvest.py

Writes europeana_hits.json: one row per item with provider, title, description, date, link.
"""
import json, os, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
TERMS = ['cifra', '"in cifra"', 'cifrata', 'cifrato', 'cifrate', 'cifrati', 'decifrata', 'decifrato', 'decifrazione',
         'zifra', 'ziffra', 'cifrario', 'cifrari', '"chiave di cifra"', 'contracifra', 'contrazifra', '"lettera cifrata"',
         '"lettere cifrate"', 'cifre', 'ziffre', 'deciferata', 'cifera']
FILTERS = ['COUNTRY:"Italy"']


def get(url):
    for _ in range(3):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return json.load(r)
        except Exception as e:
            print('retry', e, file=sys.stderr)
            time.sleep(3)
    return {}


def main():
    out = {}
    for term in TERMS:
        cursor = '*'
        n = 0
        while cursor and n < 1000:
            q = {'wskey': 'api2demo', 'query': term, 'rows': 100, 'cursor': cursor, 'profile': 'rich'}
            url = 'https://api.europeana.eu/record/v2/search.json?' + urllib.parse.urlencode(q)
            url += ''.join('&qf=' + urllib.parse.quote(f) for f in FILTERS)
            d = get(url)
            items = d.get('items', [])
            if not items:
                break
            for it in items:
                rid = it['id']
                row = out.setdefault(rid, {
                    'id': rid,
                    'provider': (it.get('dataProvider') or [''])[0],
                    'title': ' | '.join(it.get('title', [])),
                    'desc': ' | '.join(it.get('dcDescription', []))[:1500],
                    'year': it.get('year'),
                    'type': it.get('type'),
                    'link': it.get('guid'),
                    'shown': (it.get('edmIsShownAt') or [''])[0],
                    'terms': []})
                row['terms'].append(term)
            n += len(items)
            cursor = d.get('nextCursor')
        print(term, n, file=sys.stderr)
    with open(os.path.join(HERE, 'europeana_hits.json'), 'w', encoding='utf-8') as fh:
        json.dump(list(out.values()), fh, ensure_ascii=False, indent=1)
    print(len(out), 'items')


if __name__ == '__main__':
    main()
