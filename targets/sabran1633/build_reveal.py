"""Build docs/reveal/sabran1633.json: f. 66r (c139_20 .. c139_25b) decoded sign by sign with Lasry's key
(contributed/data/key.tsv) from the contributed transcription. Signs found wrong on the image here (spotcheck.md)
are marked 'unc'. Run: PYTHONUTF8=1 python targets/sabran1633/build_reveal.py"""
import os, json
H = os.path.dirname(os.path.abspath(__file__)); C = os.path.join(H, 'contributed', 'data')
key = {}
for l in open(os.path.join(C, 'key.tsv'), encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    f = l.rstrip('\n').split('\t'); key[f[0]] = (f[1], f[2])
rows = []
for l in open(os.path.join(C, 'transcription.tsv'), encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    i, s = l.rstrip('\n').split('\t', 1); rows.append((i, s.split()))
LINES = ['c139_20', 'c139_21a', 'c139_21b', 'c139_22', 'c139_23', 'c139_23b', 'c139_23c', 'c139_24a', 'c139_24b',
         'c139_25a', 'c139_25b']
UNC = {('c139_23b', 0), ('c139_23b', 1), ('c139_23c', 3)}
toks = []; prev = ''
for i, ts in rows:
    if i not in LINES: continue
    for j, t in enumerate(ts):
        if t == '|' or t.startswith('['): continue
        t0 = t.rstrip('?') if t != '?' else t
        v = key.get(t0)
        if v is None:
            toks.append({'g': t0, 'p': '?', 'cls': 'unk'}); prev = ''; continue
        val, kind = v
        if kind == 'double': p, cls = prev, ''
        elif kind == 'word': p, cls, prev = val, 'code', ''
        else: p, cls, prev = val, '', val
        if (i, j) in UNC or (t.endswith('?') and t != '?'): cls = 'unc'
        if (i, j) == ('c139_23c', 3): p = 'r'      # the image shows z (= r), not lh (= e)
        toks.append({'g': t0, 'p': p, 'cls': cls})
out = {'slug': 'sabran1633', 'anchor': 'reading',
       'title': 'Genoa, 23 September 1633: the Savona plot, f. 66r',
       'caption': "Eleven cipher runs of Sabran's letter of 23 September 1633 (BnF fr. 4134 f. 66r), as transcribed "
                  "by Harumi-Matsuba's AI pipeline and decoded with George Lasry's key. Marked uncertain: two signs "
                  "counted twice in the transcription and one AI correction that the image does not support (shown "
                  "here with the sign on the image).",
       'unit': 'signs',
       'key_note': "George Lasry's key 'BNF Francais 4134' (2022), sign names from the contributed key.tsv; 3i and 35 "
                   "are name codes not in the key.",
       'tokens': toks}
with open(os.path.join(H, '..', '..', 'docs', 'reveal', 'sabran1633.json'), 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1); f.write('\n')
print(len(toks), ''.join(t['p'] if t['cls'] != 'code' else '(' + t['p'] + ')' for t in toks))
