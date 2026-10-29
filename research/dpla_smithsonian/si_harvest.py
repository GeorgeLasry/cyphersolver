import json,time,urllib.request,urllib.parse,sys,os
K="DEMO_KEY"
terms=['cipher','cypher','"in cipher"','"in code"','cryptogram','decipher','"secret writing"','"coded letter"','"key to the cipher"','"cipher letter"','"cipher message"','"coded message"','cryptographic','"secret code"','"code book"','codebook','cryptanalysis','"code message"','encipher','"secret correspondence"','"invisible ink"','"secret message"','telegram code','"enciphered"','"cipher key"','"cipher system"','"cipher machine"','"code telegram"','"cypher key"','"ciphered"','"cypher letter"','"secret alphabet"']
out='si_hits.json'
hits=json.load(open(out)) if os.path.exists(out) else {}
def get(u):
    for i in range(4):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'cyphersolver research'}),timeout=60))
        except Exception as e:
            print('err',e,file=sys.stderr); time.sleep(10)
cnt={}
for t in terms:
    start=0
    while True:
        u="https://api.si.edu/openaccess/api/v1.0/search?"+urllib.parse.urlencode({'q':t,'api_key':K,'rows':1000,'start':start})
        d=get(u)
        if not d: break
        r=d['response']; rows=r['rows']; cnt[t]=r.get('rowCount')
        for x in rows:
            c=x.get('content',{}); ff=c.get('freetext',{})
            def g(k): return ' | '.join(i.get('content','') for i in ff.get(k,[]))
            hits.setdefault(x['id'],{'id':x['id'],'title':x.get('title'),'unit':x.get('unitCode'),'url':x.get('url'),
              'date':g('date'),'notes':g('notes')[:1500],'name':g('name'),'phys':g('physicalDescription'),'setName':g('setName'),
              'link':(c.get('descriptiveNonRepeating') or {}).get('record_link'),'terms':[]})['terms'].append(t)
        start+=len(rows)
        if not rows or start>=r.get('rowCount',0): break
        time.sleep(1)
    print(t,cnt[t],len(hits),flush=True)
    json.dump(hits,open(out,'w'))
json.dump(cnt,open('si_counts.json','w'))
