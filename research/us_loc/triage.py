"""Triage hits.json: per-collection tallies and a title/notes-level split (Oct 2026 LoC sweep).

    python triage.py   -> triage.tsv (one line per hit: class, date, collection, title, terms, url)
"""
import json, os, re, collections

HERE = os.path.dirname(os.path.abspath(__file__))
hits = json.load(open(os.path.join(HERE, 'hits.json'), encoding='utf-8'))
CRYPT = re.compile(r'cipher|cypher|cifra|chiffr|code[ds]?\b|cryptog|secret writing|invisible ink|sympathetic|nomenclat|steganog|geheim', re.I)


def year(h):
    m = re.search(r'(1[3-9]\d\d)', str(h.get('date') or '') + ' ' + (h.get('title') or ''))
    return int(m.group(1)) if m else None


def coll(h):
    p = [x for x in h.get('partof', []) if x not in ('manuscript division', 'american memory')]
    sc = h.get('source_collection')
    if isinstance(sc, list): sc = sc[0] if sc else None
    return sc or (p[-1] if p else '?')


rows = []
for k, h in hits.items():
    meta = ' '.join([h.get('title') or ''] + h.get('notes', []) + h.get('description', []))
    cls = 'META' if CRYPT.search(meta) else 'FULLTEXT'
    y = year(h)
    if y and (y < 1350 or y > 1950):
        cls += '-OUTDATE'
    rows.append((cls, y or '', coll(h), (h.get('title') or '').replace('\t', ' '), ','.join(h['terms']), h.get('url') or k))
rows.sort(key=lambda r: (r[0], r[2], str(r[1])))
with open(os.path.join(HERE, 'triage.tsv'), 'w', encoding='utf-8') as fh:
    for r in rows:
        fh.write('\t'.join(map(str, r)) + '\n')
c = collections.Counter(r[0] for r in rows)
print(c)
cc = collections.Counter((r[2], r[0]) for r in rows)
byc = collections.defaultdict(dict)
for (col, cl), n in cc.items():
    byc[col][cl] = n
for col, d in sorted(byc.items(), key=lambda x: -sum(x[1].values())):
    print(sum(d.values()), col, d)
