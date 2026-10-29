import urllib.request, urllib.parse, json, time, sys
terms=["cipher","cypher","ciphered","\"in cipher\"","decipher","deciphered","cryptogram","cryptograph*","\"code message\"","\"code telegram\"","\"code book\"","coded","\"secret writing\"","\"secret code\"","\"invisible ink\"","\"sympathetic ink\"","nomenclator","chiffre","cifra","\"en cifra\"","Geheimschrift","szyfr","encoded","\"secret alphabet\""]
out={}
for t in terms:
    for model in ["works"]:
        q=urllib.parse.quote(t)
        url=f"https://api.dc.library.northwestern.edu/api/v2/search/works?query={q}&size=100"
        try:
            r=json.load(urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 research"}),timeout=60))
        except Exception as e:
            print(t,"ERR",e); continue
        tot=r["pagination"]["total_hits"]
        out[t]={"total":tot,"items":[{"id":d["id"],"title":d.get("title"),"date":d.get("date_created"),"coll":d.get("collection",{}).get("title") if isinstance(d.get("collection"),dict) else d.get("collection"),"desc":(d.get("description") or [""])[0][:300] if d.get("description") else "","acc":d.get("accession_number")} for d in r["data"]]}
        print(t,tot,flush=True)
        time.sleep(3)
json.dump(out,open("dc_hits.json","w"),indent=1)
