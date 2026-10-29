import re,json,urllib.request,os,sys
B='https://smithsonian-open-access.s3-us-west-2.amazonaws.com/metadata/edan/'
units='acah acm acma chndm chsdm cfchfolklife eepa fbr fs fsa fsg hac hmsg hsfa naa nasm nasmac nmaa nmaahc nmafa nmah nmai nmaia npg npgcap npm nmnheducation sia sil silaf silnmahtl sri'.split()
PAT=re.compile(rb'cipher|cypher|cryptogra|secret writ|decipher|in code\b|coded|code book|codebook|chiffr|secret alphabet|enigma|code letter|cryptic',re.I)
out=open('si_bulk_hits.jsonl','a',encoding='utf8')
for u in units:
    try: idx=urllib.request.urlopen(B+u+'/index.txt',timeout=60).read().decode().split()
    except Exception as e: print(u,'noindex',e); continue
    n=h=0
    for f in idx:
        for _try in range(6):
          try:
            r=urllib.request.urlopen(f,timeout=300); lines=r.read().split(bytes([10])); break
          except Exception as e:
            import time; print('retry',f,e,flush=True); time.sleep(10)
        else: continue
        for line in lines:
          if True:
            n+=1
            if PAT.search(line):
                try: o=json.loads(line)
                except: continue
                c=o.get('content',{}); ff=c.get('freetext',{})
                g=lambda k:' | '.join(i.get('content','') for i in ff.get(k,[]))
                rec={'unit':u,'id':o.get('id'),'title':o.get('title'),'date':g('date'),'notes':g('notes')[:2000],'name':g('name'),'phys':g('physicalDescription'),'setName':g('setName'),'topic':g('topic'),'type':o.get('type'),'link':(c.get('descriptiveNonRepeating') or {}).get('record_link') or (c.get('descriptiveNonRepeating') or {}).get('guid')}
                out.write(json.dumps(rec,ensure_ascii=False)+'\n'); h+=1
    out.flush(); print(u,n,h,flush=True)
