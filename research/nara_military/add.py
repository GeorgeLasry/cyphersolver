"""Append candidate rows to candidates.json (dedup by title). Usage: python add.py rows.json"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, 'candidates.json')
FIELDS = ["year","date","title","correspondents","place","language","region","period","shelfmark","folio_note","cls",
          "status","why","importance","solvability","difficulty","score_note","verify","links","seen","source","prior_art","decode_ids"]
cur = json.load(open(P, encoding='utf-8')) if os.path.exists(P) else []
new = json.load(open(sys.argv[1], encoding='utf-8'))
titles = {c['title'] for c in cur}
for r in new:
    r.setdefault('score_note', 'Scored from the published description during the Oct 2026 US military/intelligence records sweep (research/nara_military/); not viewed')
    r.setdefault('source', 'NARA / US military and intelligence records sweep')
    r.setdefault('seen', 'catalogue')
    missing = [f for f in FIELDS if f not in r and f != 'decode_ids']
    if missing: sys.exit(f"missing {missing} in {r.get('title')}")
    r = {f: r[f] for f in FIELDS if f in r}
    if r['title'] in titles: continue
    cur.append(r); titles.add(r['title'])
json.dump(cur, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(cur), 'rows')
