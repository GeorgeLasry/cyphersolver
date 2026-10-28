"""Harvest loc.gov /manuscripts/ search results for cipher terms (Oct 2026 LoC sweep).

    python harvest.py            # all TERMS, writes hits.json and appends counts to coverage_raw.json

Each hit keeps: id, title, date, partof, notes, description, call number, url, and which terms matched.
"""
import json, os, sys, urllib.parse
import locapi

HERE = os.path.dirname(os.path.abspath(__file__))
TERMS = ['cipher', 'cypher', 'ciphered', 'cyphered', 'decipher', 'deciphered', 'decypher', 'ciphers', 'cyphers',
         '"in cipher"', '"in cypher"', '"in code"', 'cryptogram', 'cryptograph', '"secret writing"',
         '"invisible ink"', '"sympathetic ink"', 'nomenclator', 'chiffre', 'cifra', '"code telegram"',
         '"cipher telegram"', '"cipher key"', '"code book"', 'decoded', 'undeciphered', 'ciphering', 'encoded',
         'cryptography', 'steganography', 'chiffres', 'cifrado', 'geheimschrift', '"secret code"']
BASE = 'https://www.loc.gov/manuscripts/'


def harvest(term, maxpages=40):
    out, counts = [], {}
    sp = 1
    while True:
        url = BASE + '?' + urllib.parse.urlencode({'q': term, 'fo': 'json', 'c': 100, 'sp': sp})
        d = locapi.get(url)
        if d is None:
            break
        if sp == 1:
            counts['total'] = d['pagination']['of']
            counts['facets'] = {f.get('type') or f.get('title'): [(x.get('title'), x.get('count')) for x in f.get('filters', [])]
                                for f in d.get('facets', []) if (f.get('type') or f.get('title')) in ('partof', 'dates', 'contributor')}
        for r in d['results']:
            it = r.get('item') or {}
            out.append({'id': r.get('id'), 'title': r.get('title'), 'date': r.get('date'),
                        'partof': r.get('partof', []), 'notes': it.get('notes', []),
                        'description': r.get('description', []), 'call_number': it.get('call_number', []),
                        'source_collection': it.get('source_collection'), 'url': r.get('url'),
                        'online_format': r.get('online_format', []), 'segments': r.get('segments', [])})
        if not d['pagination'].get('next') or sp >= maxpages:
            break
        sp += 1
    return out, counts


def main():
    terms = sys.argv[1:] or TERMS
    hp = os.path.join(HERE, 'hits.json')
    cp = os.path.join(HERE, 'coverage_raw.json')
    hits = json.load(open(hp, encoding='utf-8')) if os.path.exists(hp) else {}
    cov = json.load(open(cp, encoding='utf-8')) if os.path.exists(cp) else {}
    for t in terms:
        try:
            res, counts = harvest(t)
        except locapi.Blocked as e:
            print('BLOCKED', e)
            break
        cov['manuscripts:' + t] = {'total': counts.get('total'), 'harvested': len(res), 'facets': counts.get('facets')}
        for h in res:
            k = h['id']
            if k in hits:
                if t not in hits[k]['terms']:
                    hits[k]['terms'].append(t)
            else:
                h['terms'] = [t]
                hits[k] = h
        print(t, counts.get('total'), len(res), 'cum', len(hits), flush=True)
        json.dump(hits, open(hp, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
        json.dump(cov, open(cp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
