"""Write docs/reveal/fiesque1567.json: the first four cipher lines of view 22 right (15 Nov 1567), decoded sign by
sign with the contributed key (contributed/data/key.tsv). Inferred values are marked 'unc', word codes 'code',
nulls 'null'. Run: PYTHONUTF8=1 python targets/fiesque1567/make_reveal.py
"""
import os, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
key, src = {}, {}
for ln in open(os.path.join(HERE, 'contributed', 'data', 'key.tsv'), encoding='utf-8'):
    if ln.startswith('#') or not ln.strip(): continue
    p = ln.rstrip('\n').split('\t'); key[p[0]], src[p[0]] = p[1], p[2]
lines = []
for ln in open(os.path.join(HERE, 'contributed', 'data', 'transcription_v022r.txt'), encoding='utf-8'):
    m = re.match(r'(c\d+):\s*(.*)', ln)
    if m: lines.append(m.group(2).split())
toks = []
for i, line in enumerate(lines[:4]):
    if i: toks.append({'g': '', 'p': ' / ', 'cls': 'plain'})
    for t in line:
        t0 = t[:-1] if t.endswith('?') and len(t) > 1 else t
        v = key.get(t0)
        if v is None or v == '?': toks.append({'g': t, 'p': '?', 'cls': 'unk'}); continue
        if v == '(null)': toks.append({'g': t, 'p': '', 'cls': 'null'}); continue
        cls = 'code' if (t0.startswith('=') and len(v) > 2) else ('unc' if src[t0] == 'inferred' or t.endswith('?') else '')
        toks.append({'g': t0, 'p': v.split('/')[0], 'cls': cls})
# mark as 'unc' every sign whose letters are not matched in the contemporary decipherment (calib_v023r.txt)
import difflib
ref = ' '.join(l for l in open(os.path.join(HERE, 'calib_v023r.txt'), encoding='utf-8') if not l.startswith('#'))
ref = re.sub(r'[^a-z]', '', ref.lower())
own, owner = '', []
for i, t in enumerate(toks):
    if t['g'] and t['cls'] not in ('null', 'unk'):
        s = re.sub(r'[^a-z]', '', t['p'].lower()); own += s; owner += [i] * len(s)
ok = [False] * len(own)
for b in difflib.SequenceMatcher(None, own, ref[:len(own) + 40], autojunk=False).get_matching_blocks():
    for k in range(b.a, b.a + b.size): ok[k] = True
bad = {owner[k] for k in range(len(own)) if not ok[k]}
for i in bad:
    if toks[i]['cls'] in ('', 'code'): toks[i]['cls'] = 'unc'
print(len(bad), 'signs disagree with the contemporary decipherment')
out = {
    'slug': 'fiesque1567',
    'anchor': 'calib',
    'title': 'Vienna, 15 November 1567: the opening of the cipher to the Queen Mother',
    'caption': ("The first four cipher lines of Fiesque's letter of 15 November 1567, BnF fr. 15919 f. 18r (Gallica view 22 "
                "right), in Harumi-Matsuba's sign names, decoded with Tomokiyo's table. The decipherment of the time on the "
                "facing page reads: Madame, j'ay puis le partement de monsr de Lignerolles qui fut le cinquiesme de ce moys "
                "et lequel alla passer devers le duc de Saxe, il n'est survenu autre chose sinon que le bruict couroit en "
                "ceste ville qu'il se levoit beaucoup de gens..."),
    'unit': 'signs',
    'key_note': "Sign names and inferred values are the contributor's (contributed/data/key.tsv); 'unc' marks a value inferred from context, not in Tomokiyo's table.",
    'tokens': toks,
}
json.dump(out, open(os.path.join(HERE, '..', '..', 'docs', 'reveal', 'fiesque1567.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(sum(1 for t in toks if t['g']), 'signs')
print(''.join(t['p'] for t in toks))
