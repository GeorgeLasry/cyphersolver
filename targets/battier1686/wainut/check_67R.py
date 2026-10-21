"""Reproduces every number in the "Contribution by WAINUT" section of ../NOTES.md.

  python3 check_67R.py          (from any directory; paths are relative to this file; standard library only)

1. decodes NA 3.01.18 inv. 401 scan 67R cipher lines 1-3 (tokens_s067R_L01-03.txt) with the key in ../key
   (letters.py and dict/*.tsv, loaded as scripts/decode.py loads them) and, for codes not in ../key/dict, key_rows.tsv;
2. the control: the same tokens with the key rotated by one row (letter n -> letter of n+1, code b:n -> b:n+1);
3. checks that s067R_L01-03.tsv carries the decoded values and counts its grades;
4. the method control for a single machine pass (machine_pass/): agreement with ../tokens/s058R.txt and s059L.txt,
   and with the checked transcription of 67R lines 1-3;
5. the key row 11:719 (../key/dict/orch.tsv) and where 11:718/11:719 occur in ../tokens.
"""
import difflib, glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.dirname(HERE)
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(TARGET, 'key'))
from letters import NUM  # noqa: E402  (Bourdeau's letter table, 2..98)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def load_dict():
    """As scripts/decode.py load_dict(): sorted dict/*.tsv, later files override earlier ones."""
    d = {}
    for f in sorted(glob.glob(os.path.join(TARGET, 'key', 'dict', '*.tsv'))):
        for line in open(f, encoding='utf-8'):
            if not line.strip() or line.startswith('#'):
                continue
            p = line.rstrip('\n').split('\t')
            if len(p) >= 2:
                d[p[0].strip()] = p[1].strip()
    return d


def load_rows():
    rows = {}
    for line in open(os.path.join(HERE, 'key_rows.tsv'), encoding='utf-8'):
        if line.startswith('#') or line.startswith('token\t') or not line.strip():
            continue
        tok, val, src, chk, use = line.rstrip('\n').split('\t')
        rows[tok] = (val, src, chk, use)
    return rows


def parse(fn):
    """As scripts/decode.py parse(): 'Lnn: tokens {clear text}'."""
    out = []
    for raw in open(fn, encoding='utf-8'):
        m = re.match(r'\s*(L\w+)\s*:\s*(.*)', raw)
        if m:
            out.append((m.group(1), re.sub(r'\{[^}]*\}', ' ', m.group(2)).split()))
    return out


D = load_dict()
ROWS = load_rows()


def norm(tok):
    """adopted alternative, no '?', bare number >= 99 -> block 1."""
    t = tok.split('|')[0].rstrip('?')
    if ':' not in t and t.isdigit() and int(t) >= 99:
        t = '1:' + t
    return t


def value(tok, shift=0, rows=True):
    """(value, kind); kind = letter / dict / rows / missing. shift=1 is the rotated-key control."""
    t = norm(tok)
    if ':' not in t:
        n = int(t)
        return NUM[(n - 2 + shift) % 97 + 2], 'letter'
    b, n = t.split(':')
    t = f'{b}:{int(n) + shift}'
    if t in D:
        return D[t], 'dict'
    if rows and t in ROWS:
        return ROWS[t][0], 'rows'
    return f'[{t}]', 'missing'


def text(tokens, shift=0, rows=True):
    """decoded line; runs of cipher letters are joined into words, as scripts/decode.py prints them."""
    out, prev = '', False
    for t in tokens:
        v, k = value(t, shift, rows)
        if k == 'letter':
            out += v if prev else ' ' + v
            prev = True
        else:
            out += ' ' + v
            prev = False
    return out.strip()


def head(s):
    print('\n## ' + s)


# 1. the checked lines -------------------------------------------------------------------------------------------
EYE = parse(os.path.join(HERE, 'tokens_s067R_L01-03.txt'))
toks = [t for _, ts in EYE for t in ts]
kinds = [value(t)[1] for t in toks]
head('1. 3.01.18 inv. 401 scan 67R, cipher lines 1-3, decoded with the key')
for ln, ts in EYE:
    print(f'{ln}: {text(ts)}')
codes = [t for t in toks if ':' in norm(t)]
print(f'tokens {len(toks)}: cipher letters {kinds.count("letter")}, codes {len(codes)} '
      f'(in ../key/dict {kinds.count("dict")}, from key_rows.tsv {kinds.count("rows")}, missing {kinds.count("missing")})')
print('tokens marked uncertain (?):', ' '.join(t for t in toks if '?' in t))
for t in toks:
    if '|' in t:
        alts = [a.rstrip('?') for a in t.split('|')]
        print(f'  {t}: ' + '; '.join(f'{a} = {value(a)[0]}' for a in alts))
print('codes taken from key_rows.tsv:', ', '.join(f'{norm(t)} {ROWS[norm(t)][0]} ({ROWS[norm(t)][1]}, {ROWS[norm(t)][2]})'
                                               for t in toks if value(t)[1] == 'rows'))

# 2. control ----------------------------------------------------------------------------------------------------
head('2. control: the same tokens with the key rotated by one row')
for ln, ts in EYE:
    print(f'{ln}: {text(ts, 1)}')
ck = [value(t, 1)[1] for t in toks]
print(f'rotated values: from ../key/dict {ck.count("dict")}, from key_rows.tsv {ck.count("rows")}, missing {ck.count("missing")}')

# 3. reading table ----------------------------------------------------------------------------------------------
head('3. s067R_L01-03.tsv against the decode')
tsv = [l.rstrip('\n').split('\t') for l in open(os.path.join(HERE, 's067R_L01-03.tsv'), encoding='utf-8')
       if l.strip() and not l.startswith('#')][1:]
bad = [r for r, t in zip(tsv, toks) if r[2] != t or r[3] != value(t)[0]]
print(f'rows {len(tsv)}, tokens {len(toks)}, rows whose token or value differs from the decode: {len(bad)}')
grades = [r[5] for r in tsv]
print('grades: ' + ', '.join(f'{g} {grades.count(g)}' for g in 'HCMI'))

# 4. machine pass -----------------------------------------------------------------------------------------------
head('4. a single machine pass against curated tokens')


def compare(ref, ours, label):
    ref = [norm(t) for t in ref]
    ours = [norm(t) for t in ours]

    def same(a, b):
        return sum(m.size for m in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks())
    n_ref = len(ref)
    exact = same(ref, ours)
    num = same([re.sub(r'^\d+:', '', t) for t in ref], [re.sub(r'^\d+:', '', t) for t in ours])
    val = same([value(t, rows=False)[0] for t in ref], [value(t, rows=False)[0] for t in ours])
    print(f'{label}: reference {n_ref} tokens, machine {len(ours)}; same token {exact} ({exact / n_ref:.0%}), '
          f'same number {num} ({num / n_ref:.0%}), same decoded value {val} ({val / n_ref:.0%})')


for page in ('s058R', 's059L'):
    ref = [t for _, ts in parse(os.path.join(TARGET, 'tokens', page + '.txt')) for t in ts]
    mp = [t for _, ts in parse(os.path.join(HERE, 'machine_pass', page + '.txt')) for t in ts]
    compare(ref, mp, f'{page} (../tokens/{page}.txt)')
mp67 = [t for ln, ts in parse(os.path.join(HERE, 'machine_pass', 's067R.txt')) if ln in ('L01', 'L02', 'L03') for t in ts]
compare(toks, mp67, 's067R L01-L03 (tokens_s067R_L01-03.txt)')

# 5. 11:719 -----------------------------------------------------------------------------------------------------
head('5. key row 11:719')
print(f'../key/dict: 11:718 = {D.get("11:718", "(absent)")}; 11:719 = {D.get("11:719", "(absent)")}')
print(f'key_rows.tsv (key scan 59L, column 1): 11:718 = {ROWS["11:718"][0]}; 11:719 = {ROWS["11:719"][0]}')
uses = {c: [] for c in ('11:718', '11:719')}
for f in sorted(glob.glob(os.path.join(TARGET, 'tokens', '*.txt'))):
    for ln, ts in parse(f):
        for t in ts:
            for alt in t.split('|'):
                if alt.rstrip('?') in uses:
                    uses[alt.rstrip('?')].append(f'{os.path.basename(f)} {ln}')
for c, u in uses.items():
    print(f'{c} in ../tokens/*.txt: {len(u)}' + (' (' + ', '.join(u) + ')' if u else ''))

