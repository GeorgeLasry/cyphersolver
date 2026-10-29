import re,html,json,sys
from net import get,S
B='https://catalogue.nrscotland.gov.uk/nrsonlinecatalogue/'
def hid(h,n):
    m=re.search(r'name="%s"[^>]*value="([^"]*)"'%n,h); return html.unescape(m.group(1)) if m else ''
def rows(h):
    out=[]
    for m in re.finditer(r"<a class=\"catDataGridLink\" href='details\.aspx\?reference=([^&]+)&[^']*'>\s*([^<]+?)\s*</a>\s*</td><td>\s*<span[^>]*>(.*?)</span>\s*</td><td>([^<]*)</td>",h,flags=re.S):
        out.append((html.unescape(m.group(1)).replace('%2f','/').replace('%2F','/'),html.unescape(m.group(3)).strip(),m.group(4).strip()))
    return out
res={}
for term in ['cipher','cypher','ciphers','decipher','deciphered','"in cipher"','"secret writing"','cryptogram','nomenclator','"in code"','"secret characters"']:
    from urllib.parse import quote
    url=B+'overview.aspx?st=1&tc=y&tl=n&tn=n&tp=n&k=%s&ko=p&r=&ro=m&df=1350&dt=1950&di=n'%quote(term)
    r=get(url);h=r.text
    m=re.search(r'Records 1 to \d+ of (\d+)',h); tot=int(m.group(1)) if m else 0
    n=0
    while True:
        rs=rows(h)
        for ref,ti,dt in rs: res.setdefault(ref,{'ref':ref,'title':ti,'date':dt,'terms':[]})['terms'].append(term)
        n+=len(rs)
        if n>=tot or not rs or 'cmdNextPage' not in h: break
        data={'__EVENTTARGET':'cmdNextPage','__EVENTARGUMENT':'','__VIEWSTATE':hid(h,'__VIEWSTATE'),'__VIEWSTATEGENERATOR':hid(h,'__VIEWSTATEGENERATOR'),'__EVENTVALIDATION':hid(h,'__EVENTVALIDATION')}
        h=S.post(url,data=data,timeout=40).text
    print(term,tot,n,len(res),flush=True)
json.dump(res,open('raw_nrs.json','w'),ensure_ascii=False,indent=0)
