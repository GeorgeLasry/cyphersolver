import sys, json, time, urllib.request, urllib.parse
UA='Mozilla/5.0 (cyphersolver research catalogue sweep)'
def q(term, start, rows=100):
    u=("https://www.masshist.org/projects/api/index.php/solrsearch?terms="+urllib.parse.quote(term)+
       "&configURL=/projects/api/configs/sitewide.json&configStart=%d&configRows=%d"%(start,rows))
    return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=60))
for term in sys.argv[1:]:
    start=0
    while True:
        d=q(term,start); r=d['response']
        with open('raw/mhs.jsonl','a',encoding='utf-8') as f:
            for doc in r['docs']:
                doc['term']=term; hl=d.get('highlighting',{}).get(doc['id'],{}); doc['hl']=hl; f.write(json.dumps(doc,ensure_ascii=False)+'\n')
        start+=100; time.sleep(3)
        if start>=r['numFound']: break
    print(term,r['numFound'],flush=True)
