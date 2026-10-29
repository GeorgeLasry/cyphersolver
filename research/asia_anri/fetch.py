import requests, sys
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36','Accept-Language':'en'}
S=requests.Session(); S.headers.update(UA)
def get(u,**kw):
    r=S.get(u,timeout=60,**kw); return r
if __name__=='__main__':
    r=get(sys.argv[1]); print(r.status_code, r.url); sys.stdout.buffer.write(r.content[:int(sys.argv[2]) if len(sys.argv)>2 else 100000])
