"""KWIC: every occurrence of the given groups in the letter, with 6 units each side under the current key."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
key = {}
for line in open(os.path.join(HERE, 'key1761.tsv'), encoding='utf8'):
    if line[:1].isdigit():
        g, v = line.split('\t')[:2]
        if v != '?':
            key[g] = v.split(' ')[0].replace('?', '')
t = open(os.path.join(HERE, 'transcription.txt'), encoding='utf8').read()
body = [m.group(2) for m in (re.match(r'(l\d+|c\d+):(.*)', l) for l in t.splitlines()) if m]
s = ' '.join(body).replace('+', '').replace('?', '')
toks = []
for m in re.finditer(r'\{([^}]*)\}|(\d+)|([;.])', s):
    if m.group(1) is not None:
        toks.append(('«' + m.group(1)[-25:] + '»', None))
    elif m.group(3):
        toks.append((m.group(3), None))
    else:
        toks.append((key.get(m.group(2), '[' + m.group(2) + ']'), m.group(2)))
W = int(os.environ.get('W', 6))
for g in sys.argv[1:]:
    print(f'== {g} ({key.get(g, "?")})')
    for i, (v, gg) in enumerate(toks):
        if gg == g:
            L = ' '.join(x for x, _ in toks[max(0, i - W):i]); R = ' '.join(x for x, _ in toks[i + 1:i + 1 + W])
            print(f'   {L:>55} <{g}> {R}')
