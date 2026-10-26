"""Vote tables for the two d'Yvoy codes from the AL lines of runs_a.txt / runs_b.txt, with a leave-one-page-out test.

Code L = London 1797-98 (pages dated 1797-98); code E = 1799 (A35-1452, ids from about 147380, and runs_b).
A number keeps its marks (1137 and 95' are different keys). Output: table_L.tsv, table_E.tsv.
Test: for each page, build the table without it and count how many of its glossed numbers decode to a word found
in the run's own decipherment (PT), against another page's run.  Usage: python tables.py
"""
import collections, os, re, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ITEM = re.compile(r"(\S+?)=(.*?)(?=\s+\S+?=|$)")


def nz(s):
    return re.sub('[^a-z]', '', unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower())


def runs():
    E99 = lambda p: 'E' if p == '147437' or int(p) >= 147380 else 'L'   # A35-1452 (1799) starts near id 147380
    for f, code_of in (('runs_a.txt', E99), ('runs_b.txt', lambda p: 'E'), ('runs_c.txt', E99), ('runs_d.txt', E99), ('runs_e.txt', E99)):
        page = None
        blk = {}
        for r in open(os.path.join(HERE, f), encoding='utf8'):
            if r.startswith('# page'):
                page = r.split()[2]
            elif r.startswith('# id'):
                blk = {'page': r.split()[2]}
            elif r[:3] in ('CT:', 'PT:', 'AL:'):
                blk[r[:2]] = r[3:].strip()
                if r.startswith('AL:') and 'CT' in blk:
                    p = blk['page']
                    al = [] if blk['AL'].lower().startswith('none') else ITEM.findall(blk['AL'])
                    yield code_of(p), p, blk['CT'].split(), nz(blk.get('PT', '')), al


def build(rows):
    t = collections.defaultdict(collections.Counter)
    for code, p, ct, pt, al in rows:
        for g, w in al:
            g = g.replace('.', ' ').split()
            w = nz(w)
            if len(g) == 1 and w and '?' not in g[0]:
                t[g[0]][w] += 1
    return t


if __name__ == '__main__':
    R = list(runs())
    for code in 'LE':
        rows = [r for r in R if r[0] == code]
        t = build(rows)
        with open(os.path.join(HERE, f'table_{code}.tsv'), 'w', encoding='utf8') as w:
            w.write('# number\tbest\tvotes\ttotal\tall\n')
            for k in sorted(t, key=lambda k: (int(re.sub(r'\D', '', k) or 0), k)):
                c = t[k]; b, v = c.most_common(1)[0]
                w.write(f'{k}\t{b}\t{v}\t{sum(c.values())}\t{dict(c)}\n')
        pages = sorted({r[1] for r in rows})
        own = oth = tot = 0
        for p in pages:
            tt = build([r for r in rows if r[1] != p])
            others = [r for r in rows if r[1] != p]
            for i, (_, _, ct, pt, _) in enumerate([r for r in rows if r[1] == p]):
                if not pt:
                    continue
                alt = others[i % len(others)][3] if others else ''
                for g in ct:
                    if g in tt:
                        v = tt[g].most_common(1)[0][0]
                        if len(v) >= 2:
                            tot += 1; own += v in pt; oth += v in alt
        print(f'code {code}: {len(rows)} runs on {len(pages)} pages; {len(t)} numbers in table; '
              f'leave-one-page-out: {own}/{tot} decoded words in own gloss ({own / max(tot, 1):.0%}), '
              f'{oth}/{tot} in another ({oth / max(tot, 1):.0%})')
