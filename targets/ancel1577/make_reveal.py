"""Build docs/reveal/ancel1577.json: p. 525 lines 9-11 decoded sign by sign with the contributor's key
(TOKENS in contributed/src/vk.py, read with ast). PYTHONUTF8=1 python targets/ancel1577/make_reveal.py"""
import ast, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.join(HERE, 'contributed')
src = open(os.path.join(C, 'src', 'vk.py'), encoding='utf-8').read()
KEY = next({k: v for k, (v, s) in ast.literal_eval(n.value).items()} for n in ast.parse(src).body
           if isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') == 'TOKENS')
# display shapes for the contributor's sign names (their PROMPT/OPEN descriptions); others shown by name
SHAPE = {'w': 'ω', 'pi': 'π', 'dl': 'δ', 'i': '∂', 'mu': 'μ', 'b': 'β', 'D': '△', 'ne': '≠', 'oc': '+', 'P': '⊣',
         'p': 'p', 'x': 'x', 'S': '(y', 'h': '//', 'th': 'θ', 'qa': 'ɑ', 'm': 'm', 'o': 'o', 'plus': 'plus',
         'di': 'δ̄', 'n': '∩', 'g': 'ℓ', '3': '3', '4': '4', '7': '7', '8': '8', '9': '9', '2': '2', 'q': 'q'}
LINES = ['525.09', '525.10', '525.11']
GLOSS = {'saturnus': "l'Empereur"}
toks = []
for ln in open(os.path.join(C, 'transcription', 'p525.txt'), encoding='utf-8'):
    if ln.startswith('#') or '\t' not in ln: continue
    lid, _, t = ln.rstrip('\n').partition('\t')
    if lid not in LINES: continue
    if toks: toks.append({'g': '', 'p': ' / ', 'cls': 'plain'})
    for tok in t.split():
        if tok == '|': continue
        if tok.startswith('{'):
            w = tok.strip('{}?')
            toks.append({'g': w, 'p': GLOSS.get(w, '?'), 'cls': 'code'}); continue
        unsure = tok.endswith('?') and len(tok) > 1
        b = tok[:-1] if unsure else tok
        if b == '?' or b not in KEY:
            toks.append({'g': '·', 'p': '?', 'cls': 'unk'}); continue
        v = KEY[b]
        cls = 'unc' if unsure else ('code' if len(v) > 2 else '')
        toks.append({'g': SHAPE.get(b, b), 'p': v, 'cls': cls})
out = {'slug': 'ancel1577', 'anchor': 'the-reading',
       'title': 'Vienna, 22 October 1577: Archduke Matthias could not leave his room',
       'caption': "Three lines of Guillaume Ancel's cipher, BnF Cinq Cents de Colbert 398 p. 525 lines 9-11 "
                  "(Gallica view 559), decoded sign by sign from Harumi-Matsuba's transcription with Tomokiyo's key.",
       'unit': 'signs',
       'key_note': "Homophonic symbol cipher (Tomokiyo's Vulcob-Ancel table, 1575-1584): two to four signs per letter, "
                   "signs for double letters, and code words in plain letters (saturnus = the Emperor). Sign shapes "
                   "are approximate; uncertain signs (marked ? in the transcription) are shown as uncertain.",
       'tokens': toks}
dst = os.path.join(HERE, '..', '..', 'docs', 'reveal', 'ancel1577.json')
open(dst, 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1) + '\n')
print(len([t for t in toks if t.get('cls') != 'plain']), 'tokens;', ''.join(t['p'] for t in toks))
