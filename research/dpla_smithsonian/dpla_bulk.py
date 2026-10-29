"""Stream DPLA bulk export (public S3, 2026/10 snapshot), keep records whose text mentions cipher vocabulary.
Usage: python dpla_bulk.py START END  (part numbers).  Output hits/part-NNNNN.jsonl (compact)."""
import sys,re,zlib,json,os,urllib.request,time
BASE='https://dpla-provider-export.s3.amazonaws.com/2026/10/all.jsonl/part-%05d.gz'
PAT=re.compile(rb'cipher|cypher|cryptogra|secret writing|secret writ|bdecipher|bdecypher|bencipher|in code\b|coded|code book|codebook|code-book|chiffr|cifra|secret alphabet',re.I)
os.makedirs('hits',exist_ok=True)
def keep(o):
    s=o.get('_source',{}); sr=s.get('sourceResource',{})
    def L(v): return v if isinstance(v,list) else ([v] if v is not None else [])
    def T(v): return [x if isinstance(x,str) else (x.get('name') or x.get('displayDate') or json.dumps(x)) for x in L(v)]
    return {'id':s.get('id'),'_id':o.get('_id'),'title':T(sr.get('title')),'desc':T(sr.get('description')),
      'date':T(sr.get('date')),'subject':T(sr.get('subject')),'type':T(sr.get('type')),'creator':T(sr.get('creator')),
      'coll':T(sr.get('collection')),'lang':T(sr.get('language')),'spatial':T(sr.get('spatial')),
      'prov':(s.get('provider') or {}).get('name'),'dp':(s.get('dataProvider') if isinstance(s.get('dataProvider'),str) else (s.get('dataProvider') or {}).get('name')) if not isinstance(s.get('dataProvider'),list) else None,
      'url':s.get('isShownAt')}
def run(n):
    out='hits/part-%05d.jsonl'%n
    if os.path.exists(out+'.done'): return
    for attempt in range(5):
        try:
            r=urllib.request.urlopen(BASE%n,timeout=120); d=zlib.decompressobj(31); buf=b''; res=[]; tot=0
            while True:
                ch=r.read(1<<20)
                if not ch: break
                buf+=d.decompress(ch)
                i=buf.rfind(b'\n')
                if i<0: continue
                blk,buf=buf[:i],buf[i+1:]
                for line in blk.split(b'\n'):
                    tot+=1
                    if line.startswith(b'{"_type":"item","_id":"nara--'): continue
                    if PAT.search(line):
                        try: res.append(keep(json.loads(line)))
                        except Exception as e: pass
            with open(out,'w',encoding='utf8') as f:
                for x in res: f.write(json.dumps(x,ensure_ascii=False)+'\n')
            open(out+'.done','w').write(str(tot)); print(n,tot,len(res),flush=True); return
        except Exception as e:
            print('retry',n,e,flush=True); time.sleep(15)
if __name__=='__main__':
    a,b=int(sys.argv[1]),int(sys.argv[2])
    for n in range(a,b): run(n)
