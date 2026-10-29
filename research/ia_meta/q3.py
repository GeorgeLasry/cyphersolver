import requests, json, time, sys, re
qs=[l.strip() for l in open(sys.argv[1]) if l.strip()]
seen=set()
for q in qs:
    full=f'({q})'
    for page in (1,2,3):
        try:
            d=requests.get('https://archive.org/advancedsearch.php',params={'q':full,'fl[]':['identifier','title','date','description','collection'],'rows':100,'page':page,'output':'json'},timeout=90).json()['response']
        except Exception as e:
            print('ERR',q,e);break
        if page==1: print('##',q,d['numFound'])
        for x in d['docs']:
            if x['identifier'] in seen: continue
            seen.add(x['identifier'])
            desc=x.get('description','');desc=' '.join(desc) if isinstance(desc,list) else desc
            m=re.search(r'(?i)cipher|cypher|cryptogra|cryptic|secret (alphabet|writing|script)|encod|coded|code\b|chiffr|cifr|geheim|steganogr|symbols|undecipher|unidentified (script|writing)|illegible code',desc)
            if m: print(' ',x['identifier'],'|',x.get('date','')[:4],'|',str(x.get('title',''))[:60],'|',desc[max(0,m.start()-100):m.start()+120].replace('\n',' '))
        if len(d['docs'])<100 or page*100>=d['numFound']: break
        time.sleep(0.6)
    time.sleep(0.6)
