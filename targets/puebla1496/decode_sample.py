"""Decode the sample of AGS PTR leg. 52 doc. 47 f. 396r with the key excerpt, and run the controls.

    python decode_sample.py            writes sample_decryption.txt and prints the controls

Standard library only. Code groups are between < > in sample_transcription.txt, as Roman numerals; they are turned
into numbers and looked up in key_excerpt.tsv. Groups the excerpt does not hold are printed as [?number], groups not
read as [?].
"""
import pathlib, random, re

HERE = pathlib.Path(__file__).resolve().parent
KEY = {}
for line in (HERE / 'key_excerpt.tsv').read_text(encoding='utf-8').splitlines():
    if line.startswith('#') or line.startswith('number'): continue
    n, roman, value, *_ = line.split('\t')
    KEY[int(n)] = value

def rom(s):
    v = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return sum(-v[a] if b in v and v[a] < v[b] else v[a] for a, b in zip(s, s[1:] + ' '))

def render(text, key, shift=0, perm=None, cmap=None):
    it = iter(perm) if perm else None
    def rep(m):
        g = next(it) if it else m.group(1)
        r = g.replace('?', '').strip()
        if not r: return '[?]'
        if cmap: r = cmap(r)
        n = rom(r) + shift
        doubt = '?' if '?' in g else ''
        return '{' + key[n] + doubt + '}' if n in key else f'[?{n}]'
    return re.sub(r'<([^>]*)>', rep, text)

L = []
for line in (HERE / 'sample_transcription.txt').read_text(encoding='utf-8').splitlines():
    if line.startswith('#') or not line.strip(): continue
    tag, text = line.split(None, 1)
    L.append((tag, text))

out = ['# Line-by-line decryption of sample_transcription.txt with key_excerpt.tsv (decode_sample.py).',
       '# T = transcription, D = decryption: code values in { }, groups the excerpt does not hold as [?number].', '']
for tag, text in L:
    out += [f'{tag} T  {text}', f'{tag} D  {render(text, KEY)}', '']
(HERE / 'sample_decryption.txt').write_text('\n'.join(out), encoding='utf-8')
print('\n'.join(out))

# controls on the heading and lines 1-2 (the securely read groups)
secure = ' '.join(t for tag, t in L if tag in ('H', 'L1', 'L2'))
for s in (-1, 1, -7, 13):
    print(f'CONTROL shift {s:+d}:', render(secure, KEY, s))
print('CONTROL every C ligature read as CC:', render(secure, KEY, cmap=lambda g: re.sub('C{3,4}', 'CC', g)))
random.seed(1)
gs = re.findall(r'<([^>]*)>', secure)
for i in range(3):
    p = gs[:]; random.shuffle(p)
    print(f'CONTROL shuffle {i}:', render(secure, KEY, perm=p))
