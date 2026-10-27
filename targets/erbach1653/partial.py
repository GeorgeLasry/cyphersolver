"""Apply a partial cell->letter table (key_cells.tsv) to ct_004.txt and print the result, '.' for unknown cells."""
import re, sys
key = {}
for l in open(sys.argv[2] if len(sys.argv) > 2 else 'key_cells.tsv', encoding='utf8'):
    l = l.split('#')[0].strip()
    if l:
        c, v = l.split()
        key[tuple(map(int, c.split(',')))] = v
for line in open(sys.argv[1] if len(sys.argv) > 1 else 'ct_004.txt', encoding='utf8'):
    if line.startswith('#'):
        continue
    lab = line.split()[0]
    body = line[len(lab):]
    out = re.sub(r'(\d+),(\d+)\??', lambda m: key.get((int(m.group(1)), int(m.group(2))), '.'), body)
    out = re.sub(r'(?<=\S) (?=\S)', lambda m: '', re.sub(r'\{[^}]*\}', lambda m: ' ' + m.group(0) + ' ', out))
    print(lab, out.strip()[:200])
