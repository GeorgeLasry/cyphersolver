"""Grep the Newberry Transcribe bulk dump (dl/nt_bulk.json, 150 MB, git-ignored) for cipher terms; writes nt_bulk_hits.json and prints counts per term and per title."""
import json,re,collections
d=json.load(open('dl/nt_bulk.json',encoding='utf8'))['transcriptions']
print(len(d),'pages',len({x['title'] for x in d}),'titles')
T={'cipher':r'cipher','cypher':r'cypher','decipher/decypher':r'de[cs]ipher|decypher','cryptogr':r'cryptogr','secret code/writing':r'secret (code|writ|alphabet|cipher)','invisible/sympathetic ink':r'(invisible|sympathetic) ink','in code':r'\bin code\b|code (letter|message|word|book)','cifra/cifrado':r'\bcifra|\ben cifra|\bcifrad|\bcifre','chiffr':r'chiffr|chifr','nomenclat':r'nomenclat','Geheimschrift':r'geheimschrift|geheimsprache|chiffri','szyfr/šifr':r'szyfr|šifr|sifr','telegraphic code':r'telegraphic code|code telegram|cipher telegram'}
cnt={k:0 for k in T}; hits=[]
for x in d:
    t=(x.get('transcription') or '')+' '+(x.get('translation') or '')
    got=[k for k,p in T.items() if re.search(p,t,re.I)]
    for k in got: cnt[k]+=1
    if got: hits.append({'title':x['title'],'date':x.get('date'),'permalink':x['permalink'],'terms':got,'ctx':[t[max(0,m.start()-150):m.end()+200].replace('\n',' ') for m in [re.search(T[got[0]],t,re.I)]]})
print(cnt); json.dump({'counts':cnt,'n_pages':len(d),'hits':hits},open('nt_bulk_hits.json','w'),ensure_ascii=False,indent=1)
