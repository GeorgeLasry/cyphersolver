import subprocess,re,time,sys,json,html
terms=["cipher","cypher","ciphered","in cipher","decipher","cryptogram","code message","code telegram","code book","coded","secret writing","secret code","invisible ink","Confederate cipher","signal code","Northwest Conspiracy","codebook","cryptography","secret ink","encoded"]
out={}
for t in terms:
    seen={}
    for p in range(1,4):
        u="https://www.chipublib.org/"+("page/%d/"%p if p>1 else "")+"?s="+t.replace(" ","+")
        r=subprocess.run(["curl","-sL","-m","30","-A","Mozilla/5.0",u],capture_output=True)
        h=r.stdout.decode("utf8","ignore")
        m=re.search(r'Search Results for',h)
        links=re.findall(r'<a[^>]+href="(https://www\.chipublib\.org/[^"?#]+)[^"]*"[^>]*>([^<]{3,150})</a>',h)
        n=0
        for l,tx in links:
            if re.search(r'/(fa-|archival_post|archival|blogs|collection)',l):
                seen[l]=html.unescape(tx.strip()); n+=1
        time.sleep(3)
        if p==1 and not links: break
    out[t]=seen
    print(t,len(seen),flush=True)
json.dump(out,open("cpl_search_raw.json","w"),indent=1)
