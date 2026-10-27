"""King Manuel II's code telegrams of August 1910 (ANTT PT/TT/CAM/M13): counts, repeats, shared groups.

    python groups.py

Reads the *_transcription.txt files next to this script (lines starting with # are comments; a trailing ? on a
group marks a doubtful digit and is dropped here; 47183 in m0021 is taken as corrected to 97183, as the receiver
wrote). Standard library only.
"""
import collections, pathlib, random, re

HERE = pathlib.Path(__file__).resolve().parent
FILES = {'m0015 (8 Aug 1910)': 'm0015_transcription.txt', 'm0019 (2 Aug 1910)': 'm0019_transcription.txt',
         'm0021 (2 Aug 1910)': 'm0021_transcription.txt'}
SHORT = {'05', '06'}


def groups(name):
    out = []
    for line in (HERE / name).read_text(encoding='utf-8').splitlines():
        if not line.lstrip().startswith('#'):
            out += [t.strip('?') for t in line.split() if re.fullmatch(r'\d+\??', t)]
    return ['97183' if g == '47183' else g for g in out]


G = {k: groups(f) for k, f in FILES.items()}
for k, v in G.items():
    c = collections.Counter(v)
    print(f'{k}: {len(v)} items, short items {dict((g, n) for g, n in c.items() if g in SHORT)}, '
          f'repeats {dict((g, n) for g, n in c.items() if n > 1 and g not in SHORT)}')
keys = list(G)
print('\nshared groups:')
for i in range(len(keys)):
    for j in range(i + 1, len(keys)):
        print(f'  {keys[i]} & {keys[j]}: {sorted((set(G[keys[i]]) & set(G[keys[j]])) - SHORT)}')

print('\nopening code runs after the same clear words "Tudo bem tempo lindo":')
print('  m0015:', ' '.join(G[keys[0]][:8]))
print('  m0021:', ' '.join(G[keys[2]][:7]), '  (after "veio Sabugosa hoje")')

random.seed(3)
trials = 20000
hits = sum(len({random.randint(0, 99999) for _ in range(36)} & {random.randint(0, 99999) for _ in range(54)}) >= 2
           for _ in range(trials))
print(f'\ncontrol: P(>=2 shared groups between random 36- and 54-group telegrams over 00000-99999) = {hits / trials:.5f}')
