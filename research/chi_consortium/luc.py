"""Loyola Archives & Special Collections: every finding aid (pdf/docx) linked from the A-Z lists, 3 s spacing, grep. PDFs in dl/luc (git-ignore)."""
import json, os, re, time, html, requests, pymupdf
UA={'User-Agent':'cyphersolver research (catalogue sweep)'}
os.makedirs('dl/luc',exist_ok=True)
links={}
for page in ['atozlistspecialcollections','atozlistuniversityarchives']:
    t=requests.get('https://www.luc.edu/archives/%s/'%page,headers=UA,timeout=60).text; time.sleep(3)
    for h,x in re.findall(r'<a [^>]*href="([^"]+\.(?:pdf|docx))"[^>]*>([^<]+)</a>',t):
        if 'policy' in h: continue
        if h.startswith('/'): h='https://www.luc.edu'+h
        links[h]=html.unescape(x).strip()
json.dump(links,open('luc_links.json','w'),indent=1); print(len(links),flush=True)
PAT=re.compile(r'(?i)ciph|cypher|cryptogr|cryptolog|in code\b|coded\b|code (letter|message|telegram|book|word)|secret (writing|code|ink|alphabet)|invisible ink|sympathetic ink|nomenclat|chiffr|cifra|geheimschrift|enciph|decod')
hits={}
for h,title in links.items():
    f='dl/luc/'+re.sub(r'[^A-Za-z0-9._-]','_',h.split('/')[-1])
    if not os.path.exists(f):
        try:
            r=requests.get(h,headers=UA,timeout=120)
            if r.status_code!=200: print('ERR',h,r.status_code); time.sleep(3); continue
            open(f,'wb').write(r.content)
        except Exception as e: print('ERR',h,e); continue
        time.sleep(3)
    try:
        if f.endswith('.pdf'): t='\n'.join(p.get_text() for p in pymupdf.open(f))
        else:
            import zipfile; t=re.sub(r'<[^>]+>',' ',zipfile.ZipFile(f).read('word/document.xml').decode('utf8'))
    except Exception as e: print('READERR',f,e); continue
    ms=[t[max(0,m.start()-200):m.end()+250].replace('\n',' ') for m in PAT.finditer(t)]
    if ms: hits[h]={'title':title,'n':len(ms),'ctx':ms[:15],'chars':len(t)}; print(title[:60],len(ms),flush=True)
    json.dump(hits,open('luc_hits.json','w'),ensure_ascii=False,indent=1)
print('done')
