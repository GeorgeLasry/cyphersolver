"""Manuscriptorium castor search (globIndex) -> manu_hits.jsonl (compact)"""
import os,re,urllib.request as u,urllib.parse as p,json,time,sys
TERMS=sys.argv[1:] or ['chiffre','chiffrierte','chiffriert','chiffrirt','chiffrirte','chiffrirten','Chiffren','Chiffern','Chiffrenschrift','Chiffreschrift','Geheimschrift','Geheimschriften','Ziffernschrift','Zifferschrift','Ziffern','Zifferbrief','dechiffriert','dechiffrirt','Dechiffrierung','Dechiffrirung','Entzifferung','entziffert','entzifferung','cifra','cifrato','cifrada','cifrado','cifré','chiffré','chiffrée','chiffrés','chiffres','šifra','šifrovaný','šifrovaná','šifrované','šifrou','šifry','šifrovací','šifrovaného','šifrovanou','tajné písmo','tajným písmem','tajnopis','tajnopisem','tajným písmo','kryptogram','kryptogramm','Kryptogramm','Cifer','Cyfer','cyfra','cyfr','cyfrą','szyfr','szyfrem','szyfrowany','szyfrowane','titkosírás','titkosírással','titkos írás','tajné písma','Geheimschrifft','Schlüssel zur','Ziffer','Ziffern','nomenclator','nomenclatura','Nomenklator','cipher','cypher','ciphered','Vigenère','Trithemius','steganograph*','stenograph*','Zeichenschrift','Notenschrift','Chiffre-Schlüssel','Schlüssel','schlüssel','klíč k šifře','klíč']
def get(url):
    for i in range(4):
        try: return json.loads(u.urlopen(u.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=90).read())
        except Exception as e: err=e; time.sleep(3)
    print('ERR',err,flush=True); return None
out=open(os.environ.get('OUT','manu_hits.jsonl'),'a',encoding='utf-8')
seen=set()
for t in TERMS:
    start=0;total=None
    while True:
        q=json.dumps([{"fieldId":"globIndex","queryRow":t,"logOp":""}])
        url='https://www.manuscriptorium.com/castor/manuscriptorium/search/formSearch?'+p.urlencode({'query':q,'coreId':'manuscriptorium','sort':'','rows':100,'start':start,'asciiSearch':'false','defLogOperator':'AND','asterL':'false','aster':os.environ.get('ASTER','false')})
        r=get(url)
        if not r: break
        res=r['response']['result']
        total=res.get('found')
        recs=res['recordList']
        for d in recs:
            gid=d.get('GulliverSourceSystemIdentifier')
            d['_term']=t
            g=' | '.join(x for x in d.get('globIndex',[]) if isinstance(x,str)); d['globIndex']=[g[:5000]]
            out.write(json.dumps(d,ensure_ascii=False)+'\n')
        out.flush()
        start+=len(recs)
        if not recs or start>=(total or 0) or start>=3000: break
    print(t,total,flush=True)
