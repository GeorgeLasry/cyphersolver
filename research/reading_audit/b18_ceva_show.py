"""b18 (ceva1632): print a letter's token stream line by line as words, codes shown as value or <code>.

    python research/reading_audit/b18_ceva_show.py r75|r84 [tokens-file]
"""
import json, sys, pathlib
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'ceva1632'
sys.path.insert(0, str(T))
import cipher
doc = sys.argv[1]
toks = json.load(open(T / (sys.argv[2] if len(sys.argv) > 2 else f'{doc}.tokens2.json')))
for i, line in enumerate(toks, 1):
    words, cur = [], []
    for t in line:
        if t == '6':
            words.append(''.join(cur)); cur = []; continue
        if t.startswith('#'):
            c = t[1:]; v = cipher.NOMEN.get(c)
            cur.append(f'[{v.upper()}:{c}]' if v else f'<{c}>')
        elif t.startswith('?'):
            cur.append('{' + t[1:] + '}')
        elif cipher.is_null(t):
            cur.append('·')
        else:
            cur.append(cipher.units(t) or '{%s}' % t)
    words.append(''.join(cur))
    print(f'{i:2d}', ' '.join(words))
