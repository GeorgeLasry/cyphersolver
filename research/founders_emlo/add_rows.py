"""Append candidate rows (from a JSON file argument) to candidates.json, skipping titles already present."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, 'candidates.json')
cur = json.load(open(P, encoding='utf-8'))
new = json.load(open(sys.argv[1], encoding='utf-8'))
titles = {r['title'] for r in cur}
for r in new:
    if r['title'] not in titles:
        cur.append(r)
json.dump(cur, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(len(cur), 'rows')
