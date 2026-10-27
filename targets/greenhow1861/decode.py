"""Greenhow letter on mourning paper, side 1 (catalogue 644, NARA naId 1634036, image 1).

Applies the 1864 Greenhow key (NARA M1091, naId 62017285, image 0484; key_1864.md) to the sign transcription in
transcription_side1.txt, where every sign is written as a neutral shape label (hk, b7, c3 ...), not as a letter.
Then runs three controls against an English word list (../../lang/lexicons/en.json.gz):
random substitution keys, the key shifted by one letter, and the true key with the signs shuffled inside each word.

    python decode.py          (output kept in decode_output.txt; seeded, standard library only)

Notation in the output: _ = paper loss, lower case = uncertain sign, (word) = written in clear.
"""
import collections
import gzip
import json
import math
import pathlib
import random

HERE = pathlib.Path(__file__).resolve().parent
KEY = {                 # shape label : letter, from the key column of M1091 image 0484
    'hk': 'A',          # + with a small x (in her hand a cross with a hook, "7+")
    'b7': 'B', 'c3': 'C',
    'cx': 'D',          # + with a small x lower right
    'yf': 'E',          # Y
    'tr': 'F',          # triangle
    'e8': 'G',          # plain 8
    'cm': 'H',          # comb
    'f4': 'I',          # crossed 4 / A
    'o0': 'J', 'n9': 'K',
    'ls': 'L',          # long s
    'dd': 'M',          # diamond with a dot
    'qm': 'N',          # ?-form
    'lb': 'N',          # looped l with a crossbar: NOT on the key sheet, value inferred from context
    'f5': 'O', 'cc': 'P', 'q1': 'Q',
    'ph': 'R',          # looped 4 / phi
    'bx': 'S',          # box with X
    'dt': 'T',          # D with a dot
    'e8s': 'U',         # struck 8 ($)
    'zt': 'V', 'fl': 'W', 'ta': 'X', 'ys': 'Y', 'rr': 'Z'}


def load_lines():
    """The sign lines of transcription_side1.txt: lines that start with a two-digit line number."""
    out = []
    for ln in (HERE / 'transcription_side1.txt').read_text(encoding='utf-8').splitlines():
        if ln[:2].isdigit() and ln[2:3] == ' ':
            out.append(ln[3:])
    return out


def parse(lines):
    """Words: lists of sign labels; '|' = word gap, '~' = paper loss, '=x' = word in clear, '+' = word runs on."""
    toks = []
    for ln in lines:
        cont = ln.rstrip().endswith('+')
        toks += ln.replace('+', '').split()
        if not cont:
            toks.append('|')
    words, cur = [], []
    for t in toks:
        if t == '|':
            if cur: words.append(cur); cur = []
        elif t.startswith('='):
            if cur: words.append(cur); cur = []
            words.append(['CLEAR:' + t[1:]])
        else:
            cur.append(t)
    if cur: words.append(cur)
    return words


def dec(word, key):
    if word[0].startswith('CLEAR:'):
        return '(' + word[0][6:] + ')'
    out = ''
    for s in word:
        if s == '~': out += '_'; continue
        q = s.endswith('?'); s = s.rstrip('?')
        out += key[s].lower() if q else key[s]
    return out


def norm(w): return w.lower().replace('v', 'u').replace('j', 'i')


LEX = json.load(gzip.open(HERE.parent.parent / 'lang' / 'lexicons' / 'en.json.gz', 'rt', encoding='utf-8'))
WORDS_KNOWN = set(LEX)
BG, UNI = collections.Counter(), collections.Counter()
for w, c in LEX.items():
    w = '^' + w + '$'
    for a, b in zip(w, w[1:]):
        BG[a + b] += c; UNI[a] += c


def bigram(s):
    tot = n = 0
    for seg in s.lower().split('_'):
        if not seg: continue
        seg = '^' + norm(seg) + '$'
        for a, b in zip(seg, seg[1:]):
            tot += math.log((BG[a + b] + 0.5) / (UNI[a] + 0.5 * 28)); n += 1
    return tot, n


def evaluate(key, words):
    txt = [dec(w, key) for w in words]
    cw = [t for t in txt if not t.startswith('(')]
    full = [t for t in cw if '_' not in t]
    hits = sum(norm(t) in WORDS_KNOWN for t in full)
    tot = n = 0
    for t in cw:
        a, b = bigram(t); tot += a; n += b
    return txt, hits, len(full), tot / n


def main():
    random.seed(644)
    words = parse(load_lines())
    txt, h, nf, bs = evaluate(KEY, words)
    print('DECODE, side 1, true key:')
    print(' '.join(txt))
    print(f'whole cipher words in the English word list: {h}/{nf}; mean bigram log-likelihood {bs:.3f}')
    glyphs = sorted(set(KEY) - {'lb'})
    letters = [KEY[g] for g in glyphs]

    def permkey():
        L = letters[:]; random.shuffle(L); k = dict(zip(glyphs, L)); k['lb'] = k['qm']; return k
    R = [evaluate(permkey(), words) for _ in range(2000)]
    hs = [r[1] for r in R]; bss = [r[3] for r in R]
    mu = sum(bss) / len(bss); sd = (sum((x - mu) ** 2 for x in bss) / len(bss)) ** .5
    print(f'CONTROL random substitution keys (n=2000): words mean {sum(hs) / len(hs):.2f} max {max(hs)}; '
          f'bigram mean {mu:.3f} sd {sd:.3f} max {max(bss):.3f}; true key z = {(bs - mu) / sd:.1f}')
    print('  example:', ' '.join(R[0][0])[:160])
    sk = {g: chr((ord(v) - 65 + 1) % 26 + 65) for g, v in KEY.items()}
    t2, h2, _, b2 = evaluate(sk, words)
    print(f'CONTROL key shifted +1: words {h2}/{nf}, bigram {b2:.3f}:', ' '.join(t2)[:160])
    SH = []
    for _ in range(500):
        ws = []
        for w in words:
            w = w[:]
            if not w[0].startswith('CLEAR:'): random.shuffle(w)
            ws.append(w)
        SH.append(evaluate(KEY, ws))
    print(f'CONTROL true key, signs shuffled inside each word (n=500): words mean {sum(r[1] for r in SH) / 500:.2f} '
          f'max {max(r[1] for r in SH)}; bigram mean {sum(r[3] for r in SH) / 500:.3f} max {max(r[3] for r in SH):.3f}')


if __name__ == '__main__':
    main()
