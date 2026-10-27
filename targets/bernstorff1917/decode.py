"""Catalogue 657: Bernstorff to the Auswaertiges Amt, 10 Jan 1917 (State Department telegram of 11 Jan 1917).

Standard library only; run from anywhere.

    python decode.py              write ciphertext_tel205.txt, ciphertext_part2.txt, decryption_tel205.txt,
                                  decryption_part2.txt from transcription.txt, codebook.tsv and align_205.tsv
    python decode.py --check      group census; every alignment span matches the transcription; spans cover 0-146
    python decode.py --controls   blind alignment test against the print, with controls; prefix-figure test

Groups 0-146 are telegram No. 205, whose German text Bernstorff printed in 1920 (printed_tel205_de.txt).
Groups 147-576 are a second text in the same code; only groups already fixed by No. 205 are filled in.
"""
import collections, os, random, re, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PART1_END = 147          # groups 0..146 = telegram No. 205


def path(name):
    return os.path.join(HERE, name)


def groups():
    """The groups of transcription.txt in order: struck {..}, notes (..) and [?] marks removed."""
    g = []
    for line in open(path('transcription.txt'), encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        s = re.sub(r'\{[^}]*\}', '', line)
        s = re.sub(r'\([^)]*\)', '', s)
        g += s.replace('[?]', '').split()
    return g


def doubtful():
    """0-based numbers of the groups marked [?] in the transcription."""
    out, i = set(), 0
    for line in open(path('transcription.txt'), encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        s = re.sub(r'\{[^}]*\}(\[\?\])?', '', line)
        s = re.sub(r'\([^)]*\)', '', s)
        for tok in s.split():
            if '[?]' in tok:
                out.add(i)
            i += 1
    return out


def base(x):
    return x[-4:] if len(x) == 5 else x


def codebook():
    cb = {}
    for line in open(path('codebook.tsv'), encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        p = line.rstrip('\n').split('\t')
        cb[p[0]] = (p[1], p[2])
    return cb


def spans():
    out = []
    for line in open(path('align_205.tsv'), encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        p = line.rstrip('\n').split('\t') + ['']
        out.append((int(p[0]), int(p[1]), p[2], p[3], p[4]))
    return out


def value(x, cb):
    """Codebook value of a group: 4-figure base, or prefix figure + base for a 5-figure group."""
    if len(x) not in (4, 5):
        return None
    m = cb.get(base(x))
    if not m:
        return None
    return (f'{x[0]}+{m[0]}' if len(x) == 5 else m[0]), m[1]


def write_texts():
    g, cb, dbt = groups(), codebook(), doubtful()

    def plain(name, title, seq, start):
        rows = [f'# {title}', f'# {len(seq)} groups (0-based numbers {start}-{start + len(seq) - 1} of transcription.txt), '
                f'without marks. Written by decode.py.']
        rows += [' '.join(seq[i:i + 10]) for i in range(0, len(seq), 10)]
        open(path(name), 'w', encoding='utf-8', newline='\n').write('\n'.join(rows) + '\n')

    plain('ciphertext_tel205.txt', 'Catalogue 657, groups 0-146: telegram No. 205', g[:PART1_END], 0)
    plain('ciphertext_part2.txt', 'Catalogue 657, groups 147-576: the second text', g[PART1_END:], PART1_END)

    # part 1: line by line against the alignment
    out = ['# Catalogue 657, telegram No. 205 (groups 0-146): decryption line by line. Written by decode.py.',
           '# Each line: group numbers | groups | value of each group from codebook.tsv (grade) | German as printed | note.',
           '# A group with no value of its own sits in a span whose split is not fixed (see align_205.tsv); [?] after a',
           '# group = doubtful reading of its figures. Value N+x = prefix figure N on base group x.', '']
    for s, e, _, de, note in spans():
        cells = []
        for i in range(s, e + 1):
            v = value(g[i], cb)
            mark = '[?]' if i in dbt else ''
            cells.append(f'{g[i]}{mark}=' + (f'{v[0]}({v[1]})' if v else '-'))
        out.append(f'{s:3d}-{e:3d} | {" ".join(g[s:e + 1])} | {"; ".join(cells)} | {de}' + (f' | {note}' if note else ''))
    open(path('decryption_tel205.txt'), 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')

    # part 2: only groups fixed by No. 205
    out = ['# Catalogue 657, groups 147-576: the second text in the same code. Written by decode.py.',
           '# Only groups whose base is fixed by telegram No. 205 are filled in; _ = unknown group. N+ = prefix figure.',
           '# No plaintext is claimed: no sentence can be built from these values.', '']
    known = 0
    seq = list(range(PART1_END, len(g)))
    for k in range(0, len(seq), 10):
        idx = seq[k:k + 10]
        cells = []
        for i in idx:
            v = value(g[i], cb)
            if v:
                known += 1
            cells.append(v[0] if v else '_')
        out.append(f'{idx[0]:3d}  ' + ' '.join(g[i] + ('[?]' if i in dbt else '') for i in idx))
        out.append('     ' + ' | '.join(cells))
    out.append('')
    out.append(f'known {known} of {len(seq)} groups ({100 * known / len(seq):.1f}%)')
    open(path('decryption_part2.txt'), 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')
    print(f'groups {len(g)}; part 1 {PART1_END}; part 2 {len(seq)}, known {known} ({100 * known / len(seq):.1f}%)')


def check():
    g = groups()
    lens = collections.Counter(len(x) for x in g)
    print('groups', len(g), 'by length', dict(sorted(lens.items())))
    print('group 20 =', g[20], '; group 40 =', g[40], '; group 377 =', g[377], '; group 146 =', g[146],
          '; groups 147-148 =', g[147], g[148])
    bad, covered = 0, set()
    for s, e, gs, _, _ in spans():
        want = gs.replace('[?]', '').split()
        if want != g[s:e + 1]:
            bad += 1
            print('MISMATCH', s, e, want, g[s:e + 1])
        covered |= set(range(s, e + 1))
    print('alignment spans: mismatches', bad, '; groups covered', len(covered), f'({min(covered)}-{max(covered)})',
          '; gaps', sorted(set(range(PART1_END)) - covered))


# --- controls -----------------------------------------------------------------------------------------------

def words(name):
    t = ' '.join(l for l in open(path(name), encoding='utf-8') if not l.startswith('#'))
    toks = re.findall(r"[A-Za-zÄÖÜäöüß]+|[.,;]", t)
    return [w.lower().rstrip('s') if w.lower().startswith(('wilson', 'memorand')) else w.lower() for w in toks]


def fit(seg, W, win):
    """Blind test: map cipher position p to word position p*len(W)/len(seg); a repeated group scores when all its
    occurrences fall within +-win of one shared word. No alignment from align_205.tsv is used."""
    n, m = len(seg), len(W)
    pos = collections.defaultdict(list)
    for i, x in enumerate(seg):
        pos[base(x)].append(i)
    rep = {k: v for k, v in pos.items() if len(v) > 1}
    hit, detail = 0, []
    for k, v in rep.items():
        sets = [set(W[max(0, int(p * m / n) - win):int(p * m / n) + win + 1]) for p in v]
        common = set.intersection(*sets) - {'.', ','}
        hit += bool(common)
        detail.append((k, v, sorted(common) if common else None))
    return hit, len(rep), detail


def controls():
    g = groups()
    W205, W212 = words('printed_tel205_de.txt'), words('control_tel212_de.txt')
    P1 = g[5:146]            # body of No. 205 without head (0-4) and trailer (146)
    print(f'print: {len(W205)} tokens (tel 205), {len(W212)} (tel 212 control); cipher body {len(P1)} groups')
    for win in (6, 3, 2):
        h, t, d = fit(P1, W205, win)
        c212 = fit(P1, W212, win)
        blocks = [fit(g[a:a + 141], W205, win) for a in (147, 288, 429)]
        random.seed(1)
        res = []
        for _ in range(2000):
            s = P1[:]
            random.shuffle(s)
            h3, t3, _ = fit(s, W205, win)
            res.append(h3 / t3)
        ge = sum(r >= h / t for r in res)
        print(f'window +-{win}: tel 205 vs groups 5-145 {h}/{t}; control tel 212 {c212[0]}/{c212[1]}; '
              f'tel 205 vs part-2 blocks ' + ', '.join(f'{b[0]}/{b[1]}' for b in blocks) +
              f'; 2000 shuffles mean {statistics.mean(res):.2f} max {max(res):.2f}, reaching observed {ge}')
        if win == 3:
            for k, v, c in d:
                print(f'    {k} at {[p + 5 for p in v]}: {", ".join(c) if c else "-"}')
    # five-figure groups: prefix figure + four-figure base?
    four = {x for x in g if len(x) == 4}
    five = [x for x in g if len(x) == 5]
    tail = [x for x in five if x[1:] in four]
    head = [x for x in five if x[:4] in four]
    print(f'five-figure groups {len(five)}: last four figures occur as a four-figure group in {len(tail)}, '
          f'first four in {len(head)}; chance about {len(five) * len(four) / 10000:.1f}')
    stops = [i for i in range(PART1_END) if g[i] in ('1515', '3377', '0404', '1724')]
    print('stop groups in No. 205 at', stops, [g[i] for i in stops])


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['--check']:
        check()
    elif a[:1] == ['--controls']:
        controls()
    else:
        write_texts()
