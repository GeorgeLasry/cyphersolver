"""Dana to Livingston, St Petersburg, 6 Apr 1783 (O.S.), No. 23: decryption and controls.

    python decrypt.py              line-by-line decryption against transcription.txt
    python decrypt.py --controls   the controls quoted in NOTES.md (about 20 s)

System: periodic numerical table of the Lovell type. Alphabet a..z plus & (27 signs). A letter p (a=0 ... &=26)
under key letter K is written (p - K) mod 27 + 1, so that the key letter itself is 1 (Lovell's convention).
Key word WIN, period 3. Numbers above 27 (29, 31, 137, 168) are code groups whose meaning is unknown.

The working text below is the transcription with every intervention written into it, so that each one can be
seen and checked. The script verifies that, with the annotations removed, it gives back transcription.txt.
  29c      code group; the key continues with the next letter
  31c+2    code group; the next letter takes the key two places on (equivalently, one place back)
  23@N     enciphered with key letter N instead of the one due (Dana's slip); the due key position is used up
  ^        a key position Dana skipped
  1>11     token cut at the frame edge, first digit visible, completed as 11
  +20      token not visible (lost at the edge or left out), supplied as 20
Python standard library only; paths are relative to this file.
"""
import gzip, json, math, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ALPHA = 'abcdefghijklmnopqrstuvwxyz&'
KEY = 'win'

WORK = [
    '29c 19 20 1 31c+2 26 14 3 19 25 27 23 24 15 22 14 22 22 23@N 1>11',
    '1 20 12 21 26 1 18 10 23 16 3 20 1 12@N 11 19 25 12 26 10 23 3 23 1 1 8 1 3 17 24 6 +20',
    '10 6 3 11 7 10 5 12 20 13 17 6 6 16 10 22 19 23 12 15 14 6 2 11 6 2 18 24 1>15',
    '24 13 5 10 15 22 6 12 7 13 24 137c 15 9 7 3 25 1 1 25 27 23 24 27 2 26 10 2>27',
    '6 17 16 10 7 3 21 7 6 10 23 16 3 20 1 14 10 5 10 11 23 24 12 15 7 ^ 26 10 1 1 +11',
    '4 8 24@I 6 17 10 1 1 25 27 19 19 24 11 25 1 1 24 27 2 23 12 3 23 7 3 10 10 2>26',
    '3 11 3 10 20 25 14 6 21 25 27 19 23 24 23 24 6 2 168c+2 22 10 10 19 13 24 +1',
    '8 24 27 3 8 5 10 11 19 19 12 18 14 25 20 14 22 8 17 12 12',
]


def dec(n, k):
    """plaintext letter of number n under key letter k"""
    return ALPHA[(n - 1 + ALPHA.index(k)) % 27]


def transcription():
    rows = []
    for line in open(os.path.join(HERE, 'transcription.txt'), encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        rows.append([t.rstrip('.') for t in line.split()])
    return rows


def visible(work_line):
    """the working line with the annotations removed: what the scan shows"""
    out = []
    for t in work_line.split():
        if t == '^' or t.startswith('+'):
            continue
        if '>' in t:
            out.append(t.split('>')[0] + '|')
        else:
            out.append(t.split('c')[0].split('@')[0])
    return out


def decrypt(KEY=KEY):
    pos = 0                      # key position, runs on across lines
    lines, notes = [], []
    for i, wl in enumerate(WORK, 1):
        out = []
        for t in wl.split():
            if t == '^':
                pos += 1; notes.append(f'L{i}: key position skipped'); continue
            if 'c' in t:
                n, _, step = t.partition('c')
                out.append(f'[{n}]')
                pos += int(step) if step else 0
                continue
            if '@' in t:
                n, k = t.split('@')
                due = dec(int(n), KEY[pos % 3])
                out.append(dec(int(n), k.lower()))
                notes.append(f'L{i}: {n} enciphered with {k} (due key letter {KEY[pos % 3].upper()} would give {due!r})')
                pos += 1; continue
            if t.startswith('+'):
                ch = dec(int(t[1:]), KEY[pos % 3])
                out.append('(' + ch + ')')
                notes.append(f'L{i}: token {t[1:]} supplied at the line end = {ch!r}')
                pos += 1; continue
            if '>' in t:
                a, b = t.split('>')
                ch = dec(int(b), KEY[pos % 3])
                out.append('(' + ch + ')')
                notes.append(f'L{i}: cut token {a}| completed as {b} = {ch!r}')
                pos += 1; continue
            out.append(dec(int(t), KEY[pos % 3]))
            pos += 1
        lines.append(''.join(out))
    return lines, notes


def plain_stream(raw):
    """letters only, for scoring"""
    return ''.join(c for c in raw if c in ALPHA[:26])


def bigram_model():
    """letter-bigram log-probabilities from the repository's English word list (lang/lexicons/en.json.gz)"""
    lex = json.load(gzip.open(os.path.join(HERE, '..', '..', 'lang', 'lexicons', 'en.json.gz'), 'rt', encoding='utf-8'))
    big = {}
    for w, c in lex.items():
        w = ''.join(ch for ch in w if ch in ALPHA[:26])
        for a, b in zip(w, w[1:]):
            big[a + b] = big.get(a + b, 0) + c
    tot = {}
    for ab, c in big.items():
        tot[ab[0]] = tot.get(ab[0], 0) + c
    return {a + b: math.log((big.get(a + b, 0) + 0.5) / (tot.get(a, 0) + 13.5)) for a in ALPHA[:26] for b in ALPHA[:26]}


def score(s, lp):
    s = plain_stream(s)
    return sum(lp[s[i:i + 2]] for i in range(len(s) - 1)) / max(1, len(s) - 1)


def controls():
    lp = bigram_model()
    lines, _ = decrypt()
    real = score(''.join(lines), lp)
    print(f'decryption with interventions: {real:.3f} per bigram')
    # raw stream: every fully visible letter token, no restorations, no slips, key running straight on
    raw = [int(t) for row in transcription() for t in row if not t.endswith('|') and int(t) <= 27]
    res = []
    for a in ALPHA:
        for b in ALPHA:
            for c in ALPHA:
                k = a + b + c
                res.append((score(''.join(dec(n, k[i % 3]) for i, n in enumerate(raw)), lp), k))
    res.sort(reverse=True)
    rot = {'win', 'inw', 'nwi'}
    ranks = [i for i, (_, k) in enumerate(res) if k in rot]
    print(f'all {len(res)} period-3 keys on the raw stream ({len(raw)} letter tokens, no corrections):')
    print('  best five:', ', '.join(f'{k} {s:.3f}' for s, k in res[:5]))
    print('  ranks of the rotations of WIN:', ranks, ' median score', f'{res[len(res) // 2][0]:.3f}')
    rnd = random.Random(1783)
    sh = []
    for _ in range(200):
        r = raw[:]; rnd.shuffle(r)
        sh.append(score(''.join(dec(n, KEY[i % 3]) for i, n in enumerate(r)), lp))
    print(f'200 shuffles of the raw stream under WIN: best {max(sh):.3f}, mean {sum(sh) / len(sh):.3f}')
    wk = []
    for _ in range(200):
        k = ''.join(rnd.choice(ALPHA) for _ in range(3))
        if k in rot: continue
        wk.append(score(''.join(decrypt(k)[0]), lp))
    print(f'{len(wk)} random wrong keys with the same alignment: best {max(wk):.3f}, mean {sum(wk) / len(wk):.3f}')


def main():
    tr = transcription()
    for i, wl in enumerate(WORK):
        if visible(wl) != tr[i]:
            sys.exit(f'line {i + 1}: working text does not match transcription.txt\n{visible(wl)}\n{tr[i]}')
    if '--controls' in sys.argv:
        controls(); return
    lines, notes = decrypt()
    for i, (row, pl) in enumerate(zip(tr, lines), 1):
        print(f'L{i}  ' + ' '.join(row))
        print(f'    {pl}')
    print('\n( ) = token completed or supplied at a line end; [n] = code group, meaning unknown')
    for n in notes:
        print(' ', n)


if __name__ == '__main__':
    main()
