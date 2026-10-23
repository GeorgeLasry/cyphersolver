"""Move closed items out of a NOTES.md "## Remaining gaps" list (the checker wants a blocker on every item there).

    python research/reading_audit/move_closed_gaps.py <folder> [<folder> ...]

A "- ..." line under "## Remaining gaps" that says "closed" (and names no blocker) or describes a leaf with no cipher
is moved, unchanged, into a "Closed items:" paragraph just above the heading.
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]


def main(folder):
    p = ROOT / 'targets' / folder / 'NOTES.md'
    s = p.read_text(encoding='utf8')
    m = re.search(r'^## Remaining gaps[^\n]*\n(.*?)(?=^## |\Z)', s, re.S | re.M)
    if not m:
        print(folder, 'no Remaining gaps'); return
    keep, moved = [], []
    for line in m.group(1).split('\n'):
        if line.startswith('- ') and 'blocker' not in line and re.search(r'\bclosed\b|without cipher|no cipher', line, re.I):
            moved.append(line)
        else:
            keep.append(line)
    if not moved:
        print(folder, 'nothing to move'); return
    head = s[:m.start()]
    block = 'Closed items (moved out of Remaining gaps):\n' + '\n'.join(moved) + '\n\n'
    s = head + block + s[m.start():m.start(1)] + '\n'.join(keep) + s[m.end(1):]
    p.write_text(s, encoding='utf8')
    print(folder, 'moved', len(moved))


if __name__ == '__main__':
    for f in sys.argv[1:]:
        main(f)
