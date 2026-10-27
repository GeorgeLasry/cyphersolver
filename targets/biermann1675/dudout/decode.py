# Decoder: frozen K55 (SHA-256 checked) + justified additions. Usage: python decode.py texts/<letter>_transcription.txt
import sys, os, hashlib
here = os.path.dirname(os.path.abspath(__file__))
kp = os.path.join(here, 'key_K55.tsv')
sha = hashlib.sha256(open(kp,'rb').read()).hexdigest()
ref = open(os.path.join(here,'K55.sha256')).read().split()[0]
assert sha == ref, 'K55 file changed'
K = {}
for l in open(kp, encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    t, v, s = l.rstrip('\n').split('\t'); K[t] = v
for f in ('key_K55_additions.tsv',):
    p = os.path.join(here, f)
    if os.path.exists(p):
        for l in open(p, encoding='utf-8'):
            if l.startswith('#') or not l.strip(): continue
            t, v = l.rstrip('\n').split('\t')[:2]; K.setdefault(t, v)
K['9'] = '{r|t|a}'
tot = ok = corr = 0
for line in open(sys.argv[1], encoding='utf-8'):
    line = line.rstrip('\n')
    if not line or line.startswith('#'): print(line); continue
    out = []
    for tok in line.split():
        if tok.startswith('['): out.append(' '+tok.strip('[]').replace('_',' ')+' '); continue
        t = tok.rstrip('?'); tot += 1
        if '=' in t:
            corr += 1; out.append('{'+t.split('=')[1]+'}'); continue
        if t in K: ok += 1; out.append(K[t])
        else: out.append('‹%s›' % t)
    print(line); print('  → ' + ''.join(out))
print('# cipher tokens: %d; valued by K55 (+additions): %d; corrected (TOK=v): %d; no value: %d' % (tot, ok, corr, tot-ok-corr))
