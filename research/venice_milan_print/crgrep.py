import re,sys,glob,html
pat=re.compile(sys.argv[1],re.I)
ctx=int(sys.argv[2]) if len(sys.argv)>2 else 200
for f in sorted(glob.glob(sys.argv[3] if len(sys.argv)>3 else 'cr_*.htm')):
    t=open(f,'rb').read().decode('utf-8','replace')
    t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
    for m in pat.finditer(t):
        print(f, '::', t[max(0,m.start()-ctx):m.end()+ctx]); print()
