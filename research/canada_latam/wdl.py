import requests,json,time,sys
H={'User-Agent':'Mozilla/5.0 (research sweep)'}
TERMS=['cipher','cypher','ciphered','chiffre','chiffré','cifra','cifrada','cifrado','carta cifrada','clave','criptograma','decifrar','descifrar','código secreto','secret writing','cryptogram','cryptograph','nomenclator','coded letter','cifre','geheimschrift']
out={}
for t in TERMS:
    p=1;n=0
    while True:
        u='https://www.loc.gov/collections/world-digital-library/'
        try:
            r=requests.get(u,params={'q':t,'fo':'json','c':100,'sp':p},headers=H,timeout=60)
            if r.status_code!=200: print(t,p,r.status_code);break
            j=r.json()
        except Exception as e: print('ERR',t,p,e);break
        res=j.get('results',[])
        for x in res:
            k=x.get('id') or x.get('url')
            d=out.setdefault(k,{'terms':[]})
            d.update(title=x.get('title'),date=x.get('date'),url=x.get('url'),desc=' '.join(x.get('description') or [])[:600],loc=x.get('location'),lang=x.get('language'),subj=x.get('subject'))
            if t not in d['terms']:d['terms'].append(t)
        n+=len(res)
        pg=j.get('pagination',{})
        if not pg.get('next') or not res or p>=15: break
        p+=1;time.sleep(1)
    print(t,n,flush=True)
json.dump(out,open('wdl_hits.json','w'),ensure_ascii=False,indent=1)
print(len(out))
