"""b22: nunzio1718, one line per cipher line of Lasry's decode rows (lasry/364D-<n>.txt): the DECODE transcriber's
PLAINTEXT line (the interlinear as copied in 2016), the figures, and Lasry's decode joined, with key_extra.txt filling
<NNNN> codes. Used as a scaffold while transcribing the interlinear decipherment from the images.

    python research/reading_audit/b22_nunzio_lines.py <n> [json_out]
"""
import json, re, sys, pathlib
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'nunzio1718'
n = sys.argv[1]
extra = {}
for ln in open(T / 'key_extra.txt', encoding='utf-8'):
    m = re.match(r'^(\d{4})\s*=\s*(.+)$', ln.strip())
    if m: extra[m.group(1)] = m.group(2).strip()
L = open(T / 'lasry' / f'364D-{n}.txt', encoding='utf-8', errors='replace').read().splitlines()


def cols(a):
    starts = []; prev_end = -2
    for m in re.finditer(r'\S+', a):
        if m.start() > prev_end + 1: starts.append(m.start())
        prev_end = m.end() - 1
    starts.append(len(a)); return starts


out = []; pt = ''; img = ''
for i in range(len(L) - 1):
    a, b = L[i], L[i + 1]
    m = re.match(r'#IMAGE NAME:\s*(.+)', a)
    if m: img = m.group(1).strip()
    m = re.match(r'<PLAINTEXT IT (.*)>', a)
    if m: pt = m.group(1); continue
    if not (a.rstrip().endswith('|') and b.rstrip().endswith('|')) or not re.match(r'^\s*\d', a): continue
    s = cols(a); toks = []
    for j in range(len(s) - 1):
        ct = a[s[j]:s[j + 1]].strip(); p = b[s[j]:s[j + 1]].strip() if s[j] < len(b) else ''
        if ct in ('|', ''): continue
        if re.fullmatch(r'<\d{4}>', p) and ct in extra: p = extra[ct] + '*'
        toks.append((ct, p))
    out.append(dict(img=img, pt=pt, toks=toks)); pt = ''
for k, r in enumerate(out):
    dec = ''.join(('' if p == '_' else (p if len(p) == 1 else ' %s ' % p)) for c, p in r['toks'])
    print('%02d [%s] PT: %s' % (k + 1, r['img'], r['pt']))
    print('   FIG:', ' '.join(c for c, p in r['toks']))
    print('   DEC:', re.sub(r'\s+', ' ', dec))
if len(sys.argv) > 2:
    json.dump(out, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
