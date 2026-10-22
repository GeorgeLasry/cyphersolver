# Calibration: compare a blind decode (key applied to a transcription made without the margin)
# with the contemporary margin decipherment, letter by letter.
# Letters only, lower case, j->i, v->u, accents dropped; code/plain groups {..} and [..] removed from the decode.
# Usage: python3 calib.py <decoded tsv from vk.py decode> <margin txt>
import sys, re, difflib, unicodedata
def norm(s):
    s = unicodedata.normalize('NFD', s); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = s.lower().replace('j', 'i').replace('v', 'u')
    return re.sub('[^a-z]', '', s)
dec = ''.join(re.sub(r'\{[^}]*\}|<[^>]*>|·', '', l.split('\t', 1)[1]) for l in open(sys.argv[1]) if '\t' in l)
dec = re.sub(r'\[([a-z]+)\]', r'\1', dec)          # double letters [ss] -> ss ; nomenclature kept as words
dec = norm(dec)
mar_words = [w for l in open(sys.argv[2]) if not l.startswith('#') for w in l.split()]
mar_clear = norm(' '.join(w for w in mar_words if '?' not in w))
mar_all = norm(' '.join(w.replace('?', '') for w in mar_words))
sm = difflib.SequenceMatcher(None, dec, mar_all, autojunk=False)
blocks = [b for b in sm.get_matching_blocks() if b.size >= 4]   # count only runs of >=4 letters (avoid chance matches)
m = sum(b.size for b in blocks)
a0 = min(b.a for b in blocks); a1 = max(b.a + b.size for b in blocks)
print(f'decode letters {len(dec)}, margin letters {len(mar_all)} (words without ?: {len(mar_clear)} letters)')
print(f'matched in runs>=4: {m} = {m/len(mar_all):.1%} of margin letters; decode span covered by margin: {a0}-{a1} ({a1-a0} letters), match {m/(a1-a0):.1%} of that span')

# letter accuracy where both sides have text: equal / (equal + short replaces/indels <=3).
# Long inserts/deletes (>=4) are treated as code-word positions or text outside the margin's span and are not scored.
def accuracy(D, M):
    sm = difflib.SequenceMatcher(None, D, M, autojunk=False)
    eq = err = skipped = 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            eq += i2 - i1
        elif max(i2 - i1, j2 - j1) <= 3:
            err += max(i2 - i1, j2 - j1)
        else:
            skipped += max(i2 - i1, j2 - j1)
    return eq, err, skipped
for label, D, M in [('as is', dec, mar_all), ('d=l merged', dec.replace('l', 'd'), mar_all.replace('l', 'd'))]:
    eq, err, sk = accuracy(D, M)
    print(f'{label}: scored letters {eq + err}, agree {eq} ({eq / (eq + err):.1%}), short disagreements {err}, not scored (long gaps) {sk}')
