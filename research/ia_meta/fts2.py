import requests, json, re, time
ids=json.load(open('cal_ids.json'))
phr=['"not deciphered" cipher','"in cipher, not deciphered"','"in cypher, not deciphered"','"cypher, not deciphered"','"cipher, undeciphered"','"cipher not deciphered"','"cypher not deciphered"','"undeciphered" cipher letter','"no key" cipher letter calendar','"in cipher" "not decyphered"','"cipher" "undecyphered"','"cypher, undeciphered"','"in cipher; not deciphered"','"in cipher, unread"','"in cipher, not decyphered"','"in cipher, undeciphered"','"remains undeciphered" cipher','"cipher" "has not been deciphered" calendar','"cipher" "not yet deciphered"','"unsolved cipher"','"cipher letter" "illegible"','"in cipher" "no decipher"','"without decipher" cipher','"decipher wanting"','"no decipher" cipher','"cipher" "decipher not"']
hit={}
for p in phr:
    for frm in (0,100):
        try:
            r=requests.get('https://be-api.us.archive.org/fts/v1/search',params={'q':p,'size':100,'from':frm},timeout=90).json()
        except Exception as e: print('ERR',p,e);break
        hs=r['hits']['hits']
        for x in hs:
            ident=x['_id'].split('|')[0]
            for s in x['highlight']['text']:
                hit.setdefault(ident,[]).append(re.sub(r'\s+',' ',s))
        if len(hs)<100: break
        time.sleep(0.7)
    print(p,r['hits']['total'],len(hit),flush=True)
    time.sleep(0.7)
json.dump(hit,open('fts_hits.json','w'))
