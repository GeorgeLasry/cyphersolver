"""Sweep ALL CARLI CONTENTdm collections via alias 'all' (dmQuery, all fields incl. full text), paginated, 3 s delay.
Writes ida_all_hits.jsonl (every record) and ida_counts.jsonl (term totals)."""
import json, sys, time, requests
UA = {'User-Agent': 'cyphersolver research (catalogue sweep)'}
B = 'https://idaillinois.org/digital/bl/dmwebservices/index.php?q='
TERMS = ['cipher','cypher','ciphered','in cipher','decipher','cryptogram','cryptography','code message','code telegram','code book','coded','secret writing','secret code','invisible ink','nomenclator','chiffre','cifra','Geheimschrift','szyfr','šifra','šifruotas','chiffriert']
def get(u):
    for i in range(3):
        try:
            r = requests.get(u, headers=UA, timeout=90)
            if r.status_code in (403, 429): sys.exit('STOP %s' % r.status_code)
            return r.json()
        except Exception as e:
            time.sleep(5)
    return None
cnt = open('ida_counts.jsonl', 'a', encoding='utf-8'); hits = open('ida_all_hits.jsonl', 'a', encoding='utf-8')
for t in TERMS:
    start = 1; tot = None
    while True:
        u = f'{B}dmQuery/all/CISOSEARCHALL^{t.replace(" ","+")}^all^and/title!date!descri/nosort/200/{start}/0/0/0/0/json'
        d = get(u); time.sleep(3)
        if d is None: print('ERR', t, start); break
        tot = int(d.get('pager', {}).get('total', 0))
        for x in d.get('records', []):
            x['term'] = t; hits.write(json.dumps(x, ensure_ascii=False) + '\n')
        hits.flush()
        n = len(d.get('records', []))
        if n == 0 or start + n > tot or start > 1500: break
        start += n
    cnt.write(json.dumps({'term': t, 'total': tot}, ensure_ascii=False) + '\n'); cnt.flush()
    print(t, tot, flush=True)
