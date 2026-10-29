import requests, json, time, re
qs=['title:("calendar of the clarendon state papers")','title:("calendar of the stuart papers")','title:("calendar of state papers" AND foreign)','title:("calendar of state papers" AND domestic)','title:("calendar of state papers" AND scotland)','title:("calendar of state papers" AND venetian)','title:("calendar of state papers" AND spanish)','title:("calendar of state papers" AND colonial)','title:("calendar of treasury papers")','title:("historical manuscripts commission") AND (cipher OR cypher)','title:("calendar of the manuscripts" AND (Salisbury OR Hatfield))','title:("calendar of the cecil papers")','title:("calendar of the state papers relating to ireland")','title:("letters and papers" AND "henry viii")','title:("hamilton papers")','title:("calendar of state papers" AND "elizabeth")','title:("calendar of state papers" AND "james i")','title:("calendar of state papers" AND "charles i")','title:("calendar of state papers" AND "charles ii")','title:("calendar of state papers" AND "william iii")','title:("state papers" AND (Thurloe))','title:("calendar of letters, despatches")','title:("calendar of letters and state papers relating to english affairs")','title:("calendar of the mss. of the marquis of")']
ids={}
for q in qs:
    for pg in (1,2):
        try:
            d=requests.get('https://archive.org/advancedsearch.php',params={'q':q+' AND mediatype:texts','fl[]':['identifier','title','date','imagecount'],'rows':100,'page':pg,'output':'json'},timeout=90).json()['response']
        except Exception as e: print('ERR',q,e);break
        for x in d['docs']: ids[x['identifier']]=x
        if pg*100>=d['numFound']: break
        time.sleep(0.5)
    print(q,len(ids),flush=True)
json.dump(ids,open('cal_ids.json','w'))
