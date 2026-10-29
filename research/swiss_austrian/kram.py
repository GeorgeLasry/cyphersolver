"""Kramerius5 Solr metadata search across instances. Writes kram_hits.jsonl"""
import urllib.request as u,urllib.parse as p,json,sys,time
INST={'nkp':'https://kramerius5.nkp.cz','mzk':'https://kramerius.mzk.cz','knav':'https://kramerius.lib.cas.cz','svkhk':'https://kramerius.svkhk.cz','vkol':'https://kramerius.vkol.cz','svkul':'https://kramerius.svkul.cz','kfbz':'https://kramerius.kfbz.cz','knihovna-cb':'https://kramerius.jvkcb.cz','svkpk':'https://kramerius.svkpk.cz','mlp':'https://kramerius.mlp.cz'}
TERMS=['šifra','šifrovaný','šifrované','šifrovan*','tajné písmo','tajnopis','tajným písmem','šifrou','chiffre','chiffriert','chiffrirt','chiffrirte','Geheimschrift','Ziffernschrift','Chiffrenschrift','Chiffreschrift','Zifferschrift','dechiffriert','Dechiffrier*','cifra','cifrato','cifrada','kryptogram','Kryptogramm','Chiffrenbrief','Geheimschriften','chifre','Zifra','Ziffer','Chiffern','Schlüssel zur Geheimschrift','titkosírás']
seen={}
def get(url):
    for i in range(3):
        try: return json.loads(u.urlopen(u.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=40).read())
        except Exception as e: err=e; time.sleep(2)
    return {'err':str(err)}
out=open('kram_hits.jsonl','w',encoding='utf-8')
for name,b in INST.items():
    for t in TERMS:
        q='(dc.title:"%s" OR keywords:"%s" OR dc.description:"%s")'%(t,t,t) if '*' not in t else 'dc.title:%s'%t
        params={'q':q,'wt':'json','rows':300,'fq':'level:0','fl':'PID,dc.title,dc.creator,datum_str,datum_begin,datum_end,fedora.model,keywords,language,root_title,dostupnost,dc.description'}
        r=get(b+'/search/api/v5.0/search?'+p.urlencode(params))
        if 'err' in r: print(name,t,'ERR',r['err'][:80],flush=True); 
        if 'err' in r and t==TERMS[0]: break
        resp=r.get('response',{})
        print(name,t,resp.get('numFound'),flush=True)
        for d in resp.get('docs',[]):
            d['_inst']=name;d['_term']=t
            out.write(json.dumps(d,ensure_ascii=False)+'\n')
out.close()
