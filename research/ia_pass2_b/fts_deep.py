import json,sys,time,urllib.parse,urllib.request
ids=set(json.load(open("ids.json")))|set(json.load(open("ids2.json")))
Qs=['"undeciphered cipher"','"not deciphered" cipher','"in cipher, undeciphered"','"cipher not deciphered"','"undecyphered" cypher','"not decyphered"','"cypher, not decyphered"','"cipher uninterpreted"','"cipher, which is not deciphered"','"in cipher, not deciphered"','"unintelligible cipher"','"cipher is lost"','"key is lost" cipher','"cannot be deciphered"','"in cipher" "no key"','"partly in cipher" undeciphered','"chiefly in cipher" undeciphered','"wholly in cipher"','"entirely in cipher"','"cipher unsolved"']
out={}
for q in Qs:
    for p in range(1,9):
        u="https://archive.org/services/search/beta/page_production/?service_backend=fts&hits_per_page=50&page=%d&user_query=%s"%(p,urllib.parse.quote(q))
        try:
            d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=60))
        except Exception as e:
            print("fail",q,p,e); break
        hs=d["response"]["body"]["hits"]["hits"]
        if not hs: break
        for h in hs:
            f=h["fields"]; i=f.get("identifier")
            out.setdefault(i,{"title":f.get("title"),"hits":[]})["hits"].append({"q":q,"pg":f.get("page_num"),"txt":(h.get("highlight") or {}).get("text",[""])[0][:300] if isinstance(h.get("highlight"),dict) else ""})
        time.sleep(1)
    print(q,len(out),flush=True)
json.dump(out,open("fts_deep.json","w"),ensure_ascii=False)
mine=[i for i in out if i in ids]
print("total ids",len(out),"in my sets",len(mine))
