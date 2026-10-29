import sys,re,json,os,time,urllib.request
site=sys.argv[1]; base={'princeton':'https://findingaids.princeton.edu/catalog/%s.xml','unc':'https://finding-aids.lib.unc.edu/catalog/%s.xml'}[site]
UA='Mozilla/5.0 (cyphersolver research catalogue sweep)'
ids=set()
for l in open(f'raw/{site}.jsonl',encoding='utf-8'):
    r=json.loads(l)
    if r['term'] in ('in code','coded'): continue
    ids.add(r['id'].split('_')[0] if site=='princeton' else r['id'].split('_')[0])
pat=re.compile(r'cipher|cypher|cryptogra|secret writing|in code|coded|code letter|decipher|decypher|key to the',re.I)
out=open(f'raw/{site}_ead_ctx.txt','w',encoding='utf-8')
for cid in sorted(ids):
    fn=f'raw/ead_{site}/{cid}.xml'
    if not os.path.exists(fn):
        try: open(fn,'wb').write(urllib.request.urlopen(urllib.request.Request(base%cid,headers={'User-Agent':UA}),timeout=120).read())
        except Exception as e: print('ERR',cid,e); continue
        time.sleep(3)
    t=open(fn,encoding='utf-8',errors='replace').read()
    t2=re.sub(r'<[^>]+>',' ',t); t2=re.sub(r'\s+',' ',t2)
    title=re.search(r'<unittitle>(.*?)</unittitle>',t,re.S)
    n=0
    for m in pat.finditer(t2):
        n+=1
        out.write(f'{cid}\t{(title.group(1)[:60] if title else "")}\t...{t2[max(0,m.start()-250):m.end()+250]}...\n')
    print(cid,len(t),n,flush=True)
