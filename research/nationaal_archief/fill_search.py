"""Fill gaps in the 1.01.02 dump with item-level searches (titles) for envoy postings and letter words."""
import json, re, sys, time, urllib.parse, urllib.request
TERMS = ['brief', 'brieven', 'missive', 'Kopenhagen', 'Stockholm', 'Parijs', 'Westminster', 'Londen', 'Madrid',
         'Wenen', 'Berlijn', 'Constantinopel', 'Lissabon', 'Brussel', 'Keulen', 'Regensburg', 'Hamburg', 'Venetie',
         'Turijn', 'Moskou', 'Petersburg', 'Warschau', 'Dresden', 'Hannover', 'Munster', 'Aken', 'Rome', 'ambassadeur',
         'gezant', 'resident', 'envoye', 'gedeputeerden', 'griffier', 'cijfer', 'duplicaat', 'translaat']
out = {}
for term in TERMS:
    page = 1
    while True:
        url = 'https://zvt.nationaalarchief.nl/api/search/eads/1.01.02?' + urllib.parse.urlencode(dict(q=term, page=page, rows=100))
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60))
        except Exception as e:
            print('err', term, page, e, file=sys.stderr); time.sleep(5); continue
        for r in d.get('results') or []:
            out.setdefault(r['title_id'], {'title_id': r['title_id'], 'title': re.sub('<[^>]+>', '', r['title']), 'terms': []})['terms'].append(term)
        if page >= (d.get('pages') or 0) or page >= 60:
            break
        page += 1; time.sleep(0.25)
    print(term, len(out), file=sys.stderr, flush=True)
json.dump(list(out.values()), open('search_1.01.02.json', 'w', encoding='utf8'), ensure_ascii=False)
