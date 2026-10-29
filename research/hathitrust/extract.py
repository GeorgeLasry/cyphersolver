"""Second pass: for volumes with hits in the scan outputs, pull each hit with its entry header, page, date.
usage: python extract.py scan_out1.txt scan_out2.txt ...   -> raw_hits.json (deduplicated across duplicate scans of one volume)"""
import sys, re, json, os, time, urllib.request
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
UA = {'User-Agent': 'Mozilla/5.0 (cipher-catalogue research; dnbourdeau@gmail.com)'}
CACHE = r'C:\Users\dbour\cypher\.work\hathi_scan\cache'
os.makedirs(CACHE, exist_ok=True)
PAT = re.compile(r"(undeci?y?phered|not (?:been )?deci?y?phered|cipher[^.\n]{0,25}(?:unread|unsolved|not (?:been )?(?:read|solved))"
                 r"|undecyphered|not decyphered|\(in cipher\)[^.\n]{0,40}(?:not|un))", re.I)
ENTRY = re.compile(r"(?:^|\s)(\d{1,3})\.\s+([A-Z\[][^\n]{3,140}?\b(?:to|from|and|petition|Petition|memorandum|Memorandum|Examination|Intelligence|Letter|Warrant)\b)")
DATE = re.compile(r"\b(Jan|Feb|Mar|Apr|May|June?|July?|Aug|Sept?|Oct|Nov|Dec)[a-z]*\.?\s*\[?(\d{1,2})\b")
PAGE = re.compile(r"(\d{2,3})\s+(?:STATE PAPERS|DOMESTIC|ADDENDA|ELIZABETH|JAMES|CHARLES|COMMONWEALTH)[^\n]{0,30}|(?:STATE PAPERS|DOMESTIC)[^\n\d]{0,25}(\d{2,3})\b")
YEAR = re.compile(r"\b(1[5-7]\d\d)(?:-\d{1,2})?\b")


def get(u):
    time.sleep(1.1)
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=120).read().decode('utf-8', 'replace')


def text(i):
    p = os.path.join(CACHE, i + '.txt')
    if not os.path.exists(p):
        open(p, 'w', encoding='utf-8').write(get(f'https://archive.org/download/{i}/{i}_djvu.txt'))
    return open(p, encoding='utf-8').read()


ids = []
for f in sys.argv[1:]:
    cur = None
    for ln in open(f, encoding='utf-8', errors='replace'):
        if ln.startswith('--- '):
            ids.append(ln.split()[1])
ids = list(dict.fromkeys(ids))
titles = {}
for f in sys.argv[1:]:
    for ln in open(f, encoding='utf-8', errors='replace'):
        if ln.startswith('VOL '):
            p = ln.rstrip().split(' ', 3)
            titles[p[1]] = p[3] if len(p) > 3 else ''
out, seen = [], set()
for i in ids:
    try: t = text(i)
    except Exception as e: print('ERR', i, e); continue
    for m in PAT.finditer(t):
        back = t[max(0, m.start() - 3200):m.end()]
        es = list(ENTRY.finditer(back))
        e = es[-1] if es else None
        full = re.sub(r'\s+', ' ', back[e.start():] if e else back[-500:]); note = full if len(full) < 1000 else full[:420] + ' <<...>> ' + full[-420:]
        key = re.sub(r'[^a-z]', '', note.lower())[:90]
        if key in seen: continue
        seen.add(key)
        pg = [x for x in PAGE.finditer(back)]
        dt = [x for x in DATE.finditer(back[:e.start() if e else len(back)])]
        yr = YEAR.findall(t[max(0, m.start() - 3000):m.start()])
        out.append(dict(vol=i, title=titles.get(i, ''), pos=m.start(), entry=e.group(1) if e else None,
                        date=dt[-1].group(0) if dt else None, page=(pg[-1].group(1) or pg[-1].group(2)) if pg else None,
                        years=yr[-3:], span=len(full), leaf=t.count('\f', 0, m.start()) + 1, note=note))
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'raw_hits.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(len(out), 'hits from', len(ids), 'volumes')
