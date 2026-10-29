import json, re, sys
D = 'research/catalogue_harvest/decode/'
old = set(json.load(open('research/venice_milan_decode/hit_ids.json')))
KW = re.compile(r'sforz|simonett|lombard|ital(?:ien|\.)? ?15[89]\d|ludovico|galeazzo|contarini|mocenigo|morosini|barbaro|giustinian|grimani|priuli|venier|dandolo|foscari|loredan|tiepolo|cornaro|soranzo|badoer|michiel|trevisan|dolfin|gradenigo|querini|bembo|sagredo|gonzag|mantu|savorgnan|vénit|veneti|venedi|venise|maino|trivulz|visconte|borromeo|torriani|adriatic|friuli|udine|treviso|rovigo|chioggia|murano|sarpi|bragadin|pisani|vendramin|zeno\b|marcello|erizzo|valier', re.I)
seen=set(); rows=[]
for f in ['views.jsonl','views_b.jsonl','views_c.jsonl']:
    for line in open(D+f, encoding='utf-8'):
        r = json.loads(line)
        if r['id'] in old or r['id'] in seen: continue
        if r.get('record_type') not in ('1','3',None) or r.get('status')=='1': continue
        txt = ' '.join(str(r.get(k) or '') for k in ['name','current_city','current_holder','additional_information','sender','receiver','author','origin_city','origin_region'])
        m = KW.findall(txt)
        if m: seen.add(r['id']); rows.append((r, sorted(set(x.lower() for x in m))))
for r, m in sorted(rows, key=lambda x:int(x[0]['id'])):
    info = re.sub(r'<[^>]+>', ' ', r.get('additional_information') or ''); info = re.sub(r'\s+',' ',info).replace('The image is not in the public domain. Publishing it is only possible with the permission of the archive.','')[:300]
    print("R%s st%s pg%s %s | %s | %s | %s->%s (%s) | kw %s | %s" % (r['id'], r['status'], r['number_of_pages'], r['start_year'], r['name'], r['current_holder'], r['sender'], r['receiver'], r['origin_city'], ','.join(m), info))
