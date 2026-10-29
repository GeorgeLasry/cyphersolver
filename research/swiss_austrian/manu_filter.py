import json,re,sys
weak={'nomenclator','nomenclatura','Nomenklator','Schlüssel','schlüssel','Ziffer','Ziffern','klíč','klíč k šifře','Schlüssel zur','cipher','cypher','Notenschrift','Zeichenschrift'}
rows={}
for l in open('manu_hits.jsonl',encoding='utf-8'):
    d=json.loads(l); r=rows.setdefault(d['ID'],{'d':d,'terms':set(),'snips':[]})
    t=d['_term']; r['terms'].add(t)
    g=' | '.join(x for x in d.get('globIndex',[]) if isinstance(x,str))
    for m in list(re.finditer(re.escape(t.rstrip('*')),g,re.I))[:2]:
        r['snips'].append(g[max(0,m.start()-120):m.end()+120])
def yr(d):
    m=re.findall(r'(\d{4})',str(d.get('origDateFrom_sort')));return int(m[0]) if m else None
out=[]
for k,r in rows.items():
    if not (r['terms']-weak): continue
    d=r['d'];t=(d.get('dcTitle') or [''])[0]
    out.append((str((d.get('dcSource') or [''])[0]),yr(d),k,t[:140],sorted(r['terms']-weak),r['snips'][0].replace('\n',' ') if r['snips'] else ''))
out.sort(key=lambda x:(x[0],x[1] or 0))
with open('manu_strong.tsv','w',encoding='utf-8') as f:
    for o in out: f.write('\t'.join(map(str,o))+'\n')
print(len(rows),len(out))
