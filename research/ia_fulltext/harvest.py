import json, time, sys
from fts import fts
Q=['"cipher not deciphered"','"cypher not deciphered"','"in cipher, not deciphered"','"cipher, undeciphered"','"cipher undeciphered"','"in cipher; not deciphered"',
'"cipher not decyphered"','"in cipher, not deciphered"','"in cypher, not deciphered"','"cipher which has not been deciphered"','"cipher has not been solved"','"cipher has not been deciphered"',
'"cypher which I cannot read"','"unintelligible cipher"','"unintelligible cypher"','"in cipher, undeciphered"','"in cypher, undeciphered"','"cipher not read"','"cipher, not decoded"','"cipher unexplained"',
'"chiffre non déchiffré"','"en chiffres non déchiffrés"','"chiffre indéchiffré"','"chiffre non déchiffrée"','"en chiffre, non déchiffré"','"en chiffres, non déchiffrée"','"chiffre qui n\'a pas été déchiffré"',
'"Chiffreschrift nicht entziffert"','"Chiffren nicht entziffert"','"in Chiffern nicht entziffert"','"chiffrirt, nicht entziffert"','"Ziffern nicht aufgelöst"','"Geheimschrift nicht entziffert"','"in Ziffern, nicht entziffert"',
'"cifra non decifrata"','"in cifra non decifrata"','"cifre non decifrate"','"in cifra, non decifrata"','"cifra indecifrata"','"cifra non decifrato"',
'"cifra sin descifrar"','"en cifra sin descifrar"','"cifra no descifrada"','"en cifra, sin descifrar"','"cifra sem decifrar"',
'"cijferschrift niet ontcijferd"','"in cijfer niet ontcijferd"','"cijfer, niet ontcijferd"','"cipher not yet deciphered"','"cypher not yet deciphered"','"in cipher (not deciphered)"','"in cipher (undeciphered)"','"cipher, no key"','"cipher; the key is lost"','"in cipher, unsolved"','"cipher not solved"','"cipher unsolved"','"in cipher, no decipher"','"cipher without decipher"','"not deciphered" cipher letter']
out={}
for q in Q:
    for p in (1,2,3,4):
        try: d=fts(q,50,p)
        except Exception as e: print("ERR",q,p,e); break
        hits=d["response"]["body"]["hits"]["hits"]
        if not hits: break
        for h in hits:
            f=h["fields"]; k=(f["identifier"],f.get("page_num"))
            o=out.setdefault("%s#%s"%k,{"id":f["identifier"],"page":f.get("page_num"),"title":f.get("title"),"year":f.get("year"),"creator":f.get("creator"),"snips":[],"q":[]})
            for s in (h.get("highlight") or {}).get("text",[]): 
                if s not in o["snips"]: o["snips"].append(s)
            if q not in o["q"]: o["q"].append(q)
        if len(hits)<50: break
        time.sleep(.5)
    print(q,len(out),flush=True)
json.dump(out,open("hits_raw.json","w"),ensure_ascii=False,indent=0)
