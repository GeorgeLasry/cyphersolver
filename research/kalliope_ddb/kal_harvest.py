import json,re,sys,time
import xml.etree.ElementTree as ET
from kal import q
NS={'srw':'http://www.loc.gov/zing/srw/','m':'http://www.loc.gov/mods/v3'}
TERMS=[l.strip() for l in open('kal_terms_run2.txt',encoding='utf8') if l.strip()]
out={}
counts={}
for term in TERMS:
    start=1;tot=None
    while True:
        t=q(term,start,100)
        if t.startswith('ERR'): print('ERR',term,t[:100]);break
        r=ET.fromstring(t.encode('utf8'))
        tot=int(r.find('srw:numberOfRecords',NS).text)
        recs=r.findall('.//srw:record',NS)
        for rec in recs:
            md=rec.find('.//m:mods',NS)
            ident=md.find('m:identifier',NS)
            rid=ident.text if ident is not None else None
            txt=ET.tostring(md,encoding='unicode')
            d={'id':rid,'title':' | '.join(x.text or '' for x in md.findall('.//m:titleInfo/m:title',NS)),
               'notes':[(n.text or '') for n in md.findall('.//m:note',NS)],
               'abstract':[(n.text or '') for n in md.findall('.//m:abstract',NS)],
               'date':[(n.text or '') for n in md.findall('.//m:dateCreated',NS)]+[(n.text or '') for n in md.findall('.//m:dateIssued',NS)],
               'names':[' '.join((x.text or '') for x in n.findall('m:namePart',NS)) for n in md.findall('m:name',NS)],
               'inst':[(n.text or '') for n in md.findall('.//m:recordContentSource',NS)],
               'loc':[(n.text or '') for n in md.findall('.//m:shelfLocator',NS)],
               'place':[(n.text or '') for n in md.findall('.//m:placeTerm',NS)],
               'parent':[(n.text or '') for n in md.findall('.//m:relatedItem//m:title',NS)]}
            key=rid or d['title']
            if key in out: out[key]['terms'].append(term)
            else: d['terms']=[term]; out[key]=d
        start+=len(recs)
        if not recs or start>tot: break
    counts[term]=tot; print(term,tot,len(out),flush=True)
    json.dump({'counts':counts,'recs':list(out.values())},open('kal_hits.json','w',encoding='utf8'),ensure_ascii=False)
