"""Decode the sample of AGS PTR leg. 52 doc. 124 with the key excerpt, and run two controls.

    python decode_sample.py            writes sample_decryption.txt and prints the controls

Standard library only. Code groups are between < > in sample_transcription.txt; script forms are turned into
Roman numerals (jV = M, dar = DCCC, da = DCC, dc = DC, ar = CCC), then into numbers, then looked up in
key_excerpt.tsv. Groups the excerpt does not hold are printed as [?number].
"""
import pathlib, random, re

HERE = pathlib.Path(__file__).resolve().parent
KEY = {}
for line in (HERE / 'key_excerpt.tsv').read_text(encoding='utf-8').splitlines():
    if line.startswith('#') or line.startswith('number'): continue
    n, roman, value, *_ = line.split('\t')
    KEY[int(n)] = value

def to_roman(group):
    g = group.replace('?', '').replace(' ', '')
    if g.isupper(): return g
    for a, b in (('jV', 'M'), ('dar', 'DCCC'), ('da', 'DCC'), ('dc', 'DC'), ('ar', 'CCC'), ('d', 'D'), ('j', 'i')):
        g = g.replace(a, b)
    return g.upper()

def rom(s):
    v = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return sum(-v[a] if b in v and v[a] < v[b] else v[a] for a, b in zip(s, s[1:] + ' '))

def lines():
    out, buf = [], ''
    for line in (HERE / 'sample_transcription.txt').read_text(encoding='utf-8').splitlines():
        if line.startswith('#') or not line.strip(): continue
        tag, text = line.split(None, 1)
        out.append((tag, text))
    return out

def groups_of(text):
    return re.findall(r'<([^>]*)>', text)

def render(text, key, shift=0, perm=None):
    it = iter(perm) if perm else None
    def rep(m):
        g = next(it) if it else m.group(1)
        n = rom(to_roman(g)) + shift
        doubt = '?' if '?' in g else ''
        return '{' + key[n] + doubt + '}' if n in key else f'[?{n}]'
    return re.sub(r'<([^>]*)>', rep, text)

# join the groups that run over a line end (p1.7 "<jVar" + p1.8 "xxix>")
L = lines()
joined = []
for tag, text in L:
    if joined and joined[-1][1].count('<') > joined[-1][1].count('>'):
        joined[-1] = (joined[-1][0] + '/' + tag, joined[-1][1] + ' ' + text)
    else:
        joined.append((tag, text))

out = ['# Line-by-line decryption of sample_transcription.txt with key_excerpt.tsv (decode_sample.py).',
       '# T = transcription, D = decryption: code values in { }, groups the excerpt does not hold as [?number].', '']
for tag, text in joined:
    out += [f'{tag} T  {text}', f'{tag} D  {render(text, KEY)}', '']
(HERE / 'sample_decryption.txt').write_text('\n'.join(out), encoding='utf-8')
print('\n'.join(out))

# controls on p.1 ll. 6-8: the key moved by one entry, and the groups shuffled
p1 = ' '.join(t for tag, t in joined if tag.startswith('p1'))
print('CONTROL shift -1:', render(p1, KEY, -1))
print('CONTROL shift +1:', render(p1, KEY, +1))
random.seed(1)
gs = groups_of(p1)
for i in range(2):
    p = gs[:]; random.shuffle(p)
    print(f'CONTROL shuffle {i}:', render(p1, KEY, perm=p))
