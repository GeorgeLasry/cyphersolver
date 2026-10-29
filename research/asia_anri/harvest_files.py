"""'Archive files' (inventory title) section of the Sejarah Nusantara search; writes files_hits.jsonl."""
import re, json, sys, time, html
from fetch import get
TERMS=sys.argv[1:]
out=open('files_hits.jsonl','a',encoding='utf8')
cl=lambda x: html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',x))).strip()
for term in TERMS:
    t=get('https://sejarah-nusantara.anri.go.id/search/',params={'q':term,'models':'all'}).text
    sec=t.split('<h3>Archive files</h3>',1)
    rows=[]
    if len(sec)>1:
        sec=sec[1].split('</table>',1)[0]
        for td in re.findall(r'<td>(.*?)</td>',sec,re.S):
            m=re.search(r'<strong>(.*?)</strong>\s*inventory number\s*([^<]+)',td)
            href=re.search(r'href="([^"]*pagebrowser[^"]*)"',td)
            divs=[cl(d) for d in re.findall(r'<div>(.*?)</div>',td,re.S)]
            rows.append({'term':term,'archive':m.group(1) if m else '','inv':(m.group(2).strip() if m else ''),'desc':divs,'scans_url':href.group(1) if href else None})
    for r in rows: out.write(json.dumps(r,ensure_ascii=False)+'\n')
    print(term,len(rows),flush=True); time.sleep(1)
