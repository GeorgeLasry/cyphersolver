import requests,sys
H={'User-Agent':'Mozilla/5.0 (research sweep; cyphersolver)'}
urls=sys.argv[1:]
for u in urls:
    try:
        r=requests.get(u,headers=H,timeout=30)
        print(r.status_code,r.headers.get('content-type'),len(r.text),u)
        print(r.text[:600].replace('\n',' '))
    except Exception as e: print('ERR',u,e)
