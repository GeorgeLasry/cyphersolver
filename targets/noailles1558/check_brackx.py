"""Rebuild the T/V decode of Brackx's issue #113 gist from his transcription and key TSV (our own code)."""
import re, sys, csv
sys.stdout.reconfigure(encoding='utf-8')
B = 'brackx/'
key = {}
for r in csv.DictReader(open(B + 'key_r5.tsv', encoding='utf-8'), delimiter='\t'):
    key[r['label']] = (r['value'], r['status'])
trans = {}
for l in open(B + 'transcription_f60r_f60v.txt', encoding='utf-8'):
    m = re.match(r'^([ABC]\d+): (.*)$', l.rstrip('\n'))
    if m: trans[m.group(1)] = m.group(2).split()
dec = {}; cur = None
for l in open(B + 'decode_tvd_r5.txt', encoding='utf-8'):
    l = l.rstrip('\n')
    if re.match(r'^[ABC]\d+$', l): cur = l; dec[cur] = {}
    elif cur and l[:2] in ('T:', 'V:'): dec[cur][l[0]] = l[2:].split()
n = ok = nk = 0; bad = []
for ln, toks in trans.items():
    d = dec.get(ln)
    if not d: bad.append((ln, 'no decode line')); continue
    if d['T'] != toks: bad.append((ln, 'T differs', len(toks), len(d['T']))); continue
    for t, v in zip(toks, d['V']):
        n += 1
        k = key.get(t)
        mine = '?' if not k else ('{%s}' % k[0] if k[1] == 'tentative' else k[0])
        if mine == '0' or v == '0': mine = '0' if (k and k[0] == '0') else mine
        if mine == v: ok += 1
        else: nk += 1; bad.append((ln, t, 'key', mine, 'decode', v))
print('tokens', n, 'agree', ok, 'differ', nk)
for b in bad[:25]: print(b)
nonnull = [(t, key.get(t)) for ln, toks in trans.items() for t in toks if not (key.get(t) and key[t][0] == '0')]
val = [1 for t, k in nonnull if k and not k[0] == '?']
tent = [1 for t, k in nonnull if k and k[1] == 'tentative']
print('non-null', len(nonnull), 'valued', len(val), f'{100*len(val)/len(nonnull):.1f}%', 'tentative', len(tent))
