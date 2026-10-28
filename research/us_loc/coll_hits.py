"""List hit titles for collections whose content is not 'manuscript' format (WDL, Rosenwald, France in America, Meeting of Frontiers)."""
import json, os, sys, urllib.parse, locapi
HERE = os.path.dirname(os.path.abspath(__file__))
out = {}
for slug in ['world-digital-library', 'lessing-j-rosenwald', 'france-in-america', 'meeting-of-frontiers', 'the-atlantic-world-america-and-the-netherlands']:
    for t in ['cipher', 'cypher', 'decipher']:
        d = locapi.get(f'https://www.loc.gov/collections/{slug}/?' + urllib.parse.urlencode({'q': t, 'fo': 'json', 'c': 100}))
        for r in (d or {}).get('results', []):
            out.setdefault(r['id'], {'slug': slug, 'title': r.get('title'), 'date': r.get('date'), 'format': r.get('original_format'), 'terms': []})['terms'].append(t)
json.dump(out, open(os.path.join(HERE, 'coll_hits.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
for k, v in out.items():
    print(v['slug'][:12], v['date'], (v['title'] or '')[:110], v['format'], k)
