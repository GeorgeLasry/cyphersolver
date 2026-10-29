import urllib.request as u,sys
def g(url,n=400):
    try:
        r=u.urlopen(u.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25);b=r.read().decode('utf8','replace');print(url,r.status,len(b));print(b[:n].replace('\n',' '));print()
    except Exception as e: print(url,'ERR',e)
for a in sys.argv[1:]: g(a)
