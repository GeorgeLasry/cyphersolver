"""King Carlos's 1903 code telegrams (ANTT PT/TT/CAM/M12): group counts, repeats, shared groups and controls.

    python groups.py

Reads the *_transcription.txt files next to this script (lines starting with # are comments; a trailing ? on a
group marks a doubtful digit and is dropped here). Standard library only.
"""
import collections, pathlib, random, re

HERE = pathlib.Path(__file__).resolve().parent
FILES = {'m0054': 'm0054_transcription.txt', 'm0056': 'm0056_transcription.txt', 'm0058': 'm0058_transcription.txt'}


def groups(name):
    out = []
    for line in (HERE / FILES[name]).read_text(encoding='utf-8').splitlines():
        if line.lstrip().startswith('#'):
            continue
        out += [t.strip('.?') for t in line.split() if re.fullmatch(r'\d+[.?]*', t)]
    return out


G = {k: groups(k) for k in FILES}
SHORT = {'03'}
for k, v in G.items():
    c = collections.Counter(v)
    five = [g for g in v if g not in SHORT]
    print(f'{k}: {len(v)} items ({len(five)} five-digit groups), repeats inside: '
          f'{ {g: n for g, n in c.items() if n > 1 and g not in SHORT} }')

print('\nshared five-digit groups:')
keys = list(G)
for i in range(len(keys)):
    for j in range(i + 1, len(keys)):
        s = sorted((set(G[keys[i]]) & set(G[keys[j]])) - SHORT)
        print(f'  {keys[i]} & {keys[j]}: {s}')

# control 1: how often do random five-digit telegrams of the same sizes share two or more groups?
random.seed(1)
trials = 20000
hits = sum(len({random.randint(10000, 99999) for _ in range(12)} & {random.randint(10000, 99999) for _ in range(44)}) >= 2
           for _ in range(trials))
print(f'\ncontrol: P(>=2 shared groups between random 12- and 44-group telegrams) = {hits / trials:.5f}')

# the m0054 alignment: the repeats stand where "ter ... com" repeats in the decode of the time (m0060)
g = [x for x in G['m0054']]
pos = collections.defaultdict(list)
for i, x in enumerate(g, 1):
    pos[x].append(i)
print('\nm0054 repeats (group: positions):', {x: p for x, p in pos.items() if len(p) > 1})
words = 'po des dar mas so depois de ter combinado com ros a e ella ter fallado com governo francez'.split()
wpos = collections.defaultdict(list)
for i, w in enumerate(words, 1):
    wpos[w].append(i)
print('decode words that repeat (word: positions):', {w: p for w, p in wpos.items() if len(p) > 1})
print('both repeat pairs are 6 apart in the groups (5/11, 7/13) and 7 apart in the words (8/15, 10/17):')
print('  one group in each stretch carries two words, and "ter" sits two places before "com" in both')

# control 2 (m0058): do the 60 digits encode the 60 letters of the decode one for one?
pt = 'icitousettoutbientaiecritamaltetembrasseetlespetitssaluetous'
ct = ''.join(G['m0058'][1:])
assert len(pt) == len(ct) == 60


def conflicts(p, c):
    m = collections.defaultdict(collections.Counter)
    for a, b in zip(p, c):
        m[a][b] += 1
    return sum(sum(v.values()) - max(v.values()) for v in m.values())


real = conflicts(pt, ct)
random.seed(0)
sh = list(ct)
ctrl = []
for _ in range(1000):
    random.shuffle(sh)
    ctrl.append(conflicts(pt, sh))
print(f'\nm0058 letter-for-digit test: {real} conflicts; 1000 shuffled digit orders: mean '
      f'{sum(ctrl) / len(ctrl):.1f}, min {min(ctrl)}. No better than chance: a code, not a letter cipher.')
