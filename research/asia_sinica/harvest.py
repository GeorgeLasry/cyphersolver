"""Harvest the Taiwan Digital Archives union catalogue (catalog.digitalarchives.tw) for cipher terms.

The Academia Sinica IMH archive search (archivesonline.mh.sinica.edu.tw; archdtsu is gone) does not resolve from
this machine, but its item metadata (館藏號, 件名, 頁數, 版本) is mirrored in the TELDAP union catalogue.
Search.jsp takes QS as Big5 bytes, ShowPage=n. Output: hits.jsonl (one line per term x item).
"""
import json, re, sys, time, urllib.parse, html
import requests, urllib3
urllib3.disable_warnings()

TERMS = sys.argv[1:] or ['密電', '密碼', '電碼', '密本', '譯電', '暗號', '暗碼', '密函', '隱語', '密信', '碼本',
                         '電報密碼', '密電本', '不能譯', '未譯', '密碼電報', '密電碼', '電本', '譯出', '無從翻譯',
                         '難譯', '密電譯文', '密碼本', '密語', '暗語', '洋文密電', '截獲', '截譯', '偵譯', '破譯']
S = requests.Session(); S.headers['User-Agent'] = 'Mozilla/5.0 (research sweep)'
out = open('hits.jsonl', 'a', encoding='utf-8')
counts = {}
for t in TERMS:
    q = urllib.parse.quote(t.encode('big5'))
    page = 1; n_total = None; seen = 0
    while True:
        url = f'https://catalog.digitalarchives.tw/Search/Search.jsp?QS={q}&ShowPage={page}'
        for attempt in range(3):
            try:
                r = S.get(url, timeout=60, verify=False); break
            except Exception as e:
                time.sleep(5)
        else:
            print('fail', t, page); break
        txt = r.content.decode('big5', errors='replace')
        if n_total is None:
            m = re.search(r'共找到\s*([\d,]+)\s*筆', txt)
            n_total = int(m.group(1).replace(',', '')) if m else 0
        blocks = re.findall(r'<div class = "expSearch">(.*?)<dl><dd>(\d+)/\d+</dd>', txt, re.S)
        if not blocks: break
        for b, idx in blocks:
            m = re.search(r'<h2><a href="(/item/[^"]+)" title="([^"]*)"', b)
            p = re.search(r'<p>(.*?)\.\.\.\.\.', b, re.S)
            body = html.unescape(re.sub(r'<[^>]+>', '', p.group(1))) if p else ''
            out.write(json.dumps({'term': t, 'idx': int(idx), 'url': 'https://catalog.digitalarchives.tw' + m.group(1) if m else None,
                                  'title': html.unescape(m.group(2)) if m else '', 'snippet': re.sub(r'\s+', ' ', body).strip()},
                                 ensure_ascii=False) + '\n')
            seen += 1
        out.flush()
        if seen >= n_total or page > 200: break
        page += 1; time.sleep(0.7)
    counts[t] = (n_total, seen); print(t, n_total, seen, flush=True)
json.dump(counts, open('harvest_counts.json', 'a', encoding='utf-8'), ensure_ascii=False); open('harvest_counts.json','a').write('\n')
