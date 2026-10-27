"""Richard Taylor's telegram letter-books, Meridian 1865 (catalogue 681): decryption and controls.

    python decrypt.py              writes <doc>_cipher.txt and <doc>_decryption.txt for the four telegrams
    python decrypt.py --controls   also writes controls.txt (wrong keys, wrong offsets, random keys, shuffles)

System: Confederate Vigenere on the tabula recta. Only the cipher words are enciphered; word division is kept.
The key COMERETRIBUTION runs over the cipher letters only, starts at its first letter (offset 0) with the first
cipher letter of each telegram and runs on through all the cipher words of that telegram.

alignment.tsv gives, for each cipher word in order: the letters as read on the image, the letters after the
corrections listed in its note column (single glyphs the clerk wrote in a misleading form, see NOTES.md), and the
plaintext. The script checks that every corrected word deciphers to its plaintext, and shows what the letters as
read give. Python standard library only; paths are relative to this file.
"""
import collections, csv, os, random, string, sys

HERE = os.path.dirname(os.path.abspath(__file__))
KEY = 'COMERETRIBUTION'
DOCS = ['v196-0061', 'v11-0022', 'v11-0036', 'v11-0039']
# English letter frequencies (per cent), for the chi-squared control
EN = dict(zip(string.ascii_lowercase, [8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, .15, .77, 4.0, 2.4, 6.7, 7.5,
                                       1.9, .095, 6.0, 6.3, 9.1, 2.8, .98, 2.4, .15, 2.0, .074]))


def p(name):
    return os.path.join(HERE, name)


def load():
    rows = collections.OrderedDict((d, []) for d in DOCS)
    with open(p('alignment.tsv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            rows[r['doc']].append(r)
    return rows


def dec(word, key, start):
    """decipher word with key letters starting at key position start"""
    return ''.join(chr((ord(c) - ord(key[(start + i) % len(key)])) % 26 + 97) for i, c in enumerate(word))


def keyslice(key, start, n):
    return ''.join(key[(start + i) % len(key)] for i in range(n))


def plain_letters(s):
    return ''.join(c for c in s.lower() if c.isalpha())


def transcription_lines(doc):
    with open(p(doc + '_transcription.txt'), encoding='utf-8') as f:
        return [ln.rstrip('\n') for ln in f if not ln.startswith('#')]


def walk(doc, rows):
    """match the cipher words of the transcription, in order, to the alignment rows"""
    out, i = [], 0
    for ln in transcription_lines(doc):
        hits = []
        for tok in ln.replace('-', ' ').split():
            t = tok.strip('.,')
            if i < len(rows) and t == rows[i]['as_read']:
                hits.append(rows[i])
                i += 1
        out.append((ln, hits))
    if i != len(rows):
        sys.exit(f'{doc}: only {i} of {len(rows)} alignment rows found in the transcription')
    return out


def write_texts(rows):
    summary = []
    for doc in DOCS:
        lines = walk(doc, rows[doc])
        with open(p(doc + '_cipher.txt'), 'w', encoding='utf-8', newline='\n') as f:
            f.write(f'# {doc}: cipher words only, as read on the image, one manuscript line per line\n')
            for ln, hits in lines:
                if hits:
                    f.write(' '.join(r['as_read'] for r in hits) + '\n')
        pos, out, n_read, n_same, n_corr = 0, [], 0, 0, 0
        for ln, hits in lines:
            out.append(ln)
            for r in hits:
                a, c, pt = r['as_read'], r['corrected'], plain_letters(r['plaintext'])
                k = keyslice(KEY, pos, len(c))
                dc = dec(c, KEY, pos)
                if dc != pt:
                    sys.exit(f'{doc} {a}: corrected {c} gives {dc}, not {pt}')
                da = dec(a, KEY, pos)
                n_read += len(a)
                n_same += sum(x == y for x, y in zip(da, pt)) if len(a) == len(c) else 0
                n_corr += len(c)
                fix = '' if a == c else f'  corrected {c}'
                out.append(f'    {a:12s} key {k:12s} -> {da:12s}{fix:22s} -> {r["plaintext"]:12s} {r["note"] or ""}'.rstrip())
                pos += len(c)
        head = [f'# {doc}: decryption line by line against {doc}_transcription.txt (python decrypt.py)',
                f'# Key {KEY}, offset 0 at the first cipher letter of the telegram, running over cipher letters only.',
                '# Under each manuscript line: cipher word as read | key letters | what the letters as read give |',
                '# corrected letters where a glyph is corrected | plaintext | note. [?] = corrected letter not re-checked',
                '# on a fresh crop.',
                f'# Cipher letters: {n_read} as read, {n_corr} after correction (the key ends at position {pos % len(KEY)}).',
                f'# Letters as read that give the plaintext directly: {n_same} of {n_corr}'
                + (' (IRUBEE, read with 6 letters for 7, not counted)' if doc == 'v11-0036' else '') + '.', '']
        with open(p(doc + '_decryption.txt'), 'w', encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(head + out) + '\n')
        summary.append(f'{doc}: {n_corr} cipher letters, {n_same} right as read, all {n_corr} right after correction')
    print('\n'.join(summary))


def chi(text):
    s = [c for c in text if c.isalpha()]
    n, cnt = len(s), collections.Counter(s)
    return sum((cnt[k] - n * EN[k] / 100) ** 2 / (n * EN[k] / 100) for k in EN)


def controls(rows):
    random.seed(1)
    out = ['# Controls for decrypt.py, run on the letters AS READ (no corrections), python decrypt.py --controls',
           '# chi2 = chi-squared distance of the decrypt from English letter frequencies (lower is more English).',
           '# agree = letters of the decrypt equal to the plaintext letter in the same place.', '']
    for doc in DOCS:
        rs = [r for r in rows[doc] if len(r['as_read']) == len(r['corrected'])]
        ct = ''.join(r['as_read'] for r in rs)
        pt = ''.join(plain_letters(r['plaintext']) for r in rs)
        # key positions as in the telegram (words with a dropped or doubled letter are left out of this control)
        pos, keypos = 0, []
        for r in rows[doc]:
            if len(r['as_read']) == len(r['corrected']):
                keypos += [pos + i for i in range(len(r['corrected']))]
            pos += len(r['corrected'])

        def run(key, off=0):
            return ''.join(chr((ord(c) - ord(key[(k + off) % len(key)])) % 26 + 97) for c, k in zip(ct, keypos))

        def agree(d):
            return sum(x == y for x, y in zip(d, pt))
        right = run(KEY)
        offs = sorted((round(chi(run(KEY, o))), o) for o in range(1, 15))
        rnd = sorted(chi(run(''.join(random.choice(string.ascii_uppercase) for _ in range(15)))) for _ in range(200))
        words = [r['as_read'] for r in rs]
        sh = []
        for _ in range(50):
            random.shuffle(words)
            sct = ''.join(words)
            sh.append(sum(chr((ord(c) - ord(KEY[k % 15])) % 26 + 97) == y for c, k, y in zip(sct, keypos, pt)))
        out += [f'== {doc} ({len(ct)} letters in words read with the right length)',
                f'COMERETRIBUTION offset 0: chi2 {chi(right):.0f}, agree {agree(right)}/{len(pt)}: {right[:60]}',
                f'best other offset of the same key: chi2 {offs[0][0]} (offset {offs[0][1]})']
        for k in ['COMPLETEVICTORY', 'MANCHESTERBLUFF']:
            d = run(k)
            out.append(f'{k}: chi2 {chi(d):.0f}, agree {agree(d)}/{len(pt)}: {d[:60]}')
        out += [f'200 random 15-letter keys: chi2 min {rnd[0]:.0f}, median {rnd[100]:.0f}',
                f'cipher words shuffled, right key, 50 runs: agree mean {sum(sh) / len(sh):.1f}, max {max(sh)}', '']
    with open(p('controls.txt'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out))
    print('\n'.join(out))


if __name__ == '__main__':
    rows = load()
    write_texts(rows)
    if '--controls' in sys.argv:
        controls(rows)
