import requests,json,re,time
UA={'User-Agent':'cyphersolver-research/1.0 (dnbourdeau@gmail.com; historical cipher survey)'}
A='https://commons.wikimedia.org/w/api.php'
cats=json.load(open('commons_cats.json',encoding='utf8'))
srch=json.load(open('commons_search.json',encoding='utf8'))
files=set()
for v in cats.values(): files.update(v['files'])
for t,h in srch.items():
    if t.startswith('File:'): files.add(t)
INC=re.compile(r'encrypt|cipher|cypher|cifr|chiffr|letter|brief|lettre|lettera|carta|шифр|письм|code|nomenclat|secret|geheim|cryptogram|undecipher|unsolved|manuscript|dispatch|despatch|folio|MS |Add|Ms\.|cod|Rákóczi|1[3-9]\d\d',re.I)
EXC=re.compile(r'diagram|icon|\.svg|rotor|logo|\.ogg|\.webm|\.gif$|animation|Enigma|NSA|block cipher|AES|RSA|hash|SHA|DES|crypto(?:currency|graphic algo)|bitcoin|SSL|TLS|VPN|Signal|\.tif$',re.I)
sel=sorted(f for f in files if INC.search(f) and not EXC.search(f))
print(len(files),len(sel))
out={}
for i in range(0,len(sel),40):
    b=sel[i:i+40]
    try:
        j=requests.get(A,params={'action':'query','titles':'|'.join(b),'prop':'imageinfo|categories','iiprop':'extmetadata|url|size','iiextmetadatafilter':'ImageDescription|DateTimeOriginal|Credit|Artist|LicenseShortName|ObjectName|Categories','cllimit':'max','format':'json'},headers=UA,timeout=60).json()
    except Exception as e: print('err',i,e); time.sleep(5); continue
    for p in j.get('query',{}).get('pages',{}).values():
        ii=(p.get('imageinfo') or [{}])[0]
        em=ii.get('extmetadata',{})
        out[p['title']]={'url':ii.get('descriptionurl'),'w':ii.get('width'),'desc':re.sub('<[^>]+>','',em.get('ImageDescription',{}).get('value','')),'date':em.get('DateTimeOriginal',{}).get('value',''),'credit':re.sub('<[^>]+>','',em.get('Credit',{}).get('value','')),'cats':[c['title'] for c in p.get('categories',[])]}
    time.sleep(0.3)
    if i%400==0: print(i,flush=True)
json.dump(out,open('commons_meta.json','w',encoding='utf8'),ensure_ascii=False)
print(len(out))
