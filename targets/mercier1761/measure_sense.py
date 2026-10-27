"""Measured proxy for 'reads as sense': decode each code run with key1761.tsv, segment the decoded string into
dictionary words (fr-gutenberg + letter vocabulary, wordscore.py) and count a code token as sense when every
character it yields lies inside a dictionary word of length >= 2 (or is a valid one-letter word a/y/à).
Unvalued groups count as not sense. Prints the share and the tokens that fail."""
import os, re, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
from solve import norm
import wordscore
key = {}
for line in open(os.path.join(HERE, 'key1761.tsv'), encoding='utf8'):
    if line[:1].isdigit():
        g, v = line.split('\t')[:2]
        if v != '?':
            key[g] = norm(v.split(' ')[0].replace('?', '').replace('M.', 'monsieur'))
words = wordscore.load_words()
for w in ['beuf', 'aviés', 'payera', 'concernand', 'payemens', 'espagnols', 'eustache', 'choiseul', 'traittes',
          'milliers', 'reviendra', 'faudra', 'survienne', 'serons', 'pouvons', 'decembre']:
    words[norm(w)] = -8.0
segs = []
t = open(os.path.join(HERE, 'transcription.txt'), encoding='utf8').read()
body = [m.group(2) for m in (re.match(r'(l\d+|c\d+):(.*)', l) for l in t.splitlines()) if m]
s = ' '.join(body).replace('+', '').replace('?', '')
runs, cur = [], []
for m in re.finditer(r'\{([^}]*)\}|(\d+)|([;.])', s):
    if m.group(2):
        cur.append(m.group(2))
    else:
        if cur: runs.append(cur); cur = []
if cur: runs.append(cur)
ok = tot = 0
fails = []
for run in runs:
    # decode, remembering char spans per token
    text, spans = '', []
    for g in run:
        v = key.get(g)
        a = len(text)
        if v: text += v
        spans.append((g, a, len(text), v is not None))
    # best segmentation into words (unknown chars cost UNK)
    n = len(text); best = [0.0] + [-math.inf] * n; back = [None] * (n + 1)
    for i in range(n):
        if best[i] == -math.inf: continue
        if best[i] - 12 > best[i + 1]: best[i + 1], back[i + 1] = best[i] - 12, (i, False)
        for j in range(i + 1, min(n, i + 25) + 1):
            w = words.get(text[i:j])
            if w is not None and (j - i >= 2 or text[i:j] in ('a', 'y')) and best[i] + w > best[j]:
                best[j], back[j] = best[i] + w, (i, True)
    good = [False] * n; k = n
    while k:
        i, isw = back[k]
        if isw:
            for c in range(i, k): good[c] = True
        k = i
    for g, a, b, known in spans:
        tot += 1
        if known and b > a and all(good[a:b]):
            ok += 1
        else:
            fails.append(g)
print(f'sense proxy: {ok}/{tot} tokens = {ok / tot:.1%}')
from collections import Counter
print('failing groups:', Counter(fails).most_common(40))
