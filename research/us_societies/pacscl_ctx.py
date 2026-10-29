import json,re,time,urllib.request,os
UA='Mozilla/5.0 (cyphersolver research catalogue sweep)'
skip=('"in code"','"encoded"')
ids={}
for l in open('raw/pacscl.jsonl',encoding='utf-8'):
    r=json.loads(l)
    if r['term'] in skip: continue
    ids.setdefault(r['id'],r)
os.makedirs('raw/pacscl_pages',exist_ok=True)
pat=re.compile(r'cipher|cypher|cryptogra|secret writing|coded|in code|code letter|decipher',re.I)
out=open('raw/pacscl_ctx.txt','w',encoding='utf-8')
for i,r in ids.items():
    if i.startswith(('PRIN_MUDD_AC19','PRIN_MUDD_MC1','TUSCRC','WHYY','BMC_BMC.RG9','LEHIGH_SCMS0374','LEHIGH_SCMS0119')): continue
    fn='raw/pacscl_pages/'+i+'.html'
    if not os.path.exists(fn):
        try: open(fn,'wb').write(urllib.request.urlopen(urllib.request.Request('https://findingaids.library.upenn.edu/records/'+i,headers={'User-Agent':UA}),timeout=120).read())
        except Exception as e: print('ERR',i,e); continue
        time.sleep(3)
    t=open(fn,encoding='utf-8',errors='replace').read()
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S); t=re.sub(r'<[^>]+>',' ',t); t=re.sub(r'\s+',' ',t)
    last=-999
    for m in pat.finditer(t):
        if m.start()-last<300: continue
        last=m.start(); out.write(f'{i}\t{t[max(0,m.start()-220):m.end()+260]}\n')
    print(i,len(t),flush=True)
