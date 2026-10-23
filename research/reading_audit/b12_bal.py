"""b12: print a Balbases tx/ file line by line as token=value pairs with the frozen key (key.json)."""
import json, sys
sys.stdout.reconfigure(encoding='utf-8')
K = json.load(open(r'C:\Users\dbour\cypher\.worktrees\reading-gate\targets\balbases1677\key.json', encoding='utf-8'))
n = 0
for line in open(sys.argv[1], encoding='utf-8'):
    if line.startswith('# page'): print(line.strip())
    if not line.startswith('C:'): continue
    n += 1
    out = []
    for t in line[2:].split():
        v = K.get(t.rstrip('?'))
        out.append('%s=%s' % (t, '·' if v == '' else (v if v is not None else '??')))
    print('%2d  %s' % (n, ' '.join(out)))
