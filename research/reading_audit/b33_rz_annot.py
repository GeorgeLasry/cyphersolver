"""b33 (ranzo1528, letter 4 = BnF fr. 4050 ff. 79-81): annotate Biermann's transcription with George Lasry's key by
key status: strong values plain; tentative values seen 3+ times in the five letters plain (they hold across their
occurrences, checked in the reread log); tentative values seen once or twice as <value?>; codes without a value as
[code]. Clear words (Biermann's transcription) kept. Output: one line per manuscript line, groups separated by '.'.

    python research/reading_audit/b33_rz_annot.py > <out>
"""
import csv, re, pathlib
T = pathlib.Path(__file__).resolve().parents[2] / 'targets/ranzo1528'
key = {r['code']: r for r in csv.DictReader(open(T / 'lasry/key.tsv', encoding='utf-8-sig'), delimiter='\t')}
for line in open(T / 'texts/biermann_transcription_letter4.txt', encoding='utf-8'):
    if not line.startswith('4:'): continue
    lid, content = line.rstrip('\n').split('\t')
    out = []
    for t in content.split():
        r = key.get(t)
        if r:
            v = r['value'].rstrip('?')
            out.append(v if r['status'].startswith('strong') or int(r['count']) >= 3 else '<%s?>' % v)
        elif re.fullmatch(r'[A-Za-z]\d+', t): out.append('[%s]' % t)
        else: out.append('"%s"' % t)
    print(lid + '\t' + '.'.join(out))
