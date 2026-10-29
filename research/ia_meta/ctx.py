import sys,re
f,pat,b,a=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4])
t=re.sub(r'\s+',' ',open(f'_txt/{f}.txt',encoding='utf-8',errors='replace').read())
for m in list(re.finditer(pat,t))[:2]:
    print('>>',t[max(0,m.start()-b):m.end()+a],'\n')
