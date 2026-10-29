"""Local-only variant of primo_search.py (scope=MyInstitution)."""
import urllib.request, urllib.parse, json, time
B="https://search.library.northwestern.edu"; V="01NWU_INST:NULV_NDE"; H={"User-Agent":"Mozilla/5.0 research"}
def tok():
    return json.load(urllib.request.urlopen(urllib.request.Request(B+f"/primaws/rest/pub/institution/01NWU_INST/guestJwt?isGuest=true&lang=en&viewId={V}",headers=H)))
T=tok()
terms=["cipher","cypher","ciphered","\"in cipher\"","decipher","deciphered","cryptogram","cryptograph*","\"code message\"","\"code telegram\"","\"code book\"","coded","\"secret writing\"","\"secret code\"","\"invisible ink\"","\"sympathetic ink\"","nomenclator","chiffre","cifra","\"en cifra\"","Geheimschrift","szyfr","encoded","\"secret alphabet\"","\"cipher letter\"","\"cipher key\""]
out={}
def get(t,rt,scope):
    p={"inst":"01NWU_INST","lang":"en","limit":100,"offset":0,"q":"any,contains,"+t,"scope":scope,"tab":"Everything","vid":V,"qInclude":"facet_rtype,exact,"+rt}
    r=json.load(urllib.request.urlopen(urllib.request.Request(B+"/primaws/rest/pub/pnxs?"+urllib.parse.urlencode(p),headers={**H,"Authorization":"Bearer "+T}),timeout=90))
    items=[]
    for d in r.get("docs",[]):
        pn=d["pnx"]; ds=pn["display"]; g=lambda k:(ds.get(k) or [""])[0]
        items.append({"id":pn["control"]["recordid"],"title":g("title")[:200],"creator":g("creator"),"date":g("creationdate"),"source":g("source"),"desc":g("description")[:500],"subject":g("subject")[:200],"link":d.get("delivery",{}).get("GetIt1",[{}])[0].get("links",[{}])[0].get("link","") if d.get("delivery") else ""})
    return r["info"]["total"],items
for t in terms:
    for rt in ["archival_material_manuscripts"]:
        try:
            tot,items=get(t,rt,"MyInstitution")
        except Exception as e:
            print(t,"ERR",e,flush=True); time.sleep(3); continue
        out[t]={"total":tot,"items":items}; print(t,tot,len(items),flush=True)
        json.dump(out,open("primo_local_hits.json","w"),indent=1,ensure_ascii=False)
        time.sleep(3)
