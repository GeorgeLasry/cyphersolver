"""b27: compare the code groups of esp318no94 (Brackx's transcription and readings) with Bergenroth's Gran cifra list.

    python research/reading_audit/b27_esp94_berg.py

Reads targets/esp318no94/ct94_brackx.txt and targets/esp318no94/texts/bergenroth_gran_cifra_codes.tsv. Spellings are
compared with the minim letters folded (n = u = v, m kept) and y = q (both descender letters in this hand).
"""
import collections, pathlib, re
R = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'esp318no94'
FIRM = dict(qa='que', rah='y', mny='de', qag='se', mys='en', mnb='la', pif='no', nae='los', nyb='lo', lux='como',
            pat='por', qe='quando', nyl='havía', gik='su', reg='yo', mnh='gente', qaz='V. Al.', pns='Puerto')
TENT = dict(mog='a', lik='buena', pnb='antes', pad='bien', re='esto', mok='dar', mas='el', pit='contra', leg='ellos',
            nag='más', neb='hazer', per='para', nob='dicho', mos='ellos')
c = collections.Counter()
for l in open(R / 'ct94_brackx.txt', encoding='utf8'):
    if l.startswith('#'): continue
    for t in re.sub(r'\{[^}]*\}', '', l).split():
        if re.fullmatch(r'[a-z]{2,4}', t): c[t] += 1
berg = collections.defaultdict(set)
for l in open(R / 'texts' / 'bergenroth_gran_cifra_codes.tsv', encoding='utf8'):
    if l.startswith('#') or l.startswith('group'): continue
    g, m, _ = l.rstrip('\n').split('\t')
    for x in g.split('/'): berg[x].add(m)
fold = lambda s: s.replace('v', 'n').replace('u', 'n').replace('y', 'q')
bf = collections.defaultdict(set)
for g, ms in berg.items(): bf[fold(g)] |= {f'{g}={m}' for m in ms}
print('A. same meaning, firm in no. 94: Brackx group vs Bergenroth group(s)')
agree = 0
for g, m in FIRM.items():
    bg = sorted(x for x, ms in berg.items() if any(mm.split('?')[0] == m for mm in ms))
    ok = any(fold(x) == fold(g) for x in bg)
    agree += ok
    print(f'  {g:5} {m:8} x{c[g]:<3} Bergenroth: {", ".join(bg) or "-":20} {"AGREE" if ok else ("differ" if bg else "")}')
print('  agreements:', agree)
print('B. no. 94 groups whose spelling (minims folded) is a Bergenroth group')
for g, n in c.most_common():
    if fold(g) in bf:
        rd = FIRM.get(g) or (TENT.get(g, '') + '?' if g in TENT else 'open')
        print(f'  {g:5} x{n:<3} no. 94: {rd:10} Bergenroth: {", ".join(sorted(bf[fold(g)]))}')
