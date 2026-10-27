"""Resolve the RK Maximiliana shelfmarks of catalogue 495 to AIS IDs by walking the archive plan
(first-child and next-sibling links), and record title, date, Darin and image count.
python find_items.py -> items.json"""
import re, json, html, requests

B = 'https://www.archivinformationssystem.at/detail.aspx?ID='
s = requests.Session(); s.headers['User-Agent'] = 'Mozilla/5.0 (research)'
cache = {}

def page(i):
    if i not in cache:
        r = s.get(B + str(i), timeout=60); r.encoding = 'utf-8'; cache[i] = r.text
    return cache[i]

def nav(i, label):
    m = re.search(r'href="detail\.aspx\?ID=(\d+)"[^>]*>\s*' + label, page(i))
    return int(m.group(1)) if m else None

def info(i):
    t = page(i)
    tx = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<script.*?</script>|<[^>]+>', ' | ', t, flags=re.S)))
    m = re.search(r'Signatur: \|[ |]*(.*?) \|', tx) or re.search(r'Ref\. code: \|[ |]*(.*?) \|', tx)
    d = {'id': i, 'sig': m.group(1).strip() if m else ''}
    for f in ['Titel', 'Title', 'Entstehungszeitraum', 'Creation date\(s\)', 'Darin', 'Ort', 'City', 'Umfang', 'Extent', 'Bemerkung', 'Comments']:
        m = re.search(r'\| ' + f + r': \|[ |]*(.*?)\s*\| \| \|', tx)
        if m: d[f.split('\\')[0]] = m.group(1).strip(' |')
    d['images'] = len(set(re.findall(r'deid=0&(?:amp;)?sqnznr=(\d+)', t)))
    return d

def children(i):
    c = nav(i, 'Zum Eintrag auf untergeordneter Stufe')
    while c:
        yield c
        c = nav(c, 'Zum n.chsten Eintrag im Archivplan')

def sig(i):
    return info(i)['sig']

WANT = '22-2-51 22-2-55 22-2-56 22-3-5 22-3-8 22-3-18 22-3-42 23-2-62 23-3-6 23-5-4 23-5-17 23-5-25 23-5-47 26-3-50 26-4-6 26-4-9 26-4-10 26-4-15 26-4-24 26-4-25 26-5-7 26-5-10 26-5-31 27-1-5 25-2-25 25-2-27 25-1-36'.split()
kartons = {}
for k in children(227):
    m = re.search(r'Maximiliana (\d+)\b', sig(k))
    if m and m.group(1) in {w.split('-')[0] for w in WANT}: kartons[m.group(1)] = k
    if len(kartons) == len({w.split('-')[0] for w in WANT}): break
out = []
for w in WANT:
    ka, ko, it = w.split('-')
    kon = next(c for c in children(kartons[ka]) if sig(c).endswith('%s-%s' % (ka, ko)))
    first = nav(kon, 'Zum Eintrag auf untergeordneter Stufe')
    guess = first + int(it) - 1
    if not sig(guess).endswith(w):
        guess = next(c for c in children(kon) if sig(c).endswith(w))
    d = info(guess); out.append(d)
    print(w, guess, d['images'], (d.get('Titel') or d.get('Title', ''))[:110])
json.dump(out, open('items.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
