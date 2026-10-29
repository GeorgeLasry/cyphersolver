import re,json,time,subprocess,sys,html,urllib.parse
terms=["cifra","cifrato","cifrata","cifrate","cifrati","in cifra","lettera cifrata","lettere cifrate","decifrazione","decifrato","decifrata","cifrario","cifrari","scrittura segreta","chiave cifra","scritture in cifra","dispacci in cifra","cifre","alfabeto cifrato","notae"]
def get(u):
    r=subprocess.run(["curl","-s","-m","40","-A","Mozilla/5.0",u],capture_output=True)
    return r.stdout.decode('utf8','replace')
hits={}
for t in terms:
    p=1
    while True:
        u="https://www.lombardiabeniculturali.it/archivi/ricerca/?current=%d&testo=%s&where=comparch"%(p,urllib.parse.quote_plus(t))
        h=get(u)
        n=re.search(r"Trovati <span class='num'>(\d+)</span>",h)
        items=re.findall(r"<li class='(?:odd|even)'>\s*<a href ='([^']+)'>(.*?)</a>\s*\(([^)]*)\)<br />(.*?)</li>",h,flags=re.S)
        for href,ti,dt,rest in items:
            rest=re.sub(r'<[^>]+>','',rest); 
            hits.setdefault(href,{"title":html.unescape(ti),"date":dt,"rest":html.unescape(rest).strip(),"terms":[]})["terms"].append(t)
        tot=int(n.group(1)) if n else 0
        print(t,p,tot,len(items),flush=True)
        if p*20>=tot or not items or p>=15: break
        p+=1; time.sleep(0.5)
    json.dump(hits,open("lbc_hits.json","w",encoding="utf8"),ensure_ascii=False,indent=1)
