import requests,json,time,re,os
UA={'User-Agent':'cyphersolver-research/1.0 (dnbourdeau@gmail.com; historical cipher survey)'}
u={}
for fn in ('raw_regex.jsonl','raw_wikisource.jsonl','raw_targeted.jsonl'):
    for l in open(fn,encoding='utf8'):
        h=json.loads(l)
        if h.get('size',0)<=80000: u.setdefault((h['lang'],h['title']),h)
bylang={}
for (lg,t) in u: bylang.setdefault(lg,[]).append(t)
print({k:len(v) for k,v in bylang.items()},flush=True)
os.makedirs('.work',exist_ok=True)
out=open('.work/pages.jsonl','a',encoding='utf8')
done=set()
if os.path.exists('.work/pages_done.txt'): done=set(open('.work/pages_done.txt',encoding='utf8').read().split('\n'))
dn=open('.work/pages_done.txt','a',encoding='utf8')
for lg,ts in bylang.items():
    ts=[t for t in ts if f'{lg}|{t}' not in done]
    for i in range(0,len(ts),20):
        b=ts[i:i+20]
        try: j=requests.get(f'https://{lg}.wikisource.org/w/api.php',params={'action':'query','titles':'|'.join(b),'prop':'revisions','rvprop':'content','rvslots':'main','format':'json'},headers=UA,timeout=90).json()
        except Exception as e: print('err',lg,i,e,flush=True); time.sleep(5); continue
        for p in j.get('query',{}).get('pages',{}).values():
            r=p.get('revisions')
            if r: out.write(json.dumps({'lang':lg,'title':p['title'],'text':r[0]['slots']['main'].get('*','')},ensure_ascii=False)+'\n')
        for t in b: dn.write(f'{lg}|{t}\n')
        out.flush();dn.flush();time.sleep(0.3)
    print(lg,'done',flush=True)
