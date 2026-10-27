"""Keyword harvest of the NARA catalogue through its open proxy (no API key).

    python research/nara_catalog/harvest.py            # all queries in QUERIES
    python research/nara_catalog/harvest.py "<lucene>"  # one extra query

Endpoint: https://catalog.archives.gov/proxy/records/search?q=<lucene>&limit=100&page=<n>
Field queries work (record.title:..., record.scopeAndContentNote:...); quoted phrases inside a field query return 0,
so phrases are written as AND of words and filtered locally. A plain q= searches the OCR text of digitised pages too.
Writes raw/hits.jsonl: one compact record per naId, with every query that found it.
"""
import json, os, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'raw', 'hits.jsonl')
BASE = 'https://catalog.archives.gov/proxy/records/search?'

F = lambda w: f'record.title:{w} OR record.scopeAndContentNote:{w}'
B = lambda a, b: [f'record.title:{a} AND record.title:{b}', f'record.scopeAndContentNote:{a} AND record.scopeAndContentNote:{b}']
# Parentheses in q make the proxy answer 503, so every query is a flat OR / AND.
QUERIES = [
    F('cipher'), F('ciphers'), F('ciphered'), F('cypher'), F('cyphered'), F('cyphers'),
    F('cryptogram'), F('cryptograms'), F('cryptographic'), F('cryptography'),
    F('undeciphered'), F('decipher'), F('deciphered'), F('decyphered'), F('decipherment'),
    F('undecoded'), F('decode'), F('decoded'), F('nomenclator'), F('codebook'), F('codebooks'),
    F('chiffre'), F('chiffres'), F('geheimschrift'), F('cifra'), F('cifrado'), F('chiffriert'),
    F('cryptographer'), F('enciphered'), F('encoded'), F('intercepted'),
] + [q for b in ('message', 'messages', 'telegram', 'telegrams', 'cable', 'cables', 'letter', 'letters',
                 'dispatch', 'despatch', 'book', 'key') for q in B('code', b)] + [
    q for a, b in (('secret', 'writing'), ('invisible', 'ink'), ('secret', 'ink'), ('sympathetic', 'ink'),
                   ('cipher', 'key')) for q in B(a, b)] + [
    # plain full-text (includes OCR of digitised pages): only the rare phrases
    'undeciphered', '"not deciphered"', '"not decoded"', '"could not be deciphered"', '"not been deciphered"',
    'undecoded', '"en chiffre"', 'nomenclator', 'cryptogram', '"in cipher"',
]


def get(q, page):
    url = BASE + urllib.parse.urlencode({'q': q, 'limit': 100, 'page': page})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'Accept': 'application/json'}), timeout=120) as r:
                return json.loads(r.read().decode('utf-8'))
        except Exception as e:
            print('  retry', page, e, file=sys.stderr)
            time.sleep(5 * (attempt + 1))
    return None


def year(d):
    return d.get('year') if isinstance(d, dict) else None


def compact(r):
    anc = r.get('ancestors', [])
    rg = next((a.get('recordGroupNumber') for a in anc if a.get('recordGroupNumber')), None)
    coll = next((a.get('collectionIdentifier') for a in anc if a.get('collectionIdentifier')), None)
    series = next((a for a in anc if a.get('levelOfDescription') == 'series'), {})
    ys = []
    for k in ('coverageStartDate', 'coverageEndDate', 'inclusiveStartDate', 'inclusiveEndDate'):
        ys.append(year(r.get(k)))
    for pd in r.get('productionDates', []) or []:
        ys.append(year(pd))
    ys2 = [year(series.get('inclusiveStartDate')), year(series.get('inclusiveEndDate'))]
    return {
        'naId': r['naId'], 'level': r.get('levelOfDescription'), 'title': r.get('title'),
        'scope': (r.get('scopeAndContentNote') or '')[:3000],
        'notes': ' | '.join(n.get('note', '') if isinstance(n, dict) else str(n) for n in (r.get('generalNotes') or []))[:1500],
        'rg': rg, 'coll': coll, 'series': series.get('title'), 'seriesNaId': series.get('naId'),
        'years': [y for y in ys if y], 'seriesYears': [y for y in ys2 if y],
        'parent': anc[0].get('title') if anc else None,
        'nObjects': len(r.get('digitalObjects', []) or []),
        'micro': [m.get('publicationNumber') for m in r.get('microformPublications', []) or [] if isinstance(m, dict)],
    }


def main(queries):
    seen = {}
    if os.path.exists(OUT):
        for line in open(OUT, encoding='utf-8'):
            o = json.loads(line); seen[o['naId']] = o
    done_q = {q for o in seen.values() for q in o['queries']}
    for q in queries:
        if q in done_q and len(sys.argv) == 1:
            print('skip', q); continue
        d = get(q, 1)
        if not d or 'body' not in d:
            print('FAIL', q); continue
        total = d['body']['hits']['total']['value']
        print(f'{total:6d}  {q}', flush=True)
        if total > 3000:
            print('   too many, first 3000 only')
        page, n = 1, 0
        while d and d['body']['hits']['hits']:
            for h in d['body']['hits']['hits']:
                r = h['_source'].get('record') or {}
                if 'naId' not in r:
                    continue
                o = seen.get(r['naId']) or compact(r)
                o.setdefault('queries', [])
                if q not in o['queries']:
                    o['queries'].append(q)
                seen[r['naId']] = o; n += 1
            page += 1
            if n >= min(total, 3000):
                break
            time.sleep(0.5)
            d = get(q, page)
        with open(OUT, 'w', encoding='utf-8') as fh:
            for o in seen.values():
                fh.write(json.dumps(o, ensure_ascii=False) + '\n')
    print('records', len(seen))


if __name__ == '__main__':
    main(sys.argv[1:] or QUERIES)
