"""Harvest Archivportal-D / DDB records for cipher terms through the public DDB Solr endpoint (no API key needed).

    python research/archivportal_d/ddb_harvest.py OUT.jsonl

Endpoint: https://api.deutsche-digitale-bibliothek.de/2/search/index/search/select (Solr; q searches the default
catch-all field: title, description, context). All sectors are harvested; sec_01 = archives (Archivportal-D).
Each record is written once (by id) with the list of terms that hit it.
"""
import json, sys, time, urllib.parse, urllib.request

B = 'https://api.deutsche-digitale-bibliothek.de/2/search/index/search/select'
TERMS = ['chiffriert', 'chiffrierte', 'chiffrierten', 'chiffrierter', 'Chiffre', 'Chiffren', 'Chiffern', 'dechiffriert',
         'dechiffrierte', 'Dechiffrierung', 'Dechiffrat', 'Geheimschrift', 'Zifferschrift', '"in Ziffern"', 'Ziffernbrief',
         'verschlüsselt', 'verschlüsselte', 'Chiffrierschlüssel', 'Chiffrenschlüssel', '"mit Chiffren"', '"in Chiffren"',
         '"in Chiffern"', 'cifra', 'chiffre', 'chiffré', 'chiffrée', 'chiffrées', 'chiffrés', 'Geheimzeichen',
         'Ziffernschrift', 'Chiffreschrift', 'Chiffrebrief', 'Chiffrebriefe', 'entziffert', 'Entzifferung', 'cifrato',
         'Kryptogramm', 'Geheimtinte', 'Zifra', 'Ziffernschlüssel']


def get(params):
    url = B + '?' + urllib.parse.urlencode(params)
    for i in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return json.load(r)
        except Exception as e:
            print('retry', e, file=sys.stderr)
            time.sleep(3 * (i + 1))
    raise RuntimeError(url)


def main(out):
    recs = {}
    counts = {}
    for t in TERMS:
        start, n = 0, None
        while True:
            d = get({'q': t, 'rows': 500, 'start': start, 'wt': 'json', 'sort': 'id asc'})
            n = d['response']['numFound']
            docs = d['response']['docs']
            for doc in docs:
                doc.pop('preview_store', None)
                rid = doc['id']
                if rid in recs:
                    recs[rid]['_terms'].append(t)
                else:
                    doc['_terms'] = [t]
                    recs[rid] = doc
            start += 500
            if start >= n or not docs:
                break
        counts[t] = n
        print(t, n, file=sys.stderr)
    with open(out, 'w', encoding='utf-8') as fh:
        for r in recs.values():
            fh.write(json.dumps(r, ensure_ascii=False) + '\n')
    json.dump(counts, open(out + '.counts.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(recs), 'unique', file=sys.stderr)


if __name__ == '__main__':
    main(sys.argv[1])
