"""Biblioteca Nacional de Chile Aleph (bncatalogo.cl, base BNC): manuscript records for a word search, with notes
and any digital-object link. usage: python bnc.py "texto en clave" -> bnc_<slug>.json"""
import requests,re,html,json,time,sys
H={'User-Agent':'Mozilla/5.0 (research sweep; cyphersolver)'}
word=sys.argv[1]; base=sys.argv[2] if len(sys.argv)>2 else 'BNC'
def txt(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S))))
r=requests.get('http://www.bncatalogo.cl/F/',params=dict(func='find-b',request=word,find_code='WRD',local_base=base),headers=H,timeout=60)
s=r.content.decode('utf-8','replace')
m=re.search(r'Registros?\s+\d+\s*-\s*\d+\s+de\s+(\d+)',txt(s)); n=int(m.group(1)) if m else 0
u=re.search(r'HREF=(https://www.bncatalogo.cl:443/F/[A-Z0-9]+)-\d+\?func=full-set-set&set_number=(\d+)',s)
print(word,n,flush=True); out=[]
for e in range(1,min(n,300)+1):
    rr=requests.get(f'{u.group(1)}?func=full-set-set&set_number={u.group(2)}&set_entry={e:06d}&format=999',headers=H,timeout=60)
    raw=rr.content.decode('utf-8','replace'); T=txt(raw)
    i=T.find('Título'); j=T.find('Escoger Formato')
    links=sorted(set(l for l in re.findall(r'href="?(https?://[^" >]+)',raw,flags=re.I) if 'bibliotecanacionaldigital' in l or 'memoriachilena' in l))
    sysno=re.search(r'No\. sis\.\s*(\d+)',T) or re.search(r'doc_number=(\d+)',raw)
    out.append({'sys':sysno.group(1) if sysno else '', 'text':T[i:j][:1800], 'links':links})
    time.sleep(0.4)
json.dump(out,open('bnc_'+re.sub(r'\W+','_',word)+'.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
