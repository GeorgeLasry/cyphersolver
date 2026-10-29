"""Crawl every CPL archival finding-aid post (sitemap bccms_archival_post), cache text (git-ignored raw/), grep terms."""
import subprocess,re,time,os,json,html
os.makedirs("raw/cpl",exist_ok=True)
def get(u):
    return subprocess.run(["curl","-sL","-m","40","-A","Mozilla/5.0 (research; polite)",u],capture_output=True).stdout.decode("utf8","ignore")
idx=get("https://www.chipublib.org/sitemap.xml")
subs=re.findall(r"<loc>([^<]*archival_post[^<]*)</loc>",idx)
urls=[]
for s in subs:
    urls+= re.findall(r"<loc>([^<]*)</loc>",get(s)); time.sleep(1)
urls=[u for u in dict.fromkeys(urls)]
urls=[u for u in urls if "/archival_post/" in u or "/fa-" in u]
json.dump(urls,open("cpl_urls.json","w"),indent=0)
print(len(urls),"finding-aid urls",flush=True)
for u in urls:
    import hashlib; fn="raw/cpl/"+hashlib.md5(u.encode()).hexdigest()+".txt"
    if os.path.exists(fn): continue
    h=get(u); h=re.sub(r"(?s)<(script|style)[^>]*>.*?</\1>","",h)
    t=html.unescape(re.sub(r"\s+"," ",re.sub(r"<[^>]+>"," ",h)))
    open(fn,"w",encoding="utf8").write(u+"\n"+t); time.sleep(3)
print("done")
