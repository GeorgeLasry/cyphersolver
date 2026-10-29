"""Harvest oai_dc from a Visual Library OAI endpoint to jsonl. usage: oai_harvest.py base out.jsonl"""
import sys,re,time,json,urllib.request as u,urllib.parse as p
import xml.etree.ElementTree as ET
base,out=sys.argv[1],sys.argv[2]
setspec=sys.argv[3] if len(sys.argv)>3 else None
ns={'o':'http://www.openarchives.org/OAI/2.0/','d':'http://purl.org/dc/elements/1.1/'}
def get(url):
    for i in range(5):
        try: return u.urlopen(u.Request(url,headers={'User-Agent':'Mozilla/5.0 (research; cyphersolver)'}),timeout=60).read()
        except Exception as e: print('retry',e,flush=True); time.sleep(3*(i+1))
    raise SystemExit('fail')
url=base+'?verb=ListRecords&metadataPrefix=oai_dc'+('&set='+setspec if setspec else '')
n=0
with open(out,'a',encoding='utf-8') as f:
    while url:
        root=ET.fromstring(get(url))
        for r in root.iter('{%s}record'%ns['o']):
            h=r.find('o:header',ns); d={'oai_id':h.findtext('o:identifier',namespaces=ns),'oai_date':h.findtext('o:datestamp',namespaces=ns)}
            for e in r.iter():
                if e.tag.startswith('{%s}'%ns['d']):
                    d.setdefault(e.tag.split('}')[1],[]).append((e.text or '').strip())
            f.write(json.dumps(d,ensure_ascii=False)+'\n'); n+=1
        t=root.find('.//o:resumptionToken',ns)
        url=base+'?verb=ListRecords&resumptionToken='+p.quote(t.text) if t is not None and t.text else None
        if n%2000<100: print(n,flush=True)
print('done',n)
