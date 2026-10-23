"""b15: join a line-by-line reading (<doc>_reading_lines.txt) into running text, and count holes per sentence over
all words (clear words in braces count as read words), with the _check_reading.py rule (a sentence is clean when at most
one word in ten is a hole, one hole allowed up to 19 words). Brackets [?w] [...] [w] count as holes.

    python research/reading_audit/b15_body.py <reading_lines.txt> [--out body.txt]
"""
import re, sys


def join(path):
    L = [l.rstrip('\n') for l in open(path, encoding='utf-8') if l.strip() and not l.startswith('#')]
    s = ''
    for l in L:
        s = s[:-1] if s.endswith('-') else (s + ' ' if s else s)
        s += l
    return s


def holes(text):
    t = re.sub(r'\{([^}]*)\}', r' \1 ', text)   # clear words count as words, never as holes
    sents = [x.split() for x in re.split(r'[.;:]\s', t) if len(x.split()) >= 3]
    out = []
    for w in sents:
        h = sum('[' in x for x in w)
        out.append((h, len(w), h <= max(1, len(w) // 10)))
    return out


if __name__ == '__main__':
    s = join(sys.argv[1])
    if '--out' in sys.argv:
        open(sys.argv[sys.argv.index('--out') + 1], 'w', encoding='utf-8').write(re.sub(r'\{([^}]*)\}', r'*\1*', s))
    r = holes(s)
    print(f'sentences {len(r)}, clean {sum(c for *_, c in r)}, share {sum(c for *_, c in r) / max(1, len(r)):.2f}, '
          f'words {sum(n for _, n, _ in r)}, holes {sum(h for h, *_ in r)}')
    for h, n, c in r:
        if not c: print('  not clean:', h, 'of', n)
