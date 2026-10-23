"""r2g: print each figure line of a DECODE transcription with both letters of each figure (alessandrino key).
usage: r2g_show.py <transcription>"""
import sys, re
P = {'1': 'ut', '2': 'im', '3': 'fg', '4': 'al', '5': 'os', '6': 'en', '7': 'dr', '8': 'bc', '9': 'pz'}
for n, line in enumerate([l for l in open(sys.argv[1], encoding='utf8') if not l.startswith('#') and l.strip()], 1):
    toks = line.split()
    out = []
    for t in toks:
        d = re.sub(r'[^0-9]', '', t)
        if '^.' in t or '_.' in t: out.append('<%s.>' % d)
        elif d == '0': out.append('.')
        elif d: out.append(''.join(P[c] for c in d))
        else: out.append('?')
    print('%2d %s' % (n, line.strip()))
    print('   ' + ' '.join(out))
