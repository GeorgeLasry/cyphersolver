import requests, json, time, sys, os
UA={'User-Agent':'cyphersolver-research/1.0 (dnbourdeau@gmail.com; historical cipher survey)'}
Q={
 'en':['"in cipher"','"in cypher"','"cipher undeciphered"','"in cipher, not deciphered"','"cypher not decyphered"','"undeciphered cipher"','"written in cipher"','"the cipher" letter','"in ciphers"','"enciphered"','"cipher letter"','"letter in cipher"','"unintelligible cipher"','"not decyphered"','"cipher unsolved"','"cypher letter"','"the cypher" despatch'],
 'fr':['"en chiffre"','"en chiffres"','"chiffre non déchiffré"','"lettre chiffrée"','"écrite en chiffre"','"chiffre indéchiffré"','"dépêche chiffrée"','"non déchiffré"','"en chiffres non déchiffrés"','"écriture chiffrée"'],
 'de':['"in Chiffren"','"Chiffre" Brief','"Geheimschrift"','"chiffriert"','"in Ziffern geschrieben"','"Chiffrenschrift"','"nicht entziffert"','"verschlüsselter Brief"','"Chiffrenbrief"','"unentziffert"'],
 'it':['"in cifra"','"cifra" lettera','"scritta in cifra"','"cifrata"','"lettera cifrata"','"non decifrata"','"in cifre"','"dispaccio cifrato"'],
 'es':['"en cifra"','"cifrada"','"carta cifrada"','"escrita en cifra"','"sin descifrar"','"carta en cifra"','"despacho cifrado"','"cifras" carta'],
 'nl':['"in cijfer"','"cijferschrift"','"in cijferschrift"','"onontcijferd"','"geheimschrift"','"brief in cijfer"','"ontcijferd"'],
 'la':['"litterae cifratae"','"in cifra"','"cifra"','"notis occultis" epistola','"cryptographia"','"occultis characteribus"','"per cifram"'],
}
PAGEWIKI={'en':'104','fr':'104','de':'102','it':'110','es':'104','nl':'104','la':'104'}
out='raw_wikisource.jsonl'
done=set()
if os.path.exists('wikisource_done.txt'):
    done=set(open('wikisource_done.txt',encoding='utf8').read().split('\n'))
f=open(out,'a',encoding='utf8')
d=open('wikisource_done.txt','a',encoding='utf8')
MAXP=int(sys.argv[1]) if len(sys.argv)>1 else 6
for lg,qs in Q.items():
    for q in qs:
        for ns in ('0',PAGEWIKI[lg]):
            key=f'{lg}|{q}|{ns}'
            if key in done: continue
            off=0;n=0
            for p in range(MAXP):
                try:
                    r=requests.get(f'https://{lg}.wikisource.org/w/api.php',params={'action':'query','list':'search','srsearch':q,'srlimit':50,'sroffset':off,'srnamespace':ns,'format':'json','srprop':'snippet|size|wordcount'},headers=UA,timeout=40)
                    j=r.json()
                except Exception as e:
                    print('err',key,e);time.sleep(5);break
                s=j.get('query',{}).get('search',[])
                for h in s:
                    h.update(lang=lg,q=q,ns=ns); f.write(json.dumps(h,ensure_ascii=False)+'\n')
                n+=len(s)
                f.flush()
                if 'continue' not in j: break
                off=j['continue']['sroffset']; time.sleep(0.4)
            d.write(key+'\n'); d.flush()
            print(key,n,flush=True)
