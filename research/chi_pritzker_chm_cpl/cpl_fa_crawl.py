"""CPL finding aids: chipublib.org pages with slug fa-* (full text of each finding aid), URL list from the WordPress page sitemaps.
Cached as plain text under raw/cplfa/ (git-ignored). 3 s between requests."""
import subprocess, re, time, os, html, hashlib

os.makedirs("raw/cplfa", exist_ok=True)
urls = open("cpl_fa_urls.txt").read().split()
for u in urls:
    fn = "raw/cplfa/" + hashlib.md5(u.encode()).hexdigest() + ".txt"
    if os.path.exists(fn):
        continue
    h = subprocess.run(["curl", "-sL", "-m", "60", "-A", "Mozilla/5.0 (research; polite)", u], capture_output=True).stdout.decode("utf8", "ignore")
    h = re.sub(r"(?s)<(script|style)[^>]*>.*?</\1>", "", h)
    t = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)))
    open(fn, "w", encoding="utf8").write(u + "\n" + t)
    time.sleep(3)
print("done", len(urls))
