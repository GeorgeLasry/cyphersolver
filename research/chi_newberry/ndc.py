"""Fetch Newberry Digital Collections (collections.newberry.org, Orange Logic) item pages by record id and print title,
key metadata and context around search terms. Usage: python ndc.py TERMREGEX ID [ID...]"""
import re, sys, time, html, requests, json
UA = {'User-Agent': 'cyphersolver research (catalogue sweep)'}
sys.stdout.reconfigure(encoding='utf-8')
rx = re.compile(sys.argv[1], re.I)
out = open('ndc_items.jsonl', 'a', encoding='utf-8')
for rid in sys.argv[2:]:
    r = requests.get(f'https://collections.newberry.org/archive/-{rid}.html', headers=UA, timeout=60)
    if r.status_code in (403, 429): sys.exit(f'STOP {r.status_code}')
    t = re.sub(r'(?s)<script.*?</script>|<style.*?</style>', ' ', r.text)
    t = html.unescape(re.sub(r'<[^>]+>', ' ', t)); t = re.sub(r'\s+', ' ', t)
    title = re.search(r'<title>([^<]*)', r.text); title = html.unescape(title.group(1)) if title else ''
    ctx = [t[max(0, m.start()-300):m.end()+300] for m in rx.finditer(t)][:4]
    out.write(json.dumps({'rid': rid, 'title': title, 'ctx': ctx, 'len': len(t)}, ensure_ascii=False) + '\n')
    print('##', rid, title, len(t)); [print('   >', c) for c in ctx]
    time.sleep(3)
