import json,re
d=json.load(open('kal_hits.json',encoding='utf8'))['recs']
pat=re.compile(r'chiffr|geheimschr|geheimzeich|geheimalph|geheimtint|kryptogr|cryptogr|ciphe|cifr|cijfer|cifer|ontcijfer|dechiffr|déchiffr|ziffern|\bin notis|nomenclat|nomenklat|verschl[üu]ssel|decifr|geheimsprach',re.I)
keep=[]
for r in d:
    t=' || '.join([r['title']]+r['notes']+r['abstract']+r['parent'])
    m=pat.findall(t)
    if m: r['m']=sorted(set(x.lower() for x in m)); r['txt']=t; keep.append(r)
print(len(d),len(keep))
json.dump(keep,open('kal_kept.json','w',encoding='utf8'),ensure_ascii=False,indent=0)
for r in keep:
    print(r['id'].split('/')[-1],'|',(r['inst'] or [''])[0][:25],'|',';'.join(r['date'])[:12],'|',r['title'][:150].replace('\n',' '),'|',r['m'])
