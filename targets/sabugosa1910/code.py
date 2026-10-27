"""Sabugosa's code (ANTT PT/TT/CAM/M14): values from the decodes of the time, an order test, and m0014.

    python code.py            print the values, the order test with its control, and m0014 with the values
    python code.py --write    also rewrite code_values.tsv from the aligned decryption files

The values come from the three group-by-group files m0010_decryption.txt, m0012_decryption.txt and
m0016_decryption.txt (lines "group  word  [notes]"), which pair the groups with the decodes written at the time
(m0008, m0005 + m0004, m0009). Grades as in the README: C = from a decode of the time, one group to one word;
M = the decoder marked it doubtful, or it stands out of alphabetical place; I = our inference (how a decoded word
splits over groups). Standard library only.
"""
import collections, pathlib, random, re, sys, unicodedata

HERE = pathlib.Path(__file__).resolve().parent
SOURCES = {'m0016_decryption.txt': 'm0016/m0009 (24 Apr 1904)', 'm0010_decryption.txt': 'm0010/m0008 (21 May 1910)',
           'm0012_decryption.txt': 'm0012-13/m0005+m0004 (24 May 1910)'}
LINE = re.compile(r'^(\d{3,5})\s+(.*)$')


def parse(name):
    out = []
    for line in (HERE / name).read_text(encoding='utf-8').splitlines():
        m = LINE.match(line.strip())
        if not m:
            continue
        group, rest = m.group(1), m.group(2)
        word = re.split(r'\s*[\[(]', rest)[0].strip().strip('-').strip()
        doubtful = '?' in rest and not rest.startswith('[?]')
        word = word.rstrip(' ?').strip('-')
        if rest.startswith('[?]'):
            word = ''
        grade = 'C'
        if 'inferred' in rest or word in ('So', 'ver', 'al') and name != 'm0012_decryption.txt':
            grade = 'I'
        if doubtful or 'alphabetical place' in rest or '(c)' in rest and '?' in rest:
            grade = 'M'
        out.append((group, word, grade))
    return out


def sort_key(word):
    w = {'á noite': 'noite', 'S. M. ElRei': 's m elrei'}.get(word, word)
    w = unicodedata.normalize('NFD', w.lower())
    return ''.join(ch for ch in w if not unicodedata.combining(ch))


values = collections.OrderedDict()
conflicts = []
for name, src in SOURCES.items():
    for group, word, grade in parse(name):
        if not word:
            continue
        if group in values and values[group][0].lower() != word.lower():
            conflicts.append((group, values[group][0], word, src))
            continue
        if group not in values:
            values[group] = [word, grade, src]
        elif grade < values[group][1]:          # keep the better grade (C < I < M alphabetically)
            values[group][1] = grade

print(f'{len(values)} groups with a value; conflicts between decodes: {conflicts or "none"}')

# order test: within each series (4-digit, 5-digit), do the numbers run in alphabetical order of the words?
def inversions(pairs):
    pairs = sorted(pairs)
    keys = [k for _, k in pairs]
    return sum(1 for i in range(len(keys)) for j in range(i + 1, len(keys)) if keys[i] > keys[j])


random.seed(7)
for label, test in (('4-digit (below 10000)', lambda g: int(g) < 10000), ('5-digit (10000 and up)', lambda g: int(g) >= 10000)):
    for which in ('all values', 'grade C only'):
        pairs = [(int(g), sort_key(v[0])) for g, v in values.items() if test(g) and (which == 'all values' or v[1] == 'C')]
        n = len(pairs)
        real = inversions(pairs)
        nums = [p[0] for p in pairs]
        keys = [p[1] for p in pairs]
        ctrl = []
        for _ in range(2000):
            random.shuffle(keys)
            ctrl.append(inversions(list(zip(nums, keys))))
        print(f'{label}, {which}: {n} values, {real} pairs out of alphabetical order of {n * (n - 1) // 2}; '
              f'2000 shuffles: mean {sum(ctrl) / len(ctrl):.1f}, min {min(ctrl)}')

out_of_order = []
for label, test in (('4', lambda g: int(g) < 10000), ('5', lambda g: int(g) >= 10000)):
    items = sorted((int(g), sort_key(v[0]), g) for g, v in values.items() if test(g) and v[1] != 'M')
    for i, (num, key, g) in enumerate(items):
        bad = sum(1 for j, (n2, k2, _) in enumerate(items) if (j < i and k2 > key) or (j > i and k2 < key))
        if bad:
            out_of_order.append((g, values[g][0], bad))
print('grade C and I values out of alphabetical place (group, word, pairs):', out_of_order)
print('grade M values (decoder doubtful or out of place):', [(g, v[0]) for g, v in values.items() if v[1] == 'M'])

# apply to m0014 (13 May 1903, no decode)
groups = []
for line in (HERE / 'm0014_transcription.txt').read_text(encoding='utf-8').splitlines():
    if not line.startswith('#'):
        groups += [t.strip('?') for t in line.split()]
hits = [(i + 1, g, values[g][0]) for i, g in enumerate(groups) if g in values]
print(f'\nm0014: {len(groups)} groups, {len(hits)} with a value: {hits}')
print('  m0014 groups, with the alphabetical neighbours of each (word before < group < word after):')
known = sorted((int(g), v[0]) for g, v in values.items())
for g in groups:
    if g in values:
        continue
    n = int(g)
    series = [k for k in known if (k[0] < 10000) == (n < 10000)]
    lo = max((k for k in series if k[0] < n), default=(None, '(start)'))
    hi = min((k for k in series if k[0] > n), default=(None, '(end)'))
    print(f'    {g:>5}: {lo[1]} .. {hi[1]}')

if '--write' in sys.argv:
    rows = ['group\tvalue\tgrade\tsource']
    for g in sorted(values, key=int):
        rows.append(f'{g}\t{values[g][0]}\t{values[g][1]}\t{values[g][2]}')
    (HERE / 'code_values.tsv').write_bytes(('\n'.join(rows) + '\n').encode('utf-8'))  # LF on every platform
    print('\nwrote code_values.tsv')
