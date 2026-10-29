import requests,json,time
UA={'User-Agent':'cyphersolver-research/1.0 (dnbourdeau@gmail.com; historical cipher survey)'}
jobs=[]
for lg,series in {'en':['"NOTES AND QUERIES"','Archaeologia','"Camden Society"',"\"Gentleman's Magazine\"",'"State Papers"','"Historical Manuscripts Commission"','"Hatfield"','"Calendar of"','"Letters and Papers"','"Philosophical Transactions"','"Athenaeum"','"Cabala"','"Thurloe"','"Clarendon"','"Stuart Papers"','"Camden Miscellany"','"Spanish Calendar"','"Venetian"','"Dictionary of National Biography"'],
 'fr':['"Bibliothèque de l’École des chartes"','"Revue des questions historiques"','"Revue historique"','"Correspondance"','"Intermédiaire des chercheurs"','"Documents inédits"','"Négociations"','"Lettres missives"'],
 'de':['"Archiv"','"Briefwechsel"','"Urkunden"','"Zeitschrift"'],'it':['"Archivio storico"','"Lettere"','"dispacci"'],'es':['"Colección de documentos inéditos"','"Cartas"','"Boletín de la Real Academia"']}.items():
    for s in series:
        for w in (['cipher','cypher','decipher','undeciphered','"in cipher"'] if lg=='en' else ['chiffre','chiffrée','déchiffrer','cifra','cifrada','Chiffre','Geheimschrift','entziffern','descifrar','decifrare']):
            jobs.append((lg,f'{s} {w}'))
out=open('raw_targeted.jsonl','a',encoding='utf8')
PW={'en':'104','fr':'104','de':'102','it':'110','es':'104'}
for lg,q in jobs:
    if lg=='fr' and not any(c in q for c in ['chiffr','déchiff']): continue
    if lg=='de' and not any(c in q for c in ['Chiffre','Geheim','entzif']): continue
    if lg=='it' and not any(c in q for c in ['cifra','decifr']): continue
    if lg=='es' and not any(c in q for c in ['cifra','descifr']): continue
    for ns in ('0',PW[lg]):
        off=0;n=0
        for p in range(10):
            try: j=requests.get(f'https://{lg}.wikisource.org/w/api.php',params={'action':'query','list':'search','srsearch':q,'srlimit':50,'sroffset':off,'srnamespace':ns,'format':'json','srprop':'snippet|size'},headers=UA,timeout=60).json()
            except Exception as e: time.sleep(4);break
            for h in j.get('query',{}).get('search',[]):
                h.update(lang=lg,q=q,ns=ns);out.write(json.dumps(h,ensure_ascii=False)+'\n');n+=1
            out.flush()
            if 'continue' not in j: break
            off=j['continue']['sroffset'];time.sleep(0.4)
        print(lg,q,ns,n,flush=True)
