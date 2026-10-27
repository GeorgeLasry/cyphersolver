"""Merge the sample alignments (align/0NN.tsv) into one table per code and measure how consistently each
code group carries the same value across occurrences. Code A = the January 1791 code; code B = the code of the
1792 Danzig letters. 037 is all B; 039 is B up to '# SECTION B', then A; 045 is A up to '# PART 2', then B."""
import re, collections, sys
FILES = {'002': 'A', '032': 'A', '037': 'B', '039': 'B', '045': 'A'}
SWITCH = {'039': ('# SECTION B', 'A'), '045': ('# PART 2', 'B')}

def norm(v):
    v = v.replace('[?]', '').strip().lower()
    return v.translate(str.maketrans('ąćęłńóśźży', 'acelnoszzi'))

def tokens():
    for d, code in FILES.items():
        for line in open(f'align/{d}.tsv', encoding='utf8'):
            if d in SWITCH and line.startswith(SWITCH[d][0]):
                code = SWITCH[d][1]
            if line.startswith('#') or not line.strip():
                continue
            g, _, v = line.rstrip('\n').partition('\t')
            yield d, code, g.strip(), v.strip()

if __name__ == '__main__':
    occ = collections.defaultdict(list)
    per = collections.Counter()
    with open('align/pairs_all.tsv', 'w', encoding='utf8') as out:
        out.write('# despatch\tcode\tgroup\tvalue (from the contemporary decipherment, ZbPop 421)\n')
        for d, c, g, v in tokens():
            out.write(f'{d}\t{c}\t{g}\t{v}\n'); per[(d, c)] += 1
            if v not in ('?', '-', ''):
                occ[(c, re.sub(r'[a-z?]+$', '', g) if False else g)].append(norm(v))
    print('tokens per despatch/code', dict(per))
    for c in 'AB':
        rep = {k: v for k, v in occ.items() if k[0] == c and len(v) >= 2}
        n = sum(len(v) for v in rep.values())
        agree = sum(collections.Counter(v).most_common(1)[0][1] for v in rep.values())
        types = sum(1 for k in occ if k[0] == c)
        print(f'code {c}: {types} group types; {len(rep)} occur twice or more, {n} occurrences, '
              f'{agree} ({agree / n:.1%}) carry the type\'s commonest value')
