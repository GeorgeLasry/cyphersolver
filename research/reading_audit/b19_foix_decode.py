"""b19 (foix1563): decode R9241 from Lawrence Beck's sign transcription (texts/beck_transcription.txt) with his key v13
(beck-preliminary/data/key.json) plus the word values of de Foix's 1565 cipher (r9241_foix1565key/key_k0.json, Tomokiyo's
chart checked on BnF fr. 15971) for the number signs Beck left open, and the b19 per-sign corrections (CORR below,
each with its evidence in texts/R9241_corrections.tsv). Writes texts/R9241_decode.txt: per line, label=value tokens,
then the passage literal.

    python research/reading_audit/b19_foix_decode.py
"""
import json, pathlib
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'foix1563'
K = dict(json.load(open(T / 'beck-preliminary' / 'data' / 'key.json', encoding='utf8'))['key'])
# 1565 key (K0) word signs for the numbers Beck did not value (10 dict, 26 bien, 34 tant, 40 faict, 70 toute, 82 ceulx,
# 37 me/car): independent of R9241.
K0_WORDS = {'10': 'dict', '26': 'bien', '34': 'tant', '40': 'faict', '70': 'toute', '82': 'ceulx', '37': 'me'}
for k, v in K0_WORDS.items():
    K.setdefault(k, v)
CORR = {}   # (line, index) -> value; filled from texts/R9241_corrections.tsv
cf = T / 'texts' / 'R9241_corrections.tsv'
if cf.exists():
    for row in cf.read_text(encoding='utf8').splitlines()[1:]:
        f = row.split('\t')
        if len(f) >= 5 and f[0] and f[3] != '':
            CORR[(f[0], int(f[1]))] = f[3] if f[3] != '-' else ''
out = ['# R9241 decode (b19): Beck transcription, Beck key v13 + 1565-key word signs (10 dict, 26 bien, 34 tant, 40 faict,',
       '# 70 toute, 82 ceulx, 37 me) + per-sign corrections (texts/R9241_corrections.tsv). label=value; ? = no value.']
lit = {}
for line in open(T / 'texts' / 'beck_transcription.txt', encoding='utf8'):
    if line.startswith('#') or not line.strip():
        continue
    lid, pas, signs = line.rstrip('\n').split('\t')
    toks = []
    for i, s in enumerate(signs.split()):
        v = CORR.get((lid, i), K.get(s))
        toks.append('%s=%s' % (s, v if v is not None else '?'))
        lit.setdefault(pas, []).append(v if v is not None else '[%s]' % s)
    out.append('%s\t%s' % (lid, ' '.join(toks)))
for p in sorted(lit):
    out.append('# passage %s literal: %s' % (p, ''.join(lit[p])))
(T / 'texts' / 'R9241_decode.txt').write_text('\n'.join(out) + '\n', encoding='utf8')
for p in sorted(lit):
    print(p, ''.join(lit[p]))
