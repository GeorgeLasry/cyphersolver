"""Europeana title/description sweep for ciphertexts. Writes hits.jsonl (one raw item per line, deduped by id).
    PYTHONUTF8=1 python harvest.py
Public demo key; paging by cursor. Terms are phrase queries in the languages of the European cipher record."""
import json, sys, time, urllib.parse, urllib.request
KEY = 'api2demo'
TERMS = ['parcialmente cifrada','totalmente cifrada','cifrada','texto cifrado','en cifra','con cifra','descifrado','descifrada','descifrar','cifra de','clave de cifra','carta cifrada','carta en cifra','documento cifrado','carta en clave','escritura cifrada','escritura secreta','in Geheimschrift','Geheimschrift Brief','chiffrierter Brief','chiffrierte','Chiffrenschlüssel','Geheimschlüssel','lettre chiffrée','lettre en chiffres','déchiffrée','alphabet secret','écriture secrète','cypher letter','letter in cipher','secret writing','secret alphabet','lettera cifrata','cifrata','scrittura segreta','lettre en chiffre','dépêche chiffrée','tajne pismo','šifrované','šifrovaná','tajné písmo','szyfrem','pismo tajne','brief in cijfer','cijferschrift','geheim schrift','cifrada con','cifras secretas']
FILT = ['TYPE:TEXT', 'TYPE:IMAGE']
def get(params):
    url = 'https://api.europeana.eu/record/v2/search.json?' + urllib.parse.urlencode(params, doseq=True)
    for i in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return json.load(r)
        except Exception as e:
            time.sleep(2 + i * 3)
    return None
seen = {}
for l in open('hits.jsonl',encoding='utf8'):
    o=json.loads(l); seen[o['id']]=o
try:
    for l in open('hits2.jsonl', encoding='utf8'):
        o = json.loads(l); seen[o['id']] = o
except FileNotFoundError:
    pass
out = open('hits2.jsonl', 'a', encoding='utf8')
log = {}
for t in TERMS:
    q = '"%s"' % t
    cur, n = '*', 0
    while cur and n < 2000:
        d = get({'wskey': KEY, 'query': q, 'qf': FILT[:1] if False else ['YEAR:[1300 TO 1950]'], 'rows': 100,
                 'cursor': cur, 'profile': 'standard'})
        if not d or not d.get('success'):
            break
        for it in d.get('items', []):
            if it['id'] in seen:
                seen[it['id']].setdefault('terms', [])
                continue
            it['terms'] = [t]
            seen[it['id']] = it
            out.write(json.dumps(it, ensure_ascii=False) + '\n')
        out.flush()
        n += len(d.get('items', []))
        cur = d.get('nextCursor')
    log[t] = n
    print(t, n, len(seen), flush=True)
json.dump(log, open('harvest2_counts.json', 'w'))
