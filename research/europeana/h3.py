import json,urllib.parse,urllib.request,time,sys
def get(p):
    u='https://api.europeana.eu/record/v2/search.json?'+urllib.parse.urlencode(p,doseq=True)
    for i in range(4):
        try:
            return json.load(urllib.request.urlopen(u,timeout=60))
        except Exception: time.sleep(2+3*i)
Q=['cifrad* AND (carta OR cartas OR despacho OR minuta)','cifra AND (carta OR cartas) AND Mss','"parcialmente cifrada"','"en cifra" AND carta','cifrada AND (embajador OR rey OR virrey OR secretario)',
   'chiffre* AND (lettre OR dépêche) AND (ambassadeur OR roi)','Geheimschrift OR chiffriert* OR verschlüsselt*','cifrat* AND lettera','cipher* AND (letter OR despatch) ','gecijferd OR "in cijfer"','"en chiffre" AND lettre',
   'descifrad* AND carta','"texto descifrado"','"clave" AND cifra AND carta','"cifra" AND "Mss/"']
seen={}
for q in Q:
    cur='*';n=0
    while cur and n<3000:
        d=get({'wskey':'api2demo','query':q,'qf':['YEAR:[1300 TO 1900]'],'rows':100,'cursor':cur,'profile':'standard'})
        if not d or not d.get('success'): break
        for it in d['items']: seen.setdefault(it['id'],it)
        n+=len(d['items']);cur=d.get('nextCursor')
    print(q,n,len(seen),flush=True)
json.dump(list(seen.values()),open('hits3.json','w',encoding='utf8'),ensure_ascii=False)
