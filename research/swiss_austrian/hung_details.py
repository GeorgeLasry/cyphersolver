import json,re,html,requests,time
H={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36','Accept-Language':'en'}
rows=[json.loads(l) for l in open('raw/hungaricana.jsonl',encoding='utf-8')]
seen={}
for r in rows:
    if r['badge']!='Viennese inventory': continue
    d=r['text'].split('Description:')[-1]
    if re.search(r'feloldás nélkül|feloldás nélküli|megfejtés nélkül|feloldatlan|megfejtetlen|nem oldott|nincs feloldás|feloldás hiányzik|feloldása nincs',d,re.I):
        seen.setdefault(r['href'].split('?')[0].lstrip('/'),r)
print(len(seen))
done=set()
try: done={json.loads(l)['href'] for l in open('raw/hung_detail.jsonl',encoding='utf-8')}
except: pass
out=open('raw/hung_detail.jsonl','a',encoding='utf-8')
for h,r in seen.items():
    if h in done: continue
    try:
        x=requests.get('https://'+h,headers=H,timeout=40).text
    except Exception as e: print('ERR',h,e); continue
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',x,flags=re.S);t=re.sub(r'<[^>]+>',' | ',t);t=html.unescape(re.sub(r'(\s|\|)+',' ',t))
    m=re.search(r'Reference code (.*?) Database (.*?) Type (.*?) Date of Creation (.*?) Description (.*?) Links',t)
    d={'href':h}
    if m: d.update(ref=m.group(1),type=m.group(3),date=m.group(4),desc=m.group(5))
    else: d['raw']=t[:300]
    out.write(json.dumps(d,ensure_ascii=False)+'\n'); out.flush(); time.sleep(0.3)
