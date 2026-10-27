"""Decode transcription.txt with key.tsv; --reveal writes docs/reveal/livingston1781.json.
usage: python tools/decode.py [--reveal <repo root>]"""
import json, os, sys
here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
key = {}
for line in open(os.path.join(here, 'key.tsv'), encoding='utf-8'):
    if line.startswith('#') or not line.strip():
        continue
    g, v, _ = line.rstrip('\n').split('\t')
    key[g] = v
lines = [l.split() for l in open(os.path.join(here, 'transcription.txt'), encoding='utf-8')
         if l.strip() and not l.startswith('#')]
tokens = []
for i, groups in enumerate(lines):
    vals = [key.get(g, '?') for g in groups]
    print(' '.join(groups), '=', ''.join(v.rstrip('?') for v in vals))
    for j, (g, v) in enumerate(zip(groups, vals)):
        t = {'g': g, 'p': v.rstrip('?')}
        if v == '?':
            t['cls'], t['p'] = 'unk', '?'
        elif v.endswith('?'):
            t['cls'] = 'unc'
        if i == 0 and j < 2 or j == len(groups) - 1:
            t['w'] = 1
        tokens.append(t)
    if i >= 1:
        tokens.append({'g': '', 'p': '%d' % (599 + i), 'cls': 'plain', 'w': 1})
if '--reveal' in sys.argv:
    root = sys.argv[sys.argv.index('--reveal') + 1]
    out = {'slug': 'livingston1781', 'anchor': 'reading',
           'title': 'The addition, 28 November 1781',
           'caption': 'The last line of the sent original: "Make this addition to your cypher", then six pairs of groups, each spelling a syllable, with the new group number after it.',
           'unit': 'code groups',
           'key_note': 'Values from the glosses in Livingston\'s draft and the entries on Jay\'s copy of the Thomson code; the division of 23.473.370 (cypher) into syllables is not settled.',
           'tokens': tokens}
    with open(os.path.join(root, 'docs', 'reveal', 'livingston1781.json'), 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
        f.write('\n')
