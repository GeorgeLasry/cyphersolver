"""Keyword harvest of NARA catalog descriptions held at the National Archives at Chicago.

    python research/chi_nara/harvest.py
Filter: record.physicalOccurrences.referenceUnits.city:Chicago (flat AND; parentheses give 503).
Writes raw/hits.jsonl (one compact record per naId with the queries that found it) and raw/harvest.log.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import client
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'raw', 'hits.jsonl'); LOG = os.path.join(HERE, 'raw', 'harvest.log')
LOC = 'record.physicalOccurrences.referenceUnits.city:Chicago'
TERMS = ['cipher', 'ciphers', 'ciphered', 'cypher', 'cryptogram', 'cryptograms', 'cryptographic', 'cryptography',
         'decipher', 'deciphered', 'decode', 'decoded', 'coded', 'codebook', 'encoded', 'enciphered',
         'espionage', 'spy', 'spies', 'sabotage', 'Hindu', 'Ghadr', 'Gadar', 'Gupta', 'conspiracy AND German',
         'invisible AND ink', 'secret AND ink', 'secret AND writing', 'code AND message', 'code AND messages',
         'code AND telegram', 'code AND telegrams', 'code AND letter', 'code AND letters', 'code AND book',
         'rum AND code', 'liquor AND code', 'radio AND code', 'smuggling AND code', 'Trading AND Enemy',
         'German AND agent', 'Bund AND espionage', 'Nazi', 'Japanese AND espionage', 'intercepted', 'secret AND code',
         'cablegram', 'enemy AND alien AND letters', 'censor', 'Bolshevik', 'IWW AND code', 'counterfeit AND code',
         'Duquesne', 'Haupt', 'saboteurs', 'Pastorius', 'Lusitania', 'Jahnke', 'Witzke', 'Rintelen', 'Bopp',
         'Ram Chandra', 'Sekunna', 'Boehm', 'Jacobsen', 'Ras Bihari', 'Hindu AND German', 'treason']

def compact(r):
    anc = r.get('ancestors', [])
    rg = next((a.get('recordGroupNumber') for a in anc if a.get('recordGroupNumber')), None)
    series = next((a for a in anc if a.get('levelOfDescription') == 'series'), {})
    fu = next((a for a in anc if a.get('levelOfDescription') == 'fileUnit'), {})
    yr = lambda d: d.get('year') if isinstance(d, dict) else None
    ys = [yr(r.get(k)) for k in ('coverageStartDate', 'coverageEndDate', 'inclusiveStartDate', 'inclusiveEndDate')]
    ys += [yr(p) for p in r.get('productionDates', []) or []]
    return {'naId': r['naId'], 'level': r.get('levelOfDescription'), 'title': r.get('title'),
            'scope': (r.get('scopeAndContentNote') or '')[:3000],
            'notes': ' | '.join(n.get('note', '') if isinstance(n, dict) else str(n) for n in (r.get('generalNotes') or []))[:1500],
            'rg': rg, 'series': series.get('title'), 'seriesNaId': series.get('naId'), 'fileUnit': fu.get('title'),
            'years': [y for y in ys if y], 'nObjects': len(r.get('digitalObjects', []) or [])}

def main(terms):
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    seen = {}
    if os.path.exists(OUT):
        for line in open(OUT, encoding='utf-8'):
            o = json.loads(line); seen[o['naId']] = o
    log = open(LOG, 'a', encoding='utf-8')
    for t in terms:
        q = f'{LOC} AND {t}'
        page, n, total = 1, 0, None
        while True:
            try:
                d = client.search(q=q, limit=100, page=page)
            except client.Blocked as e:
                print('BLOCKED', e); log.write(f'BLOCKED {e}\n'); return
            if not d or 'body' not in d:
                print('FAIL', q); break
            total = d['body']['hits']['total']['value']
            hits = d['body']['hits']['hits']
            for h in hits:
                r = h['_source'].get('record') or {}
                if 'naId' not in r: continue
                o = seen.get(r['naId']) or compact(r)
                o.setdefault('queries', [])
                if t not in o['queries']: o['queries'].append(t)
                seen[r['naId']] = o; n += 1
            if not hits or n >= min(total, 1000): break
            page += 1
        print(f'{total!s:>6}  {t}', flush=True); log.write(f'{total}\t{t}\n'); log.flush()
        with open(OUT, 'w', encoding='utf-8') as fh:
            for o in seen.values(): fh.write(json.dumps(o, ensure_ascii=False) + '\n')
    print('records', len(seen))

if __name__ == '__main__':
    main(sys.argv[1:] or TERMS)
