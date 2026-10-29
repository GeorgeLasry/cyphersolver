import subprocess,json,time,urllib.parse
terms=["cyphers","ciphers","cipher letter","cyphered","cryptic","cryptography","cryptographic","secret ink","coded letter","coded message","codes and ciphers","telegram code","Camp Douglas","Confederate prisoners","Confederate conspiracy","Sons of Liberty","Haymarket","anarchist letters","spy","espionage","signal corps","secret service","symbols letter","secret correspondence","invisible","Burr conspiracy","Hines","Judge Buckner Morris","Walsingham","code key","unintelligible","private cipher"]
res={}
for t in terms:
    u="https://collections.carli.illinois.edu/digital/api/search/collection/chm_fa/searchterm/%s/field/all/mode/exact/conn/and/maxRecords/100"%urllib.parse.quote(t)
    try: d=json.loads(subprocess.run(["curl","-sL","-m","60","-A","Mozilla/5.0",u],capture_output=True).stdout)
    except Exception: print(t,"ERR"); time.sleep(3); continue
    res[t]=[(i['itemId'],i['title']) for i in d['items']]
    print(t,d['totalResults'],[x[1][:50] for x in res[t]][:8],flush=True); time.sleep(3)
json.dump(res,open("chm_cdm2.json","w"),indent=1)
