"""Align the 1798 cipher copy (ct_49.txt) with its clear copy (pt_51.txt) and build a group -> word table.

A group (page,word) stands for one plaintext word, or for one letter when a word is spelled out. Clear words in
the cipher copy match the same plaintext word. Suffixes written after a group (ing, ed, es, est, o) belong to that
group's word. Dynamic programming over (cipher token, plaintext word, letter position) finds the cheapest
alignment; the table it implies is written to table_1798.tsv and the alignment to align_1798.tsv.

    python targets/jones1802/align.py
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
SUFFIXES = {'ing', 'ed', 'es', 'est', 'o', 's', 'd'}
# Hand corrections to the DP alignment, checked on the images: at "India - Government (said he emphatically)"
# the cipher has 169,25. (327,66. 128,24.) with "he" not coded; the DP shifted it by one and gave 169,25 = said.
# 327,66 = said is confirmed by "Force, he said" (152,12. he 327,66.).
OVERRIDES = {'169,25': 'government', '327,66': 'said'}
# Letter codes read off the spelled names (Constantinople, Russians, India). Seeded by hand, then checked by
# the alignment: every spelled word must come out letter for letter.
LETTERS = {'1,1': 'a', '29,10': 'c', '93,66': 'd', '123,1': 'e', '187,63': 'i', '215,23': 'l', '229,28': 'n',
           '256,12': 'o', '266,63': 'p', '305,25': 'r', '327,1': 's', '376,56': 't', '398,16': 'u',
           '161,70': 'g'}  # g learnt by the first alignment from ENGLAND, then seeded


def cipher_tokens(path):
    toks = []
    for line in Path(path).read_text(encoding='utf-8').splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        for raw in re.findall(r'\d+(?:,\d+)*|[A-Za-z]+|[~+]', line.replace('(', ' ').replace(')', ' ')):
            if raw[0].isdigit() and (',' not in raw or re.fullmatch(r'\d{1,3},\d{3}', raw)):
                # a plain number written in clear (a date, a sum, "(12,000)"); word indexes never run to 3 digits
                toks.append(('w', raw))
            elif raw[0].isdigit():
                nums = raw.split(',')
                if len(nums) == 4:  # two groups written without a stop
                    toks.append(('g', ','.join(nums[:2])))
                    toks.append(('g', ','.join(nums[2:])))
                else:
                    toks.append(('g', raw))
            elif raw.lower() in SUFFIXES and toks and toks[-1][0] == 'g':
                toks[-1] = ('g', toks[-1][1], raw.lower())
            else:
                toks.append(('w', raw.lower()))
    return toks


def plain_words(path):
    text = ' '.join(l for l in Path(path).read_text(encoding='utf-8').splitlines() if not l.startswith('#'))
    return [w.lower() for w in re.findall(r"[A-Za-z0-9']+", text)]


def letter_cost(group, ch):
    """Cost of reading group as letter ch: cheap when it is the known letter code, dearer when the group is
    not a known letter code (a new letter is being learnt), impossible when it is a different known letter.
    A spelled word must start with a known letter code (see align)."""
    known = LETTERS.get(group)
    if known is None:
        return 0.9
    return 0.2 if known == ch else None


def align(ct, pt):
    INF = 10 ** 9
    n, m = len(ct), len(pt)
    # state (i, j, k): i cipher tokens used, j plaintext words done, k letters of word j spelled so far
    best = {(0, 0, 0): (0, None, None)}
    order = sorted({(i, j) for i in range(n + 1) for j in range(m + 1)})
    for i in range(n + 1):
        for j in range(m + 1):
            for k in range(0, 20):
                st = (i, j, k)
                if st not in best:
                    continue
                cost = best[st][0]

                def relax(ns, c, move):
                    if ns not in best or best[ns][0] > cost + c:
                        best[ns] = (cost + c, st, move)
                if k > 0:  # inside a spelled word: only letters may follow
                    if i < n and ct[i][0] == 'g' and j < m:
                        c = letter_cost(ct[i][1], pt[j][k])
                        if c is not None:
                            if k + 1 == len(pt[j]):
                                relax((i + 1, j + 1, 0), c, ('letter', i, j))
                            else:
                                relax((i + 1, j, k + 1), c, ('letter', i, j))
                    continue
                if i < n and j < m:
                    t = ct[i]
                    if t[0] == 'w':
                        relax((i + 1, j + 1, 0), 0 if t[1] == pt[j] else 4, ('clear', i, j))
                    else:
                        relax((i + 1, j + 1, 0), 1, ('word', i, j))
                        c = letter_cost(t[1], pt[j][0])
                        if len(pt[j]) > 3 and c is not None and t[1] in LETTERS:
                            relax((i + 1, j, 1), c, ('letter', i, j))
                if i < n:
                    relax((i + 1, j, 0), 2.5, ('skipc', i, None))
                if j < m:
                    relax((i, j + 1, 0), 2, ('skipp', None, j))
    st = (n, m, 0)
    moves = []
    while best[st][1] is not None:
        moves.append(best[st][2])
        st = best[st][1]
    return best[(n, m, 0)][0], moves[::-1]


def main():
    ct = cipher_tokens(HERE / 'ct_49.txt')
    pt = plain_words(HERE / 'pt_51.txt')
    cost, moves = align(ct, pt)
    table = defaultdict(lambda: defaultdict(int))
    learnt = defaultdict(set)
    rows = []
    for kind, i, j in moves:
        tok = ct[i] if i is not None else None
        word = pt[j] if j is not None else ''
        if kind == 'word':
            table[tok[1]][OVERRIDES.get(tok[1], word)] += 1
        if kind == 'letter':
            learnt[tok[1]].add(word)
        rows.append((kind, ' '.join(tok[1:]) if tok else '', word))
    with open(HERE / 'align_1798.tsv', 'w', encoding='utf-8') as f:
        f.write('move\tcipher\tplain\n')
        for r in rows:
            f.write('\t'.join(r) + '\n')
    with open(HERE / 'table_1798.tsv', 'w', encoding='utf-8') as f:
        f.write('group\tword\tcount\tpage\n')
        for g in sorted(table, key=lambda g: [int(x) for x in g.split(',')]):
            for w, c in table[g].items():
                f.write(f'{g}\t{w}\t{c}\t{g.split(",")[0]}\n')
        for g, l in sorted(LETTERS.items(), key=lambda x: int(x[0].split(',')[0])):
            f.write(f'{g}\t[{l}]\t-\t{g.split(",")[0]}\n')
    kinds = defaultdict(int)
    for r in rows:
        kinds[r[0]] += 1
    print(f'cipher tokens {len(ct)}, plain words {len(pt)}, cost {cost:.1f}', dict(kinds))
    conflicts = {g: dict(ws) for g, ws in table.items() if len(ws) > 1}
    print('groups with two words:', conflicts)
    print('letter groups not seeded:', {g: sorted(w) for g, w in learnt.items() if g not in LETTERS})


if __name__ == '__main__':
    sys.exit(main())
