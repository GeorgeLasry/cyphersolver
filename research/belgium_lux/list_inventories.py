"""List AGATHA (State Archives of Belgium) inventories by heading, via the search page's ajax.php.
The search is session-based: POST the form, then page through method=getResults."""
import json, sys, time, urllib.request, urllib.parse, http.cookiejar

BASE = 'https://agatha.arch.be/en/search/ead/'
cj = http.cookiejar.CookieJar()
op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
op.addheaders = [('User-Agent', 'Mozilla/5.0 (cyphersolver research sweep)')]

def post(url, data):
    return op.open(url, urllib.parse.urlencode(data).encode(), timeout=90).read().decode('utf8')

def search(free='', heading='-1', holding='-1'):
    post(BASE + 'results/', {'FREE': free, 'HOLDING': holding, 'HEADING': heading,
                             'CHOOSE_DATE_PERIODE': '', 'exactYear': '', 'SHOW_PERIODE': ''})
    out, page = [], 1
    while True:
        r = json.loads(post(BASE + 'ajax.php', {'method': 'getResults', 'pageNumber': page, 'pageSize': 50}))
        resp = r.get('response') or {}
        docs = resp.get('docs', [])
        out += [{k: d.get(k) for k in ('id', 'findingaid_name', 'didtitle', 'start_year', 'end_year',
                                        'num_daos', 'num_items', 'holding', 'heading')} for d in docs]
        if not docs or len(out) >= resp.get('numFound', 0):
            return resp.get('numFound', 0), out
        page += 1; time.sleep(0.5)

if __name__ == '__main__':
    res = {}
    for spec in sys.argv[1:]:          # e.g. heading:A1  free:chiffre
        kind, val = spec.split(':', 1)
        n, docs = search(**({'heading': val} if kind == 'heading' else {'free': val}))
        print(spec, n, len(docs), file=sys.stderr)
        res[spec] = docs
    json.dump(res, sys.stdout, ensure_ascii=False, indent=1)
