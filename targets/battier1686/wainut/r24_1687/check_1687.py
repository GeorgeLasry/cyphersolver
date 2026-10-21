"""Reproduces the numbers in "Further contribution by WAINUT (21 Oct 2026)" of ../../NOTES.md.

  python3 check_1687.py          (from any directory; paths are relative to this file; standard library only)

1. decodes the checked tokens in tokens/ (NA 3.01.18 inv. 401) with the key in ../../key (letters.py and dict/*.tsv,
   loaded as scripts/decode.py loads them) and, for codes not in ../../key/dict, key_rows_machine.tsv;
2. counts groups and groups left uncertain ('?') per letter, and how many codes come from each source;
3. prints the line of ../../inv/orch_letters.tsv for the letter of 2 Jan 1687.
"""
import glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.dirname(os.path.dirname(HERE))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(TARGET, 'key'))
from letters import NUM  # noqa: E402  (Bourdeau's letter table, 2..98)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def load_tsv(files):
    d = {}
    for f in files:
        for line in open(f, encoding='utf-8'):
            if not line.strip() or line.startswith('#'):
                continue
            p = line.rstrip('\n').split('\t')
            if len(p) >= 2:
                d[p[0].strip()] = p[1].strip()
    return d


D = load_tsv(sorted(glob.glob(os.path.join(TARGET, 'key', 'dict', '*.tsv'))))
ROWS = load_tsv([os.path.join(HERE, 'key_rows_machine.tsv')])


def parse(fn):
    """As scripts/decode.py parse(): 'Lnn: tokens {clear text}'."""
    out = []
    for raw in open(fn, encoding='utf-8'):
        m = re.match(r'\s*(L\w+)\s*:\s*(.*)', raw)
        if m:
            out.append((m.group(1), re.sub(r'\{[^}]*\}', ' ', m.group(2)).split()))
    return out


def value(tok):
    t = tok.split('|')[0].rstrip('?')
    if t.startswith('v:'):
        return '?', 'letter'
    if ':' not in t:
        n = int(t)
        if 2 <= n <= 98:
            return NUM[n], 'letter'
        t = f'1:{n}'
    if t in D:
        return D[t], 'dict'
    if t in ROWS:
        return ROWS[t] + '*', 'rows'
    return f'[{t}]', 'missing'


def text(tokens):
    out, prev = '', False
    for t in tokens:
        v, k = value(t)
        q = '?' if t.endswith('?') else ''
        if k == 'letter':
            out += (v if prev else ' ' + v) + q
            prev = True
        else:
            out += ' ' + v + q
            prev = False
    return out.strip()


LETTERS = [
    ('16 Jan 1687', ['038L', '038R', '039L']),
    ('13 Feb 1687', ['045R', '046L', '046R']),
    ('27 Feb 1687', ['047R', '048L', '048R', '049L', '049R', '050L']),
    ('13 Mar 1687 (55L only)', ['055L']),
    ('10 Jun 1687 (67R)', ['067R']),
    ('20 Nov 1687', ['089R']),
    ('18 Dec 1687 (94R lines 1-5)', ['094R']),
]

print('## 1. decoded (word* = key_rows_machine.tsv; x? = uncertain group)')
tot = [0, 0]
kinds = {}
summary = []
for name, pages in LETTERS:
    n = unc = 0
    print(f'\n### {name}')
    for p in pages:
        for ln, ts in parse(os.path.join(HERE, 'tokens', f's{p}.txt')):
            print(f's{p} {ln}: {text(ts)}')
            n += len(ts)
            unc += sum(t.endswith('?') for t in ts)
            for t in ts:
                k = value(t)[1]
                kinds[k] = kinds.get(k, 0) + 1
    summary.append(f'{name}: {n} groups checked by eye, {unc} left uncertain')
    tot[0] += n
    tot[1] += unc

print('\n## 2. counts')
print('\n'.join(summary))
print(f'ALL: {tot[0]} groups, {tot[1]} uncertain')
print('groups by source: ' + ', '.join(f'{k} {v}' for k, v in sorted(kinds.items())))

print('\n## 3. ../../inv/orch_letters.tsv, 2 Jan 1687')
for line in open(os.path.join(TARGET, 'inv', 'orch_letters.tsv'), encoding='utf-8'):
    if line.startswith('1687-01-02'):
        print(line.rstrip('\n'))
