"""Lead 6 (26 Oct 2026): a lexicon of the recurring units of the Indus texts, built from the clean ICIT objects with
records. Units: name bodies (the signs before an ending, rtools.name_of), bound pairs (adjacent pairs in 5+ distinct
lines where each sign predicts the other in 50%+ of its lines), count units (numeral + sign), the closing formulas and
the single signs with 20+ tokens. For each: distinct texts, objects, sites, object kinds, endings that follow,
numerals that precede, field motifs, and whether it occurs on Mahadevan's lines (B). Writes results/unit_lexicon.tsv and
results/unit_lexicon.md."""
from collections import Counter, defaultdict

import rtools as R
from leadkit import ab, objects
from numerals import NUMS

FORMULAS = {('705', '33', '520'), ('706', '33', '520')}


def grams(t, n):
    return [tuple(t[i:i + n]) for i in range(len(t) - n + 1)]


def main():
    O = objects()
    DA, DB = ab()
    Bset = {g for t in DB for n in range(1, 7) for g in grams(t, n)}
    big, first, second = Counter(), Counter(), Counter()
    DL = sorted({t for s, ty, mo, size, lines, rec in O for t in lines})
    for t in DL:
        for a, b in set(zip(t, t[1:])):
            big[(a, b)] += 1
        for a in set(t[:-1]):
            first[a] += 1
        for b in set(t[1:]):
            second[b] += 1
    bound = {ab_ for ab_, n in big.items() if n >= 5 and n / first[ab_[0]] >= 0.5 and n / second[ab_[1]] >= 0.5}
    occ = Counter(g for t in DL for g in t)
    units = {}
    for t in DL:
        nm = R.name_of(list(t))
        if nm and nm[0] and len(nm[0]) >= 2:
            units.setdefault(('name', tuple(nm[0])), set()).add(t)
        for a, b in zip(t, t[1:]):
            if (a, b) in bound:
                units.setdefault(('bound', (a, b)), set()).add(t)
            if a in NUMS and b not in NUMS:
                units.setdefault(('count', (b,)), set()).add(t)
        for g3 in grams(t, 3):
            if g3 in FORMULAS:
                units.setdefault(('formula', g3), set()).add(t)
        for g in set(t):
            if occ[g] >= 20 and g not in NUMS:
                units.setdefault(('sign', (g,)), set()).add(t)
    rows = []
    for (kind, u), texts in units.items():
        if kind == 'name' and len(texts) < 2:
            continue
        objs, sites, kinds, motifs, ends, nums = 0, Counter(), Counter(), Counter(), Counter(), Counter()
        for s, ty, mo, size, lines, rec in O:
            hit = [t for t in lines if t in texts]
            if not hit:
                continue
            objs += 1
            sites[s] += 1
            kinds[ty] += 1
            motifs[mo or 'None'] += 1
            for t in hit:
                for i in range(len(t) - len(u) + 1):
                    if tuple(t[i:i + len(u)]) == u:
                        j = i + len(u)
                        ends[t[j] if j < len(t) and t[j] in R.END else ('$' if j >= len(t) else '-')] += 1
                        if i and t[i - 1] in NUMS:
                            nums[NUMS[t[i - 1]][0]] += 1
        fmt = lambda c, k=4: ' '.join('%s:%d' % x for x in c.most_common(k))
        rows.append((kind, ' '.join(u), len(texts), objs, fmt(sites), fmt(kinds), fmt(ends), fmt(nums), fmt(motifs), 'yes' if u in Bset or any(all(tt[i:i + len(u)] == u for i in [0]) for tt in []) else 'no'))
    rows.sort(key=lambda r: (r[0], -r[3]))
    with open('results/unit_lexicon.tsv', 'w', encoding='utf-8') as f:
        f.write('kind\tunit\tdistinct_texts\tobjects\tsites\tobject_kinds\tfollowed_by\tpreceded_by_numeral\tmotifs\ton_M77\n')
        for r in rows:
            f.write('\t'.join(map(str, r)) + '\n')
    by = Counter(r[0] for r in rows)
    with open('results/unit_lexicon.md', 'w', encoding='utf-8') as f:
        f.write('# Unit lexicon (26 Oct 2026)\n\nBuilt by `unit_lexicon.py` from %d distinct clean ICIT lines on %d objects. Rows: %s.\n\n' % (len(DL), len(O), ', '.join('%s %d' % kv for kv in sorted(by.items()))))
        f.write('Columns: distinct texts and objects carrying the unit; sites, object kinds and field motifs of those objects (top four, with counts); what follows the unit (740 / 520, $ = line end, - = another sign); the numeral values before it; whether the unit also occurs in Mahadevan\'s lines not in ICIT.\n\nThe table is descriptive: it records where each unit occurs, not what it means. See `results/unit_lexicon.tsv`.\n')
    print({k: v for k, v in by.items()}, 'bound pairs', len(bound))


if __name__ == '__main__':
    main()
