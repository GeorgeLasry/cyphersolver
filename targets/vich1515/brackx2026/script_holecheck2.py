# holecheck2.py: compares, line by line, the marks of the reading (reading_original.md) and of the English
# (translation_en.md) in the #94 notation. Per line it counts: words carrying a tentative value ({?...}), doubtful words
# ([?word], [?], or a size label inside a word), words with a supplied letter or word ([x]), and the sizes of the
# free-standing unread runs ([?n groups, n signs, n letters]: groups, signs, letter runs). Both files must agree.
import re, sys
SIZE = re.compile(r'\[\?((?:\d+ (?:groups?|signs?|letters?)|sign)(?:, (?:\d+ (?:groups?|signs?|letters?)|sign))*)\]')


def lines(p):
    t = open(p).read(); a = t.index('```') + 3; b = t.index('```', a); out = {}
    for l in t[a:b].split('\n'):
        m = re.match(r'\s*(\d+)\s{2}(.*)', l)
        if m: out[int(m.group(1))] = m.group(2)
    return out


def marks(s):
    c = {'T': 0, 'D': 0, 'S': 0, 'groups': 0, 'signs': 0, 'letter runs': 0}
    # protect multi-word labels and brackets from the word split
    prot = re.sub(r'\[[^\]]*\]|\{[^}]*\}', lambda m: m.group(0).replace(' ', '\x01'), s)
    for w in prot.split():
        w = w.replace('\x01', ' ')
        core = w.strip(',.;:()')
        if not core: continue
        labels = SIZE.findall(core)
        rest = SIZE.sub('', core)
        if labels and not re.search(r'[^\W\d_]', re.sub(r'[\[\]{}?]', '', rest)) and not re.search(r'\[|\{', rest):
            for lab in labels:
                for part in lab.split(', '):
                    if part == 'sign': c['signs'] += 1
                    else:
                        n, kind = part.split(' ')
                        if kind.startswith('group'): c['groups'] += int(n)
                        elif kind.startswith('sign'): c['signs'] += int(n)
                        else: c['letter runs'] += 1
            continue
        if '{?' in core: c['T'] += 1
        elif '[?' in core: c['D'] += 1
        elif re.search(r'\[[^\]?]', core): c['S'] += 1
    return c


R = lines('reading_original.md'); E = lines('translation_en.md'); bad = 0
for n in sorted(R):
    a, b = marks(R[n]), marks(E.get(n, ''))
    if a != b:
        bad += 1
        print(f'{n:3d} es {a}\n    en {b}' if '-v' in sys.argv else f'{n} {a} {b}')
        if '-v' in sys.argv: print('    ES:', R[n], '\n    EN:', E.get(n, ''))
print('mismatched lines:', bad, 'of', len(R))
