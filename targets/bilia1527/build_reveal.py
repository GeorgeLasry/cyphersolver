"""Write docs/reveal/bilia1527.json: lines 1-6 of f. 102r decoded sign by sign with our R5258 key (decode_check.py).

Signs our key has no value for take the contributor's inferred value and are marked 'unc'; the crossed x takes s,
the value in the s column of the R5258 sheet (checked on the sheet image 21 Oct 2026), where our Gilino key had it
as a null. Run from the repository root: PYTHONUTF8=1 python targets/bilia1527/build_reveal.py
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import decode_check as dc

TK = dc.theirs_key()
toks = []
for lab, ts in dc.lines('f102r'):
    if lab > '102r.06': break
    for t in ts:
        o = dc.ours(t); v = dc.K.get(o)
        cls = ''
        if t == 'x': v = 's'
        elif t == 'o': cls = 'unc'   # our Gilino key: z; the contributor: o
        elif v is None:
            v = TK.get(t.rstrip('?'))
            cls = 'unc'
            if t.startswith('B.58'): v, cls = '?', 'code'
        if v == '': cls = 'null'; v = ''
        if t.endswith('?') and cls == '': cls = 'unc'
        toks.append({'g': t.rstrip('?'), 'p': v if v is not None else '?', **({'cls': cls} if cls else {})})
    toks.append({'g': '', 'p': ' | ', 'cls': 'plain'})
toks.pop()
out = {
    'slug': 'bilia1527',
    'anchor': 'f102r',
    'title': 'Burgos, 22 November 1527: the opening of Bilia\'s letter',
    'caption': 'Lines 1-6 of BnF fr. 3013 no. 43 f. 102r, transcribed by Harumi-Matsuba (AI transcription, issue #55) and decoded here with the Sforza key DECODE R5258. | marks a line end.',
    'unit': 'signs',
    'key_note': 'Barred letters with two-digit numbers are syllables in ordered rows (B.31-50 ba..gu, o.51-65 la..nu, G.56-80 pa..tu, o.33-47 va..zu); bare numbers and signs are letters; B.58 is an unread name code. Grey (uncertain) values are the contributor\'s, inferred from this letter, not on the key sheet.',
    'tokens': toks,
}
p = os.path.join(HERE, '..', '..', 'docs', 'reveal', 'bilia1527.json')
open(p, 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1) + '\n')
print(len([t for t in toks if t['g']]), 'signs;', ''.join(t['p'] for t in toks))
