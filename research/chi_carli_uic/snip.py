import sys,json,re,requests,time
host=sys.argv[1]; alias=sys.argv[2]; ptr=sys.argv[3]; pat=sys.argv[4] if len(sys.argv)>4 else r'ci?y?pher|cryptogram|secret|code'
B=f'https://{host}/digital/bl/dmwebservices/index.php?q='
d=requests.get(f'{B}dmGetItemInfo/{alias}/{ptr}/json',headers={'User-Agent':'cyphersolver research'},timeout=60).json()
print({k:str(v)[:120] for k,v in d.items() if k in('title','titla','date','creato','descri','subjec','source','collec','format')})
t=' '.join(str(v) for k,v in d.items() if k in('full','text','transc'))
print(len(t))
for m in list(re.finditer(pat,t,re.I))[:4]:
    print('   ...',t[max(0,m.start()-200):m.end()+200].replace('\n',' '))
time.sleep(3)
