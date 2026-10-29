import json,requests,time,os
UA={'User-Agent':'cyphersolver-research/1.0 (dnbourdeau@gmail.com; research, low rate)'}
s=json.load(open('gut_sel3.json',encoding='utf8'))
os.makedirs('.work/gut',exist_ok=True)
for r in s:
    fn=f".work/gut/{r['id']}.txt"
    if os.path.exists(fn): continue
    for u in (f"https://www.gutenberg.org/cache/epub/{r['id']}/pg{r['id']}.txt",f"https://www.gutenberg.org/files/{r['id']}/{r['id']}-0.txt"):
        try:
            x=requests.get(u,headers=UA,timeout=60)
            if x.status_code==200:
                open(fn,'wb').write(x.content); break
        except Exception as e: time.sleep(3)
    time.sleep(1.0)
print('done')
