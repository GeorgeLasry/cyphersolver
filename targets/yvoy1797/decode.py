"""Decode the unglossed runs (runs_c.txt, runs_d.txt) with table_L.tsv and table_E.tsv.

Per page, both tables are tried and the one covering more numbers is used; unknown numbers stay as [n].
Writes reading_unglossed.txt (BEFORE | decoded | AFTER per run) and prints coverage per page and overall.
Usage: python decode.py
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))


def table(code):
    t = {}
    for line in open(os.path.join(HERE, f'table_{code}.tsv'), encoding='utf8'):
        if line[0].isdigit():
            k, best, *_ = line.split('\t')
            t[k] = best
    return t


def pages(files):
    for f in files:
        page, head, blocks, blk = None, '', [], {}
        for r in open(os.path.join(HERE, f), encoding='utf8'):
            if r.startswith('# page'):
                if page and blocks:
                    yield page, head, blocks
                parts = r.split(None, 3)
                page, head, blocks = parts[2], (parts[3].strip() if len(parts) > 3 else ''), []
            elif r.startswith('# id'):
                blk = {}
                blocks.append(blk)
            elif r[:7] in ('BEFORE:',) or r[:3] in ('CT:', 'PT:') or r.startswith('AFTER:'):
                k, v = r.split(':', 1)
                blk[k] = v.strip()
        if page and blocks:
            yield page, head, blocks


if __name__ == '__main__':
    T = {c: table(c) for c in 'LE'}
    out, tot, hit = [], 0, 0
    for page, head, blocks in pages(['runs_c.txt', 'runs_d.txt']):
        nums = [g for b in blocks for g in b.get('CT', '').split() if re.match(r'\d', g)]
        if not nums:
            continue
        cov = {c: sum(1 for g in nums if g in T[c]) for c in 'LE'}
        c = max(cov, key=cov.get)
        tot += len(nums); hit += cov[c]
        out.append(f'## {page} {head}  [table {c}: {cov[c]}/{len(nums)}; other {cov["E" if c == "L" else "L"]}]\n')
        for b in blocks:
            ct = b.get('CT', '').split()
            if not ct:
                continue
            dec = ' '.join(T[c].get(g, f'[{g}]') for g in ct)
            out.append(f"... {b.get('BEFORE', '')} | {dec} | {b.get('AFTER', '')}\n")
    open(os.path.join(HERE, 'reading_unglossed.txt'), 'w', encoding='utf8').write(''.join(out))
    print(f'{tot} numbers on unglossed pages; {hit} decoded ({hit / max(tot, 1):.0%})')
