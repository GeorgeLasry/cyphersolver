"""b32: decode targets/r9367/r9367/transcription_v2.txt with the extended block 2_4 values (nulls dropped)."""
import re, pathlib
M = dict(q='a', v='b', V='m', T='c', C='s', J='f', o='g', g='g', H='k', w='i', X='u', u='o', A='r', y='s', e='t',
         E='ch', K='z', Z='z', O='b', S='sch', U='ll', P='[Π]', R='[R]', d='[d]', **{'#': '[#]', '+': 'd', '6': 'e',
         '3': 'n', '4': 'h', '8': 'l', '&': '[&]', '?': '[?]', '.': '.', '10': '10', ')': ''})
NULL = set('QWD')
f = pathlib.Path(__file__).resolve().parents[2] / 'targets/r9367/r9367/transcription_v2.txt'
for l in f.read_text(encoding='utf8').splitlines():
    if not re.match(r'(L\d\d|P\d) ', l):
        continue
    tag, rest = l.split(' ', 1)
    rest = rest.split('   (')[0]
    out = []
    for part in re.split(r'(\[[^\]]*\])', rest):
        if part.startswith('['):
            out.append('|' + part[1:-1] + '|'); continue
        s = ''.join(M.get(c, '_') for c in part.split() if c not in NULL)
        if s: out.append('{' + s + '}')
    print(tag, ' '.join(out))
