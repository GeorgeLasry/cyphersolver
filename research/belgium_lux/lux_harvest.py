"""Archives nationales de Luxembourg (ANLux), Archeevo public API: full-text search for cipher terms.
GET /api/descriptions/search?filter.*.ContainsAllWords=<term>&page=N&perPage=100 works without the eAccess login."""
import json, sys, time, urllib.request, urllib.parse

API = 'https://archives.services-publics.lu/api/descriptions/search'
TERMS = ['chiffre', 'chiffres', 'chiffré', 'chiffrée', 'chiffrés', 'chiffrées', 'déchiffré', 'déchiffrement',
         'déchiffrée', 'chiffrement', 'cryptogramme', 'cryptographie', 'code secret', 'clef du chiffre',
         'Chiffre', 'chiffriert', 'Chiffrierung', 'dechiffriert', 'Geheimschrift', 'Ziffer', 'Ziffern',
         'Chiffreschlüssel', 'cifra', 'cijfer', 'nomenclateur', 'écriture secrète', 'encre sympathique',
         'télégramme chiffré', 'câble chiffré', 'câbles chiffrés', 'chiffreur', 'Code', 'Kode']
FIELDS = ('ID', 'CompleteUnitId', 'UnitTitle', 'UnitDates', 'UnitDateInitial', 'UnitDateFinal', 'DescriptionLevel',
          'ScopeContent', 'Signatures', 'HasPublishedFiles', 'LangMaterial')

def get(term, page):
    q = urllib.parse.urlencode({'filter.*.ContainsAllWords': term, 'page': page, 'perPage': 100})
    req = urllib.request.Request(API + '?' + q, headers={'User-Agent': 'Mozilla/5.0 (cyphersolver research sweep)',
                                                         'Accept': 'application/json'})
    return json.loads(urllib.request.urlopen(req, timeout=120).read())

out = {}
for term in TERMS:
    page, rows = 1, []
    while True:
        d = get(term, page)
        rows += [{k: x.get(k) for k in FIELDS} for x in d['Items']]
        if len(rows) >= d.get('Total', 0) or not d['Items']:
            break
        page += 1; time.sleep(0.5)
    print(term, d.get('Total'), len(rows), file=sys.stderr, flush=True)
    for r in rows:
        out.setdefault(r['CompleteUnitId'], dict(r, terms=[]))['terms'].append(term)
    time.sleep(0.5)
json.dump(out, open('lux_hits.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(out), 'unique', file=sys.stderr)
