import json,re,sys
CW=re.compile(r'cipher|cypher|chiffr|cifr|cijfer|Chiffre|Geheimschrift|Ziffern|cifra',re.I)
# digit-string runs: >=8 numbers separated by punctuation/space (not simple year lists/page lists)
DR=re.compile(r'(?<![\w])\d{1,4}(?:[\s.,;:\-·|/]+\d{1,4}){7,}')
SYM=re.compile(r'[Ͱ-Ͽ∀-⋿☀-➿←-⇿■-◿ɐ-ʯ]{6,}')
rows=[]
for l in open('.work/pages.jsonl',encoding='utf8'):
    p=json.loads(l); t=p['text']
    hits=[]
    for m in CW.finditer(t):
        a=max(0,m.start()-500); b=min(len(t),m.end()+800)
        w=t[a:b]
        d=DR.search(w)
        if d and not re.search(r'\b1[3-9]\d\d\b[\s,.;-]+\b1[3-9]\d\d\b',d.group(0)[:30]): hits.append((m.group(0),w))
    if hits: rows.append({'lang':p['lang'],'title':p['title'],'n':len(hits),'ctx':hits[0][1],'len':len(t)})
json.dump(rows,open('page_hits.json','w',encoding='utf8'),ensure_ascii=False)
print(len(rows))
for r in rows: print(r['lang'],r['title'],r['n'])
