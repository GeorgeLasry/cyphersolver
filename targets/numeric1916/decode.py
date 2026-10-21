"""Independent decoder for the three June 1916 numeric codes (共密, 容密, 辰密) as Brice Dudout states them.

Written here from the key descriptions in his email of 19 Oct 2026 and on his pages; it does not import his code.
The character table is the Unihan kTaiwanTelegraph table already in targets/sunyatsen/tw.csv (kMainlandTelegraph
cn.csv as fallback). The digit streams are his re-readings, copied into groups.tsv by extract_groups.py.

  python decode.py              # per-telegram and per-family agreement with his published raw texts
  python decode.py --show N16   # one telegram, group by group
  python decode.py --key rongmi 2081 3308
"""
import argparse, csv, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUN = HERE.parent / 'sunyatsen'

def load_table():
    t = {}
    for name in ('cn.csv', 'tw.csv'):            # tw last, so it wins where both have the code
        for r in csv.DictReader(open(SUN / name, encoding='utf-8')):
            for code in r['code'].split():         # a few rows list two codes for one character
                t[int(code)] = r['character']
    return t

CTC = load_table()

# 共密: tens digit t -> phi(t), then P = (9000 - C') mod 10000
PHI = [9, 7, 6, 1, 4, 0, 5, 2, 8, 3]
def gongmi(g):
    c = int(g)
    t = c // 10 % 10
    return (9000 - (c - 10 * t + 10 * PHI[t])) % 10000

# 容密: one substitution per place, then P = sigma(C) + 0901 mod 10000 with ordinary carries
SIG = ['0123456790', '0123456789', '0198276543', '9801723456']   # thousands, hundreds, tens, units
def rongmi(g):
    s = int(''.join(SIG[i][int(ch)] for i, ch in enumerate(g)))
    return (s + 901) % 10000

# 辰密: page = rank of the first two digits in the countdown 99, 98 ... 91, 89 ... 11 (no zero);
# tens and units permuted, units 9 standing for 10 (it carries into the tens)
COUNTDOWN = [n for n in range(99, 10, -1) if '0' not in str(n)]
PAGE = {n: i for i, n in enumerate(COUNTDOWN)}
T = [3, 9, 8, 7, 1, 0, 2, 6, 4, 5]
U = [1, 9, 5, 4, 3, 2, 6, 7, 8, 10]
def chenmi(g):
    p = int(g[:2])
    if p not in PAGE:
        return None
    return 100 * PAGE[p] + 10 * T[int(g[2])] + U[int(g[3])]

def clair(g):
    return int(g)

KEYS = {'gongmi': gongmi, 'rongmi': rongmi, 'chenmi': chenmi, 'clair': clair}

def decode(fam, g):
    if not g.isdigit() or len(g) != 4:
        return None
    return KEYS[fam](g)

def glyph(p):
    return '□' if p is None else CTC.get(p, '□')

def load():
    out = []
    for line in open(HERE / 'groups.tsv', encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        mid, fam, prefix, direction, day, sheets, groups, raw = line.rstrip('\n').split('\t')
        out.append(dict(id=mid, fam=fam, prefix=prefix, dir=direction, day=day, sheets=sheets,
                        groups=groups.split(), raw=raw))
    return out

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    ap = argparse.ArgumentParser()
    ap.add_argument('--show')
    ap.add_argument('--key', choices=sorted(KEYS))
    ap.add_argument('groups', nargs='*')
    a = ap.parse_args()
    if a.key:
        ps = [decode(a.key, g) for g in a.groups]
        print(' '.join('????' if p is None else f'{p:04d}' for p in ps))
        print(''.join(glyph(p) for p in ps))
        return
    msgs = load()
    if a.show:
        m = next(x for x in msgs if x['id'] == a.show)
        for i, g in enumerate(m['groups']):
            p = decode(m['fam'], g)
            pub = m['raw'][i] if i < len(m['raw']) else ''
            print(i + 1, g, '????' if p is None else f'{p:04d}', glyph(p), '' if glyph(p) == pub else f'(published {pub})')
        return
    fams = {}
    print(f'{"id":5} {"family":7} {"groups":>6} {"match":>6} {"illegible":>9}  first disagreements')
    for m in msgs:
        mine = [glyph(decode(m['fam'], g)) for g in m['groups']]
        raw = list(m['raw'])
        n = len(mine)
        same = sum(x == y for x, y in zip(mine, raw))
        ill = sum(not g.isdigit() for g in m['groups'])
        diff = [(i + 1, m['groups'][i], mine[i], raw[i]) for i in range(min(n, len(raw))) if mine[i] != raw[i]]
        f = fams.setdefault(m['fam'], [0, 0, 0, 0, 0])
        f[0] += 1; f[1] += n; f[2] += same; f[3] += ill; f[4] += (len(raw) == n and same == n)
        print(f'{m["id"]:5} {m["fam"]:7} {n:6} {same:6} {ill:9}  {diff[:3] if diff else ""}{"" if len(raw) == n else f" length {len(raw)} vs {n}"}')
    print()
    print(f'{"family":7} {"tel.":>4} {"groups":>6} {"match":>6} {"illegible":>9} {"identical texts":>15}')
    for fam, (k, n, s, ill, ident) in fams.items():
        print(f'{fam:7} {k:4} {n:6} {s:6} {ill:9} {ident:>11}/{k}')
    print(f'{"all":7} {sum(v[0] for v in fams.values()):4} {sum(v[1] for v in fams.values()):6} '
          f'{sum(v[2] for v in fams.values()):6} {sum(v[3] for v in fams.values()):9} '
          f'{sum(v[4] for v in fams.values()):>11}/{sum(v[0] for v in fams.values())}')

if __name__ == '__main__':
    main()
