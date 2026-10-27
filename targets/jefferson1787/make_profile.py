"""Write ct/<letter>.txt (code groups, one line per manuscript line) and profile.json for jefferson1787.

Lengths are measured with docs/_check_profile.py's measure(); reading counts come from reading.tsv
(make_reading.py). Solution steps are kept here in order, failures included. Run after make_reading.py.
"""
import csv, glob, json, os, re, sys
from collections import Counter, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'docs'))
from _check_profile import measure  # noqa: E402

DOCS = OrderedDict([
    ('barclay_17860410', ('Barclay to the American Commissioners, Madrid, 10 Apr 1786', 'Library of Congress, Thomas Jefferson Papers ser. 1, mtj1 005_0494-0497 (RC, TJ interlinear decoding)', 1786, 'Madrid -> Paris', 'TJ interlinear', 'interlinear')),
    ('barclay_17870703', ('Barclay to Jefferson, undated [ca. 3 Jul 1787], two coded footnotes', 'Library of Congress, Thomas Jefferson Papers ser. 1, mtj1 007_0476-0481 (RC, filed under 12 Jun 1787)', 1787, 'Lorient -> Paris', 'none', 'none')),
    ('tj_17870704', ('Jefferson to Barclay, Paris, 4 Jul 1787', 'Library of Congress, Thomas Jefferson Papers ser. 1, mtj1 007_0605-0606 (PrC)', 1787, 'Paris -> Lorient', 'none', 'none')),
    ('tj_17870925', ('Jefferson to Carmichael, Paris, 25 Sep 1787', 'Library of Congress, Thomas Jefferson Papers ser. 1, mtj1 008_0145-0149 (PrC and clear-text sheet)', 1787, 'Paris -> Madrid', "TJ's clear-text sheet", 'separate folio')),
    ('tj_17870928', ('Jefferson to Adams, Paris, 28 Sep 1787, postscript', 'Library of Congress, Thomas Jefferson Papers ser. 1, mtj1 008_0161-0163 (PrC; RC at Massachusetts Historical Society)', 1787, 'Paris -> London', 'none', 'none')),
    ('tj_17871215', ('Jefferson to Carmichael, Paris, 15 Dec 1787, test line', 'Library of Congress, Thomas Jefferson Papers ser. 1, mtj1 008_0689 (PrC); plaintext 007_0489', 1787, 'Paris -> Madrid', 'the 14 Jun 1787 letter', 'separate folio')),
    ('carmichael_17880508', ('Carmichael to Jefferson, Aranjuez, 8 May 1788', 'Library of Congress, Thomas Jefferson Papers ser. 1, mtj1 009_0339-0342 (RC, TJ interlinear)', 1788, 'Aranjuez -> Paris', 'TJ interlinear', 'interlinear')),
    ('carmichael_17880529', ('Carmichael to Jefferson, 29 May 1788', 'Library of Congress, Thomas Jefferson Papers ser. 1, mtj1 009_0469-0472 (RC, TJ interlinear)', 1788, 'Madrid -> Paris', 'TJ interlinear', 'interlinear')),
    ('tj_17880603', ('Jefferson to Carmichael, Paris, 3 Jun 1788', 'Library of Congress, Thomas Jefferson Papers ser. 1, mtj1 009_0503-0511 (PrC and list of encoded passages)', 1788, 'Paris -> Madrid', "TJ's list", 'separate folio')),
    ('carmichael_17880605', ('Carmichael to Jefferson, 5 Jun 1788', 'Library of Congress, Thomas Jefferson Papers ser. 1, mtj1 009_0516-0517 (RC, TJ interlinear)', 1788, 'Madrid -> Paris', 'TJ interlinear', 'interlinear')),
    ('carmichael_17880724', ('Carmichael to Jefferson, 24 Jul 1788', 'Library of Congress, Thomas Jefferson Papers ser. 1, mtj1 009_0892-0895 (RC, TJ interlinear)', 1788, 'Madrid -> Paris', 'TJ interlinear', 'interlinear')),
    ('tj_17881225', ('Jefferson to Carmichael, Paris, 25 Dec 1788', 'Library of Congress, Thomas Jefferson Papers ser. 1, mtj1 010_0626-0630 (PrC)', 1788, 'Paris -> Madrid', 'none', 'none')),
    ('carmichael_17890126', ('Carmichael to Jefferson, 26 Jan 1789', 'Library of Congress, Thomas Jefferson Papers ser. 1, mtj1 010_0877-0885 (RC, TJ interlinear)', 1789, 'Madrid -> Paris', 'TJ interlinear', 'interlinear')),
    ('tj_17890809', ('Jefferson to Carmichael, Paris, 9 Aug 1789', 'Library of Congress, Thomas Jefferson Papers ser. 1, mtj1 011_0780-0783 (PrC)', 1789, 'Paris -> Madrid', 'none', 'none')),
    ('short_17891009', ('Short to Jay, Paris, 9 Oct 1789 (No. 2)', 'NARA RG 59, Despatches from U.S. Ministers to France vol. 1 = M34 roll 2 (letter-book copy)', 1789, 'Paris -> New York', 'decoding in the copy', 'interlinear')),
    ('short_17891025', ('Short to Jay, Paris, 25 Oct 1789 (No. 5)', 'NARA RG 59, Despatches from U.S. Ministers to France vol. 1 = M34 roll 2 (letter-book copy)', 1789, 'Paris -> New York', 'decoding in the copy', 'interlinear')),
    ('short_17891028', ('Short to Jay, Paris, 28 Oct 1789 (No. 6)', 'NARA RG 59, Despatches from U.S. Ministers to France vol. 1 = M34 roll 2 (letter-book copy)', 1789, 'Paris -> New York', 'decoding in the copy', 'interlinear')),
    ('tj_17910411', ('Jefferson to Carmichael, Philadelphia, 11 Apr 1791', 'Library of Congress, Thomas Jefferson Papers ser. 1, mtj1 014_0279-0285 (PrC in clerk\'s hand and "decyphered" sheet)', 1791, 'Philadelphia -> Madrid', 'clear-text sheet', 'separate folio')),
])


def write_ct(name):
    rows = [r for r in csv.DictReader(open(os.path.join(HERE, 'transcription', name + '.tsv'), encoding='utf-8'),
                                      delimiter='\t') if (r.get('code') or '').strip() not in ('', '=')]
    os.makedirs(os.path.join(HERE, 'ct'), exist_ok=True)
    lines, cur, key = [], [], None
    for r in rows:
        k = (r.get('image'), r.get('line'))
        if k != key and cur:
            lines.append(cur); cur = []
        key = k
        cur.append(re.sub(r'[^0-9?]', '', r['code']) or '?')
    if cur:
        lines.append(cur)
    p = os.path.join(HERE, 'ct', name + '.txt')
    with open(p, 'w', encoding='utf-8') as f:
        f.write(f'# {DOCS[name][0]}: code groups as transcribed, one line per manuscript line\n')
        for l in lines:
            f.write('.'.join(l) + '.\n')
    return p


def main():
    reading = list(csv.DictReader(open(os.path.join(HERE, 'reading.tsv'), encoding='utf-8'), delimiter='\t'))
    by = {}
    for r in reading:
        by.setdefault(r['letter'], []).append(r)
    docs = []
    all_groups = Counter()
    for name, (title, shelf, year, route, pt_src, loc) in DOCS.items():
        if not os.path.exists(os.path.join(HERE, 'transcription', name + '.tsv')):
            continue
        p = write_ct(name)
        m = measure(p)
        rs = [r for r in by.get(name, []) if r['grade'] != 'x']
        n = len(rs)
        rd = sum(1 for r in rs if r['reading'] and not ('?' in r['code'] and r['grade'] != 'H'))
        state = 'read' if n and rd / n >= 0.95 else ('read in part' if rd else 'not read')
        for r in rs:
            all_groups[re.sub(r'[^0-9]', '', r['code'])] += 1
        docs.append({
            'id': name, 'read': state, 'shelfmark': shelf, 'date': title.split(', ')[-1] if ',' in title else 'unknown',
            'year': year, 'country': 'United States', 'route': route, 'language': 'English',
            'cleartext_in_document': 'mostly clear',
            'plaintext': {'location': [loc], 'source': pt_src if pt_src != 'none' else
                          'No contemporary decoding; the Jefferson Papers editors printed a reading from a partial reconstruction.',
                          'partial': pt_src == 'none'},
            'length': {'tokens': m['tokens'], 'distinct': m['distinct'], 'unit': 'code groups', 'measured': True,
                       'file': 'ct/' + name + '.txt'},
            'transcription': {'by': 'llm from images', 'source': shelf,
                              'image_quality': 'poor' if name in ('tj_17870928', 'tj_17870925') else 'fair',
                              'notes': f'{n} groups counted in reading.tsv, {rd} with a reading.'}})
    N = sum(len([r for r in by.get(d['id'], []) if r['grade'] != 'x']) for d in docs)
    R = 0
    grades = Counter()
    for d in docs:
        for r in by.get(d['id'], []):
            if r['grade'] == 'x':
                continue
            if r['reading'] and not ('?' in r['code'] and r['grade'] != 'H'):
                R += 1
            if r['grade']:
                grades[r['grade']] += 1
    key_n = sum(1 for _ in open(os.path.join(HERE, 'key.tsv'), encoding='utf-8')) - 1
    prof = json.load(open(os.path.join(HERE, 'profile.json'), encoding='utf-8')) if os.path.exists(
        os.path.join(HERE, 'profile.json')) else {}
    prof.update({'schema_version': 1, 'target': 'jefferson1787',
                 'title': "Jefferson's Code No. 11 (the Barclay-Lamb code), coded passages of Barclay, Carmichael, Short and Jefferson, 1786-1791 (catalogue 483)"})
    prof['documents'] = docs
    prof.setdefault('system', {})
    prof['system'].update({
        'types': ['code', 'syllabic'],
        'summary': 'A two-part numerical code of about 1,750 groups (words, syllables, letters, punctuation), groups separated by dots, with homophones.',
        'symbol_kind': 'digits', 'digit_groups': {'width': '1-4', 'separation': 'dots'},
        'distinct_symbols': len(all_groups), 'diacritics': {'used': False},
        'homophones': {'used': True}, 'nomenclator': {'present': True, 'entries': 'unknown',
                                                      'kinds': ['syllables', 'word parts', 'common words', 'names'],
                                                      'unread_groups': 'unknown'},
        'nulls': {'present': 'unknown'}, 'key_order': 'random', 'word_division': 'none',
        'doubled_letters': 'unknown',
        'sibling_key': 'No key sheet survives; values rebuilt from Jefferson\'s interlinear decodings and clear-text sheets in the same series (key.tsv).',
        'notes': f'distinct_symbols counts distinct groups across the counted letters. Homophones: full stop 1013/1235, is 1363/1306, the 1196/1190, their 1365/1565, minister 396/896. key.tsv holds {key_n} attested values. Two-part code: numbers not in alphabetical order (key_order random).'})
    json.dump(prof, open(os.path.join(HERE, 'profile.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    open(os.path.join(HERE, 'profile.json'), 'a', encoding='utf-8').write('\n')
    print(f'{len(docs)} documents; {R}/{N} groups with a reading ({R/N:.3f}); grades {dict(grades)}; key {key_n}')


if __name__ == '__main__':
    main()
