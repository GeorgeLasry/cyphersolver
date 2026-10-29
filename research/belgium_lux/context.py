"""Print an EAD component's ancestors and siblings: python context.py <eadid> <regex on unittitle>"""
import re, sys
import xml.etree.ElementTree as ET
CT = re.compile(r'c(0\d|1[0-2])?')
t = lambda e: re.sub(r'\s+', ' ', ''.join(e.itertext())).strip() if e is not None else ''
root = ET.parse(f'ead/{sys.argv[1]}.xml').getroot()
pat = re.compile(sys.argv[2], re.I)
def walk(c, anc):
    did = c.find('did')
    line = (t(did.find('unitid')) + ' | ' + t(did.find('unittitle'))[:400] + ' | ' + t(did.find('unitdate'))) if did is not None else ''
    if did is not None and pat.search(t(did.find('unittitle')) + ' ' + t(c.find('scopecontent'))):
        for a in anc[-3:]: print('  ^', a[:300])
        print('  >', line, '|', t(c.find('scopecontent'))[:600])
        kids = [k for k in c if CT.fullmatch(k.tag)]
        for k in kids[:8]: print('     -', t(k.find('did/unitid')), t(k.find('did/unittitle'))[:200])
        print()
    for k in c:
        if CT.fullmatch(k.tag): walk(k, anc + [line])
for dsc in root.iter('dsc'):
    for k in dsc:
        if CT.fullmatch(k.tag): walk(k, [])
