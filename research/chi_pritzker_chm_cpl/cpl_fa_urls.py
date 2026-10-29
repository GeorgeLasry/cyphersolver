"""List CPL finding-aid pages (slug fa-*) from the WordPress page sitemaps, then crawl them (cpl_fa_crawl.py)."""
import subprocess, re, time

idx = subprocess.run(["curl", "-sL", "https://www.chipublib.org/sitemap.xml"], capture_output=True).stdout.decode()
subs = re.findall(r"<loc>([^<]*sitemap-pt-page[^<]*)</loc>", idx)
urls = []
for s in subs:
    h = subprocess.run(["curl", "-sL", "-m", "40", s], capture_output=True).stdout.decode("utf8", "ignore")
    urls += re.findall(r"<loc>([^<]*)</loc>", h)
    time.sleep(1)
fa = [u for u in dict.fromkeys(urls) if "/fa-" in u or "finding-aid" in u]
print(len(urls), len(fa))
open("cpl_fa_urls.txt", "w").write("\n".join(fa))
