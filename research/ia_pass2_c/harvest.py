import json,sys,time
from fts import fts
Q={
'fr':['"chiffre non déchiffré"','"en chiffre" "non déchiffré"','"chiffres non déchiffrés"','"lettre en chiffres" "non déchiffrée"','"en chiffre" "indéchiffrable"','"chiffre" "n\'a pas été déchiffré"','"chiffre" "reste indéchiffré"','"dépêche en chiffres" "non déchiffrée"','"en chiffre, non déchiffré"'],
'de':['"in Ziffern" "nicht entziffert"','"Chiffre" "nicht entziffert"','"Chiffrenschrift" "unentziffert"','"in Chiffern" "nicht aufgelöst"','"chiffrirt" "nicht entziffert"','"Ziffernschrift" "nicht entziffert"','"unentziffert" Chiffre','"in Chiffren" "nicht entziffert"','"Geheimschrift" "unentziffert"','"verschlüsselt" "nicht entziffert" Brief'],
'it':['"in cifra" "non decifrata"','"in cifra" "indecifrabile"','"cifra non sciolta"','"in cifra" "non sciolta"','"lettera in cifra" "non decifrata"','"cifra" "non decifrato"','"in cifra" "non interpretata"'],
'es':['"en cifra" "sin descifrar"','"cifra no descifrada"','"en cifra" "no descifrada"','"carta en cifra" "sin descifrar"','"cifra" "sin descifrar" carta','"en cifra" "indescifrable"'],
'nl':['"in cijfer" "niet ontcijferd"','"cijferschrift" "niet ontcijferd"','"in cijferschrift" "onontcijferd"','"in cijfer" "onontcijferd"'],
'pt':['"em cifra" "por decifrar"','"em cifra" "não decifrada"','"cifra" "indecifrada"'],
'la':['"litterae cifratae" "non"','"ciphris" "non explicat"'],
'pl':['"szyfrem" "nie odczytan"','"szyfr" "nierozszyfrowan"'],
'sv':['"chiffer" "otydd"','"chiffer" "ej tydd"'],
}
out={}
for lg,qs in Q.items():
    for q in qs:
        for p in (1,2,3):
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
json.dump(out,open('hits_raw.json','w'),ensure_ascii=False,indent=1)
print(len(out))
