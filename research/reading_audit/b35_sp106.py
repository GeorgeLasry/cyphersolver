"""b35 (sp106r787, sp106r924): rebuild a sign transcription of one SP 106/10 letter from Pettersson's DECODE rows,
apply this project's corrections (a tsv: row, index, op, value, note; op = sub | ins | del, index 0-based in the row
as it stands after earlier edits of that row), carry George Lasry's '&' signs from his plaintext, add extra rows
(margin text), and decode with his key.

    python b35_sp106.py <target dir> <record> <section> <key doc> <interlinear doc> <plaintext doc> [--signs out] [--decode out]

The '&' positions: Lasry's plaintext has '&' (the ampersand sign written in the cipher, not a figure); they are placed
by aligning his plaintext letters with the key decode (difflib) and inserted as a sign '&'.
"""
import sys, re, csv, pathlib, difflib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'sp106r787'))
from apply_key import load_key

tdir, rec, sec, kf, inf, pf = sys.argv[1:7]
tdir = pathlib.Path(tdir)
key = load_key(tdir / 'decode' / kf)


def rows_of(path, sec):
    cur, out = None, []
    lines = pathlib.Path(path).read_text(encoding='utf-8', errors='replace').splitlines()
    for l in lines:
        m = re.match(r'#{6,}\s*tna[ _]sp106.(\S+?)(\.txt)?\s*$', l)
        if m: cur = m.group(1); continue
        if l.startswith('#KEY'): cur = None; continue
        if cur == sec and l.strip() and not l.lstrip().startswith(('#', '<CLEAR')):
            out.append(l)
    body = out
    return [body[i].rstrip().rstrip('|').split() for i in range(0, len(body) - 1, 2)]


rows = rows_of(tdir / 'decode' / inf, sec)
ctsv = tdir / f'{rec}_corrections.tsv'
if ctsv.exists():
    for r in csv.DictReader(open(ctsv, encoding='utf-8'), delimiter='\t'):
        if r['row'].startswith('m'): continue
        i, j, op, v = int(r['row']), int(r['index']), r['op'], r['value']
        if op == 'sub':
            assert rows[i][j] == r['old'], (r, rows[i][j]); rows[i][j] = v
        elif op == 'ins': rows[i].insert(j, v)
        elif op == 'del':
            assert rows[i][j] == r['old'], (r, rows[i][j]); del rows[i][j]


def dec(g):
    if g == '&': return '&'
    if g.startswith('='): return '{%s}' % g[1:]      # written in clear (a date or a numeral)
    v = key.get(g)
    return v if v else '<%s>' % g


# '&' from Lasry's plaintext
def ptoks(path, sec):
    cur, buf = None, []
    for l in pathlib.Path(path).read_text(encoding='utf-8', errors='replace').splitlines():
        m = re.match(r'#{6,}\s*tna[ _]sp106.(\S+?)(\.txt)?\s*$', l)
        if m: cur = m.group(1); continue
        if cur == sec and not l.startswith('#'): buf.append(l)
    t = ' '.join(buf)
    t = re.sub(r'\([^)]*\)', '', t)
    toks = []
    for m in re.finditer(r'<[^>]*>|&|[A-Z]', t):
        s = m.group(0)
        toks.append('<>' if s.startswith('<') else s)
    return toks


if '--no-amp' not in sys.argv:
    flat = [(i, j) for i, r in enumerate(rows) for j in range(len(r))]
    dtoks = ['<>' if dec(rows[i][j])[0] in '<{' else dec(rows[i][j]) for i, j in flat]
    lt = ptoks(tdir / 'decode' / pf, sec)
    sm = difflib.SequenceMatcher(None, dtoks, lt, autojunk=False)
    ins = []
    for op, a0, a1, b0, b1 in sm.get_opcodes():
        if op in ('insert', 'replace'):
            for b in range(b0, b1):
                if lt[b] == '&': ins.append(a0)
    for a in sorted(ins, reverse=True):
        if a < len(flat): i, j = flat[a]
        else: i, j = len(rows) - 1, len(rows[-1])
        rows[i].insert(j, '&')
    print('& placed', len(ins))

extra = tdir / f'{rec}_margin_signs.txt'
mrows = []
if extra.exists():
    for l in extra.read_text(encoding='utf-8').splitlines():
        if l.strip() and not l.startswith('#'): mrows.append(l.split())

if '--signs' in sys.argv:
    out = sys.argv[sys.argv.index('--signs') + 1]
    with open(out, 'w', encoding='utf-8') as f:
        f.write('# %s sign transcription: Pettersson (DECODE) rows, with %s_corrections.tsv applied and Lasry\'s & signs; '
                'one manuscript line per row\n' % (rec, rec))
        for r in rows: f.write(' '.join(r) + '\n')
if '--decode' in sys.argv:
    out = sys.argv[sys.argv.index('--decode') + 1]
    with open(out, 'w', encoding='utf-8') as f:
        for r in rows: f.write(''.join(' %s ' % dec(g) if len(dec(g)) > 1 else dec(g) for g in r) + '\n')
        if mrows:
            f.write('# margin\n')
            for r in mrows: f.write(''.join(' %s ' % dec(g) if len(dec(g)) > 1 else dec(g) for g in r) + '\n')
n = sum(len(r) for r in rows); print(rec, 'rows', len(rows), 'signs', n, 'margin', sum(len(r) for r in mrows))
