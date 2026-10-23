"""b37: word-by-word alignment of a reading with its source transcription.
python b37_align.py <transcription.txt> <reading.md>
Source tokens: clear words, {value} of a decoded group, bare code numbers. Reading tokens: words of the ## Reading body.
Lists every unbracketed reading word that the source does not carry at that place (difflib alignment)."""
import sys, re, difflib, unicodedata
def norm(w):
    w = unicodedata.normalize('NFKD', w.lower()); w = ''.join(c for c in w if not unicodedata.combining(c))
    return w.replace('v', 'u').replace('j', 'i').replace('y', 'i').strip('.,;:()/!?=')
src = []
for line in open(sys.argv[1], encoding='utf8'):
    if line.startswith('#') or not line.strip(): continue
    line = re.sub(r'\b(\d+(?:\.\d+)*)\.?\{([^}]*)\}', lambda m: ' ' + m.group(2) + ' ', line)
    line = line.replace('=\n', '').replace('(?)', '')
    for t in line.split():
        n = norm(t)
        if n: src += n.split()
# rejoin hyphenated line breaks
txt = open(sys.argv[2], encoding='utf8').read()
body = re.search(r'^## Reading[^\n]*\n(.*?)(?=^## |\Z)', txt, re.S | re.M).group(1)
rd = []
for t in body.split():
    br = t.startswith('[') or ']' in t
    rd.append((t, norm(re.sub(r'[\[\]?]', '', t)), br))
# source with letters joined: spelled runs give one token per letter group already
sm = difflib.SequenceMatcher(None, src, [r[1] for r in rd], autojunk=False)
unc = []
for op, a1, a2, b1, b2 in sm.get_opcodes():
    if op in ('replace', 'insert'):
        for r in rd[b1:b2]:
            if not r[2]: unc.append((r[0], ' '.join(src[a1:a2])))
print('reading words', len(rd), 'unbracketed words not matched to the source:', len(unc))
for w, s in unc: print('  ', w, '<-', s)
