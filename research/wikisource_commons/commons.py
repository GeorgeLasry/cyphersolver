import requests, json, time
UA={'User-Agent':'cyphersolver-research/1.0 (dnbourdeau@gmail.com; historical cipher survey)'}
A='https://commons.wikimedia.org/w/api.php'
def get(p):
    p['format']='json'
    for i in range(3):
        try: return requests.get(A,params=p,headers=UA,timeout=40).json()
        except Exception as e: time.sleep(3)
    return {}
res={}
# categories (recursive depth 3)
roots=['Category:Cryptography','Category:Cipher manuscripts','Category:Cryptography manuscripts','Category:Cipher letters','Category:Ciphers','Category:Historical ciphers','Category:Undeciphered writing systems','Category:Diplomatic ciphers','Category:Nomenclators','Category:Cryptograms','Category:Letters in cipher','Category:Encrypted letters','Category:Coded messages','Category:Substitution ciphers','Category:History of cryptography','Category:Cryptology','Category:Ciphers by century','Category:Secret writing','Category:Codes','Category:Chiffre','Category:Cifrario','Category:Geheimschrift','Category:Chiffriermaschinen']
seen=set(); cats={}
def walk(c,depth):
    if c in seen or depth>2: return
    seen.add(c)
    cm=None; files=[]; subs=[]
    p={'action':'query','list':'categorymembers','cmtitle':c,'cmlimit':500,'cmtype':'file|subcat'}
    while True:
        j=get(dict(p))
        for m in j.get('query',{}).get('categorymembers',[]):
            (files if m['ns']==6 else subs).append(m['title'])
        if 'continue' in j: p.update(j['continue'])
        else: break
    cats[c]={'files':files,'subs':subs}
    print(c,len(files),len(subs),flush=True)
    import re
    for s in subs:
        if re.search(r'crypt|cipher|cypher|cifr|chiffr|nomenclat|secret|encod|encrypt|code|coded|geheim|decod|decrypt|letter|manuscript|diplomat|unsolved|undeciph|steganog',s,re.I) and not re.search(r'enigma|barcode|QR|zip|postal|dress|colo|codex|building|penal|civil|ISO|code of|Morse|Hammurabi',s,re.I): walk(s,depth+1)
for r in roots: walk(r,0)
json.dump(cats,open('commons_cats.json','w',encoding='utf8'),ensure_ascii=False,indent=0)
# full-text search of file descriptions
qs=['cipher letter','ciphered letter','undeciphered cipher','unsolved cipher','undeciphered letter','cypher letter','encrypted letter 17th century','lettre chiffrée','lettre en chiffre','dépêche chiffrée','Chiffrenbrief','chiffrierter Brief','carta cifrada','lettera cifrata','lettera in cifra','geheimschrift brief','nomenclator cipher manuscript','cipher manuscript','coded letter manuscript','secret code letter 18th century','diplomatic cipher','cipher key nomenclator','undeciphered manuscript','unsolved code manuscript','cifra carta manuscrito','cipher dispatch','encoded letter','enciphered letter']
hits={}
for q in qs:
    for ns in ('6','0','14'):
        p={'action':'query','list':'search','srsearch':q,'srnamespace':ns,'srlimit':50,'srprop':'snippet|size'}
        n=0
        while n<500:
            j=get(dict(p))
            s=j.get('query',{}).get('search',[])
            for h in s: hits.setdefault(h['title'],{**h,'qs':[]})['qs'].append(q)
            n+=len(s)
            if 'continue' in j: p.update(j['continue']); time.sleep(0.3)
            else: break
        print(q,ns,n,flush=True)
json.dump(hits,open('commons_search.json','w',encoding='utf8'),ensure_ascii=False)
print('total',len(hits))
