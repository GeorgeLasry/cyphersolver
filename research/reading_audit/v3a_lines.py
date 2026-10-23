"""v3 verify (a): join numbered reading lines ("12. text") of given line ranges of a file into running text.

    python research/reading_audit/v3a_lines.py <file> <from:to> [<from:to> ...]  > body.txt    (file line numbers)

Drops the line number, *(...)* annotations and "(continues ...)" remarks; joins hyphenated ends.
"""
import re, sys, pathlib
L = pathlib.Path(sys.argv[1]).read_text(encoding='utf8').splitlines()
out = []
for r in sys.argv[2:]:
    a, b = map(int, r.split(':'))
    for l in L[a - 1:b]:
        m = re.match(r'^\s*\d+\.\s+(.*)$', l)
        if not m: continue
        t = re.sub(r'\*\([^)]*\)\*', '', m.group(1))
        t = re.sub(r'\((?:continues|cont\.)[^)]*\)', '', t).strip()
        out.append(t)
s = ' '.join(out)
s = re.sub(r'(\w)- (\w)', r'\1\2', s)
print('## Reading\n\n' + s)
