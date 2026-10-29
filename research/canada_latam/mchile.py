import requests,re,json,time,html
H={'User-Agent':'Mozilla/5.0'}
TERMS=['carta cifrada','cifra','cifrada','cifrado','escritura cifrada','clave secreta','criptograma','descifrar','decifrar','correspondencia en clave','cartas en cifra','chiffre','cipher']
out={}
for t in TERMS:
    for mode in ('exact',):
        pg=0
        while pg<8:
            u='https://www.memoriachilena.gob.cl/602/w3-search.php'
            r=requests.get(u,params={'keywords':'"%s"'%t,'searchmode':'exact','offset':pg*10} if False else {'keywords':t,'searchmode':'exact'},headers=H,timeout=40)
            break
        s=r.text
        items=re.findall(r'<a[^>]*href="(/602/w3-article-\d+\.html)"[^>]*>(.*?)</a>',s,flags=re.S)
        for h,ti in items:
            ti=html.unescape(re.sub(r'<[^>]+>','',ti)).strip()
            out.setdefault(h,{'title':ti,'terms':[]})['terms'].append(t)
        print(t,len(items),re.findall(r'(\d+) resultados',s)[:2],flush=True)
json.dump(out,open('memoriachilena_hits.json','w'),ensure_ascii=False,indent=1)
for h,v in out.items(): print(h,v['title'][:100],v['terms'])
