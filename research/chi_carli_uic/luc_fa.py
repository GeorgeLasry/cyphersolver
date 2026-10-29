"""Fetch all Loyola Archives & Special Collections finding-aid PDFs linked from luc.edu/archives pages, grep for cipher terms.
Texts cached in luc_txt/ (git-ignored by size; delete before commit)."""
import re, requests, time, os, json, html, fitz
from urllib.parse import urljoin
UA={'User-Agent':'Mozilla/5.0 (cyphersolver research)'}
pages=['https://www.luc.edu/archives/collectionsbysubject/','https://www.luc.edu/archives/atozlistspecialcollections/','https://www.luc.edu/archives/atozlistuniversityarchives/','https://www.luc.edu/archives/rare_book_collection.shtml','https://www.luc.edu/archives/cpsa.shtml','https://www.luc.edu/archives/opencollections.shtml']
links={}
for p in pages:
    try:
        t=requests.get(p,headers=UA,timeout=60).text
    except Exception as e: print('ERR',p,e); continue
    for h,x in re.findall(r'href="([^"]+\.pdf)"[^>]*>([^<]*)',t,re.I):
        u=urljoin(p,h)
        if '/archives/pdfs/' in u: links.setdefault(u,html.unescape(x).strip())
    time.sleep(3)
print(len(links),'pdfs')
os.makedirs('luc_txt',exist_ok=True)
pat=re.compile(r'c[iy]pher|cryptogr|secret (writing|code|ink)|invisible ink|nomenclat|chiffr|cifra|code (message|telegram|book)|coded (message|letter|telegram)|in code\b',re.I)
out=open('luc_hits.jsonl','a',encoding='utf-8')
import re as _re
def early(name):
    return any(int(y)<1900 for y in _re.findall(r'(1[0-9]{3})',name))
for u,name in links.items():
    if not early(name): continue
    fn='luc_txt/'+re.sub(r'\W+','_',u.split('/')[-1])+'.txt'
    if not os.path.exists(fn):
        try:
            r=requests.get(u,headers=UA,timeout=45); time.sleep(3)
            d=fitz.open(stream=r.content,filetype='pdf'); txt='\n'.join(p.get_text() for p in d)
        except Exception as e: print('ERR',u,e); continue
        open(fn,'w',encoding='utf-8').write(txt)
    txt=open(fn,encoding='utf-8').read()
    for m in pat.finditer(txt):
        out.write(json.dumps({'url':u,'name':name,'term':m.group(0),'ctx':txt[max(0,m.start()-200):m.end()+200].replace('\n',' ')},ensure_ascii=False)+'\n')
    out.flush()
print('done')
