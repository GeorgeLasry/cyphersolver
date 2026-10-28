"""Hit counts per term on loc.gov /manuscripts/ (c=1 requests). Writes counts.json."""
import json, os, sys, urllib.parse
import locapi
HERE = os.path.dirname(os.path.abspath(__file__))
TERMS = ['cipher', 'cypher', 'ciphered', 'cyphered', 'ciphers', 'cyphers', 'decipher', 'deciphered', 'decypher',
         'decyphered', 'undeciphered', '"in cipher"', '"in cypher"', '"in code"', 'cryptogram', 'cryptograph',
         'cryptography', '"secret writing"', '"invisible ink"', '"sympathetic ink"', 'nomenclator', 'chiffre',
         'chiffres', 'cifra', 'cifrado', 'geheimschrift', '"code telegram"', '"cipher telegram"', '"cipher key"',
         '"code book"', '"cipher book"', 'decoded', 'decode', 'encoded', 'steganography', '"secret code"',
         '"telegraph code"', '"private code"', '"cipher dispatch"', '"cipher despatch"', '"key to the cipher"']
out = {}
p = os.path.join(HERE, 'counts.json')
if os.path.exists(p):
    out = json.load(open(p, encoding='utf-8'))
for t in (sys.argv[1:] or TERMS):
    if t in out: continue
    d = locapi.get('https://www.loc.gov/manuscripts/?' + urllib.parse.urlencode({'q': t, 'fo': 'json', 'c': 1}))
    r = d['results'][0]['id'] if d and d.get('results') else None
    out[t] = {'total': d['pagination']['of'] if d else None, 'first': r}
    print(t, out[t], flush=True)
    json.dump(out, open(p, 'w', encoding='utf-8'), indent=1)
