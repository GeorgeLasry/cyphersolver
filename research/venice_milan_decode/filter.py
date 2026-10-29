import json, re, sys
D = 'research/catalogue_harvest/decode/'
KW = re.compile(r'venic|venez|venis|venet|venecia|venedig|milan|milán|mailand|sforza|visconti|mantua|mantova|mantoue|gonzaga|asve|asmi\b|archivio di stato di milano|dieci|doge|serenissima|inquisitori|signoria|ambrosian|sanud|sanuto|bergamo|brescia|padua|padova|verona|vicenza|crema|cremona|pavia|lodi\b|como\b|dalmat|zara|candia|corfu|cyprus|famagusta|ragusa', re.I)
rows = []
for f in ['views.jsonl','views_b.jsonl','views_c.jsonl']:
    for line in open(D+f, encoding='utf-8'):
        r = json.loads(line)
        if r.get('record_type') not in ('1', '3', None): continue
        if r.get('status') == '1': continue
        txt = ' '.join(str(r.get(k) or '') for k in ['name','current_city','current_holder','additional_information','sender','receiver','author','origin_city','origin_region'])
        m = KW.findall(txt)
        if m: rows.append((r, sorted(set(x.lower() for x in m))))
print(len(rows), file=sys.stderr)
out = open('research/venice_milan_decode/hits.txt','w',encoding='utf-8')
for r, m in sorted(rows, key=lambda x: int(x[0]['id'])):
    info = re.sub(r'<[^>]+>', ' ', r.get('additional_information') or ''); info = re.sub(r'\s+', ' ', info).replace('The image is not in the public domain. Publishing it is only possible with the permission of the archive.','')[:400]
    out.write("R%s st%s ct%s ss%s pg%s %s-%s-%s | %s | %s | %s->%s (%s,%s) | lang %s/%s | kw %s | %s\n" % (r['id'], r['status'], r['cipher_types'], r['symbol_sets'], r['number_of_pages'], r['start_year'], r['start_month'], r['start_day'], r['name'], r['current_holder'], r['sender'], r['receiver'], r['origin_city'], r['origin_region'], r['cleartext_lang'], r['plaintext_lang'], ','.join(m), info))
json.dump([r['id'] for r,m in rows], open('research/venice_milan_decode/hit_ids.json','w'))
