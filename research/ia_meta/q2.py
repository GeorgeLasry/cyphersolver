import requests, json, time, sys, re
seen=json.load(open('raw_hits.json'))
qs=[l.strip() for l in open(sys.argv[1]) if l.strip()]
for q in qs:
    full=f'({q}) AND mediatype:texts'
    try:
        d=requests.get('https://archive.org/advancedsearch.php',params={'q':full,'fl[]':['identifier','title','date','creator','collection','description'],'rows':60,'output':'json'},timeout=90).json()['response']
    except Exception as e:
        print('ERR',q,e);continue
    print('##',q,d['numFound'])
    for x in d['docs']:
        if x['identifier'] in seen: continue
        seen[x['identifier']]=x
        desc=x.get('description','');desc=' '.join(desc) if isinstance(desc,list) else desc
        print(' ',x['identifier'],'|',x.get('date','')[:4],'|',str(x.get('title',''))[:70],'|',desc[:110].replace('\n',' '))
    time.sleep(0.6)
json.dump(seen,open('raw_hits.json','w'))
