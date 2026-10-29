import re,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8',errors='replace')
S='C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/9b550102-0a57-408e-82db-2b82e44e748c/scratchpad/txt/inventairedesarc00cauc.txt'
t=re.sub(r'\s+',' ',open(S,encoding='utf8',errors='ignore').read())
pat=re.compile(r'sans déchiffré|non déchiffr|déchiffré (?:est perdu|manque)|chiffrées?, sans|le déchiffré (?:est )?perdu|déchiffré a disparu|sans clef',re.I)
last=0
for m in pat.finditer(t):
    p=m.start()
    if p-last<150: continue
    last=p
    fs=[x for x in re.finditer(r'Fascio (\d{2,4})\b',t[:p])]
    fno=fs[-1].group(1) if fs else '?'
    ent=re.search(r'\[\s*([\dIil\s]{2,6})\s*\]',t[p:p+500])
    st=max(t.rfind('. [',0,p),p-420)
    print('F%s ent%s @%d: %s\n'%(fno,ent.group(1) if ent else '?',p,t[st:p+160]))
