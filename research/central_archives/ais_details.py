"""Fetch AIS detail pages for harvested hits and extract the description fields.
python ais_details.py hits.jsonl details.jsonl   (skips AVA Verkehr / AdR / items dated after 1950)"""
import re, sys, json, html, time, requests
F = ['Titel', 'Entstehungszeitraum', 'Darin', 'Inhalt', 'Ort', 'Sprache', 'Umfang', 'Reproduktion vorhanden', 'Physische Benützbarkeit', 'Zugänglichkeit', 'Veröffentlichungen', 'Bemerkung', 'Inhalt und Form']
def text(t):
    t = re.sub(r'<script.*?</script>', '', t, flags=re.S)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' | ', t)))
def fields(t):
    tx = text(t); d = {}
    for f in F:
        m = re.search(r'\| ' + re.escape(f) + r': \|[ |]*(.*?)\s*\| \| \|', tx)
        if m: d[f] = m.group(1).strip(' |')
    d['images'] = len(re.findall(r'imgThumb|Ansichtsbild', t)) and len(re.findall(r'class="[^"]*thumb', t, re.I))
    d['has_view'] = 'Ansichtsbild' in tx
    return d
done = set()
try:
    done = {json.loads(l)['id'] for l in open(sys.argv[2], encoding='utf-8')}
except FileNotFoundError: pass
out = open(sys.argv[2], 'a', encoding='utf-8'); s = requests.Session(); s.headers['User-Agent'] = 'Mozilla/5.0 (research)'
seen = set()
for l in open(sys.argv[1], encoding='utf-8'):
    x = json.loads(l)
    if x['id'] in seen or x['id'] in done: continue
    seen.add(x['id'])
    if 'Verkehr' in x['sig'] or '/AdR' in x['sig']: continue
    yrs = [int(y) for y in re.findall(r'\b(1[0-9]{3})\b', x['date'])]
    if yrs and min(yrs) > 1950: continue
    try:
        r = s.get('https://www.archivinformationssystem.at/detail.aspx?ID=' + x['id'], timeout=60)
        r.encoding = 'utf-8'; x.update(fields(r.text))
    except Exception as e:
        x['error'] = str(e)
    out.write(json.dumps(x, ensure_ascii=False) + '\n'); out.flush(); time.sleep(0.4)
