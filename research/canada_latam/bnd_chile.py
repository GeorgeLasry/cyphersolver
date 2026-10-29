import requests,json,time
H={'User-Agent':'Mozilla/5.0'}
u='https://engine.bibliotecanacionaldigital.gob.cl/mod/find/cgi/find.cgi'
TERMS=['carta cifrada','cartas cifradas','cifra','cifrada','cifrado','escritura cifrada','clave secreta','criptograma','descifrar','decifrar','en cifra','chiffre','cipher','correspondencia cifrada','manuscrito cifrado','despacho cifrado','oficio cifrado','clave de cifra']
out={}
for t in TERMS:
    for start in range(0,60,10):
        p=dict(action='jsonquery',engine='SwisheFind',start=start,rpp=10,cid=502,iid=602,searchmode='and',properties='567,509,559,571,797,551',group=1,show_ancestors=1,limit=7500,javascript=1,keywords=t)
        try:
            j=json.loads(requests.get(u,params=p,headers=H,timeout=40).text,strict=False)
        except Exception as e:
            print('ERR',t,start,e);break
        res=[v for k,v in j.items() if isinstance(v,dict) and 'results' in v]
        arts=j.get('articles',{}).get('results',[]) if 'articles' in j else (res[0]['results'] if res else [])
        n=j.get('articles',{}).get('num_results') if 'articles' in j else None
        for a in arts:
            d=out.setdefault(a.get('id'),{'terms':[]})
            d.update(title=a.get('title'),desc=a.get('description'),cid=a.get('cid'))
            d['terms'].append(t)
        print(t,start,n,len(arts),flush=True)
        if len(arts)<10:break
json.dump(out,open('bnd_chile_hits.json','w'),ensure_ascii=False,indent=1)
print(len(out))
