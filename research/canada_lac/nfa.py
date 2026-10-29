"""Query the New France Archives database (nouvelle-france.org, LAC/ANOM/BAnQ item descriptions + images)
through its DataTables POST endpoint. Usage: python nfa.py term... -> nfa_hits.json"""
import re,sys,json,time,urllib.request,urllib.parse,http.cookiejar,os
cj=http.cookiejar.CookieJar(); op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
UA={'User-Agent':'Mozilla/5.0'}
s=op.open(urllib.request.Request('https://nouvelle-france.org/eng/item/search',headers=UA),timeout=40).read().decode('utf8')
tok=re.search(r"'RequestVerificationToken': '([^']+)'",s).group(1)
cols=['keyword','title','series','date','repository','fond']
def q(kw,start=0,n=100):
    d={'draw':'1','start':str(start),'length':str(n)}
    for i,c in enumerate(cols):
        d[f'columns[{i}][data]']=c; d[f'columns[{i}][name]']=c.capitalize()
        d[f'columns[{i}][searchable]']='true'; d[f'columns[{i}][orderable]']='true'
        d[f'columns[{i}][search][value]']=kw if i==0 else ''; d[f'columns[{i}][search][regex]']='false'
    d['order[0][column]']='3'; d['order[0][dir]']='asc'; d['search[value]']=''; d['search[regex]']='false'
    r=urllib.request.Request('https://nouvelle-france.org/eng/item/search',data=urllib.parse.urlencode(d).encode(),
        headers={**UA,'RequestVerificationToken':tok,'X-Requested-With':'XMLHttpRequest','Content-Type':'application/x-www-form-urlencoded'})
    return json.loads(op.open(r,timeout=60).read().decode('utf8'))
here=os.path.dirname(os.path.abspath(__file__)); fn=os.path.join(here,'nfa_hits.json')
allh=json.load(open(fn,encoding='utf8')) if os.path.exists(fn) else {}
for term in sys.argv[1:]:
    rows=[]; start=0
    while True:
        j=q(term,start)
        rows+=j.get('data',[]); tot=j.get('recordsFiltered',0)
        start+=100
        if start>=tot or start>=1000: break
        time.sleep(1)
    print(f'## {term}: {tot}')
    for r in rows[:60]:
        print('  ',re.sub('<[^>]+>','',str(r.get('date')))[:12],'|',re.sub('<[^>]+>','',str(r.get('title')))[:130],'|',re.sub('<[^>]+>','',str(r.get('fond')))[:40])
    allh[term]=rows; time.sleep(1)
json.dump(allh,open(fn,'w',encoding='utf8'),ensure_ascii=False,indent=1)
