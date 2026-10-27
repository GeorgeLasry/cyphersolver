"""Hintze Ribeiro's two code telegrams to Queen Amélie, 1903 (ANTT PT/TT/CAM/M15, catalogue 406).

    python code.py        output kept in code_output.txt

Reads m0001_transcription.txt and m0003_transcription.txt (lines starting with # are comments) and
code_values.tsv. Standard library only. It runs:
  1. the telegraph word count against the form headers (5 figures = 1 word, address counted, punctuation not);
  2. the alignment of m0003's groups with the decode of the time, segment by segment between the clear words;
  3. the order of the code: raw rank correlation, and the page model (page = n // 100, pages below a split
     reflected, lines kept in order) with a null control that gives shuffled words the same freedom;
  4. the brackets of m0001's unread groups under the page model;
  5. the groups shared with the codes of the sibling folders.
"""
import csv, pathlib, random, re

HERE = pathlib.Path(__file__).resolve().parent
ADDR = {'m0001': "SA MAJESTE LA REINE DE PORTUGAL A' BORD DU YACHT AMELIA NAPLES",
        'm0003': "SA MAGESTE LA REINE DE PORTUGAL HOTEL BRISTOL PARIS"}
HEADER = {'m0001': 75, 'm0003': 46}


def text(doc):
    return ' '.join(l for l in (HERE / f'{doc}_transcription.txt').read_text(encoding='utf-8').splitlines()
                    if not l.lstrip().startswith('#'))


def taxed(s):
    n = 0
    for t in s.split():
        if not re.search(r'[A-Z0-9]', t):
            continue  # punctuation is not taxed
        n += -(-len(t) // 5) if t.isdigit() else 1
    return n


def groups(doc):
    return [t for t in text(doc).split() if t.isdigit()]


def rank(xs):
    o = sorted(range(len(xs)), key=lambda i: xs[i]); r = [0] * len(xs)
    for k, i in enumerate(o):
        r[i] = k
    return r


def rho(a, b):
    ra, rb = rank(a), rank(b); n = len(a)
    return 1 - 6 * sum((x - y) ** 2 for x, y in zip(ra, rb)) / (n * (n * n - 1))


def T(n, split):
    p, l = divmod(n, 100)
    return (split - p) * 100 + l if p < split else n


VALUES = {int(r['group']): r for r in csv.DictReader(open(HERE / 'code_values.tsv', encoding='utf-8'), delimiter='\t')}
# alphabetical sort key of each decoded value (first word, accent-free)
SORT = {1378: 'hoje', 24724: 'camara', 29878: 'arroio', 11876: 'divorciado', 37600: 'interpellar', 43322: 'ministro',
        34962: 'acerca', 62851: 'viagem', 41285: 'magestade (vossa)', 53538: 'referencia', 28643: 'ausencia',
        28605: 'auctoridades', 67398: 'livorno', 5556: 'falta', 63416: 'visita', 50554: 'presidente', 3707: 'da',
        49641: 'franceza', 18148: 'contestar', 5554: 'falso', 26541: 'boato', 5897: 'factos', 59587: 'termos',
        17836: 'convenientes'}

if __name__ == '__main__':
    print('1. telegraph word count (address + text, 5 figures = 1 word)')
    for doc in ('m0001', 'm0003'):
        a, t = taxed(ADDR[doc]), taxed(text(doc))
        print(f'  {doc}: {a} + {t} = {a + t}, header {HEADER[doc]}')
    t1 = text('m0001')
    print('  m0001 with 60134 read as one 6-figure group 601341:', taxed(ADDR['m0001']) + taxed(t1.replace('60134', '601341')))

    print('\n2. m0003: groups between the clear words against the units of the decode of the time')
    units = [['Hoje'], ['Camara dos Pares', 'Arroio', 'divorciado'],
             ['interpellar', 'Mi. Estrangeiros', 'acerca de', 'viagem', 'V. M.'],
             ['referencia', 'ausencia', 'auctoridades', 'Livorno'],
             ['falta', 'visita', 'Presidente', 'da Rep.', 'franceza', 'Mm. dos Estrangeiros', 'contestar', 'falso'],
             ['boato'], ['factos'], ['termos', 'convenientes']]
    segs, cur = [], []
    for tok in text('m0003').split():
        if tok.isdigit():
            cur.append(tok)
        elif re.search('[A-Z]', tok) and cur:
            segs.append(cur); cur = []
    if cur:
        segs.append(cur)
    for g, u in zip(segs, units):
        print(f'  {len(g)} groups / {len(u)} units {"ok" if len(g) == len(u) else "MISMATCH"}: '
              + ', '.join(f'{a}={b}' for a, b in zip(g, u)))

    nums = list(SORT); ws = [SORT[n] for n in nums]
    print(f'\n3. order: raw Spearman rho (value, alphabetical) over {len(nums)} decoded groups = {rho(nums, ws):.3f}')
    splits = range(50, 681, 5)
    best = max((rho([T(n, s) for n in nums], ws), s) for s in splits)
    print(f'  page model: best rho {best[0]:.3f} at split {best[1]} (pages below it reflected, lines kept)')
    split = best[1]
    prev = ''
    for n in sorted(nums, key=lambda n: T(n, split)):
        out = SORT[n] < prev
        print(f'    {n:5d} -> {T(n, split):5d} {SORT[n]}' + ('   <- out of order' if out else ''))
        prev = prev if out else SORT[n]
    random.seed(7); N = 2000; hits = 0; null = []
    for _ in range(N):
        sh = ws[:]; random.shuffle(sh)
        m = max(rho([T(n, s) for n in nums], sh) for s in splits); null.append(m); hits += m >= best[0] - 1e-9
    null.sort()
    print(f'  null (shuffled words, same choice of split): median {null[N // 2]:.3f}, max {null[-1]:.3f}; '
          f'P(>= {best[0]:.3f}) = {hits}/{N}')

    print('\n4. m0001 groups bracketed under the page model (decoded neighbours in model order)')
    for g in groups('m0001'):
        n = int(g)
        if n in SORT:
            print(f'  {g}: = {VALUES[n]["value"]}'); continue
        lo = max((k for k in nums if T(k, split) < T(n, split)), key=lambda k: T(k, split), default=None)
        hi = min((k for k in nums if T(k, split) > T(n, split)), key=lambda k: T(k, split), default=None)
        guess = VALUES.get(n, {}).get('value', '')
        print(f'  {g}: after {SORT.get(lo)}, before {SORT.get(hi)}' + (f'   [guess: {guess}]' if guess else ''))

    print('\n5. groups shared with the sibling folders')
    mine = {str(int(g)) for d in ('m0001', 'm0003') for g in groups(d)}
    for folder in ('carlos1903', 'sabugosa1910', 'manuel1910', 'lima1909'):
        sib = set()
        for f in (HERE.parent / folder).glob('*_transcription.txt'):
            for line in f.read_text(encoding='utf-8').splitlines():
                if not line.lstrip().startswith('#'):
                    sib |= {str(int(t.strip('.?,='))) for t in line.split() if re.fullmatch(r'=?\d{4,6}[.?,]*', t)}
        print(f'  {folder}: {len(sib)} distinct groups, shared: {sorted(mine & sib) or "none"}')
    print(f'  range of this code: {min(map(int, mine))}-{max(map(int, mine))}')
