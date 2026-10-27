"""Render the letter with key1761.tsv as running text: known units joined, unknown groups as [n]."""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
SEP = os.environ.get('SEP', '·')
key = {}
for line in open(os.path.join(HERE, 'key1761.tsv'), encoding='utf8'):
    if line[:1].isdigit():
        g, v = line.split('\t')[:2]
        if v != '?':
            key[g] = v.split(' ')[0].replace('?', '')
t = open(os.path.join(HERE, 'transcription.txt'), encoding='utf8').read()
body = []
for line in t.splitlines():
    m = re.match(r'(l\d+|c\d+):(.*)', line)
    if m:
        body.append(m.group(2))
s = ' '.join(body).replace('+', '').replace('?', '')
out = []
for t in re.finditer(r'\{([^}]*)\}|(\d+)|([;.])', s):
    if t.group(1) is not None:
        out.append(' «' + t.group(1)[-60:] + '» ')
    elif t.group(3):
        out.append(t.group(3) + ' ')
    else:
        g = t.group(2)
        out.append(key.get(g, f'[{g}]') + SEP)
print(''.join(out))
