"""Harvest cipher-related inventory items from the Nationaal Archief EAD search.

API (found from the zvt client, Oct 2026):
  GET https://zvt.nationaalarchief.nl/api/search/eads?q=..&page=..&rows=..       archive-level hits
  GET https://zvt.nationaalarchief.nl/api/search/eads/<eadID>?q=..&page=..&rows=.. item-level hits
Writes hits.jsonl (one row per archive x item, with the search terms that found it).
"""
import json, re, sys, time, html, urllib.parse, urllib.request

BASE = 'https://zvt.nationaalarchief.nl/api/search'
TERMS = ['cijfer', 'cijfers', 'gecijferd', 'ontcijferd', 'ontcijfering', 'ontcijferingen', 'decijfering',
         'dechiffrement', 'dechiffrementen', 'déchiffrement', 'chiffre', 'chiffres', 'chiffré', 'cijferschrift',
         'geheimschrift', 'cijfersleutel', 'cijfersleutels', 'sleutels van cijfers', 'cifra', 'zifra', 'nomenclator',
         'chiffreur', 'geheime brieven', 'secrete brieven', 'secreta']
MAX_START = 1900  # archives whose period starts after this are modern statistics noise


def get(path, **params):
    url = f'{BASE}/{path}?' + urllib.parse.urlencode(params)
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (cyphersolver research)'})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception as e:
            print('retry', url, e, file=sys.stderr)
            time.sleep(3 * (attempt + 1))
    return {}


def archives(term):
    out, page = [], 1
    while True:
        d = get('eads', q=term, page=page, rows=50)
        res = d.get('results') or []
        out += res
        if page >= (d.get('pages') or 0) or not res:
            return out
        page += 1


def items(ead, term):
    out, page = [], 1
    while True:
        d = get(f'eads/{urllib.parse.quote(ead)}', q=term, page=page, rows=100)
        res = d.get('results') or []
        out += res
        if page >= (d.get('pages') or 0) or not res:
            return out
        page += 1
        time.sleep(0.3)


def start_year(period):
    m = re.match(r'\D*(\d{4})', period or '')
    return int(m.group(1)) if m else 0


def main():
    seen = {}
    for term in TERMS:
        for a in archives(term):
            if a.get('type') != 'ARCHIVE' or start_year(a.get('period')) > MAX_START:
                continue
            ead = a['id']
            for it in items(ead, term):
                if it.get('type') != 'CLEVEL':
                    continue
                key = (ead, it['title_id'])
                row = seen.setdefault(key, {'ead': ead, 'archive': html.unescape(a['title']), 'period': a.get('period'),
                                            'title_id': it['title_id'],
                                            'title': html.unescape(re.sub('<[^>]+>', '', it['title'])), 'terms': []})
                row['terms'].append(term)
            time.sleep(0.3)
        print(term, len(seen), file=sys.stderr)
    with open('hits.jsonl', 'w', encoding='utf8') as f:
        for row in seen.values():
            f.write(json.dumps(row, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    main()
