"""Europeana API sweep for cipher manuscripts held in Poland (aggregates FBC/Polish digital libraries).

    python research/polish_archives/europeana.py     # writes europeana_hits.jsonl

Endpoint: https://api.europeana.eu/record/v2/search.json?wskey=api2demo&query=...&qf=COUNTRY:poland
"""
import json, os, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
TERMS = ['szyfr', 'szyfrem', 'szyfrowany', 'szyfrowana', 'szyfrowane', 'szyfrowanych', 'zaszyfrowany',
         'zaszyfrowana', 'zaszyfrowane', 'szyfrowy', 'szyfrów', 'szyfru', 'cyfrą', 'cyframi', 'Chiffre', 'chiffre',
         'chiffres', 'chiffré', 'Ziffer', 'Ziffern', 'chiffriert', 'Geheimschrift', 'cifra', 'cifre', 'ciphra', 'zifra',
         'kryptogram', 'tajnopis', 'nomenklator', 'klucz szyfrowy']


def search(q, cursor):
    url = 'https://api.europeana.eu/record/v2/search.json?' + urllib.parse.urlencode(
        [('wskey', 'api2demo'), ('query', q), ('qf', 'COUNTRY:poland'), ('rows', '100'), ('cursor', cursor),
         ('profile', 'rich')])
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.load(r)


def main():
    seen = {}
    for t in TERMS:
        cursor, n = '*', 0
        while cursor and n < 10:
            try:
                d = search(t, cursor)
            except Exception as e:
                print('ERR', t, e); break
            for it in d.get('items', []):
                k = it['id']
                if k in seen:
                    seen[k]['terms'].append(t); continue
                seen[k] = {'id': k, 'title': it.get('title'), 'year': it.get('year'),
                           'provider': it.get('dataProvider'), 'type': it.get('type'),
                           'desc': it.get('dcDescription'), 'link': it.get('guid'), 'shown_at': it.get('edmIsShownAt'),
                           'terms': [t]}
            print(t, n, d.get('totalResults'))
            cursor, n = d.get('nextCursor'), n + 1
            time.sleep(0.3)
    with open(os.path.join(HERE, 'europeana_hits.jsonl'), 'w', encoding='utf-8') as fh:
        for v in seen.values():
            fh.write(json.dumps(v, ensure_ascii=False) + '\n')
    print(len(seen), 'unique')


if __name__ == '__main__':
    main()
