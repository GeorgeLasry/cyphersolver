import requests, json, time, sys
UA={'User-Agent':'cyphersolver-research/1.0 (dnbourdeau@gmail.com; historical cipher survey)'}
W={'en':['cipher','cypher','ciphers','decipher','decypher','cyphers'],
 'fr':['chiffre','chiffrée','chiffrées','chiffré','déchiffré','déchiffrer','chiffres'],
 'de':['Chiffre','Chiffren','Geheimschrift','chiffriert','Ziffern','entziffert','Chiffrenschrift'],
 'it':['cifra','cifre','cifrata','decifrare','decifrata','cifrato'],
 'es':['cifra','cifras','cifrada','descifrar','descifrada','cifrado'],
 'nl':['cijfer','cijfers','cijferschrift','ontcijferd','geheimschrift'],
 'la':['cifra','cifrae','cifrata','cifris','notis']}
PAGEWIKI={'en':'104','fr':'104','de':'102','it':'110','es':'104','nl':'104','la':'104'}
REG=[r'[0-9]{1,4}([.,;:\- ]+[0-9]{1,4}){7,}', r'[0-9]{1,4}(\.[0-9]{1,4}){6,}', r'[0-9]{2,3}[ ]+[0-9]{2,3}[ ]+[0-9]{2,3}[ ]+[0-9]{2,3}[ ]+[0-9]{2,3}[ ]+[0-9]{2,3}']
out=open('raw_regex.jsonl','a',encoding='utf8')
for lg,ws in W.items():
    for w in ws:
        for ri,rg in enumerate(REG):
            for ns in ('0',PAGEWIKI[lg]):
                q=f'{w} insource:/{rg}/'
                off=0;n=0
                for p in range(8):
                    try:
                        r=requests.get(f'https://{lg}.wikisource.org/w/api.php',params={'action':'query','list':'search','srsearch':q,'srlimit':50,'sroffset':off,'srnamespace':ns,'format':'json','srprop':'snippet|size'},headers=UA,timeout=90)
                        j=r.json()
                    except Exception as e:
                        print('err',lg,w,ri,e,flush=True);time.sleep(5);break
                    if 'error' in j: print('apierr',lg,w,ri,str(j['error'])[:100],flush=True);break
                    s=j.get('query',{}).get('search',[])
                    for h in s:
                        h.update(lang=lg,q=w,ri=ri,ns=ns); out.write(json.dumps(h,ensure_ascii=False)+'\n')
                    out.flush(); n+=len(s)
                    if 'continue' not in j: break
                    off=j['continue']['sroffset']; time.sleep(0.5)
                print(lg,w,ri,ns,n,flush=True)
                time.sleep(0.5)
