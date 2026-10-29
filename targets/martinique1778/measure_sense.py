"""Measured proxy for 'reads as sense' on the 1778 letter, same method as targets/mercier1761/measure_sense.py but STRICTER:
the decoded text is cut at every unvalued group, so a valued stretch must segment into dictionary words by itself
(the 1761 version let words span an unvalued gap). Key: key_bouille.tsv (first value of each group; conflicting groups use
the value given first). A token counts as sense when every character it yields lies inside a dictionary word of length >= 2
(or a, y, or an elided l' d' n' s' c' j' m' t' before a vowel). Words are fr-gutenberg (wordscore.py of mercier1761)
plus the declared additions below. Prints the share and the failing groups."""
import os, re, sys, math, collections
HERE = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(HERE, '..', 'mercier1761')
sys.path.insert(0, M); sys.path.insert(0, os.path.join(HERE, '..', '..'))
from solve import norm
import wordscore
key = {}
for l in open(os.path.join(HERE, 'key_bouille.tsv'), encoding='utf8'):
    if l[:1].isdigit():
        g, v = l.split('\t')[:2]
        key[g] = norm(v.split('/')[0].replace('?', '').replace('M.', 'monsieur').replace('1er', 'premier'))
wordscore.HERE = r'C:/Users/dbour/cypher/targets/mercier1761'   # corpora are not checked out in cyph-merge; read-only use of the main checkout's lang/corpora
words = wordscore.load_words()
# declared additions: words of the letters (period spellings, proper nouns) missing from the corpus sample
for w in ['martinique', 'guadeloupe', 'garnison', 'hopital', 'hopitaux', 'recrues', 'recrue', 'escadre', 'deffense', 'deffendre',
          'moitie', 'troupes', 'premier', 'mois', 'etat', 'situation', 'colonie', 'critiques', 'honneur', 'compte', 'vous', 'isle']:
    words.setdefault(norm(w), -8.0)
for w in ['l', 'd', 'n', 's', 'c', 'j', 'm', 't']: words[w] = -9.0
toks = [t for l in open(os.path.join(HERE, 'transcription.txt'), encoding='utf8') if l[0] != '#' for t in l.split()]
# runs of valued tokens only
runs, cur = [], []
for g in toks:
    if g in key: cur.append(g)
    else:
        if cur: runs.append(cur); cur = []
if cur: runs.append(cur)
ok = 0; fails = []
for run in runs:
    text, spans = '', []
    for g in run:
        a = len(text); text += key[g]; spans.append((g, a, len(text)))
    n = len(text); best = [0.0] + [-math.inf] * n; back = [None] * (n + 1)
    for i in range(n):
        if best[i] == -math.inf: continue
        if best[i] - 12 > best[i + 1]: best[i + 1], back[i + 1] = best[i] - 12, (i, False)
        for j in range(i + 1, min(n, i + 25) + 1):
            w = words.get(text[i:j])
            if w is not None and (j - i >= 2 or text[i:j] in ('a', 'y') or (text[i:j] in 'ldnscjmt' and j < n and text[j] in 'aeiouyh')) and best[i] + w > best[j]:
                best[j], back[j] = best[i] + w, (i, True)
    good = [False] * n; k = n
    while k:
        i, isw = back[k]
        if isw:
            for c in range(i, k): good[c] = True
        k = i
    for g, a, b in spans:
        if b > a and all(good[a:b]): ok += 1
        else: fails.append(g)
tot = len(toks)
print('tokens', tot, 'valued', sum(t in key for t in toks), '= %.1f%%' % (100 * sum(t in key for t in toks) / tot))
print('sense proxy (strict, runs cut at unvalued groups): %d/%d tokens = %.1f%%' % (ok, tot, 100 * ok / tot))
print('valued but failing:', collections.Counter(fails).most_common(30))
