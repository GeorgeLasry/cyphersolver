"""Search AtoM portals for cipher vocabulary and print/save each hit's title + scope note.
usage: python atom.py host1,host2  -> atom_hits_<host>.json"""
import requests,re,html,json,time,sys
H={'User-Agent':'Mozilla/5.0 (research sweep; cyphersolver)'}
import os
TERMS=os.environ['TERMS'].split('|') if os.environ.get('TERMS') else ['cifra','cifrada','cifrado','cifradas','cifrados','"en cifra"','criptograma','criptografía','descifrado','descifrar','"tinta simpática"','"signos convencionales"','jeroglífico','clave secreta','"carta en clave"','"telegrama cifrado"','chiffre','cipher','cifrada carta']
def txt(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S)))).strip()
for host in sys.argv[1].split(','):
    out={}
    for t in TERMS:
        for page in range(1,6):
            try:
                r=requests.get(f'https://{host}/index.php/informationobject/browse',params=dict(topLod=0,query=t,page=page,limit=50),headers=H,timeout=60,verify=False)
            except Exception as e:
                print('ERR',host,t,e); break
            s=r.text
            seen=set(); slugs=[]
            for blk in re.split(r'<article class="search-result',s)[1:]:
                m=re.search(r'href="/index.php/([^"?/]+)"',blk)
                if not m or m.group(1) in seen: continue
                tm=re.search(r'title="([^"]*)"',blk) or re.search(r'alt="([^"]*)"',blk)
                seen.add(m.group(1)); slugs.append((m.group(1),tm.group(1) if tm else ''))
            if not slugs:  # older AtoM theme
                for m in re.finditer(r'<p class="title">\s*<a href="/index.php/([^"?/]+)"[^>]*>(.*?)</a>',s,flags=re.S):
                    if m.group(1) not in seen: seen.add(m.group(1)); slugs.append((m.group(1),m.group(2)))
            for sl,ti in slugs:
                out.setdefault(sl,{'title':txt(ti),'terms':[]})['terms'].append(t)
            print(host,t,page,len(slugs),flush=True)
            if len(slugs)<50: break
            time.sleep(1)
    for sl,v in out.items():
        if 'body' in v: continue
        try:
            r=requests.get(f'https://{host}/index.php/{sl}',headers=H,timeout=60,verify=False)
            T=txt(r.text); i=T.find('Reference code'); i = i if i>=0 else T.find('Código de referencia')
            v['body']=T[max(i,0):max(i,0)+2500]
        except Exception as e: v['body']='ERR '+str(e)
        time.sleep(0.7)
    json.dump(out,open(f'atom_hits_{host}{os.environ.get("SUF","")}.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
    print(host,'total',len(out))
