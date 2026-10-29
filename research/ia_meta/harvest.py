import requests, json, time, re
terms = ['cipher','cypher','ciphers','chiffre','chiffré','chiffrée','"en chiffres"','"en chiffre"','chiffrierte','chiffrirte','geheimschrift','cifra','cifrado','cifrata','cifrada','cifrato','kryptogram','undeciphered','uncracked','"in cipher"','"in cypher"','nomenclator','"secret writing"','"code letter"','steganography','cryptogram','cryptographic','zifferschrift','"cijferschrift"','cijfer','"in cijfer"','cifre','"lettere cifrate"','"cartas en cifra"','"carta en cifra"','"secret correspondence"','decipher','deciphered','deciphering','"secret alphabet"','"secret code"','"cipher diary"','"cipher letter"','"cipher despatch"','"cipher dispatch"','"lettres chiffrées"','"geheime schrift"','"in cifra"','"en clave"','"cipher manuscript"','"secret cipher"','"code book"','"cryptographie"','kryptografi','szyfr','"chiffer"','"chiffre-schrift"','cifrario','"clave"','cryptography']
seen = {}
try: seen = json.load(open('raw_hits.json'))
except: pass
def run(q, extra=''):
    rows=[]
    for page in (1,2):
        try:
            r = requests.get('https://archive.org/advancedsearch.php', params={'q': q, 'fl[]': ['identifier','title','date','creator','collection','description','mediatype','language'], 'rows': 100, 'page': page,'output': 'json'}, timeout=90)
            d = r.json()['response']
        except Exception as e:
            print('ERR', q, e); break
        rows += d['docs']
        if len(rows) >= d['numFound']: break
        time.sleep(0.6)
    return rows
for t in terms:
    for fld in ('title','subject','description'):
        q = f'{fld}:({t}) AND mediatype:texts AND date:[1350-01-01 TO 1950-12-31]'
        rows = run(q)
        new=0
        for x in rows:
            if x['identifier'] not in seen:
                seen[x['identifier']] = x; x['q']=f'{fld}:{t}'; new+=1
        print(fld, t, len(rows), new, flush=True)
        time.sleep(0.6)
    json.dump(seen, open('raw_hits.json','w'))
