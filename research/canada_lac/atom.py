"""Search an AtoM portal (Canadian archives) for cipher terms. Usage: python atom.py BASE term...
BASE e.g. https://archivalcollections.library.mcgill.ca/index.php . Writes atom_<host>.json beside this script."""
import re,sys,json,urllib.request,urllib.parse,time,os
base=sys.argv[1].rstrip('/'); out=[]
def clean(x): return re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',x)).strip()
for term in sys.argv[2:]:
    url=f"{base}/informationobject/browse?topLod=0&sort=relevance&query={urllib.parse.quote(term)}"
    try:
        s=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=40).read().decode('utf8','replace')
    except Exception as e:
        print(term,'ERR',e); continue
    n=re.findall(r'Showing ([\d,]+) results|Results [\d,]+ to [\d,]+ of ([\d,]+)',s)
    hits=[]
    for a in s.split('<article class="search-result')[1:]:
        m=re.search(r'<a class="h5[^"]*" href="([^"]+)"[^>]*>(.*?)</a>',a,re.S)
        if not m: continue
        ref=re.search(r'<span class="text-primary">(.*?)</span>',a,re.S)
        part=re.search(r'Part of\s*<a[^>]*>(.*?)</a>',a,re.S)
        body=re.search(r'<span class="text-block d-none">(.*?)</span>',a,re.S)
        hits.append({'term':term,'href':m.group(1),'title':clean(m.group(2)),'ref':clean(ref.group(1)) if ref else '',
                     'part':clean(part.group(1)) if part else '','snip':clean(body.group(1))[:400] if body else ''})
    print(f'## {term}: {n} ({len(hits)} on page)')
    for h in hits: print('  ',h['ref'],'|',h['title'][:90],'|',h['part'][:50],'|',h['snip'][:150])
    out+=hits; time.sleep(1)
host=re.sub(r'\W','_',base.split('//')[1].split('/')[0])
json.dump(out,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),f'atom_{host}.json'),'w',encoding='utf8'),ensure_ascii=False,indent=1)
