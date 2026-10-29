import requests,json,time
H={'User-Agent':'Mozilla/5.0 (research sweep)'}
TERMS=['carta cifrada','cifrada','cifrado','en cifra','clave secreta','criptograma','chiffre','lettre chiffrée','carta em cifra','cifra','letter in cipher','cipher letter','cipher code manuscript','coded despatch','cipher despatch','nomenclator','cipher key','secret code letter']
FA=['original-format:manuscript/mixed material','original-format:manuscript']
out={}
def get(params):
    for a in range(4):
        try:
            r=requests.get('https://www.loc.gov/search/',params=params,headers=H,timeout=60)
            if r.status_code==200: return r.json()
            if r.status_code==429: time.sleep(20)
        except Exception as e: time.sleep(3)
    return None
for t in TERMS:
    for fa in FA:
        for p in range(1,6):
            j=get({'q':t,'fo':'json','c':100,'sp':p,'fa':fa,'dates':'1500/1950'})
            if not j: print('fail',t,fa,p);break
            res=j.get('results',[])
            for x in res:
                k=x.get('id') or x.get('url')
                d=out.setdefault(k,{'terms':[]})
                d.update(title=x.get('title'),date=x.get('date'),url=x.get('url'),desc=' '.join(x.get('description') or [])[:500],loc=x.get('location'),subj=(x.get('subject') or [])[:6],fmt=x.get('original_format'),coll=x.get('partof'))
                if t not in d['terms']:d['terms'].append(t)
            tot=j.get('pagination',{}).get('total')
            print(t,fa[-10:],p,len(res),tot,flush=True)
            if not j.get('pagination',{}).get('next') or not res: break
            time.sleep(1.5)
    json.dump(out,open('loc_hits.json','w'),ensure_ascii=False,indent=1)
print(len(out))
