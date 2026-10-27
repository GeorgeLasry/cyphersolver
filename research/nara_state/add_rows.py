"""Append candidate rows to candidates.json (dedup on title). Rows live in rows_*.json files in this folder.

    python add_rows.py rows_1.json
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'candidates.json')
FIELDS = ['year', 'date', 'title', 'correspondents', 'place', 'language', 'region', 'period', 'shelfmark',
          'folio_note', 'cls', 'status', 'why', 'importance', 'solvability', 'difficulty', 'score_note', 'verify',
          'links', 'seen', 'source', 'prior_art', 'decode_ids']

rows = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else []
have = {r['title'] for r in rows}
for f in sys.argv[1:]:
    for r in json.load(open(os.path.join(HERE, f), encoding='utf-8')):
        missing = [k for k in FIELDS if k not in r and k != 'decode_ids']
        extra = [k for k in r if k not in FIELDS]
        assert not missing and not extra, (r['title'], missing, extra)
        if r['title'] in have:
            continue
        rows.append(r); have.add(r['title'])
json.dump(rows, open(OUT, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(len(rows), 'rows')
