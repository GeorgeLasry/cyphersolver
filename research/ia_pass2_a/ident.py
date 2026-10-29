import glob,os,re
T="C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/9b550102-0a57-408e-82db-2b82e44e748c/scratchpad/p2txt"
for p in sorted(glob.glob(T+"/*.txt")):
    t=open(p,encoding="utf8",errors="replace").read()
    h=re.sub(r"\s+"," ",t[:6000])
    m=re.search(r"(?i)(VOL(?:UME)?\.?\s*[IVXL0-9]+|PART\s+[IVXL0-9]+)",h)
    yrs=re.findall(r"1[5-7]\d\d",h)[:4]
    k=re.search(r"(?i)(venice|venetian|spain|salisbury|foreign|domestic|milan|rome)",h)
    print(os.path.basename(p)[:-4],len(t)//1000,"k",(k.group(1) if k else "-"),(m.group(1) if m else "-"),yrs)
