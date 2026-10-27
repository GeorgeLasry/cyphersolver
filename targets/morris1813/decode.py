"""Decode Anthony Morris's code groups (catalogue 650) with the State Department code table of ../jqa/code_table.tsv
(the = 1385, used unchanged) under Morris's block order (block_map.tsv: his sixteen blocks of 100 are the table's
blocks in reverse order, each block keeping its inner order: Morris 100*i + r = JQA 100*(15 - i) + r).

    python decode.py                      morris1813_transcription.txt -> group-by-group decryption, line by line
    python decode.py FILE                 another transcription in the same format
    python decode.py --controls           the tests quoted in NOTES.md section 5 (A-D below)

Transcription format: one written line per row, label first (L1:); groups of one word are joined by '.', words are
separated by a space; "..." = words written in clear; (5) (c) (s) = marks under a group; '=' = the short double stroke
after a group; [?] = the group's reading is doubtful; ? = a group cut by the frame edge.
Output per group: morris>jqa=value/grade (grade as in ../jqa/code_table.tsv: H clerk decode, C Ford-aligned,
M uncertain, I slot inference; '?' = no value), then '=>' and the word with its syllables joined by '-'.

Controls (--controls), on the groups of the transcription:
  A  coverage and function-word share under block_map.tsv, under the identity (no block change), and under 20,000
     random orders of the 16 blocks (seed 1);
  B  for each Morris block, the JQA block that gives the most function words (ties broken by coverage);
  C  for each Morris block, the rank of its block_map.tsv block among all 16 when the decoded word pairs touching the
     block are counted as word bigrams of Ford, Writings of J. Q. Adams vols 3-4 (../jqa/ford_writingsofjohnqu03adam.txt,
     ../jqa/ford_writingsofjohnqu04wort.txt), every other block kept as in block_map.tsv;
  D  repeated multi-group words.
Python standard library only; paths are relative to this file.
"""
import collections, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
JQA = os.path.join(HERE, '..', 'jqa')
FW = set('the of to and in a that it is be for with by as on this which have not their they he his at from or but '
         'been was will would has an i my me we our us them there any if so no all are were had may can should'.split())


def code_table():
    tab = {}
    for line in open(os.path.join(JQA, 'code_table.tsv'), encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        p = line.rstrip('\n').split('\t')
        tab[int(p[0])] = (p[1], p[2] if len(p) > 2 else '')
    return tab


def block_map():
    """Morris block index (0..15) -> JQA block index (0..15)"""
    m = {}
    for line in open(os.path.join(HERE, 'block_map.tsv'), encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        p = line.split('\t')
        m[(int(p[0]) - 1) // 100] = (int(p[2]) - 1) // 100
    assert sorted(m) == list(range(16)) and sorted(m.values()) == list(range(16)), 'block_map.tsv: not a permutation'
    return m


def to_jqa(g, bmap):
    if not 1 <= g <= 1600:
        return None
    i, r = (g - 1) // 100, (g - 1) % 100 + 1
    return 100 * bmap[i] + r


def parse(path):
    """[(label, [item, ...])]; item = ('clear', text) or ('word', [(number or None, marks), ...])"""
    rows = []
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        label, rest = line.rstrip('\n').split(None, 1)
        items = []
        for m in re.finditer(r'"([^"]*)"|(\S+)', rest):
            if m.group(1) is not None:
                items.append(('clear', m.group(1)))
                continue
            word = []
            for piece in m.group(2).strip(',').split('.'):
                if not piece or piece == '=':
                    continue
                if piece == '?':
                    word.append((None, '?'))
                    continue
                n = re.match(r'(\d+)(.*)', piece)
                if n:
                    word.append((int(n.group(1)), n.group(2)))
            if word:
                items.append(('word', word))
        rows.append((label.rstrip(':'), items))
    return rows


def groups_of(rows):
    return [g for _, items in rows for kind, w in items if kind == 'word' for g, _ in w if g is not None]


def words_of(rows):
    return [[g for g, _ in w if g is not None] for _, items in rows for kind, w in items if kind == 'word']


def plain(v):
    return re.sub(r'\(.*?\)', '', v).split('/')[0]


def decode(path):
    tab, bmap = code_table(), block_map()
    rows = parse(path)
    out = ['# Anthony Morris to James Monroe, M31 roll 14 frame 0039 (catalogue 650): decryption line by line against',
           '# morris1813_transcription.txt, with ../jqa/code_table.tsv under block_map.tsv (output of python decode.py).',
           '# Each group: morris>jqa=value/grade (? = no value in the table; marks of the transcription kept after the value).',
           '# Then => the words, syllables joined by -, [n] = Morris group n with no value, "..." = written in clear.',
           '# This is the mechanical decode. The sentences, with the holes and the context readings marked, are in',
           '# morris1813_reading.md.', '']
    tot = hit = 0
    for label, items in rows:
        cells, words = [], []
        for kind, w in items:
            if kind == 'clear':
                cells.append('"%s"' % w)
                words.append('"%s"' % w)
                continue
            syl = []
            for g, mk in w:
                tot += 1
                if g is None:
                    cells.append('?=?')
                    syl.append('[?]')
                    continue
                j = to_jqa(g, bmap)
                v = tab.get(j)
                if v:
                    hit += 1
                    cells.append('%d>%d=%s/%s%s' % (g, j, v[0], v[1], mk))
                    syl.append(plain(v[0]))
                else:
                    cells.append('%d>%s=?%s' % (g, j if j else '-', mk))
                    syl.append('[%d]' % g)
            words.append('-'.join(syl))
        out.append('%-4s %s' % (label, '  '.join(cells)))
        out.append('   => ' + ' '.join(words))
    out.append('')
    out.append('# %d of %d groups have a value in the table (%.3f)' % (hit, tot, hit / tot))
    return '\n'.join(out) + '\n'


def controls(path):
    tab, bmap = code_table(), block_map()
    rows = parse(path)
    G, W = groups_of(rows), words_of(rows)
    G = [g for g in G if 1 <= g <= 1600]
    W = [[g for g in w if 1 <= g <= 1600] for w in W]
    W = [w for w in W if w]
    val = {k: v[0] for k, v in tab.items()}

    def score(f):
        cov = sum(1 for g in G if f(g) in val)
        fw = sum(1 for g in G if val.get(f(g), '').lower() in FW)
        return cov / len(G), fw / len(G)

    def perm_f(p):
        return lambda g: 100 * p[(g - 1) // 100] + (g - 1) % 100 + 1

    print('A  %d groups (1-1600) on the frame' % len(G))
    print('   block_map.tsv      coverage %.3f  function words %.3f' % score(perm_f(bmap)))
    print('   identity           coverage %.3f  function words %.3f' % score(lambda g: g))
    random.seed(1)
    null = []
    for _ in range(20000):
        p = list(range(16))
        random.shuffle(p)
        null.append(score(perm_f(dict(enumerate(p))))[1])
    null.sort()
    print('   20,000 random block orders: function words median %.3f, 99.9th percentile %.3f, max %.3f'
          % (null[len(null) // 2], null[int(.999 * len(null))], null[-1]))

    cnt = collections.Counter(G)
    print('B  best JQA block per Morris block on function words alone (fw = function-word tokens, cov = groups valued)')
    agree = 0
    for i in range(16):
        gs = {g: n for g, n in cnt.items() if (g - 1) // 100 == i}
        sc = []
        for j in range(16):
            f = lambda g, j=j: 100 * j + (g - 1) % 100 + 1
            sc.append((sum(n for g, n in gs.items() if val.get(f(g), '').lower() in FW),
                       sum(n for g, n in gs.items() if f(g) in val), j))
        sc.sort(reverse=True)
        ok = sc[0][2] == bmap[i]
        agree += ok
        print('   M%4d-%4d n=%3d  best J%4d-%4d (fw %d, cov %d)  block_map J%4d-%4d  %s' % (
            i * 100 + 1, i * 100 + 100, sum(gs.values()), sc[0][2] * 100 + 1, sc[0][2] * 100 + 100, sc[0][0], sc[0][1],
            bmap[i] * 100 + 1, bmap[i] * 100 + 100, 'agrees' if ok else 'differs'))
    print('   function words alone pick the block_map.tsv block for %d of 16 Morris blocks' % agree)

    bigrams = set()
    for f in ('ford_writingsofjohnqu03adam.txt', 'ford_writingsofjohnqu04wort.txt'):
        toks = re.findall(r'[a-z]+', open(os.path.join(JQA, f), encoding='utf-8', errors='ignore').read().lower())
        bigrams.update(zip(toks, toks[1:]))

    def clean(v):
        return re.sub(r'[^a-z]', '', plain(v).lower())

    def dec(w, i, J):
        vs = []
        for g in w:
            b = (g - 1) // 100
            v = val.get(100 * (J if b == i else bmap[b]) + (g - 1) % 100 + 1)
            if v is None:
                return None
            vs.append(clean(v))
        return ''.join(vs)

    print('C  rank of the block_map.tsv block among the 16 JQA blocks on word bigrams of Ford vols 3-4')
    first = 0
    for i in range(16):
        sc = {}
        for J in range(16):
            D = [dec(w, i, J) for w in W]
            k = 0
            for a in range(len(W) - 1):
                if not any((g - 1) // 100 == i for g in W[a] + W[a + 1]):
                    continue
                if D[a] and D[a + 1] and (D[a], D[a + 1]) in bigrams:
                    k += 1
            sc[J] = k
        rank = 1 + sum(1 for J in sc if sc[J] > sc[bmap[i]])
        ties = sum(1 for J in sc if sc[J] == sc[bmap[i]]) - 1
        best = max(sc, key=lambda J: (sc[J], J == bmap[i]))
        first += rank == 1
        print('   M%4d-%4d  block_map J%4d-%4d bigrams %2d  rank %d%s  | best J%4d-%4d %d' % (
            i * 100 + 1, i * 100 + 100, bmap[i] * 100 + 1, bmap[i] * 100 + 100, sc[bmap[i]], rank,
            ' (tied with %d)' % ties if ties and rank == 1 else '', best * 100 + 1, best * 100 + 100, sc[best]))
    print('   the block_map.tsv block ranks first (ties included) for %d of 16 Morris blocks' % first)

    print('D  repeated multi-group words')
    seq = collections.Counter(tuple(w) for w in W if len(w) > 1)
    for s, c in seq.most_common():
        if c < 2:
            break
        print('   %dx %s = %s' % (c, '.'.join(map(str, s)),
                                 '-'.join(plain(val.get(to_jqa(g, bmap), '?')) for g in s)))
    pairs = collections.Counter(zip(G, G[1:]))
    print('   adjacent 76 285 (of the): %dx; 285 alone %dx; 76 alone %dx' % (pairs[(76, 285)], cnt[285], cnt[76]))


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    path = args[0] if args else 'morris1813_transcription.txt'
    if not os.path.isabs(path):
        path = os.path.join(HERE, path)
    sys.stdout.reconfigure(encoding='utf-8', newline='\n')
    if '--controls' in sys.argv:
        controls(path)
    else:
        sys.stdout.write(decode(path))
