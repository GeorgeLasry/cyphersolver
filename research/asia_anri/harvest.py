"""Full-text search of sejarah-nusantara.anri.go.id for cipher terms; writes hits.jsonl."""
import re, json, sys, time, html
from fetch import get
BASE='https://sejarah-nusantara.anri.go.id/search/'
TERMS=sys.argv[1:] or ['cijfer','cijffer','cijfers','cijffers','gecijferd','gecijfert','gecijffert','cijferschrift','cijfferschrift',
 'chiffre','chiffres','gechiffreerd','dechiffreren','ontcijferd','ontcijffert','ontcijfferen','geheimschrift','sleutel',
 'cipher','ciphers','cyphers','cypher','codetelegram','code','sandi','rahasia','geheime','secrete','secreete','secreet',
 'cijfferletter','cijfferletters','zyffer','sijffer','cyffer','cyffers','ciffer','ciffers','geciffreert','nomenclator','cypherschrift']
out=open('hits.jsonl','a',encoding='utf8')
def parse(t):
    body=t.split('Search results',1)[-1]
    res=[]
    for m in re.finditer(r'<span>\d+</span>\.\s*<a href="([^"]+)"><span class="searchresult_title">(.*?)</span>\s*<span class="searchresult_type">(.*?)</span>.*?searchresult_link.*?</div>\s*<div>(.*?)</div>',body,re.S):
        clean=lambda x: html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>','',x))).strip()
        res.append({'href':m.group(1),'title':clean(m.group(2)),'type':clean(m.group(3)),'snippet':clean(m.group(4))})
    return res
def _old(t):
    res=[]
    for m in re.finditer(r'<li[^>]*>\s*.*?</li>',t,re.S):
        pass
    # fallback: split on numbered results
    body=t.split('Search results',1)[-1]
    for blk in re.split(r'\n\s*\d+\.\s*\n',re.sub(r'<[^>]+>','\n',body))[1:]:
        lines=[html.unescape(l.strip()) for l in blk.split('\n') if l.strip()]
        res.append(lines[:6])
    return res
for term in TERMS:
    page=1; n=0
    while True:
        r=get(BASE,params={'q':term,'models':'all','page':page})
        t=r.text
        m=re.search(r'We found ([\d,]+) result',t); total=int(m.group(1).replace(',','')) if m else 0
        rows=parse(t)
        # capture hrefs in result area too
        hrefs=re.findall(r'href="(/[^"]+)"',t.split('Search results',1)[-1])
        for i,rw in enumerate(rows):
            out.write(json.dumps(dict(term=term,page=page,**rw),ensure_ascii=False)+'\n'); n+=1
        print(term,'page',page,'total',total,'rows',len(rows),flush=True)
        if not rows or n>=total or page>=60: break
        page+=1; time.sleep(1)
    time.sleep(1)
