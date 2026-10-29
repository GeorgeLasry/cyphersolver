"""Hungaricana search (server-rendered). Keep non-Library hits (charters, archives, Viennese inventory ...)."""
import requests,re,json,base64,html,sys,time
H={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36','Accept-Language':'en'}
TERMS=sys.argv[1:] or ['titkosírás','titkosírással','titkosírásban','titkosírású','titkos írás','titkos írással','rejtjel','rejtjeles','rejtjelezett','cifra','cifrás','cifrával','cifrával írt','chiffre','chiffrirt','chiffriert','Geheimschrift','tajné písmo','tajnopis','šifra','šifrovaný','šifrované','tajopis','tajopisom','šifrovaný list','kulcs titkosírás','titkos kulcs','kriptogram','Chiffer','cyfra','Cifra']
out=open('raw/hungaricana.jsonl','a',encoding='utf-8')
def getp(list_b64,page):
    return requests.get('https://www.hungaricana.hu/en/search/results/',params={'list':list_b64,'per_page':100,'page':page},headers=H,timeout=60).text
for t in TERMS:
    lb=base64.b64encode(json.dumps({'query':t}).encode()).decode()
    pg=1;tot=None;n=0;kept=0
    while True:
        try: tx=getp(lb,pg)
        except Exception as e: print('ERR',t,e);break
        if tot is None:
            m=re.search(r'(\d[\d ,]*)\s*hit',tx);tot=int(re.sub(r'\D','',m.group(1))) if m else 0
        items=re.split(r'<li class="(?:result )?list-group-item[^>]*?id="hit-(\d+)"',tx)
        # alternate split: items=[pre, id, body, id, body...]
        blocks=re.findall(r'id="hit-(\d+)">(.*?)</li>',tx,re.S)
        if not blocks: break
        for hid,b in blocks:
            n+=1
            badge=re.search(r'badge[^>]*>\s*([^<]+?)\s*<',b)
            badge=badge.group(1) if badge else ''
            if badge.lower() in('library','gallery'): continue
            a=re.search(r'<a\s+href="([^"]+)"[^>]*>\s*(.*?)\s*</a>',b,re.S)
            plain=html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',b))).strip()
            out.write(json.dumps({'term':t,'badge':badge,'href':a.group(1) if a else '','text':plain[:700]},ensure_ascii=False)+'\n');kept+=1
        if n>=tot or pg>=40: break
        pg+=1;time.sleep(0.4)
    out.flush();print(t,tot,n,kept,flush=True)
