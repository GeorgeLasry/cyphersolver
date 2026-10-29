"""Item-level cipher search over the downloaded AGATHA EAD files (ead/*.xml) -> ead_hits.json."""
import glob, json, re, sys
import xml.etree.ElementTree as ET

TERMS = re.compile(r"\b(chiffr\w*|d[ée]chiffr\w*|en chiffres?|cijfer\w*|ontcijfer\w*|gecijfer\w*|cifra\w*|cifr[ao]\w*|"
                   r"descifra\w*|cyfr\w*|ziffer\w*|chiffrier\w*|dechiffrier\w*|geheimschrift\w*|nomenclat\w*|"
                   r"clefs?\s+(?:du|des|de)\s+chiffre|clavis|occult\w*\s+script\w*|"
                   r"caract[èe]res?\s+(?:secrets?|occultes?)|lettres?\s+interceptées|intercept\w*|"
                   r"jargon|contre-?chiffre|encre\s+sympathique)", re.I)
# drop the commonest false positives (numbers, statistics, pagination)
NOISE = re.compile(r"chiffres?\s+(?:de\s+(?:la\s+)?population|d.affaires|statisti|romains|arabes|index)|"
                   r"cijfers?\s+(?:van|over)\s+de\s+(?:bevolking|productie)|statisti|cijferlijst|"
                   r"chiffres?\s+de\s+production|nomenclature", re.I)

def text(el):
    return re.sub(r'\s+', ' ', ''.join(el.itertext())).strip() if el is not None else ''

hits = []
CTAG = re.compile(r'c(0\d|1[0-2])?')

def walk(c, chain, eadid, inv):
    did = c.find('did')
    uid = text(did.find('unitid')) if did is not None else ''
    chain = chain + [uid] if uid else chain
    if did is not None:
        own = ' '.join(text(x) for x in [did.find('unittitle'), c.find('scopecontent'), c.find('odd'), c.find('note'),
                                          did.find('physdesc')])
        m = [x.group(0) for x in TERMS.finditer(own)]
        if m and not all(NOISE.search(own[max(0, own.find(x) - 40):own.find(x) + 60]) for x in m):
            hits.append({'ead': eadid, 'inventory': inv, 'unitid': uid, 'chain': chain,
                         'level': c.get('level'), 'title': text(did.find('unittitle'))[:600],
                         'date': text(did.find('unitdate')), 'scope': text(c.find('scopecontent'))[:800],
                         'daos': sum(1 for _ in c.iter('dao')),
                         'dao': [d.get('href') or d.get('{http://www.w3.org/1999/xlink}href') for d in c.iter('dao')][:2],
                         'terms': sorted(set(t.lower() for t in m))})
    for k in c:
        if CTAG.fullmatch(k.tag):
            walk(k, chain, eadid, inv)

for path in sorted(glob.glob('ead/*.xml')):
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as e:
        print('parse error', path, e, file=sys.stderr); continue
    eadid, inv = text(root.find('.//eadid')), text(root.find('.//titleproper'))
    for dsc in root.iter('dsc'):
        for k in dsc:
            if CTAG.fullmatch(k.tag):
                walk(k, [], eadid, inv)
json.dump(hits, open('ead_hits.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(hits), 'hits in', len(glob.glob('ead/*.xml')), 'inventories', file=sys.stderr)
