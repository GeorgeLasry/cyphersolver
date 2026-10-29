import json,sys,time
from fts import fts
Q={
'fr':['"chiffrées, non déchiffrées"','"entièrement chiffrée"','"entièrement en chiffre"','"lettre en chiffre non déchiffrée"','"en chiffres non déchiffrés"','"chiffre non déchiffré"','"chiffres non déchiffrés"','"chiffrée, non déchiffrée"','"lettre chiffrée" "non déchiffrée"','"pièce chiffrée" "non déchiffrée"','"dépêche chiffrée" "non déchiffrée"','"en chiffre" "n est pas déchiffrée"'],
'de':['"Chiffer" "nicht aufgelöst"','"Chiffre" "nicht aufgelöst"','"Ziffern" "nicht aufgelöst"','"in Ziffern" "nicht aufgelöst"','"chiffrirt" "nicht aufgelöst"','"chiffrierte" "nicht aufgelöst"','"Chiffrenschreiben" "nicht aufgelöst"','"in Chiffern" "nicht entziffert"','"in Ziffern geschrieben" "nicht"','"Chiffre" "nicht entschlüsselt"','"chiffrirtes" "unaufgelöst"','"Zifferschrift" "nicht aufgelöst"'],
'it':['"in cifra" "non decifrata"','"in cifra" "non decifrato"','"lettera in cifra" "non sciolta"','"cifra" "non sciolta"','"in cifra" "non sciolto"','"cifra" "non decifrata"','"in cifre" "non decifrate"','"cifrata" "non decifrata"','"in cifra, non sciolta"'],
'es':['"en cifra" "sin descifrar"','"en clave" "no descifrada"','"en clave" "sin descifrar"','"gran parte en cifra"','"en cifra" "no descifrada"','"cifra" "sin descifrar"','"en cifra, sin descifrar"','"en guarismos" "sin descifrar"','"cifrada" "sin descifrar"','"cifrada" "no descifrada"'],
'nl':['"in cijfer" "niet ontcijferd"','"in cijfers" "niet ontcijferd"','"cijferschrift" "ontcijfer"','"in cijferschrift" "niet ontcijferd"'],
'pt':['"em cifra" "por decifrar"','"em cifra" "não decifrada"','"cifrada" "não decifrada"','"em cifra" "sem decifrar"'],
'la':['"litteris cifratis"','"literis cifratis" "non"','"in cifra" "non intellig"'],
}
out={}
for lg,qs in Q.items():
    for q in qs:
        for p in (1,2,3,4,5,6):
            try:
                d=fts(q,50,p); hs=d["response"]["body"]["hits"]["hits"]
            except Exception as e:
                print('ERR',q,p,e); break
            for h in hs:
                f=h["fields"]; k=f.get("identifier")
                o=out.setdefault(k,{"title":f.get("title"),"year":f.get("year") or f.get("date"),"q":[],"snips":[]})
                o["q"].append(q)
                hl=h.get("highlight")
                if isinstance(hl,dict):
                    for s in hl.get("text",[])[:2]: o["snips"].append(s[:300])
            print(lg,q,p,len(hs),flush=True)
            if len(hs)<50: break
            time.sleep(.5)
json.dump(out,open('hits_raw2.json','w'),ensure_ascii=False,indent=1)
print(len(out))
