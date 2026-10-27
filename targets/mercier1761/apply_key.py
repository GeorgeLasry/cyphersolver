"""Apply key1761.tsv to the letter (transcription.txt); print line by line and coverage."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
key = {}
for line in open(os.path.join(HERE, 'key1761.tsv'), encoding='utf8'):
    if line[:1].isdigit():
        g, v, conf = line.split('\t')[:3]
        if v != '?':
            key[g] = (v, conf)
tok = known = 0
for line in open(os.path.join(HERE, 'transcription.txt'), encoding='utf8'):
    m = re.match(r'(l\d+):(.*)', line)
    if not m:
        if line.startswith('[img'):
            print(line.strip())
        continue
    s = m.group(2).replace('+', '')
    out = []
    for t in re.finditer(r'\{([^}]*)\}|(\d+)\??|([;.])', s):
        if t.group(1):
            out.append('{' + t.group(1)[:40] + ('…' if len(t.group(1)) > 40 else '') + '}')
        elif t.group(3):
            out.append(t.group(3))
        else:
            g = t.group(2); tok += 1
            if g in key:
                known += 1
                v, c = key[g]
                out.append(v.split(' ')[0] + ('?' if c == 'C' else ''))
            else:
                out.append('[' + g + ']')
    print(m.group(1), ' '.join(out))
print(f'\ncoverage: {known}/{tok} tokens = {known / tok:.1%}')
