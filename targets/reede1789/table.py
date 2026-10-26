"""Build Van Reede's 1789-92 code table from the aligned runs (AL: lines of pairs_*.txt) by vote.

A group is keyed twice: with its marks (e.g. 207{u3}) and by its bare number (207). The overlined 3 that the
agents wrote as a separate {3} prefix is dropped. Output: table.tsv (key, best value, votes, all values).
Usage: python table.py
"""
import collections, glob, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ITEM = re.compile(r'(\S+?)=(.*?)(?=\s+\S+?=|$)')


def norm_group(g):
    g = g.replace('{3}', '')
    m = re.match(r"(\d+)((?:\{[^}]*\}|')*)$", g)
    if not m:
        return None, None
    n, marks = m.groups()
    marks = ''.join(sorted(re.findall(r"\{[^}]*\}|'", marks)))
    return n, n + marks


def runs():
    for f in sorted(glob.glob(os.path.join(HERE, 'pairs_*.txt'))):
        tag = ''
        for raw in open(f, encoding='utf8'):
            if raw.startswith('# scan'):
                tag = raw[2:].strip()
            elif raw.startswith('AL:'):
                yield tag, ITEM.findall(raw[3:].strip())


if __name__ == '__main__':
    marked = collections.defaultdict(collections.Counter)
    bare = collections.defaultdict(collections.Counter)
    for tag, items in runs():
        for g, out in items:
            out = out.strip().lower()
            if not out or '?' in out or '?' in g:
                continue
            n, key = norm_group(g)
            if not n:
                continue
            marked[key][out] += 1
            bare[n][out] += 1
    with open(os.path.join(HERE, 'table.tsv'), 'w', encoding='utf8') as w:
        w.write('# key\tbest\tvotes\ttotal\tall values (marked keys first, then bare numbers prefixed #)\n')
        for k in sorted(marked, key=lambda k: (int(re.match(r'\d+', k).group()), k)):
            c = marked[k]; b, v = c.most_common(1)[0]
            w.write(f'{k}\t{b}\t{v}\t{sum(c.values())}\t{dict(c.most_common(5))}\n')
        for k in sorted(bare, key=int):
            c = bare[k]; b, v = c.most_common(1)[0]
            w.write(f'#{k}\t{b}\t{v}\t{sum(c.values())}\t{dict(c.most_common(5))}\n')
    nb = len(bare); agree = sum(1 for c in bare.values() if c.most_common(1)[0][1] / sum(c.values()) >= 0.6)
    print(len(marked), 'marked keys;', nb, 'bare numbers,', agree, 'with >=60% agreement; range',
          min(map(int, bare)), '-', max(map(int, bare)))
