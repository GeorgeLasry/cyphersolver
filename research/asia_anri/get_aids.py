"""Download ANRI textual finding-aid PDFs listed in finding_aids.json into pdf/ (git-ignored) and extract text."""
import json, re, os, time, pymupdf
from fetch import get
d=json.load(open('finding_aids.json'))
sel=[k for k in d if not re.search(r'foto|film|video|pamflet|siaran|pengumuman|sop-|surat-edaran|covid|olahraga|pemilu|stunting|soeharto|bappenas|kearsitekturan|statistik|iptn|19[6-9]\d-|20\d\d-\d|setwapres|nahdlatul|pertanian-1950|bni-1946',k)]
print(len(sel))
for k in sel:
    name=k.split('/')[-1][:120]
    p='pdf/'+name+'.pdf'
    if os.path.exists(p+'.txt'): continue
    try:
        r=get('https://anri.go.id'+k)
        if not r.content.startswith(b'%PDF'): print('notpdf',k,r.headers.get('content-type')); continue
        open(p,'wb').write(r.content)
        doc=pymupdf.open(p); txt='\n'.join(pg.get_text() for pg in doc)
        open(p+'.txt','w',encoding='utf8').write(txt); os.remove(p)
        print(len(r.content)//1000,'KB',len(doc),'pp',len(txt),name,flush=True)
    except Exception as e: print('ERR',k,e)
    time.sleep(0.5)
