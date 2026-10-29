import re,glob,os,json
rx=re.compile(r'(?i)(in|part|partly|mostly|entirely|largely|all|nearly all|and|the|italics are|italic|first part|and larger part)[\s,]+(cipher|cypher)[s]?[,;]?\s*(undeciphered|not\s+deciphered|undecyphered|not\s+decyphered|unread|not\s+yet\s+deciphered)|(cipher|cypher)s?\s+(undeciphered|undecyphered|not\s+deciphered)|(in|part)\s+(cipher|cypher)\.?\s*\(?no (decipher|key)')
out=[]
for f in sorted(glob.glob('_txt/*.txt')):
    t=open(f,encoding='utf-8',errors='replace').read()
    t=re.sub(r'[ \t]+',' ',t)
    last=-1000
    for m in rx.finditer(t):
        if m.start()-last<400: continue
        last=m.start()
        out.append({'f':os.path.basename(f)[:-4],'pos':m.start(),'ctx':re.sub(r'\s+',' ',t[max(0,m.start()-420):m.end()+160])})
json.dump(out,open('cal_hits.json','w'),ensure_ascii=False)
from collections import Counter
print(len(out),Counter(o['f'] for o in out).most_common(80))
