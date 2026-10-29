"""CHM finding aids (CONTENTdm alias chm_fa on collections.carli.illinois.edu), plus all CHM-held CARLI collections. Full-text term search."""
import subprocess,json,time,urllib.parse,sys
terms=["cipher","cypher","ciphered","in cipher","decipher","deciphered","cryptogram","code message","code telegram","code book","codebook","coded","secret writing","secret code","invisible ink","Confederate cipher","signal code","Northwest Conspiracy","cryptograph","secret ink","encoded","enciphered","cypher key"]
def q(alias,t,mode="all"):
    u="https://collections.carli.illinois.edu/digital/api/search/collection/%s/searchterm/%s/field/all/mode/%s/conn/and/maxRecords/100"%(alias,urllib.parse.quote(t),mode)
    r=subprocess.run(["curl","-sL","-m","60","-A","Mozilla/5.0",u],capture_output=True).stdout
    try: return json.loads(r)
    except Exception: return None
res={}
for alias in sys.argv[1:]:
    for t in terms:
        d=q(alias,t); time.sleep(3)
        if d is None: print(alias,t,"ERR"); continue
        res[(alias+"|"+t)]=[(i['collectionAlias'],i['itemId'],i['title']) for i in d['items']]
        print(alias,"|",t,d['totalResults'],flush=True)
json.dump(res,open("chm_cdm_%s.json"%"_".join(sys.argv[1:]),"w"),indent=1)
