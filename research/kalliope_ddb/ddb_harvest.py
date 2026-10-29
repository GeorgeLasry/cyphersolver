import json,urllib.request,urllib.parse,time
TERMS=[l.strip() for l in open('kal_terms_run2.txt',encoding='utf8') if l.strip()]
TERMS=[t.strip('"') for t in TERMS]
TERMS+=['Chiffrenschrift','Geheimcode','Geheimschriftbrief','verschlüsselter','chiffrierter','Chiffrierung','Codeschlüssel','Dechiffrierschlüssel','"en chiffres"','nomenclateur','chiffrier*','dechiffr*','verschlüssel*','geheimschrift*','zifferschrift','Zahlenschrift','Zahlenchiffre','Zeichenschrift','Geheimzeichen','Geheimbriefe','Geheimkorrespondenz','secret writing','cypher','Chiffernschlüssel','Auflösung der Chiffre']
def get(term,start):
    u='https://api.deutsche-digitale-bibliothek.de/2/search/index/search/select?'+urllib.parse.urlencode({'q':term,'rows':500,'start':start,'wt':'json','fq':'-sector_fct:sec_01'})
    for i in range(3):
        try: return json.load(urllib.request.urlopen(u,timeout=90))['response']
        except Exception as e: err=e; time.sleep(3)
    raise err
out={};counts={}
for t in dict.fromkeys(TERMS):
    s=0
    while True:
        r=get(t,s)
        for d in r['docs']:
            k=d['id']
            if k in out: out[k]['terms'].append(t)
            else:
                out[k]={'id':k,'label':d.get('label'),'view':d.get('view'),'provider':d.get('provider_fct') or d.get('provider'),'sector':d.get('sector_fct'),'objecttype':d.get('objecttype_fct'),'type':d.get('type_fct'),'terms':[t]}
        s+=len(r['docs'])
        if not r['docs'] or s>=r['numFound']: break
    counts[t]=r['numFound']; print(t,r['numFound'],len(out),flush=True)
    json.dump({'counts':counts,'recs':list(out.values())},open('ddb_hits.json','w',encoding='utf8'),ensure_ascii=False)
