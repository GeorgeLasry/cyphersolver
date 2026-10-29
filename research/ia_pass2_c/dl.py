import json,sys,os,urllib.request,concurrent.futures as cf
OUT=sys.argv[1]; os.makedirs(OUT,exist_ok=True)
ids=[x[0] for x in json.load(open(sys.argv[2]))]
def go(i):
    p=os.path.join(OUT,i+'.txt')
    if os.path.exists(p): return i,'have'
    try:
        r=urllib.request.urlopen(urllib.request.Request(f'https://archive.org/download/{i}/{i}_djvu.txt',headers={'User-Agent':'Mozilla/5.0'}),timeout=120)
        b=r.read(40_000_000)
        open(p,'wb').write(b); return i,len(b)
    except Exception as e: return i,str(e)[:40]
with cf.ThreadPoolExecutor(6) as ex:
    for i,r in ex.map(go,ids): print(i,r,flush=True)
