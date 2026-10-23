"""b15: align a reading, letter by letter, with the figures of a Keresdi Bethlen cipher line (transylvania1645).

    python research/reading_audit/b15_align.py <transcription.txt> <reading_lines.txt> [--tsv OUT] [--quiet]

Both files have the same line order; '#' lines are skipped, {...} is clear text and is dropped before aligning.
The cipher is the reciprocal letter substitution of the family (shared-key-hypothesis.json): a-v b-f c-p d-o e-y
g-u h-r i-n k-l m-z q-t s-x (and w = a, 7 = the z variant = m). The hand's g/q/u, c/e, h/r, i/n and a/v are not
always distinct, so a figure label may stand for the other member of its pair: such a letter is 'class-resolved'
(C) and listed; a letter of the reading that no figure carries is 'not carried' (I), a letter carried by a figure
of another value is a 'mismatch' (X). A figure that no reading letter uses is 'unused'.
Per word: carried (all P/C), or flagged with its X/I letters. Words written [?word] or [...] are expected to flag.
"""
import re, sys

KEY = dict(a='v', b='f', c='p', d='o', e='y', f='b', g='u', h='r', i='n', k='l', l='k', m='z', n='i', o='d',
           p='c', q='t', r='h', u='g', v='a', w='a', x='s', y='e', z='m', s='x', t='t', **{'7': 'm'})
ALT = dict(g='tg', q='ug', u='ut', c='yn', e='p', i='i', n='n', a='a', v='uv', h='h', r='r', t='u')
NORM = str.maketrans({'j': 'i', 'v': 'u'})   # the cipher writes i for j; u/v one letter


def plain_opts(fig):
    if fig == '_': return {}
    p = KEY.get(fig, fig)
    o = {p.translate(NORM): 0.0}
    for a in ALT.get(fig, ''):
        o.setdefault(a.translate(NORM), 0.5)
    return o


def cipher_part(line):
    return re.sub(r'\{[^}]*\}', ' ', line)


def letters_of_reading(line):
    """[(letter, word_index)] and the words, brackets kept on the word for the report."""
    words = cipher_part(line).split()
    out = []
    for wi, w in enumerate(words):
        for ch in re.sub(r'\[\.\.\.\]|[^a-z]', '', w.lower()):
            out.append((ch.translate(NORM), wi))
    return out, words


def align(figs, lets):
    n, m = len(figs), len(lets)
    INF = 1e9
    D = [[INF] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0
    SKIPF, SKIPL, MIS = 2.5, 2.5, 4.0
    for i in range(n + 1):
        for j in range(m + 1):
            d = D[i][j]
            if d >= INF: continue
            if i < n and d + SKIPF < D[i + 1][j]:
                D[i + 1][j] = d + SKIPF; B[i + 1][j] = (i, j, 'U')
            if j < m and d + SKIPL < D[i][j + 1]:
                D[i][j + 1] = d + SKIPL; B[i][j + 1] = (i, j, 'I')
            if i < n and j < m:
                o = plain_opts(figs[i])
                c, t = (o[lets[j][0]], 'P' if o[lets[j][0]] == 0 else 'C') if lets[j][0] in o else (MIS, 'X')
                if figs[i] == '_': c, t = 2.0, 'X'
                if d + c < D[i + 1][j + 1]:
                    D[i + 1][j + 1] = d + c; B[i + 1][j + 1] = (i, j, t)
    path = []; i, j = n, m
    while (i, j) != (0, 0):
        pi, pj, t = B[i][j]
        path.append((pi if t != 'I' else None, pj if t != 'U' else None, t)); i, j = pi, pj
    return path[::-1]


def main(tr, rd, tsv=None, quiet=False):
    T = [l.rstrip('\n') for l in open(tr, encoding='utf-8') if l.strip() and not l.startswith('#')]
    R = [l.rstrip('\n') for l in open(rd, encoding='utf-8') if l.strip() and not l.startswith('#')]
    assert len(T) == len(R), (len(T), len(R))
    rows = []; tot = dict(P=0, C=0, X=0, I=0, U=0); flagged = []
    for ln, (t, r) in enumerate(zip(T, R), 1):
        figs = [c for c in cipher_part(t) if not c.isspace()]
        lets, words = letters_of_reading(r)
        path = align(figs, lets)
        per = {}
        unused = []
        for fi, li, ty in path:
            tot[ty] += 1
            if ty == 'U': unused.append(figs[fi]); continue
            wi = lets[li][1]
            per.setdefault(wi, []).append((figs[fi] if fi is not None else '-', lets[li][0], ty))
        for wi, w in enumerate(words):
            if wi not in per: continue
            seq = per[wi]
            bad = [x for x in seq if x[2] in 'XI']
            cls = [x for x in seq if x[2] == 'C']
            status = 'carried' if not bad else 'FLAG'
            marked = w.startswith('[')
            if bad and not marked: flagged.append((ln, w, bad))
            rows.append((ln, w, ''.join(x[0] for x in seq), status + (' (marked)' if marked else ''),
                         ' '.join(f'{f}={p}' for f, p, _ in cls), ' '.join(f'{f}>{p}:{t}' for f, p, t in bad)))
        if unused and not quiet: print(f'line {ln}: unused figures {"".join(unused)}')
    if tsv:
        with open(tsv, 'w', encoding='utf-8') as f:
            f.write('line\tword\tfigures\tstatus\tclass_resolved\tnot_carried\n')
            for r_ in rows: f.write('\t'.join(map(str, r_)) + '\n')
    letters = tot['P'] + tot['C'] + tot['X'] + tot['I']
    print(f"letters {letters}: primary {tot['P']}, class-resolved {tot['C']}, mismatch {tot['X']}, "
          f"not carried {tot['I']}; unused figures {tot['U']}")
    print(f'unmarked words with X/I: {len(flagged)}')
    for ln, w, bad in flagged: print(f'  line {ln}: {w}  {bad}')


if __name__ == '__main__':
    a = sys.argv[1:]
    tsv = a[a.index('--tsv') + 1] if '--tsv' in a else None
    main(a[0], a[1], tsv, '--quiet' in a)
