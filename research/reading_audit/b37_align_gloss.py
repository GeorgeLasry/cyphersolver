"""b37: check every unbracketed word of a reading against a gloss transcription ({figures = syl|syl|...} + clear text).
python b37_align_gloss.py <transcription.txt> <reading.md> [<key decode.txt>]
A reading word is carried if it is a clear word of the source, or a substring of the joined glosses+clear text of the
source (glossed words are syllables joined across groups). Lists the words carried by neither. Abbreviation expansions
are listed too (check by hand)."""
import sys, re, unicodedata
def norm(w):
    w = unicodedata.normalize('NFKD', w.lower()); w = ''.join(c for c in w if not unicodedata.combining(c))
    return re.sub(r'[^a-z]', '', w.replace('y', 'i').replace('j', 'i').replace('v', 'u').replace('w', 'u'))
src = open(sys.argv[1], encoding="utf8").read()
if len(sys.argv) > 3:   # a key decode with <...> runs (b37_vetesi_dec.py output): runs joined, nulls dropped
    src += '\n' + re.sub(r'<([^>]*)>', lambda m: ' ' + m.group(1).replace('·', '').replace('.', '') + ' ',
                         open(sys.argv[3], encoding='utf8').read())
src = '\n'.join(l for l in src.splitlines() if not l.startswith('#'))
src = re.sub(r'\{[\d.A-Z()?]+\s*=\s*([^}]*)\}', lambda m: ' ' + m.group(1).replace('|', '').replace('-', '').replace('(struck)', '') + ' ', src)
src = src.replace('-\n', '')
words = {norm(w) for w in src.split()}
joined = norm(src)
txt = open(sys.argv[2], encoding='utf8').read()
body = re.search(r'^## Reading[^\n]*\n(.*?)(?=^## |\Z)', txt, re.S | re.M).group(1)
miss = []
n = 0
for t in body.split():
    if '[' in t or ']' in t: continue
    w = norm(t)
    if not w: continue
    n += 1
    if w in words or w in joined: continue
    miss.append(t)
print('unbracketed reading words', n, 'not carried by the source:', len(miss))
print(' '.join(miss))
