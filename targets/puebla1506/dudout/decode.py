# Decrypts transcription.tsv with Satoshi Tomokiyo's table of Puebla's First Cipher (Cryptiana) plus our additions.
import sys,re,random,math,json,html,collections
KEY_T={'q':'a','M':'a','o':'u','p':'b','C':'c','d':'d','+':'e','t':'e','g':'f','f':'g','a':'h','b':'i','5':'i','e':'l','m':'m','n':'n','z':'o','U':'p','Q':'q','r':'r','s':'s','R':'t'}
ADD={'Z':'z','k':'n'}   # our additions to Tomokiyo's table (5 = i is his variant)
ADDED_FLAG={'Z','k','5'}
rows=[l.rstrip('\n').split('\t') for l in open('transcription.tsv') if not l.startswith('#') and l.strip()]
def dec(signs,key):
    return ''.join(key.get(s,'?') if s!='|' else '' for s in signs)
key=dict(KEY_T);key.update(ADD)
tot=0;unk=0;added=0;out=[]
for sid,lin,sg in rows:
    s=sg.split(); tot+=sum(1 for x in s if x!='|'); unk+=s.count('?'); added+=sum(1 for x in s if x in ADDED_FLAG)
    out.append((sid,lin,dec(s,key)))
for o in out: print('\t'.join(o))
print(f'\ncipher signs: {tot}; illegible ?: {unk}; read: {(tot-unk)/tot:.3f}; through our additions (Z,k,5): {added}')
