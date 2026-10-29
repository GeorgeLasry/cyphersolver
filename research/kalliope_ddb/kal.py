import sys,urllib.request,urllib.parse,re,json,time
def q(query,start=1,n=1,schema='mods'):
    u='https://kalliope-verbund.info/sru?'+urllib.parse.urlencode({'version':'1.2','operation':'searchRetrieve','query':query,'maximumRecords':n,'startRecord':start,'recordSchema':schema})
    for i in range(3):
        try:
            return urllib.request.urlopen(u,timeout=60).read().decode('utf8')
        except Exception as e: err=e; time.sleep(2)
    return 'ERR '+str(err)
if __name__=='__main__':
    for qq in sys.argv[1:]:
        t=q(qq); m=re.search(r'numberOfRecords>(\d+)',t); d=re.search(r'diag:message>([^<]*)',t)
        print(qq,'->',m and m.group(1), d and d.group(1), t[:80] if 'ERR' in t else '')
