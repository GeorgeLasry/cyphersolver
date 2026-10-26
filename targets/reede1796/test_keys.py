"""Test the two candidate keys on Van Reede's 1796-1807 code passages (runs_a.txt, runs_b.txt).

Keys: (R) target reede1789's table.tsv, Van Reede's 1789-92 marked code to Wilhelmina (bare numbers; word values);
      (E) target wilhelmina1795's key_euler.tsv, the 1795-96 Euler word list (k)N drop first k, N^k drop last k,
          N.p.q letter positions, N_ whole entry).
For glossed runs (PT not none) each decoded piece of 2+ letters is checked against the run's own gloss and against
another run's gloss. For every run the decoding is printed. Usage: python test_keys.py
"""
import os, re, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')


def nz(s):
    return re.sub('[^a-z]', '', unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower())


R = {}
for l in open(os.path.join(ROOT, 'reede1789', 'table.tsv'), encoding='utf8'):
    if l.startswith('#') and l[1:2].isdigit():
        k, b, v, t, _ = l.rstrip('\n').split('\t')
        R[int(k[1:])] = b
E = {}
for l in open(os.path.join(ROOT, 'wilhelmina1795', 'key_euler.tsv'), encoding='utf8'):
    if l[0].isdigit():
        n, w, _ = l.rstrip('\n').split('\t')
        E[int(n)] = w.replace('+', '')

GROUP = re.compile(r'(?:(\d+)[)/])?(\d+)((?:[.,]\d+)*)(?:\^(\d+))?(?:/\d+)?$')


def parse(g):
    g = re.sub(r'\{[^}]*\}|_', '', g)
    m = GROUP.match(g)
    if not m:
        return None
    k, n, pos, j = m.groups()
    return int(k or 0), int(n), [int(p) for p in re.split('[.,]', pos)[1:]] if pos else [], int(j or 0)


def dec_R(g):
    p = parse(g)
    return R.get(p[1]) if p else None


def dec_E(g):
    p = parse(g)
    if not p or p[1] not in E:
        return None
    k, n, pos, j = p
    w = E[n]
    if pos:
        return ''.join(w[q - 1] if 0 < q <= len(w) else '?' for q in pos)
    if k + j >= len(w):
        return '!'          # cut longer than the entry: does not fit
    return w[k:len(w) - j] if j else w[k:]


def runs():
    for f in ('runs_a.txt', 'runs_b.txt'):
        path = os.path.join(HERE, f)
        if not os.path.exists(path):
            continue
        blk = None
        for r in open(path, encoding='utf8'):
            if r.startswith('# id'):
                blk = {'tag': r[2:].strip()}
            elif blk is not None and ':' in r and r.split(':')[0] in ('CT', 'PT', 'BEFORE', 'AFTER'):
                k, v = r.split(':', 1)
                blk[k] = v.strip()
                if k == 'PT':
                    yield blk


if __name__ == '__main__':
    rows = list(runs())
    glossed = [b for b in rows if nz(b.get('PT', '')) and not b['PT'].lower().startswith('none')]
    for name, dec in (('reede1789 table', dec_R), ('Euler list', dec_E)):
        own = oth = tot = 0
        for i, b in enumerate(glossed):
            alt = nz(glossed[(i + 3) % len(glossed)]['PT']) if len(glossed) > 1 else ''
            pt = nz(b['PT'])
            for g in re.sub(r'\[[^\]]*\]', ' ', b.get('CT', '')).split():
                v = dec(g)
                if v and len(nz(v)) >= 2:
                    tot += 1; own += nz(v) in pt; oth += nz(v) in alt
        print(f'{name}: glossed controls {len(glossed)} runs; decoded pieces in own gloss {own}/{tot}, in another {oth}/{tot}')
    print()
    for b in rows:
        groups = re.sub(r'\[[^\]]*\]', ' ', b.get('CT', '')).split()
        r = ' '.join(dec_R(g) or f'[{g}]' for g in groups)
        e = ' '.join(dec_E(g) or f'[{g}]' for g in groups)
        unfit = sum(1 for g in groups if dec_E(g) == '!')
        print(f"# {b['tag']}  ({len(groups)} groups; Euler cuts that do not fit: {unfit})")
        print('  PT:', b.get('PT', ''))
        print('  R :', r[:300])
        print('  E :', e[:300])
