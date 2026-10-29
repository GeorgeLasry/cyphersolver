"""Fetch detail pages for New France Archives hits on cipher terms -> nfa_details.json"""
import re,json,time,urllib.request,os,html
here=os.path.dirname(os.path.abspath(__file__))
d=json.load(open(os.path.join(here,'nfa_hits.json'),encoding='utf8'))
terms=['chiffre','chiffrée','chiffres','chiffrés','code','traduite','en chiffre','clef']
ids={}
for k in terms:
    for r in d.get(k,[]): ids[r['keyword']]=k
fn=os.path.join(here,'nfa_details.json')
out=json.load(open(fn,encoding='utf8')) if os.path.exists(fn) else {}
for i in ids:
    if i in out: continue
    s=urllib.request.urlopen(urllib.request.Request(f'https://nouvelle-france.org/eng/item/details?id={i}',headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read().decode('utf8')
    t=s[s.find('Database item number'):]
    t=re.sub(r'<script.*?</script>','',t,flags=re.S); t=re.sub(r'<[^>]+>','\n',t); t=html.unescape(t)
    t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    rec={'term':ids[i]}
    for f in ['Title','Language','Date','Repository','Reference','Notes','Number of images']:
        m=re.search(f+r':\s*\n(.*?)\n(?=[A-Z][a-z ]+:\s*\n|This item)',t,re.S)
        if m: rec[f]=m.group(1).strip()
    part=t.split('This item is part of:')[-1].strip().split('\n')[:4]; rec['part']=part
    out[i]=rec; time.sleep(0.7)
    json.dump(out,open(fn,'w',encoding='utf8'),ensure_ascii=False,indent=1)
print(len(out))
