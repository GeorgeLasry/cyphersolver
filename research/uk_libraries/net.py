import requests, time
S=requests.Session(); S.headers['User-Agent']='Mozilla/5.0 (cyphersolver research; dnbourdeau@gmail.com)'
def get(url,**kw):
    err=''
    for i in range(3):
        try:
            return S.get(url,timeout=40,**kw)
        except Exception as e:
            err=str(e); time.sleep(2)
    class R: status_code=0; text=''; content=b''
    R.err=err; return R
