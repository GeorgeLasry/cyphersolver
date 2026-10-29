import requests, json, sys, time, re
phr=[l.strip() for l in open(sys.argv[1]) if l.strip()]
out={}
for p in phr:
    try:
        r=requests.get('https://be-api.us.archive.org/fts/v1/search',params={'q':p,'size':40},timeout=90).json()
    except Exception as e: print('ERR',p,e);continue
    h=r['hits']; print('##',p,h['total'])
    for x in h['hits']:
        ident=x['_id'].split('|')[0]
        sn=' / '.join(x['highlight']['text'])[:300].replace('\n',' ')
        sn=re.sub(r'\s+',' ',sn)
        out.setdefault(ident,[]).append((p,sn))
        print(' ',ident,'|',sn[:240])
    time.sleep(0.7)
json.dump(out,open(sys.argv[1]+'.json','w'))
