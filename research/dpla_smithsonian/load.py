import json,glob,re
def load():
    d={}
    for f in sorted(glob.glob('hits/part-*.jsonl')):
        for l in open(f,encoding='utf8'):
            x=json.loads(l); d[x['id']]=x
    return d
STRONG=re.compile(r'\b(in cipher|in cypher|in code|ciphered|cyphered|enciphered|cipher letter|cypher letter|cipher key|key to (the )?(cipher|cypher)|cipher message|cryptogram|secret writing|coded (letter|message|telegram|dispatch|document|writing)|written in (cipher|code|cypher)|deciphered|cipher alphabet|secret alphabet|cipher code|code letter|letter in code|cipher telegram|cipher dispatch|cipher book|cypher book|code book|codebook|secret code|secret cipher|cryptograph)\b',re.I)
def text(x): return ' ; '.join(x['title']+x['desc']+x['subject'])
def year(x):
    for dd in x['date']:
        m=re.search(r'\b(1[0-9]{3}|20[0-2][0-9])\b',dd)
        if m: return int(m.group(1))
    return None
def hub(x):
    i=x['_id']; return i.split('--')[0] if '--' in i else ('ohio' if 'ohio' in i else i[:20])
CORE=re.compile(r'cipher|cypher|cryptogra|secret writ|in code\b|coded\b|code ?book|secret alphabet|encipher',re.I)
NOISE=re.compile(r'indecipher|undecipher|illegible|\bcipher(ing)? (book|slate)|ciphering|arithmetic|monogram|royal cipher|cipher of',re.I)
