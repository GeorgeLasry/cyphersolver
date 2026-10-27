"""Apply this folder's code table (../code_table.tsv, JQA's St Petersburg code, the = 1385) to the later legation
texts in the same code: Madrid 1823 and 1825 (catalogue 637, 638), Paris 1813 (652) and Mexico 1839 (653), and run
the controls quoted in ../NOTES.md.

    python decode.py appleton1823_transcription.txt            group-by-group decryption, line by line
    python decode.py everett1825_transcription.txt
    python decode.py crawford1813_transcription.txt
    python decode.py ellis1839_transcription.txt
    python decode.py everett1825_transcription.txt --controls   wrong-key controls (any of the four files)

Output per group: number=value/grade, the grade as in code_table.tsv (H clerk decode, C Ford-aligned, M uncertain,
I slot inference); '?' = no value in the table. The marks of the transcription are kept after the value.
A first column like 27R01: or 0298.01: or without digits (A, B, C) is the line label. Words written in clear
among the groups ("word") are copied through; groups written above the line ([ins: ...]) are decoded in place; a
group with an unreadable digit (?03) counts as a group without a value.
Python standard library only; paths are relative to this file.
"""
import os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TABLE = os.path.join(HERE, '..', 'code_table.tsv')
FUNCTION = set('the of that and to in i not he is it his be by as with for this which was would have had upon been '
               'on at from more such well who are all a an'.split())


def table():
    tab = {}
    for line in open(TABLE, encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        p = line.rstrip('\n').split('\t')
        tab[int(p[0])] = (p[1], p[2] if len(p) > 2 else '')
    return tab


def groups(path):
    """[(label, [(number, marks), ...]), ...]; a leading letter on a line is its passage label"""
    rows = []
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        toks = line.split()
        label = toks.pop(0) if toks and (re.fullmatch(r'\w*[A-Za-z.]\w*(\.\w+)?:', toks[0]) or not re.search(r'\d', toks[0])) else ''
        gs = []
        for t in toks:
            if t.startswith('"'):                       # words in clear among the groups: number None
                gs.append((None, t))
                continue
            t = t.replace('[ins:', '').rstrip(']')      # groups inserted above the line
            m = re.fullmatch(r'-?(\d+)(\S*)', t)
            if m:
                gs.append((int(m.group(1)), m.group(2).rstrip('-')))
            elif re.fullmatch(r'[\d?]*\?[\d?]*', t):     # a digit lost (blot): a group with no value
                gs.append((-1, t))
        rows.append((label.rstrip(':'), gs))
    return rows


def value(tab, n):
    v = tab.get(n, ('?', ''))[0]
    return re.sub(r'\(.*?\)', '', v).split('/')[0]


def decode(path):
    tab = table()
    tot = hit = 0
    for label, gs in groups(path):
        out = []
        for n, mk in gs:
            if n is None:
                out.append(mk)
                continue
            tot += 1
            if n == -1:
                out.append(f'{mk}=?')
            elif n in tab:
                hit += 1
                out.append(f'{n}={tab[n][0]}{mk}/{tab[n][1]}')
            else:
                out.append(f'{n}=?{mk}')
        print((label + '  ' if label else '') + '  '.join(out))
    print(f'# {hit} of {tot} groups have a value in ../code_table.tsv')


def function_rate(words):
    """share of decoded groups that are common English function words"""
    return sum(w.lower() in FUNCTION for w in words) / max(1, len(words))


def controls(path):
    """Wrong keys: every group shifted by k, or the table permuted at random. A true key gives English, with many
    function words; a wrong key gives scattered syllables. (Shuffling the group order keeps the same words, so it
    needs a word-order model; that check is described in ../NOTES.md and not repeated here.)"""
    tab = table()
    seq = [n for _, gs in groups(path) for n, _ in gs if n is not None and n >= 0]
    dec = lambda f: [value(tab, f(n)) for n in seq]
    hits = lambda f: sum(f(n) in tab for n in seq)
    print(f'{len(seq)} groups. real decode (table, no corrections): {hits(lambda n: n)} with a value, '
          f'function-word rate {function_rate(dec(lambda n: n)):.2f}')
    for k in (1, -1, 2, -2, 3, -3, 7, -7, 50, -50, 100):
        f = lambda n, k=k: n + k
        print(f'  every group shifted {k:+4d}: {hits(f)} with a value, function-word rate {function_rate(dec(f)):.2f}'
              f'   {" ".join(dec(f)[:12])}')
    rnd = random.Random(1825)
    keys = sorted(tab)
    for r in range(3):
        perm = keys[:]; rnd.shuffle(perm); mp = dict(zip(keys, perm))
        f = lambda n: mp.get(n, n)
        print(f'  random permutation of the table {r + 1}: function-word rate {function_rate(dec(f)):.2f}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    p = sys.argv[1] if os.path.isabs(sys.argv[1]) else os.path.join(HERE, sys.argv[1])
    controls(p) if '--controls' in sys.argv else decode(p)
