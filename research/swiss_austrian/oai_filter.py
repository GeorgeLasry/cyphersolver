import json,re,glob,sys
rx=re.compile(r'chiffr|chifr|cifr|geheimschr|geheimschrift|ziffernschr|dechiffr|kryptogr|geheimsprache|geheimalphabet|geheimzeichen|code secret|écriture secrète|ecriture secrete|secret writing|cipher|cypher|geheim ?schrift|verschl[üu]ssel|schlüsselschrift',re.I)
seen={};
for f in sorted(glob.glob(sys.argv[1] if len(sys.argv)>1 else 'raw/em_*.jsonl')):
    for l in open(f,encoding='utf-8'):
        d=json.loads(l)
        txt=' | '.join(' '.join(v) for k,v in d.items() if isinstance(v,list))
        m=rx.search(txt)
        if m and d['oai_id'] not in seen:
            d['_ctx']=txt[max(0,m.start()-150):m.end()+150]; d['_f']=f; seen[d['oai_id']]=d
json.dump(list(seen.values()),open('oai_hits_%s.json'%('em' if len(sys.argv)<2 else sys.argv[2]),'w',encoding='utf-8'),ensure_ascii=False,indent=0)
print(len(seen))
for d in seen.values(): print(d['oai_id'].split(':')[-1],'|',(d.get('title') or [''])[0][:70],'|',(d.get('date') or [''])[:1],'|',d['_ctx'].replace('\n',' ')[:260])
