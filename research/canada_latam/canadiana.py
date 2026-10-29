import requests,re,json,time,html
H={'User-Agent':'Mozilla/5.0 (research sweep)'}
TI=['cipher','cypher','chiffre','chiffré','chiffrée','cifra','cifrada','cryptogram','cryptograph*','secret writing','nomenclator','decipher*','déchiffr*','code secret','secret correspondence','correspondance chiffrée','cipher letter','lettre chiffrée','in cipher','en chiffre']
out={}
def parse(t):
    items=[]
    for blk in t.split('<section class="search-item">')[1:]:
        m=re.search(r'href="(https://www.canadiana.ca/view/[^"]*)"[^>]*>(.*?)</a>',blk,flags=re.S)
        if not m: continue
        def f(lbl):
            mm=re.search(r'<dt[^>]*>'+lbl+r'</dt>\s*<dd[^>]*>(.*?)</dd>',blk,flags=re.S)
            return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',mm.group(1)))).strip() if mm else ''
        items.append(dict(url=m.group(1),title=re.sub(r'\s+',' ',html.unescape(m.group(2))).strip(),published=f('Published'),notes=f('Notes'),source=f('Document source')))
    return items
for fld in ['ti','su','tx']:
    for t in TI:
        if fld=='tx' and t not in('cipher letter','lettre chiffrée','in cipher','en chiffre','carta cifrada','cifrada','cipher'): continue
        for pg in range(1,6 if fld!='tx' else 4):
            try:
                r=requests.get('https://www.canadiana.ca/search/',params={'q0.0':f'{fld}:{t}' if ' ' not in t else f'{fld}:"{t}"','so':'oldest','pg':pg,'df':1500,'dt':1950},headers=H,timeout=60)
            except Exception as e: print('ERR',fld,t,e);break
            its=parse(r.text)
            n=re.findall(r'(\d[\d,]*) results? for',r.text)
            for it in its:
                d=out.setdefault(it['url'],dict(it,hits=[]));d['hits'].append(f'{fld}:{t}')
            print(fld,t,pg,n,len(its),flush=True)
            if len(its)<10: break
            time.sleep(1)
json.dump(out,open('canadiana_hits.json','w'),ensure_ascii=False,indent=1)
print(len(out))
