"""Merge the aligned runs (AL: lines of pairs_*.txt) with hereditary1796's R2237 alignment and rebuild the word list.

Writes all_assign.txt (one run per line, group=output, outputs lower-case without spaces or accents) and
key_wordlist.txt (number, entry; '.' unknown letter, '+' length unknown), and prints the conflicts with their scans.
Usage: python merge.py
"""
import glob, os, re, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'hereditary1796'))
import wordtable as wt

ITEM = re.compile(r'(\S+?)=(.*?)(?=\s+\S+?=|$)')


def norm(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r"[^a-z?]", '', s)


lines = []
for f in sorted(glob.glob(os.path.join(HERE, 'pairs_*.txt'))):
    tag, ct = '', []
    for raw in open(f, encoding='utf8'):
        if raw.startswith('# scan'):
            tag, ct = raw[2:].strip(), []
        elif raw.startswith('CT:'):
            ct = [t for t in raw[3:].split() if wt.parse(t)]
        elif raw.startswith('AL:'):
            items, used = [], set()
            for g, out in ITEM.findall(raw[3:].strip()):
                out = norm(out)
                if g == '?' or not out or '?' in out or wt.parse(g) is None:
                    continue
                # the AL group often lacks its marks: take the full form from the CT line (same entry, in order)
                n = wt.parse(g)[0]
                for i, t in enumerate(ct):
                    if i not in used and wt.parse(t)[0] == n:
                        used.add(i)
                        if g.isdigit() or len(t) > len(g):
                            g = t
                        break
                items.append(f'{g}={out}')
            if items:
                lines.append((tag, ' '.join(items)))
prior = os.path.join(HERE, '..', 'hereditary1796', 'r2237_assign.txt')
for raw in open(prior, encoding='utf8'):
    if raw.strip() and not raw.startswith('#'):
        lines.append(('r2237', raw.strip()))

with open(os.path.join(HERE, 'all_assign.txt'), 'w', encoding='utf8') as out:
    out.write('# merged alignments: pairs_*.txt AL lines + hereditary1796 r2237_assign.txt (built by merge.py)\n')
    for tag, s in lines:
        out.write(f'# {tag}\n{s}\n')

letters, length, conflicts = wt.build(os.path.join(HERE, 'all_assign.txt'))
with open(os.path.join(HERE, 'key_wordlist.txt'), 'w', encoding='utf8') as out:
    out.write('# Euler word list rebuilt from A32-630 interlined pages + R2237 (merge.py); . unknown, + length unknown\n')
    for n in sorted(letters):
        out.write(f'{n} {wt.show(n, letters, length)}\n')
full = sum(1 for n in letters if n in length and '.' not in wt.show(n, letters, length))
print(len(lines), 'runs;', len(letters), 'entries,', full, 'complete; max entry', max(letters))
print(len(conflicts), 'conflicts')
for c in conflicts[:80]:
    print('  ', c)
