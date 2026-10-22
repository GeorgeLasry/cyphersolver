"""Calibration of the contributed reading of view 22 right against the contemporary decipherment on view 23 right.

Compares contributed/data/decoded_v022r.txt (Harumi-Matsuba's key output) with calib_v023r.txt (the
decipherment as read here by eye), letters only, 'early' normalisation, code words expanded (QUEL/QUIL -> quil).
Agreement = letters of the decipherment matched by difflib's longest-common-subsequence blocks, over the
decipherment's letters; also over the decode's letters.

Run: PYTHONUTF8=1 python targets/fiesque1567/calib.py
"""
import os, re, sys, difflib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
from lang import lm

def letters(s): return re.sub(r'[^a-z]', '', lm.norm(s, 'early'))

ref = ' '.join(l for l in open(os.path.join(HERE, 'calib_v023r.txt'), encoding='utf-8') if not l.startswith('#'))
ref = re.sub(r'\[\?\]', '', ref)
dec = []
for l in open(os.path.join(HERE, 'contributed', 'data', 'decoded_v022r.txt'), encoding='utf-8'):
    if l.startswith('#'): continue
    t = l.split(' ', 1)[1] if ' ' in l else ''
    t = re.sub(r'([A-Z]+)/[A-Z]+', r'\1', t).replace('[?]', '').replace('?', '')
    t = t.replace('QUEL', 'QUIL')          # the code sign stands for qu'il/quel; the decipherment writes qu'il
    dec.append(t)
a, b = letters(ref), letters(' '.join(dec))
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
m = sum(bl.size for bl in sm.get_matching_blocks())
print(f'decipherment letters {len(a)}, decode letters {len(b)}, matched {m}')
print(f'agreement over the decipherment: {m/len(a):.1%}; over the decode: {m/len(b):.1%}')
# words of the decipherment (length >= 3) found in the decode as substrings at the aligned place
words = [letters(w) for w in re.findall(r"[A-Za-z']+", ref.replace("'", ' '))]
words = [w for w in words if len(w) >= 3]
pos, hit = 0, 0
for w in words:
    i = b.find(w, max(0, pos - 30), pos + len(w) + 60)
    if i >= 0: hit += 1; pos = i + len(w)
    else: pos += len(w)
print(f'words of 3+ letters of the decipherment found intact in the decode near their place: {hit}/{len(words)} = {hit/len(words):.1%}')
