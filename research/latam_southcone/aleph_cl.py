"""Search the Archivo Nacional de Chile Aleph bases (bncatalogo.cl) for cipher vocabulary; writes aleph_cl_hits.json."""
import requests,re,html,json,time,sys
H={'User-Agent':'Mozilla/5.0 (research sweep; cyphersolver)'}
B='http://www.bncatalogo.cl/F/'
BASES=sys.argv[1].split(',') if len(sys.argv)>1 else ['ARNHI','ARNES','ARCHIVO_NACIONAL']
TERMS=['cifra','cifrada','cifrado','cifradas','cifrados','clave','descifrar','descifrado','jeroglifico','criptografia','simpatica','en cifra','chiffre']
def txt(s):
    s=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S)
    return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s)))
out={}
for b in BASES:
  for t in TERMS:
    r=requests.get(B,params=dict(func='find-b',request=t,find_code='WRD',local_base=b),headers=H,timeout=60)
    s=r.content.decode('utf-8','replace')
    m=re.search(r'Registros\s+\d+\s*-\s*\d+\s+de\s+(\d+)',txt(s))
    n=int(m.group(1)) if m else 0
    print(b,t,n,flush=True)
    if not n: continue
    # result set link: set_number
    sn=re.search(r'set_number=(\d+)',s)
    rows=[]
    if sn:
      for e in range(1,min(n,300)+1,10):
        rr=requests.get(B,params=dict(func='short-jump',jump=e,set_number=sn.group(1),local_base=b),headers=H,timeout=60)
        ss=rr.content.decode('utf-8','replace')
        for doc in re.findall(r'func=full-set-set&(?:amp;)?set_number=\d+&(?:amp;)?set_entry=(\d+)',ss):
            rows.append(doc)
        time.sleep(0.5)
      for e in sorted(set(rows),key=int):
        rr=requests.get(B,params=dict(func='full-set-set',set_number=sn.group(1),set_entry=e,format='999',local_base=b),headers=H,timeout=60)
        T=txt(rr.content.decode('utf-8','replace'))
        i=T.find('Registro'); body=T[T.find('Formato'):][:1500] if 'Formato' in T else T[:1500]
        out.setdefault(b+':'+t+':'+e,body)
        time.sleep(0.5)
    json.dump(out,open('aleph_cl_hits.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(out))
