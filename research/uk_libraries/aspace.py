import re,json,sys,html,time
from net import get
TERMS=['cipher','cypher','ciphers','decipher','deciphered','enciphered','ciphered','"in cipher"','"in cypher"','"in code"','"secret writing"','"key to the cipher"','cryptogram','cryptographic','nomenclator','"secret characters"','"secret alphabet"','"cypher key"','"cipher key"','"in figures"','coded','encoded','chiffre','cifra','"secret hand"','"secret language"','"private cipher"','"cipher letter"','"letter in cipher"','steganography','"deciphered by"','"decipher of"','"decypher"','"decyphered"','"cyphers"','"cyphered"','"in characters"']
def strip(s): return html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',s))).strip()
def run(base,name,terms=TERMS,maxpages=40):
    out={}
    for t in terms:
        p=1
        while p<=maxpages:
            r=get(base+'/search',params={'q[]':t,'op[]':'','field[]':'','page':p})
            if r.status_code!=200: print(name,t,p,'status',r.status_code);break
            rows=re.findall(r'<div class="recordrow.*?(?=<div class="recordrow|<div class="pagination|</main>|$)',r.text,flags=re.S)
            tot=re.search(r'of ([\d,]+)',strip(r.text[r.text.find('Showing Results'):][:200])) if 'Showing Results' in r.text else None
            n=0
            for row in rows:
                m=re.search(r'href="(/repositories/\d+/[a-z_]+/\d+)"[^>]*>(.*?)</a>',row,flags=re.S)
                if not m: continue
                n+=1
                ident=re.search(r'class="component">(.*?)</span>',row,flags=re.S)
                d=out.setdefault(m.group(1),{'uri':base+m.group(1),'title':strip(m.group(2)),'id':strip(ident.group(1)) if ident else '', 'text':strip(row)[:1500],'terms':[]})
                if t not in d['terms']: d['terms'].append(t)
            total=int(tot.group(1).replace(',','')) if tot else 0
            print(name,t,p,total,len(out),flush=True)
            if n==0 or p*10>=total and p*25>=total: break
            p+=1
            time.sleep(0.5)
    rx=re.compile(r'ciph|cyph|crypto|secret writ|secret char|secret alph|nomenclat|in code|in figures|chiffr|cifra|steganog|encod|coded',re.I)
    out={k:v for k,v in out.items() if rx.search(v['text']+v['title'])}
    json.dump(out,open(f'raw_{name}.json','w'),ensure_ascii=False,indent=0)
    return out
if __name__=='__main__':
    run(sys.argv[1],sys.argv[2])
