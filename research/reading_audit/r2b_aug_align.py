"""r2b: align augurelio1535 pass2/reading.txt word by word with decrypt_v7.txt, line by line (difflib on letters).
Lists unbracketed reading words whose letters the decode carries for less than half (candidates for supplied words)."""
import re, difflib, pathlib
D = pathlib.Path(__file__).resolve().parents[2] / 'targets/augurelio1535/pass2'
def lines(f):
    return {l[:5]: l[6:] for l in (D / f).read_text(encoding='utf8').splitlines() if re.match(r'P\d\.\d\d ', l)}
R, C = lines('reading.txt'), lines('decrypt_v7.txt')
nw = low = 0
for k, r in R.items():
    c = re.sub(r'\[[^\]]*\]|\|[^|]*\||[^a-z]', '', C.get(k, '').lower())
    words = re.sub(r'\|[^|]*\|', ' ', r).split()
    # letters of reading with word index; bracketed letters excluded
    seq, idx = [], []
    for i, w in enumerate(words):
        if re.search(r'[{}]', w): continue
        bare = re.sub(r'\[[^\]]*\]', '', w).lower()
        for ch in re.sub(r'[^a-z]', '', bare.replace('v', 'u').replace('j', 'i')):
            seq.append(ch); idx.append(i)
    sm = difflib.SequenceMatcher(None, ''.join(seq), c.replace('v', 'u').replace('j','i'), autojunk=False)
    hit = [0] * len(seq)
    for a, b, n in sm.get_matching_blocks():
        for j in range(n): hit[a + j] = 1
    tot = {}
    for h, i in zip(hit, idx): tot.setdefault(i, [0, 0]); tot[i][0] += h; tot[i][1] += 1
    for i, (h, n) in tot.items():
        nw += 1
        if h / n < 0.5:
            low += 1; print(k, words[i], f'{h}/{n}', '|', c)
print('words', nw, 'low', low)
