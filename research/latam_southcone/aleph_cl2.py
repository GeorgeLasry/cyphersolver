"""Archivo Nacional de Chile, Aleph base ARNES ('Archivo especial', item-level letters): full records for a word search.
usage: python aleph_cl2.py clave [BASE]  -> arnes_<word>.json"""
import requests,re,html,json,time,sys
H={'User-Agent':'Mozilla/5.0 (research sweep; cyphersolver)'}
word=sys.argv[1]; base=sys.argv[2] if len(sys.argv)>2 else 'ARNES'
def txt(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S))))
r=requests.get('http://www.bncatalogo.cl/F/',params=dict(func='find-b',request=word,find_code='WRD',local_base=base),headers=H,timeout=60)
s=r.content.decode('utf-8','replace')
m=re.search(r'Registros?\s+\d+\s*-\s*\d+\s+de\s+(\d+)',txt(s)); n=int(m.group(1)) if m else 0
u=re.search(r'HREF=(https://www.bncatalogo.cl:443/F/[A-Z0-9]+)-\d+\?func=full-set-set&set_number=(\d+)',s)
out=[]
print(word,base,n,flush=True)
for e in range(1,min(n,400)+1):
    rr=requests.get(f'{u.group(1)}?func=full-set-set&set_number={u.group(2)}&set_entry={e:06d}&format=999',headers=H,timeout=60)
    T=txt(rr.content.decode('utf-8','replace'))
    i=T.find('Formato'); body=T[i:i+1800] if i>=0 else T[:1800]
    out.append(body)
    if e%20==0:
        print(e,flush=True); json.dump(out,open(f'arn_{base}_{word.replace("?","Q")}.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
    time.sleep(0.4)
json.dump(out,open(f'arn_{base}_{word.replace("?","Q")}.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
