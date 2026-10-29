"""Build the code table from the deciphered sibling transcriptions.

Reads transcription/sib*.txt (lines "Lnn group=value ...", see sib188_60917.txt for the conventions) and
writes codetable.tsv: group, value, grade, sources (file:line), count, and the other values seen if the
glosses disagree.

Grades (README Conventions): H = the contemporary interlinear gloss, legible, digits certain, and the
occurrences agree (all of them, or at least 4 and 85%); M = only glosses or digits marked ? in the
transcription, or the glosses disagree.

    python build_table.py            # write codetable.tsv and print a summary
"""
import collections
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
# 835 is "pour" everywhere; the 188 enclosure writes "pourr-i-es" (pourriez) with the r of the next syllable run on.
ALIAS = {'pourr': 'pour'}
TOKEN = re.compile(r'(\d+)(\??)=(\S+)')


def read_pairs():
    """Yield (group, value, doubtful, source) for every glossed group, struck groups left out."""
    for path in sorted(glob.glob(os.path.join(HERE, 'transcription', 'sib*.txt'))):
        name = os.path.basename(path)[:-4]
        for line in open(path, encoding='utf-8'):
            if not line.startswith('L'):
                continue
            label, rest = line.split(None, 1)
            rest = re.sub(r'\{[^}]*\}(=\S+)?', ' ', rest)          # struck groups
            for m in TOKEN.finditer(rest):
                group, qdigit, value = m.group(1), m.group(2), m.group(3)
                doubtful = bool(qdigit) or '?' in value
                value = value.strip('[]').lstrip('?')
                yield group, value, doubtful, f'{name}:{label}'


def norm(value):
    """Spelling-only differences (capitals, apostrophe, accent on a/à) are not disagreements."""
    value = value.lower().replace("'", '').replace('à', 'a').replace('é', 'e')
    return ALIAS.get(value, value)


def build():
    seen = collections.defaultdict(list)
    for group, value, doubtful, src in read_pairs():
        seen[int(group)].append((value, doubtful, src))
    rows = []
    for group in sorted(seen):
        occ = seen[group]
        firm = [v for v, d, _ in occ if not d] or [v for v, _, _ in occ]
        counts = collections.Counter(norm(v) for v in firm)
        value = collections.Counter(ALIAS.get(v, v) for v in firm).most_common(1)[0][0]
        others = sorted(set(v for v, _, _ in occ if norm(v) != norm(value)))
        top = counts.most_common(1)[0][1]
        # H: every firm gloss agrees, or at least 4 firm glosses and 85% of them agree (one copyist's slip in
        # eighteen is not a doubt); anything else, or only doubtful glosses, is M.
        agree = len(counts) == 1 or (sum(counts.values()) >= 4 and top / sum(counts.values()) >= 0.85)
        grade = 'H' if agree and any(not d for _, d, _ in occ) else 'M'
        rows.append((group, value, grade, ' '.join(s for _, _, s in occ), len(occ), '|'.join(others)))
    with open(os.path.join(HERE, 'codetable.tsv'), 'w', encoding='utf-8') as f:
        f.write('# group\tvalue\tgrade\tsources\tcount\tother_values\n')
        f.write('# Built by build_table.py from transcription/sib*.txt. value "_" = no gloss (null or punctuation).\n')
        for r in rows:
            f.write('\t'.join(str(x) for x in r) + '\n')
    return rows


if __name__ == '__main__':
    rows = build()
    print(f'{len(rows)} groups, {sum(r[4] for r in rows)} glossed occurrences, '
          f'{sum(1 for r in rows if r[2] == "H")} grade H, {sum(1 for r in rows if r[2] == "M")} grade M')
    for r in rows:
        if r[5] and r[2] == 'M':
            print('  disagreement:', r[0], r[1], 'also', r[5], r[3])
