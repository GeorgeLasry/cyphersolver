"""Two checks on the alphabetical-order hypothesis for the code table, and candidates for the open report groups.

1. Order test: take the firm table entries in group order, normalise each value (accents off, letters only) and count
   the adjacent pairs that are in alphabetical order (<=). Compare with the same count on shuffled orders. A large
   gap supports "roughly alphabetical"; the pairs out of order show where the blocks restart (syllables, then words).
2. Slot candidates: for each open group in the report, the words of the French lexicon (lang/lexicons/fr.json.gz,
   period-normalised, count >= 20) that sort between the nearest firm neighbours below and above. Candidates are
   not readings: the table's blocks restart (syllables, then words), so a slot can also hold a word of another
   block. Output: decryption/slot_candidates.txt.

    python slotsearch.py
"""
import gzip
import json
import os
import random
import re
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = re.sub(r'[^a-z]', '', ''.join(c for c in s if not unicodedata.combining(c)))
    return s.replace('j', 'i').replace('v', 'u')      # the lexicon is normalised 'early' (j = i, v = u)


table = {}
for line in open(os.path.join(HERE, 'codetable.tsv'), encoding='utf-8'):
    if line[0] != '#' and line.strip():
        g, v, grade = line.split('\t')[:3]
        if grade == 'H' and v != '_' and norm(v):
            table[int(g)] = norm(v)
order = sorted(table)
vals = [table[g] for g in order]


def ordered(seq):
    return sum(1 for a, b in zip(seq, seq[1:]) if a <= b)


pairs = len(vals) - 1
real = ordered(vals)
rnd = random.Random(1)
base = []
for _ in range(200):
    s = vals[:]
    rnd.shuffle(s)
    base.append(ordered(s))
mean = sum(base) / len(base)
sd = (sum((x - mean) ** 2 for x in base) / len(base)) ** 0.5
out = [f'order test: {real} of {pairs} adjacent firm entries in alphabetical order ({real / pairs:.1%}); '
       f'shuffled: mean {mean:.0f} ({mean / pairs:.1%}), sd {sd:.1f}, max {max(base)}; '
       f'real is {(real - mean) / sd:.0f} sd above the shuffles', '']
# where the order breaks: runs
breaks = [(order[i], vals[i], order[i + 1], vals[i + 1]) for i in range(pairs) if vals[i] > vals[i + 1]]
out.append(f'{len(breaks)} breaks (group a value a > group b value b), first 40:')
out += [f'  {a}={va} > {b}={vb}' for a, va, b, vb in breaks[:40]]
out.append('')

lex = json.load(gzip.open(os.path.join(ROOT, 'lang', 'lexicons', 'fr.json.gz'), 'rt', encoding='utf-8'))
words = sorted(w for w, n in lex.items() if n >= 20 and 2 <= len(w) <= 14)
open_groups = {}
for line in open(os.path.join(HERE, 'transcription', 'report_61005_tokens.txt'), encoding='utf-8'):
    if line[0] == '#':
        continue
    label, *gs = line.split()
    for g in gs:
        if int(g) not in table:
            open_groups.setdefault(int(g), []).append(label)
out.append('slot candidates for the open report groups (French words sorting between the neighbours, commonest first; v = u, j = i):')
for g in sorted(open_groups):
    lo = max((k for k in order if k < g), default=None)
    hi = min((k for k in order if k > g), default=None)
    a = table.get(lo, '')
    b = table.get(hi, '~')
    if a <= b:
        cands = [w for w in words if a <= w <= b]
        note = ''
    else:     # the neighbours are out of order (a block restarts here): use each bound on its own, same initial letter
        cands = [w for w in words if (w >= a and w[:1] == a[:1]) or (w <= b and w[:1] == b[:1])]
        note = ' [neighbours out of order: words after the lower or before the upper]'
    top = sorted(cands, key=lambda w: -lex[w])[:15]
    out.append(f'{g:>5} {",".join(open_groups[g]):<8} {lo}={a} .. {hi}={b}{note}: {len(cands)} words; commonest: {" ".join(top)}')
text = '\n'.join(out) + '\n'
open(os.path.join(HERE, 'decryption', 'slot_candidates.txt'), 'w', encoding='utf-8').write(
    '# Output of slotsearch.py (28 Oct 2026). Candidates are slots, not readings.\n' + text)
print(text)
