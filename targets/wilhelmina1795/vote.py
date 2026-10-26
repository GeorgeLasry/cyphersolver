"""Rebuild the Euler word list by majority vote over all aligned groups (all_assign.txt, from merge.py).

Strict building (wordtable.build) stops at the first misread mark; the transcriptions of struck-through groups have
many. Here every group=output votes for the letters it implies and for the entry's length (when a k)N, N^k or whole
group fixes it); each position takes its most-voted letter. Output: key_vote.tsv (number, entry, votes, agreement,
length votes) and a summary. Usage: python vote.py [min_agreement]
"""
import collections, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'hereditary1796'))
import wordtable as wt

letters = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
lengths = collections.defaultdict(collections.Counter)
for raw in open(os.path.join(HERE, 'all_assign.txt'), encoding='utf8'):
    if raw.startswith('#'):
        continue
    for item in raw.split():
        g, _, out = item.partition('=')
        p = wt.parse(g)
        if not p or not out:
            continue
        n, k, j, whole, pos = p
        if pos:
            if len(pos) != len(out):
                continue
            for q, c in zip(pos, out):
                letters[n][q][c] += 1
        else:
            for t, c in enumerate(out):
                letters[n][k + 1 + t][c] += 1
            lengths[n][k + len(out) + j] += 1


def entry(n):
    L = lengths[n].most_common(1)[0][0] if lengths[n] else max(letters[n])
    s, agree, tot = '', 0, 0
    for q in range(1, L + 1):
        c = letters[n].get(q)
        if c:
            ch, v = c.most_common(1)[0]
            s += ch; agree += v; tot += sum(c.values())
        else:
            s += '.'
    return s + ('' if lengths[n] else '+'), agree, tot


if __name__ == '__main__':
    with open(os.path.join(HERE, 'key_vote.tsv'), 'w', encoding='utf8') as out:
        out.write('# entry\tword\tagreeing letter votes\tall letter votes\tlength votes\n')
        for n in sorted(letters):
            s, a, t = entry(n)
            out.write(f'{n}\t{s}\t{a}\t{t}\t{dict(lengths[n])}\n')
    ents = sorted(letters)
    good = [n for n in ents if (lambda e: e[2] and e[1] / e[2] >= 0.8 and '.' not in e[0])(entry(n))]
    print(len(ents), 'entries;', len(good), 'with no gap and >=80% letter agreement; range', ents[0], '-', ents[-1])
    missing = [n for n in range(1, max(ents) + 1) if n not in letters]
    print(len(missing), 'numbers never seen:', missing)
