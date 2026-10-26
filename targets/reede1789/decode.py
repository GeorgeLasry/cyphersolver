"""Decode the unglossed runs (unglossed_*.txt) with table.tsv and measure coverage.

Each group is looked up with its marks first (e.g. 207{u3}), then by its bare number; values below 60% agreement
are shown with a trailing '?', unknown groups as [n]. Writes reading_unglossed.txt with BEFORE / decoded / AFTER.
Usage: python decode.py
"""
import glob, os, re
from table import norm_group

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    marked, bare = {}, {}
    for line in open(os.path.join(HERE, 'table.tsv'), encoding='utf8'):
        if line.startswith('# ') or not line.strip():
            continue
        k, best, v, t, _ = line.rstrip('\n').split('\t')
        sure = int(v) / int(t) >= 0.6
        (bare if k.startswith('#') else marked)[k.lstrip('#')] = (best, sure)
    return marked, bare


def decode(groups, marked, bare):
    out, known, sure = [], 0, 0
    for g in groups:
        n, key = norm_group(g)
        if not n:
            out.append(f'[{g}]'); continue
        hit = marked.get(key) or bare.get(n)
        if hit:
            known += 1; sure += hit[1]
            out.append(hit[0] + ('' if hit[1] else '?'))
        else:
            out.append(f'[{n}]')
    return out, known, sure


if __name__ == '__main__':
    marked, bare = load()
    tot = kn = su = 0
    lines = []
    for f in sorted(glob.glob(os.path.join(HERE, 'unglossed_*.txt'))):
        blk = {}
        for raw in open(f, encoding='utf8'):
            if raw.startswith('# id'):
                blk = {'tag': raw[2:].strip()}
            for k in ('BEFORE', 'AFTER', 'PT'):
                if raw.startswith(k + ':'):
                    blk[k] = raw[len(k) + 1:].strip()
            if raw.startswith('CT:'):
                groups = [g for g in raw[3:].split() if g != '?']
                out, a, b = decode(groups, marked, bare)
                tot += len(groups); kn += a; su += b
                blk['dec'] = ' '.join(out)
            if raw.startswith('AFTER:') and 'dec' in blk:
                lines.append(f"# {blk['tag']}\n... {blk.get('BEFORE', '')} | {blk['dec']} | {blk.get('AFTER', '')}\n")
    open(os.path.join(HERE, 'reading_unglossed.txt'), 'w', encoding='utf8').write(''.join(lines))
    print(f'{tot} groups; {kn} with a table value ({kn / max(tot, 1):.0%}), {su} of them sure ({su / max(tot, 1):.0%})')
