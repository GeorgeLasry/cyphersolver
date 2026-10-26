"""Harvest all result pages of an AIS (archivinformationssystem.at) full-text search into a JSONL.
python ais_harvest.py OUT.jsonl TERM [TERM ...]"""
import re, sys, json, html, time
from ais_search import search, hidden, B
ROW = re.compile(r'hylTitel" href="detail\.aspx\?ID=(\d+)"[^>]*>(.*?)</a>.*?</td><td>(.*?)</td><td>(.*?)</td><td>\s*<span[^>]*lblSignatur">(.*?)</span>', re.S)
def clean(x): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', x))).strip()
def rows(t):
    for m in ROW.finditer(t):
        yield dict(id=m.group(1), title=clean(m.group(2)), date=clean(m.group(3)), level=clean(m.group(4)), sig=clean(m.group(5)))
out = open(sys.argv[1], 'a', encoding='utf-8')
for term in sys.argv[2:]:
    s, r = search(term); page = 1; seen = set()
    while True:
        new = 0
        for x in rows(r.text):
            if x['id'] in seen: continue
            seen.add(x['id']); new += 1; x['term'] = term; out.write(json.dumps(x, ensure_ascii=False) + '\n')
        m = re.search(r'class="nextPage" href="javascript:__doPostBack\(&#39;([^&]+)&#39;', r.text)
        if not m or not new: break
        d = hidden(r.text); d['__EVENTTARGET'] = m.group(1); d['__EVENTARGUMENT'] = ''
        r = s.post(B + 'resultatliste.aspx', data=d, timeout=120); page += 1; time.sleep(0.3)
    out.flush(); print(term, len(seen), 'pages', page, flush=True)
