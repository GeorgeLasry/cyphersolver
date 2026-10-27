"""Triage raw/hits.jsonl: date filter (<1951), noise filter, cipher-context score. Writes raw/triage.tsv.

    python research/nara_catalog/triage.py [--all]
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
recs = [json.loads(l) for l in open(os.path.join(HERE, 'raw', 'hits.jsonl'), encoding='utf-8')]

NOISE = re.compile(r'zip code|building code|area code|legal code|penal code|code of federal|criminal code|civil code|'
                   r'code of ethics|morse|code number|postal code|tariff code|code of fair|fair competition|nra code|'
                   r'code authority|codes? of conduct|commercial code|code of laws|labor code|uniform code|'
                   r'zone improvement|bar code|color code|code talker|shorthand|census|naturali[sz]ation|'
                   r'navajo|cypher, |cipher, [A-Z]', re.I)
GOOD = re.compile(r'undecipher|not (been )?decipher|not (been )?decod|undecod|could not be (read|deciph|decod)|'
                  r'unable to (read|deciph|decod)|in cipher|in cypher|in code|ciphered|cyphered|cryptogram|'
                  r'enciphered|en chiffre|chiffr|geheimschrift|cifra|nomenclator|secret writing|invisible ink|'
                  r'sympathetic ink|secret ink|intercepted', re.I)
YEAR = re.compile(r'\b(1[3-9]\d\d)\b')


def years(o):
    ys = list(o.get('years') or [])
    if not ys:
        ys = [int(y) for y in re.findall(r'\b(1[5-9]\d\d)[01]\d[0-3]\d\b', o.get('title') or '')]
    if not ys:
        ys = list(o.get('seriesYears') or [])
    if not ys:
        ys = [int(y) for y in YEAR.findall(o.get('title') or '') if 1700 <= int(y) <= 1960]
    return ys


rows = []
for o in recs:
    ys = years(o)
    if ys and min(ys) > 1950:
        continue
    txt = ' '.join([o.get('title') or '', o.get('scope') or '', o.get('notes') or ''])
    noise = bool(NOISE.search(txt))
    good = len(GOOD.findall(txt))
    rows.append((good, noise, min(ys) if ys else 0, o))

rows.sort(key=lambda r: (-r[0], r[1], r[2]))
with open(os.path.join(HERE, 'raw', 'triage.tsv'), 'w', encoding='utf-8') as fh:
    for good, noise, y, o in rows:
        if not ('--all' in sys.argv or good or not noise):
            continue
        fh.write('\t'.join(str(x) for x in [good, int(noise), y, o['naId'], o['level'], o.get('rg'), o.get('coll'),
                                              o['nObjects'], (o['title'] or '')[:160], (o.get('series') or '')[:80],
                                              (o.get('scope') or '').replace('\n', ' ').replace('\t', ' ')[:400]]) + '\n')
print(len(recs), 'records;', len(rows), 'pre-1951 or undated;', sum(1 for r in rows if r[0]), 'with cipher context')
