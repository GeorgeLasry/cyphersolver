import re,glob,json,os
CW=re.compile(r'\b(?:in\s+)?(?:cipher|cypher|ciphers|cyphers|chiffre|chiffres|cifra|cifre|Chiffre)\b',re.I)
DR=re.compile(r'(?<![\w])\d{1,4}(?:[\s.,;:\-]+\d{1,4}){7,}')
meta={r['id']:r for r in json.load(open('gut_sel3.json',encoding='utf8'))}
out=[]
for fn in sorted(glob.glob('.work/gut/*.txt')):
    t=open(fn,encoding='utf8',errors='ignore').read()
    i=os.path.basename(fn)[:-4]
    n=0
    for m in CW.finditer(t):
        w=t[max(0,m.start()-300):m.end()+700]
        d=DR.search(w)
        if d and not re.search(r'1[3-9]\d\d\D{1,3}1[3-9]\d\d',d.group(0)):
            out.append({'id':i,'title':meta.get(i,{}).get('title',''),'ctx':re.sub(r'\s+',' ',w)}); n+=1
            if n>=5: break
json.dump(out,open('gut_hits.json','w',encoding='utf8'),ensure_ascii=False)
print(len(out))
import collections
for k,v in collections.Counter((o['id'],o['title'][:60]) for o in out).items(): print(k,v)
