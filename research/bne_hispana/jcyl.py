import requests,re,sys,time,json
S=requests.Session();S.headers['User-Agent']='Mozilla/5.0'
terms=['cifrada','cifrado','cifra','descifrado','"en cifra"','"parcialmente cifrada"','clave','contraseña','cifras','criptografia']
res={}
for t in terms:
    r=S.get('https://bibliotecadigital.jcyl.es/es/consulta/resultados_busqueda.do',params={'busq_general':t,'tipoBusqueda':'general'},timeout=60)
    txt=r.text
    m=re.search(r'(\d[\d.,]*)\s*(?:resultados|registros|results)',txt)
    ids=sorted(set(re.findall(r'registro\.do\?id=(\d+)',txt)))
    titles=re.findall(r'registro\.do\?id=(\d+)[^>]*>\s*([^<]{5,200})<',txt)
    print(t,r.status_code,len(txt),m.group(0) if m else None,len(ids))
    res[t]=titles
    time.sleep(2)
json.dump(res,open('raw/jcyl.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
