"""Classify flagged frames of the 1789-1906 RG 59 slice from their OCR snippet; write frames.tsv and print per item.

Classes: table (statistical/tabular keywords, decimals, money, sorted runs), code (mostly 1-4 digit groups,
few words, no table markers), mixed (code-like run inside prose), noise (other).
"""
import json, re, os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
TABLE = re.compile(r'\b(total|tons?|dollars?|cents?|value|quantity|exports?|imports?|barometer|thermometer|vessels?|'
                   r'population|census|tariff|tarif|pounds|lbs|kilos?|bales?|bags|cases|piastres?|francs?|marks?|'
                   r'florins?|rupees?|taels?|yen|pesos?|reis|duties|duty|amount|average|per cent|percent|'
                   r'statement|return|recapitulation|schedule|invoice|account|balance|salary|expenses?|'
                   r'arrivals?|clearances?|cargo|freight|price|prices|rate|rates|bushels|barrels|gallons|'
                   r'hectol|kilog|metres?|miles|acres|deaths?|births?|lottery|loteria|no\.|number|nos|page|'
                   r'folio|vol|volume|art\.|article|section|sec\.|chap|register|index|received|date|dated|'
                   r'sterling|shillings|cuadro|estado|tabla|tableau|año|anno|jahr|summa|betrag|registered)\b', re.I)
NUM = re.compile(r'^\d{1,4}[.,;:]?$')
DEC = re.compile(r'\d[.,]\d{2,3}\b|\$|£')
YEAR = re.compile(r'^1[6-9]\d\d$')
ANCH = {'jqa': {'1385', '1576', '1384', '668', '1401'}, 'armstrong': {'972', '1354'},
        'pinckney': {'1651', '133', '1343', '244', '1578'}}


def feats(s):
    toks = s.split()
    n = len(toks) or 1
    nums = [t.strip('.,;:') for t in toks if NUM.match(t) and not YEAR.match(t.strip('.,;:'))]
    words = [t for t in toks if re.fullmatch(r'[A-Za-z]{3,}[.,;:]?', t)]
    tab = len(TABLE.findall(s))
    dec = len(DEC.findall(s))
    ints = [int(x) for x in nums]
    asc = sum(1 for a, b in zip(ints, ints[1:]) if 0 < b - a <= 2)
    anch = {k: sum(1 for x in nums if x in v) for k, v in ANCH.items()}
    return dict(n=n, nn=len(nums), nw=len(words), tab=tab, dec=dec, asc=asc, anch=anch,
                share=len(nums) / n)


def classify(d):
    f = feats(d['snippet'])
    if f['nn'] < 8:
        return 'few', f
    if f['tab'] >= 2 or f['dec'] >= 4 or f['asc'] >= f['nn'] * 0.3:
        return 'table', f
    if f['share'] >= 0.5:
        return 'code', f
    if f['share'] >= 0.25:
        return 'mixed', f
    return 'prose', f


if __name__ == '__main__':
    rows = [json.loads(l) for l in open(os.path.join(HERE, 'slice.jsonl'), encoding='utf-8')]
    rows = [d for d in rows if d['kind'] == 'frame']
    out = open(os.path.join(HERE, 'frames.tsv'), 'w', encoding='utf-8')
    out.write('pub\tnaId\tyr\tfile\tcls\tnn\tnw\ttab\tanch\tsnippet\n')
    for d in rows:
        c, f = classify(d)
        a = ','.join(f'{k}{v}' for k, v in f['anch'].items() if v)
        out.write(f"{d['pub']}\t{d['naId']}\t{d['yr']}\t{d['file']}\t{c}\t{f['nn']}\t{f['nw']}\t{f['tab']}\t{a}\t"
                  f"{d['snippet'][:300].replace(chr(9),' ').replace(chr(10),' ')}\n")
    out.close()
