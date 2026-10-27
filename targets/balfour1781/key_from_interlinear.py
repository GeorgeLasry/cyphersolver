"""Rebuild the Balfour number key from the transcribed interlinear and decipher with it.

Usage: python key_from_interlinear.py [page ...]   (default: every transcription/p*.txt)

Each transcription file has L (cipher numbers, '-' for the dashes) and I (interlinear letters) lines.
Numbers >= NULL_FROM are taken as dummies (hypothesis from p. 717, tested by the vote table).
Per line, the kept numbers are aligned with the interlinear letters by edit distance and each
pairing votes for number -> letter. The majority key then deciphers every line; the output and the
letter agreement with the interlinear go to decipherment.txt and stdout.
"""
import collections
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
NULL_FROM = 50
# each numbered letter has its own table (No. 1 a=19 e=16; No. 2 a=16 e=14)
GROUPS = {'A1': range(717, 721), 'A2': range(721, 725), 'A3': range(725, 728),
          'B': range(729, 733), 'C': range(733, 737)}


def group_of(page):
    return next((g for g, r in GROUPS.items() if int(page) in r), 'other')


def load(paths):
    lines = []
    for p in paths:
        page = re.search(r'p(\d+)', os.path.basename(p)).group(1)
        cur = {}
        for raw in open(p, encoding='utf8'):
            m = re.match(r'([LIN])(\d+)\s*\|\s?(.*)', raw.rstrip('\n'))
            if not m:
                continue
            kind, no, body = m.groups()
            key = (page, int(no))
            cur.setdefault(key, {'page': page, 'line': int(no), 'L': '', 'I': ''})
            if kind in 'LI':
                cur[key][kind] = body
        lines.extend(cur[k] for k in sorted(cur, key=lambda k: k[1]))
    return lines


def tokens(L):
    out = []
    for t in L.split():
        if t == '-':
            out.append('-')
            continue
        if re.fullmatch(r'\d[xX]\??', t):
            # a two-digit figure cut at the page edge: first digit read, second lost
            out.append((int(t[0]) * 10, True))
            continue
        n = re.sub(r'[^0-9]', '', t)
        out.append((int(n) if n else None, '?' in t))
    return out


def align(nums, letters):
    """Edit-distance alignment of numbers and letters; returns (num, letter) pairs."""
    n, m = len(nums), len(letters)
    d = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        d[i][0] = i
    for j in range(m + 1):
        d[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1])
    pairs, i, j = [], n, m
    while i > 0 and j > 0:
        if d[i][j] == d[i - 1][j - 1]:
            pairs.append((nums[i - 1], letters[j - 1]))
            i, j = i - 1, j - 1
        elif d[i][j] == d[i - 1][j] + 1:
            i -= 1
        else:
            j -= 1
    return pairs


def build_key(lines, rounds=3):
    key = {}
    for _ in range(rounds):
        votes = collections.defaultdict(collections.Counter)
        for ln in lines:
            nums = [n for t in tokens(ln['L']) if t != '-' for n in [t[0]] if n is not None and n < NULL_FROM]
            letters = [c for c in ln['I'].lower() if c.isalpha()]
            if key:
                # second pass: align on the current key so a cost reflects disagreement
                pairs = align2(nums, letters, key)
            else:
                pairs = align(nums, letters) if abs(len(nums) - len(letters)) <= 3 else []
            for a, b in pairs:
                votes[a][b] += 1
        key = {n: c.most_common(1)[0][0] for n, c in votes.items()}
    return key, votes


def align2(nums, letters, key):
    n, m = len(nums), len(letters)
    INF = 10 ** 9
    d = [[INF] * (m + 1) for _ in range(n + 1)]
    d[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if i and d[i - 1][j] + 1 < d[i][j]:
                d[i][j] = d[i - 1][j] + 1
            if j and d[i][j - 1] + 1 < d[i][j]:
                d[i][j] = d[i][j - 1] + 1
            if i and j:
                c = 0 if key.get(nums[i - 1]) == letters[j - 1] else 1
                if d[i - 1][j - 1] + c < d[i][j]:
                    d[i][j] = d[i - 1][j - 1] + c
    pairs, i, j = [], n, m
    while i > 0 and j > 0:
        c = 0 if key.get(nums[i - 1]) == letters[j - 1] else 1
        if d[i][j] == d[i - 1][j - 1] + c:
            pairs.append((nums[i - 1], letters[j - 1]))
            i, j = i - 1, j - 1
        elif d[i][j] == d[i - 1][j] + 1:
            i -= 1
        else:
            j -= 1
    return pairs


def decipher(L, key):
    out = []
    for t in tokens(L):
        if t == '-':
            out.append(' ')
        elif t[0] is None:
            out.append('?')
        elif t[0] >= NULL_FROM:
            continue
        else:
            out.append(key.get(t[0], f'[{t[0]}]') + ('?' if t[1] else ''))
    return re.sub(' +', ' ', ''.join(out)).strip()


def main():
    args = sys.argv[1:]
    paths = [os.path.join(HERE, 'transcription', f'p{a}.txt') for a in args] or \
        sorted(glob.glob(os.path.join(HERE, 'transcription', 'p*.txt')))
    lines = load(paths)
    keys = {}
    with open(os.path.join(HERE, 'key_votes.txt'), 'w', encoding='utf8') as f:
        for g in GROUPS:
            gl = [ln for ln in lines if group_of(ln['page']) == g]
            if not gl:
                continue
            key, votes = build_key(gl)
            keys[g] = key
            f.write(f'== {g}\n')
            for n in sorted(votes):
                f.write(f'{n:3d} {key[n]}  {dict(votes[n].most_common())}\n')
    agree = total = 0
    stats = collections.Counter()
    with open(os.path.join(HERE, 'decipherment.txt'), 'w', encoding='utf8') as f:
        for ln in lines:
            key = keys.get(group_of(ln['page']), {})
            dec = decipher(ln['L'], key)
            il = ''.join(c for c in ln['I'].lower() if c.isalpha())
            dl = ''.join(c for c in dec if c.isalpha())
            pairs = align(list(dl), list(il))
            a = sum(a == b for a, b in pairs)
            agree += a
            total += max(len(dl), len(il))
            stats[group_of(ln['page']), 'a'] += a
            stats[group_of(ln['page']), 't'] += max(len(dl), len(il))
            f.write(f"p{ln['page']} L{ln['line']:02d} | {ln['L']}\n          I | {ln['I']}\n          D | {dec}\n\n")
    for g in keys:
        print(f"{g}: key numbers {len(keys[g])}  agreement {stats[g, 'a']}/{stats[g, 't']} = {stats[g, 'a'] / max(stats[g, 't'], 1):.1%}")
    print(f'lines {len(lines)}  letter agreement {agree}/{total} = {agree / max(total, 1):.1%}')


if __name__ == '__main__':
    main()
