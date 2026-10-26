"""Kalliope SRU harvest (kalliope-verbund.info/sru, MODS). python kalliope_sru.py OUT.jsonl TERM ..."""
import sys, json, time, requests, xml.etree.ElementTree as ET
NS = {'srw': 'http://www.loc.gov/zing/srw/', 'm': 'http://www.loc.gov/mods/v3'}
def rec(m):
    g = lambda p: [(e.text or '').strip() for e in m.findall(p, NS) if (e.text or '').strip()]
    tit = [' '.join(t.split()) for t in (''.join(e.itertext()) for e in m.findall('m:titleInfo/m:title', NS))]
    par = [' '.join(''.join(e.itertext()).split()) for e in m.findall('m:relatedItem/m:titleInfo/m:title', NS)]
    return dict(src=g('m:recordInfo/m:recordContentSource'), id=(g('m:recordInfo/m:recordIdentifier') or [''])[0], title=' | '.join(tit), parent=' | '.join(par),
                names=g('m:name/m:namePart'), date=g('m:originInfo/m:dateCreated') + g('m:originInfo/m:dateOther'),
                place=g('m:originInfo/m:place/m:placeTerm'), holder=g('m:location/m:physicalLocation'),
                shelf=g('m:location/m:shelfLocator'), notes=g('m:note') + g('m:physicalDescription/m:note') + g('m:abstract'),
                extent=g('m:physicalDescription/m:extent'), urls=g('m:location/m:url'), lang=g('m:language/m:languageTerm'))
out = open(sys.argv[1], 'a', encoding='utf-8')
for term in sys.argv[2:]:
    start, n = 1, None
    while True:
        r = requests.get('https://kalliope-verbund.info/sru', params=dict(version='1.2', operation='searchRetrieve', query=term,
                         maximumRecords=50, startRecord=start, recordSchema='mods'), timeout=120)
        root = ET.fromstring(r.content)
        n = int(root.findtext('srw:numberOfRecords', '0', NS))
        recs = root.findall('.//srw:recordData/m:mods', NS)
        for m in recs:
            x = rec(m); x['term'] = term; out.write(json.dumps(x, ensure_ascii=False) + '\n')
        start += 50
        if not recs or start > n or start > 2000: break
        time.sleep(0.5)
    out.flush(); print(term, n, flush=True)
