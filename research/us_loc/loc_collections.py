"""Per-collection coverage: list LoC digital collections that hold manuscripts and count hits per cipher term.

    LOC_GAP=6.5 python loc_collections.py list      -> collections_list.json
    LOC_GAP=6.5 python loc_collections.py count     -> collections_counts.json (term -> count per collection)

The collection search (/collections/<slug>/?q=...) reaches the same index as /manuscripts/ but per collection;
counts are recorded so coverage is auditable even where the answer is zero.
"""
import json, os, re, sys, urllib.parse
import locapi

HERE = os.path.dirname(os.path.abspath(__file__))
TERMS = ['cipher', 'cypher', 'decipher']
SKIP = re.compile(r'folk|music|chant|dance|ballet|song|oral hist|lomax|gershwin|bernstein|copland|kostelanetz|koussevitzky|totenberg|mendelssohn|sousa|graham|kaye|guthrie|blues|sonidos|j.ouvert|houma|kohala|comanche|matachines|goombay|chaldeans|diversity plaza|weaving|mangyan|tai painted|naxi|calligraphy|prayer|cuneiform|ethiopic|coptic|armenian|athos|sinai|patriarchates|hebr|yiddish|islamic|arabic|persian|south asian|ainu|motion picture|supreme court|aids memorial|quilt|9-11|baseball|rosa parks|hurston|o.keeffe|sagan|cosmos|freud|arendt|marie bonaparte|moldenhauer|reynolds|schmidt|colwell|edinger|whitman|carroll|lawmaking|local history|rumor|radio research|federal theatre|federal writers|slave narratives|merriam|mead|wright papers|morse|maritime|cajun|acadian|lowell|pinelands|montana|colorado|rhode island|new mexico|occupational|italian americans|ethnic|georgia folklife|chicago|florida|blue ridge|omaha', re.I)


def list_collections():
    out = []
    sp = 1
    while True:
        d = locapi.get('https://www.loc.gov/collections/?' + urllib.parse.urlencode(
            {'fa': 'original-format:manuscript/mixed material', 'fo': 'json', 'c': 150, 'sp': sp}))
        if not d:
            break
        for r in d['results']:
            out.append({'title': r.get('title'), 'url': r.get('url') or r.get('id'), 'date': r.get('date'),
                        'items': r.get('items') or r.get('count')})
        if not d['pagination'].get('next'):
            break
        sp += 1
    json.dump(out, open(os.path.join(HERE, 'collections_list.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print(len(out), 'collections')


def count():
    cols = json.load(open(os.path.join(HERE, 'collections_list.json'), encoding='utf-8'))
    p = os.path.join(HERE, 'collections_counts.json')
    res = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}
    for c in cols:
        url = c['url'].replace('about-this-collection/', '')
        if '/collections/' not in url or SKIP.search(c['title']):
            continue
        res.setdefault(url, {'title': c['title']})
        for t in TERMS:
            if t in res[url]:
                continue
            try:
                d = locapi.get(url.rstrip('/') + '/?' + urllib.parse.urlencode({'q': t, 'fo': 'json', 'c': 1}))
            except locapi.Blocked as e:
                print('BLOCKED', e)
                json.dump(res, open(p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
                return
            res[url][t] = d['pagination']['of'] if d and d.get('pagination') else None
        print(c['title'][:60], {k: v for k, v in res[url].items() if k != 'title'}, flush=True)
        json.dump(res, open(p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)


if __name__ == '__main__':
    {'list': list_collections, 'count': count}[sys.argv[1]]()
