"""Triage emlo_hits.json: add manifestation notes + institution names, keep works whose text says cipher, print
a compact line per work and write emlo_triage.json.

    python -I research/founders_emlo/emlo_triage.py
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from emlo_harvest import get  # noqa

HERE = os.path.dirname(os.path.abspath(__file__))
W = json.load(open(os.path.join(HERE, 'emlo_hits.json'), encoding='utf-8'))
RX = re.compile(r'(ciph|cyph|chiffr|cijf|geheimschr|cifra|zyfer|cyffer|ziffer|in code|nomenclat|cryptog|steganog|jargon)', re.I)

# manifestation comments + institutions
mc, inst = set(), set()
for w in W:
    for m in w['_manifs']:
        mc.update(m.get('ox_isAnnotatedBy-comment') or [])
        inst.update(m.get('ox_resourceAt-institution') or [])


def fetch(core, uris):
    out = {}
    uris = [u.split('/')[-1] for u in uris]
    for i in range(0, len(uris), 40):
        ids = ' OR '.join('"%s"' % u for u in uris[i:i + 40])
        for doc in get(core, {'q': 'uuid:(%s)' % ids, 'rows': 100, 'wt': 'json'})['response']['docs']:
            out[doc['uuid']] = doc
    return out


MC = fetch('comments', mc)
IN = fetch('institutions', inst)
rows = []
for w in W:
    texts = []
    for k in ('dcterms_abstract', 'ox_keywords', 'ox_incipit', 'ox_excipit'):
        if w.get(k):
            texts.append((k, w[k] if isinstance(w[k], str) else ' '.join(w[k])))
    for n in w['_notes']:
        if n.get('bibo_Note'):
            texts.append(('note', n['bibo_Note']))
    manifs = []
    for m in w['_manifs']:
        insts = [IN.get(u.split('/')[-1], {}).get('geonames_officialName', '') for u in m.get('ox_resourceAt-institution') or []]
        shelf = (m.get('dcterms_identifier-shelf_') or '').replace('shelf_', '')
        manifs.append({'type': m.get('dcterms_type'), 'inst': '; '.join(insts), 'shelf': shelf,
                       'printed': m.get('ox_printedEditionDetails', ''), 'images': bool(m.get('frbr_Image-image'))})
        for c in m.get('ox_isAnnotatedBy-comment') or []:
            n = MC.get(c.split('/')[-1], {})
            if n.get('bibo_Note'):
                texts.append(('mnote', n['bibo_Note']))
    ctx = []
    for k, t in texts:
        t = re.sub(r'\s+', ' ', t)
        for mm in RX.finditer(t):
            ctx.append('%s: ...%s...' % (k, t[max(0, mm.start() - 160): mm.end() + 160]))
            break
    rows.append({'uuid': w['uuid'], 'url': 'https://emlo.bodleian.ox.ac.uk/profile/work/' + w['uuid'],
                 'date': w.get('started_date_sort', '')[:10], 'year': w.get('ox_started-ox_year'),
                 'author': w.get('author_sort', ''), 'recipient': w.get('recipient_sort', ''),
                 'origin': w.get('origin_sort', ''), 'dest': w.get('destination_sort', ''),
                 'lang': w.get('dcterms_language', ''), 'catalogue': w.get('cito_Catalog', ''),
                 'terms': w['_terms'], 'ctx': ctx, 'manifs': manifs})
keep = [r for r in rows if r['ctx']]
keep.sort(key=lambda r: (r['catalogue'], r['date']))
json.dump(keep, open(os.path.join(HERE, 'emlo_triage.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(rows), 'works;', len(keep), 'with cipher wording')
