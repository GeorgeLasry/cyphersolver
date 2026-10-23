"""v7 translate list 2 (ranzo1528 letters 1-3): annotate Biermann's transcription with George Lasry's key by key status,
as b33_rz_annot.py did for letter 4, and add Paolo Rosson's independent key (letters 1-3; fetched to the scratchpad,
reread/rosson/key/table.tsv) where Lasry's value is tentative and seen once or twice or missing.

Lasry firm, or tentative seen 3+ times: plain. Tentative seen once or twice: plain if Rosson gives the same value,
else <value?> (with Rosson's value as <value?|R:other> when it differs). No Lasry value: [code], or [code|R:value]
when Rosson has one. Clear words (quoted in Biermann's transcription) kept as "word".

    python research/reading_audit/translate_v7_2_rz_annot.py <letter number> <rosson table.tsv> > <out>
"""
import csv, re, sys, pathlib
T = pathlib.Path(__file__).resolve().parents[2] / 'targets/ranzo1528'
n, rpath = sys.argv[1], sys.argv[2]
key = {r['code']: r for r in csv.DictReader(open(T / 'lasry/key.tsv', encoding='utf-8-sig'), delimiter='\t')}
ros = {}
for r in csv.DictReader(open(rpath, encoding='utf-8'), delimiter='\t'):
    if r['value'] and r['value'] != '_' and r['class'] != 'null': ros[r['group']] = (r['value'], r['class'])
norm = lambda v: v.rstrip('?').lower()
for line in open(T / f'texts/biermann_transcription_letter{n}.txt', encoding='utf-8'):
    if not line.startswith(f'{n}:'): continue
    lid, content = line.rstrip('\n').split('\t')
    out = []
    for t in content.split():
        r = key.get(t); rv = ros.get(t)
        if r:
            v = r['value'].rstrip('?')
            if r['status'].startswith('strong') or int(r['count']) >= 3: out.append(v)
            elif rv and norm(rv[0]) == norm(v): out.append(v)
            elif rv: out.append('<%s?|R:%s>' % (v, rv[0]))
            else: out.append('<%s?>' % v)
        elif re.fullmatch(r'[A-Za-z]\d+', t):
            out.append('[%s|R:%s]' % (t, rv[0]) if rv else '[%s]' % t)
        else: out.append('"%s"' % t)
    print(lid + '\t' + '.'.join(out))
