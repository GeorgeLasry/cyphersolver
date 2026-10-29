import json
R=json.load(open('calames_rows.json',encoding='utf-8'))+json.load(open('fa_rows.json',encoding='utf-8'))
keys="year date title correspondents place language region period shelfmark folio_note cls status why importance solvability difficulty score_note verify links seen source prior_art".split()
extra={"Marquis de L'Hospital":"Calames-2017517115583886","Cardinal de La Rochefoucauld":"Calames-2017621176592554"}
for r in R:
    for k,i in extra.items():
        if r['title'].startswith(k): r['links']=[{"label":"Calames notice","href":"https://calames.abes.fr/pub/ms/"+i}]
    if r['title'].startswith('Père Hacki'):
        r['prior_art']="open (checked 28 Oct 2026: web search 'Christine de Suède Hacki lettres chiffrées Pologne 1668 H 258' found only blog transcriptions of the Montpellier letters, no cipher study; repo ledgers)"
    if 'Pichegru' in r['title']:
        r['prior_art']="open (checked 28 Oct 2026: web search found nothing on these ciphers; Daudet's Conjuration de Pichegru prints much of the correspondence, not yet checked)"
    assert all(k in r for k in keys),[k for k in keys if k not in r]
    assert r['links'],r['title']
    assert r['period'] in "15th century, 1497-1559, 1560-1589, 1589-1598, 1598-1610, 1611-1650, 1651-1700, 1701-1800, 1801-1900, 1901-1950, unknown".split(', '),(r['period'],r['title'])
    assert r['region'] in "England, France, Italy, Spain, Portugal, Low Countries, Central Europe, Germany, Scandinavia, Poland-Lithuania, Papacy, Americas, Other".split(', ')
json.dump(R,open('candidates.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(R))
