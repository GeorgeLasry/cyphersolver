import json,os,sys
from tna import q
H="hits.jsonl"
seen=set()
if os.path.exists(H):
    for l in open(H,encoding="utf8"): seen.add(json.loads(l)["id"])
out=open(H,"a",encoding="utf8")
log=open("harvest.log","a",encoding="utf8")
KEEP=["id","reference","title","description","coveringDates","startDate","endDate","numStartDate","numEndDate","department","heldBy","context","catalogueLevel","source","note"]
def run(term,dept=None):
    page=1;tot=0;new=0
    while True:
        p={"sps.searchQuery":term,"sps.dateFrom":"1350-01-01","sps.dateTo":"1950-12-31","sps.resultsPageSize":100,"sps.page":page}
        if dept: p["sps.departments"]=dept
        j=q(**p)
        if not j or not j["records"]: break
        for r in j["records"]:
            tot+=1
            if r["id"] in seen: continue
            seen.add(r["id"]);new+=1
            d={k:r.get(k) for k in KEEP};d["term"]=term
            out.write(json.dumps(d,ensure_ascii=False)+"\n")
        out.flush()
        if len(j["records"])<100 or page>=100: break
        page+=1
    msg=f"{term!r} dept={dept} count={j and j.get('count')} fetched={tot} new={new}"
    print(msg);log.write(msg+"\n");log.flush()
terms=['cipher','cypher','ciphers','cyphers','"in cipher"','"in cypher"','"in ciphers"','"in cyphers"','ciphered','cyphered','enciphered','encyphered','decipher','decypher','deciphered','decyphered','deciphering','decyphering','decipherment','"key to the cipher"','"key to the cypher"','"key of the cipher"','"cipher key"','"cypher key"','"partly in cipher"','"partly in cypher"','"part in cipher"','"in part in cipher"','"in secret characters"','"in characters"','"in figures"','"in numbers"','"in numeral"','"in code"','cryptogram','cryptographic','cryptography','nomenclator','nomenclature','"secret writing"','"secret alphabet"','"secret code"','"cipher alphabet"','"alphabet of cipher"','"table of cipher"','"in a cipher"','"in a cypher"','"in the cipher"','"in the cypher"','"in cifra"','"en chiffre"','"en chiffres"','"cifra"','chiffre','"in cypher"','"in cyphers"','"cipher letter"','"letter in cipher"','"despatch in cipher"','"dispatch in cipher"','"written in cipher"','"written in cypher"','"ciphered letter"','"ciphered despatch"','cryptic','"secret cipher"','"cipher message"','"cipher telegram"','"cipher book"','"cipher code"']
if __name__=="__main__":
    for t in terms: run(t)
