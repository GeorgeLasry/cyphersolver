import requests, json, time, re, os
UA={'User-Agent':'cyphersolver-research/1.0 (dnbourdeau@gmail.com)'}
terms=['state papers','calendar of state papers','calendar state papers','despatches','dispatches','correspondence','letters and papers','diplomatic','ambassador','cipher','cypher','decipher','nomenclator','secret writing','cryptography','historical manuscripts commission','hatfield','stuart papers','clarendon','thurloe','state letters','negotiations','memoirs of the court','papers relating','secret correspondence','lettres','briefe','cartas','lettere','intercepted letters','spy','conspiracy','mary queen of scots letters','walsingham','cecil','burghley','elizabeth letters','calendar','royalist','jacobite','revolution papers','lettres missives','documents inedits','correspondance','depeches','relazioni','diary and correspondence','papers','memorials','journal of the','history of the plot','gunpowder','babington','casket letters','letters of','despachos','correspondencia','state trials','trial of','secret service','Dutch republic','Walsingham papers','Winwood','Sydney papers','Sidney','Egerton','Cabala','Sully','Bacon letters','King James letters','Strafford letters','Hardwicke','Burnet','Bolingbroke','Marlborough','Wentworth papers','Cornwallis correspondence','Franklin papers','Jefferson writings','Washington writings','Madison papers','Hamilton works','Monroe','Burr','Arnold treason','Andre']
os.makedirs('.work/gut',exist_ok=True)
books={}
for t in terms:
    url='https://gutendex.com/books/?search='+requests.utils.quote(t)
    for p in range(5):
        try: j=requests.get(url,headers=UA,timeout=60).json()
        except Exception as e: print('err',t,e); break
        for b in j.get('results',[]):
            if 'en' in b['languages'] or any(l in b['languages'] for l in ('fr','de','it','es','nl','la')):
                books[b['id']]={'id':b['id'],'title':b['title'],'authors':[a['name'] for a in b['authors']],'langs':b['languages'],'fmts':{k:v for k,v in b['formats'].items() if k.startswith('text/plain')}}
        url=j.get('next')
        if not url: break
        time.sleep(0.3)
    print(t,len(books),flush=True)
json.dump(books,open('gutenberg_books.json','w',encoding='utf8'),ensure_ascii=False)
