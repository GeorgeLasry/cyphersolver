import sys,json,time,urllib.request,urllib.parse
UA='Mozilla/5.0 (cyphersolver research catalogue sweep)'
def flat(v):
    if isinstance(v,dict) and 'attributes' in v and 'value' in v['attributes']: return v['attributes']['value']
    return v
for term in sys.argv[1:]:
    p=1;n=None;cnt=0
    while True:
        u="https://findingaids.library.upenn.edu/records.json?per_page=100&page=%d&q=%s"%(p,urllib.parse.quote(term))
        try: d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=60))
        except Exception as e: print('ERR',term,p,e);break
        with open('raw/pacscl.jsonl','a',encoding='utf-8') as f:
            for r in d['data']:
                rec={'id':r['id'],'term':term}
                for k,v in r['attributes'].items(): rec[k]=flat(v)
                f.write(json.dumps(rec,ensure_ascii=False)+'\n'); cnt+=1
        n=d['meta']['pages']['total_count']
        if not d['meta']['pages']['next_page']: break
        p+=1; time.sleep(3)
    print(term,n,cnt,flush=True); time.sleep(3)
