"""Pritzker Military Museum & Library: download each archival-collection finding-aid PDF
(text only, ~100 KB each, git-ignored raw/pmml/), 3 s apart. The list of PDF names was read from
https://www.pritzkermilitary.org/resources/archival-collections in the built-in browser
(the site is behind Incapsula for HTML pages; the PDFs download with curl)."""
import subprocess, os, time, re, sys

os.makedirs("raw/pmml", exist_ok=True)
BASE = "https://www.pritzkermilitary.org/sites/default/files/files/"
names = open("pmml_list.txt").read().split()
urls = ["https://www.pritzkermilitary.org/sites/default/files/2026-10/HaffHenryL_FA2026.pdf"] + [BASE + n for n in names]
for u in urls:
    fn = "raw/pmml/" + u.rsplit("/", 1)[1].replace("%20", "_")
    if os.path.exists(fn) and os.path.getsize(fn) > 1000:
        continue
    subprocess.run(["curl", "-sL", "-m", "60", "-A", "Mozilla/5.0 (research; polite)", "-o", fn, u])
    time.sleep(3)
print("done", len(urls))
