"""Rebuild Code No. 11 values by segmenting every coded passage against its plaintext.

Each passage is a run of code groups whose plaintext is known (TJ's interlinear decoding, his clear-text
sheets, or the printed Founders text). A group stands for a whole word, a syllable, a letter or a punctuation
mark. The solver iterates: with the values fixed so far, a dynamic programme finds the cheapest ways to cut each
passage's plaintext among its groups; a group whose cut is the same in every cheapest solution gets that value.
Values that contradict across passages are reported, not forced.

Input: passages.tsv (passage id, source, groups, plaintext; built by make_passages.py).
Output: key.tsv (code, value, evidence count, passages), segment_report.txt.
"""
import csv, os, re, sys
from collections import defaultdict, Counter

HERE = os.path.dirname(os.path.abspath(__file__))
PUNCT = set('.,;:?')
MAXLEN = 12


def norm_plain(s):
    s = s.lower().replace('&', 'and').replace('’', "'")
    out = []
    for ch in s:
        if ch.isalnum():
            out.append(ch)
        elif ch in PUNCT:
            out.append(ch)
    return ''.join(out)


def load():
    ps = []
    with open(os.path.join(HERE, 'passages.tsv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            groups = r['groups'].split()
            ps.append({'id': r['id'], 'source': r['source'], 'groups': groups,
                       'plain': norm_plain(r['plain']), 'raw': r['plain']})
    return ps


def best_cuts(groups, plain, known, beam=4000, cap=200):
    """Cheapest segmentations under one rule a DP cannot carry: a code repeated in the passage keeps one
    value. Beam search over (group index, text position, assignments). Known groups must match exactly
    (a mismatch costs 12 and consumes len(value)); an unknown code takes 1..MAXLEN chars (cost 2 up to 4
    chars, 3 longer) or nothing (cost 8, a null or slip)."""
    n, m = len(groups), len(plain)
    states = [(0, 0, ())]  # (cost, j, assignment tuple of (code, value))
    for i in range(n):
        g = groups[i]
        nxt = {}
        for c0, j, asg in states:
            a = dict(asg)
            opts = []
            if g in known:
                v = known[g]
                opts.append((len(v), 0) if plain.startswith(v, j) else (min(len(v), m - j), 12))
            elif g in a:
                v = a[g]
                if plain.startswith(v, j):
                    opts.append((len(v), 0))
                else:
                    continue
            else:
                for L in range(1, min(MAXLEN, m - j) + 1):
                    opts.append((L, 2 if L <= 4 else 3))
                opts.append((0, 8))
            for L, c in opts:
                k = j + L
                na = asg
                if g not in known and g not in a:
                    na = tuple(sorted(asg + ((g, plain[j:k]),)))
                key = (k, na)
                nc = c0 + c
                if key not in nxt or nc < nxt[key]:
                    nxt[key] = nc
        # remaining-length feasibility: drop states that cannot finish (each later group <= MAXLEN)
        rem = n - i - 1
        states = sorted(((c, k, na) for (k, na), c in nxt.items() if m - k <= rem * MAXLEN + 0),
                        key=lambda x: x[0])[:beam]
    fin = [(c, na) for c, k, na in states if k == m]
    if not fin:
        return None, []
    best = min(c for c, _ in fin)
    sols = []
    for c, na in fin:
        if c != best:
            continue
        a = dict(na)
        seg, j = [], 0
        for g in groups:
            v = known.get(g, a.get(g, ''))
            if g in known and not plain.startswith(v, j):
                v = plain[j:j + len(v)]
            seg.append(v)
            j += len(v)
        sols.append(seg)
        if len(sols) >= cap:
            break
    return best, sols


def main():
    ps = load()
    known = {}
    # Seed: single-group interlinear values are given per group in passages of kind 'interlinear-1'.
    for p in ps:
        if p['source'] == 'pair':
            known.setdefault(p['groups'][0], p['plain'])
    for rnd in range(30):
        new = {}
        for p in ps:
            if p['source'] == 'pair':
                continue
            total, sols = best_cuts(p['groups'], p['plain'], known)
            if not sols or len(sols) >= 200:
                continue
            for idx, g in enumerate(p['groups']):
                if g in known:
                    continue
                vals = {s[idx] for s in sols}
                if len(vals) == 1:
                    v = vals.pop()
                    if v:
                        new.setdefault(g, Counter())[v] += 1
        added = 0
        for g, cnt in new.items():
            v, c = cnt.most_common(1)[0]
            if len(cnt) == 1 or c >= 2 * sum(cnt.values()) / 3:
                known[g] = v
                added += 1
        if not added:
            break
    # Final pass: report per passage
    uses = defaultdict(list)
    lines = []
    for p in ps:
        if p['source'] == 'pair':
            uses[p['groups'][0]].append((p['plain'], p['id']))
            continue
        total, sols = best_cuts(p['groups'], p['plain'], known)
        s = sols[0] if sols else []
        amb = len(sols)
        lines.append(f"## {p['id']} ({p['source']}) cost={total} solutions={amb}")
        lines.append('   ' + p['raw'])
        segs = []
        for idx, g in enumerate(p['groups']):
            v = s[idx] if idx < len(s) else '?'
            if g in known and known[g] != v:
                segs.append(f'{g}={known[g]}!≠{v}')
            else:
                segs.append(f'{g}={v}' if g in known else f'{g}=({v})')
            uses[g].append((v, p['id']))
        lines.append('   ' + '  '.join(segs))
    with open(os.path.join(HERE, 'segment_report.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    with open(os.path.join(HERE, 'key.tsv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['code', 'value', 'n', 'readings_seen', 'passages'])
        for g in sorted(uses, key=lambda x: int(re.sub(r'\D', '', x) or 0)):
            seen = Counter(v for v, _ in uses[g])
            w.writerow([g, known.get(g, ''), len(uses[g]),
                        ' | '.join(f'{v}x{c}' for v, c in seen.most_common()),
                        ' '.join(sorted({pid for _, pid in uses[g]}))])
    print(f'{len(known)} values fixed; report in segment_report.txt, key in key.tsv')


if __name__ == '__main__':
    sys.exit(main())
