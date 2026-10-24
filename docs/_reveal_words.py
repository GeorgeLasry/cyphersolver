"""Mark word starts in a "watch it decipher" file (docs/reveal/<slug>.json) from a spaced reading.

The reading is the passage's plaintext with spaces between words, exactly the letters of the tokens in order
(punctuation is ignored). Each token whose letters begin a word gets "w": 1; cipher-reveal.js then keeps a
word's tiles together and spaces the words.

Usage: python _reveal_words.py <slug> "spaced reading"     (or --file reading.txt)
       python _reveal_words.py --audit                    (which reveal files have no word starts yet)
"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).parent
SKIP = ' ,.;:'


def mark(slug, text):
    path = HERE / 'reveal' / f'{slug}.json'
    raw = path.read_text(encoding='utf-8'); d = json.loads(raw)
    lines = raw.strip().split('\n')
    indent = len(lines[1]) - len(lines[1].lstrip(' ')) if len(lines) > 1 else None   # keep the file's own layout
    pos, n, after_gap = 0, 0, True
    for i, t in enumerate(d['tokens']):
        p = str(t.get('p') or '')
        lead = len(text[pos:]) - len(text[pos:].lstrip(SKIP))
        t.pop('w', None)
        pos += lead
        if not p.strip():                       # a null or a word-divider sign: it holds no letters of the reading
            after_gap = after_gap or bool(lead) or p == ' '
            continue
        if after_gap or lead:
            t['w'] = 1; n += 1
        after_gap = False
        if text[pos:pos + len(p)] != p:
            sys.exit(f'{slug}: token {i} {p!r} does not match the reading at {text[pos:pos + 30]!r}')
        pos += len(p)
    if text[pos:].strip(SKIP):
        sys.exit(f'{slug}: reading has text left over: {text[pos:pos + 30]!r}')
    path.write_text(json.dumps(d, ensure_ascii=False, indent=indent) + '\n', encoding='utf-8')
    print(f'{slug}: {n} word starts marked')


def audit():
    for f in sorted((HERE / 'reveal').glob('*.json')):
        d = json.loads(f.read_text(encoding='utf-8'))
        if isinstance(d, dict) and 'tokens' in d and not any(t.get('w') for t in d['tokens']):
            print(f.stem)


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--audit']:
        audit()
    elif len(a) == 3 and a[1] == '--file':
        mark(a[0], pathlib.Path(a[2]).read_text(encoding='utf-8').strip())
    elif len(a) == 2:
        mark(a[0], a[1])
    else:
        sys.exit(__doc__)
