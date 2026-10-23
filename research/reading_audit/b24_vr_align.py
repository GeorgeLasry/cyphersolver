"""b24 (vanreede1787): word check of a reading against its decode, and the look-alike count.
Each reading word (cipher part only: the clear passages, read from the image, are listed apart) is looked for in the
stream of decoded key words (nulls dropped, accents/apostrophes/spaces removed); a word not found is printed for a
manual look (bar-inflected forms show here). Look-alike count: letters of the decoded key words whose group carried a
DECODE 'J+' (hooked 1) or a label corrected on the image.
    python b24_vr_align.py R1026|R1027"""
import re, sys, pathlib, unicodedata
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from b24_vr_decode import groups, word
from b24_vr_key import load, is_null
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'vanreede1787'
def nz(s):
    s = unicodedata.normalize('NFD', s); s = ''.join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z]", '', s)
rec = sys.argv[1]
k, _ = load()
rows = [l.split('\t') for l in (T / f'{rec}_transcription_corrected.tsv').read_text(encoding='utf8').splitlines() if l and not l.startswith('#')]
orig = [it for it in groups(rec) if it[0] == 'g']
stream, look = '', 0
corr = {l.split('\t')[1] for l in (T / f'{rec}_corrections.tsv').read_text(encoding='utf8').splitlines()[2:]}
corrg = set(' '.join(corr).split())
jcount = sum(1 for it in orig if 'J' in it[3])
jgroups = [it[1] for it in orig if 'J' in it[3]]
for r in rows:
    if r[0] == 'C': continue
    g = r[1]; w = word(k, g)
    if w == '·' or w.startswith('['): continue
    stream += nz(w)
# look-alike letters: words of groups with J+ or a corrected label
from collections import Counter
jc = Counter(jgroups)
for r in rows:
    if r[0] == 'C': continue
    g = r[1]; w = word(k, g)
    if w == '·': continue
    if jc[g] > 0: jc[g] -= 1; look += len(nz(w))
    elif g in corrg: look += len(nz(w))
t = (T / f'{rec}_reading.md').read_text(encoding='utf8')
body = re.search(r'^## Reading[^\n]*\n(.*?)(?=^## |\Z)', t, re.S | re.M).group(1)
paras = [p for p in body.split('\n\n') if p.strip()]
miss, tot, letters = [], 0, 0
for p in paras:
    for w in re.findall(r"\[[^\]]*\]|[A-Za-zÀ-ÿ']+", p):
        if w.startswith('['): continue
        for part in re.split(r"'", w):
            n = nz(part)
            if not n: continue
            tot += 1; letters += len(n)
            if n not in stream: miss.append(part)
print(rec, 'reading words', tot, 'letters', letters, 'not in the decode stream:', len(miss))
print(' ', miss)
print('look-alike letters (J+ groups %d, corrected labels %s): %d of %d decoded letters' % (jcount, sorted(corrg), look, len(stream)))
