"""Eckert ledger mssEC 19 (War Department Ciphers Sent, 1864), pp. 1-7, decoded with Cipher Book No. 9.

    python decode.py              writes mssEC19_p1-7_decryption.txt (T1-T11) and mssEC19_p1-7_unread_decode.txt (U1-U3)
    python decode.py --controls   also writes controls.txt (the decode against the Official Records clear texts,
                                  with the meanings shuffled among the code words as a control)

The ledger copies each telegram after the code words were put in and before the route transposition, so the
words are in reading order and only the code layer is open. cipher9_key_used.tsv gives the meaning of each code
word used, read from the images of Cipher Book No. 9 (Huntington mssEC 67, item 1750). In the output a code word is
replaced by [MEANING]; a time word by <time>; words after the signature (Applause/Abortion after "sig" or
"signed", or followed by a time word) are check or null words, shown as {null: ...}. Words split by the volunteers with " = " (Ab = or = tion) are joined when the
joined word is a code word. A code word with an added s (Readings, suppers, Quotients) keeps it as +s.
Python standard library only; paths are relative to this file.
"""
import csv, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SIGNATURE = {'applause', 'abortion'}          # H. W. Halleck
# what to look for in the printed clear text, for meanings whose printed form differs (controls only)
MATCH = {'Brig Genls': 'brig', 'Maj [Genls]': 'maj', 'Adjutant [General]': 'adjutant', 'W. S. Sherman': 'sherman',
         'Joe Johnston': 'johnston', 'H. W. Halleck': 'halleck', 'U. S. Grant': 'grant', 'B. F. Butler': 'butler',
         'Rail Road': 'railroad', 'Telegraphs': 'telegraph', 'Batteries': 'batter', 'Reinforcements': 'enforcements',
         'Troops': 'troop', 'Cut Off': 'cut off', 'Lieutenant': 'lieut', 'Colonel': 'col'}


def p(name):
    return os.path.join(HERE, name)


def load_key():
    code, time = {}, {}
    with open(p('cipher9_key_used.tsv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if re.fullmatch(r'[\d.]+ (a\.m\.|p\.m\.|M\.)', r['meaning']):
                time[r['code_words'].lower()] = r['meaning']
                continue
            for w in r['code_words'].split('/'):
                code[w.strip().lower()] = r['meaning']
    return code, time


def telegrams():
    """[(label, [lines])] from the transcription, in order"""
    out, cur = [], None
    with open(p('mssEC19_p1-7_transcription.txt'), encoding='utf-8') as f:
        for ln in f:
            ln = ln.rstrip('\n')
            if ln.startswith('#') or ln.startswith('== p.') or not ln.strip():
                continue
            if ln.startswith('== '):
                cur = (ln[3:], [])
                out.append(cur)
            else:
                cur[1].append(ln)
    return out


def tokens(line):
    """split a ledger line into words, joining 'a = b = c' when the joined word is wanted later"""
    raw = line.replace('<deletion>p</deletion>', '').split()
    out, i = [], 0
    while i < len(raw):
        if raw[i] == '=' and out and i + 1 < len(raw):
            out[-1] = out[-1] + '=' + raw[i + 1]
            i += 2
        elif raw[i] == '=' and out:                 # word broken at the line end
            out[-1] = out[-1] + '-'
            i += 1
        elif raw[i].startswith('=') and out:
            out[-1] = out[-1] + raw[i]
            i += 1
        else:
            out.append(raw[i])
            i += 1
    return out


def lookup(tok, code):
    w = re.sub(r'[^a-z]', '', tok.lower())
    if w in code:
        return code[w], '', w
    if w.endswith('s') and w[:-1] in code:
        return code[w[:-1]], '+s', w[:-1]
    return None, '', w


def decode_tel(lines, code, time):
    out, closed, used, prev = [], False, [], ''
    for ln in lines:
        words = []
        for tok in tokens(ln):
            w = re.sub(r'[^a-z]', '', tok.lower())
            joined_parts = tok.split('=')
            m, suf, base = lookup(tok, code)
            if closed and w not in time:
                words.append('{null: ' + tok + '}')
                prev = w
                continue
            if w in time:
                words.append('<' + time[w] + '>')
                used.append(('time', w, time[w]))
                if prev in SIGNATURE:
                    closed = True          # time word after the signature: what follows is check words
            elif m:
                words.append('[' + m + ']' + suf)
                used.append(('code', base, m))
                if w in SIGNATURE and prev in ('sig', 'signed'):
                    closed = True          # the signature closes the telegram; what follows is check words
            elif len(joined_parts) > 1:
                words.append(' '.join(joined_parts))     # not a code word: keep the volunteers' split
            else:
                words.append(tok)
            prev = w
        out.append((ln, ' '.join(words)))
    return out, used


def write(code, time):
    tels = telegrams()
    files = {'T': ('mssEC19_p1-7_decryption.txt',
                   'telegrams T1-T11, decoded with Cipher Book No. 9; see mssEC19_p1-7_reading.md for the sentences'),
             'U': ('mssEC19_p1-7_unread_decode.txt',
                   'telegrams U1-U3, NOT read: the No. 9 meanings give no sense here; shown for checking only')}
    results = {}
    for kind, (fname, what) in files.items():
        out = [f'# mssEC 19 pp. 1-7: {what}.', '# python decode.py; key cipher9_key_used.tsv; transcription '
               'mssEC19_p1-7_transcription.txt.',
               '# Each ledger line, then -> the line with [code meanings], <time words> and {null: ...} words.', '']
        for label, lines in tels:
            if not label.startswith(kind):
                continue
            dec, used = decode_tel(lines, code, time)
            results[label.split()[0]] = (lines, dec, used)
            out.append('== ' + label)
            for ln, d in dec:
                out.append('    ' + ln)
                out.append('  -> ' + d)
            out.append('')
        with open(p(fname), 'w', encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(out))
    n = sum(1 for k, v in results.items() if k.startswith('T') for u in v[2] if u[0] == 'code')
    print(f'T1-T11: {n} code-word tokens decoded; files written')
    return results


def or_texts():
    out, cur = {}, None
    with open(p('or_clear_texts.txt'), encoding='utf-8') as f:
        for ln in f:
            if ln.startswith('#'):
                continue
            if ln.startswith('== '):
                cur = ln.split()[1]
                out[cur] = []
            elif cur:
                out[cur].append(ln.strip())
    return {k: ' '.join(v) for k, v in out.items()}


def score(results, meanings_of):
    """code-word tokens whose meaning appears in the printed clear text of the same telegram"""
    orx = or_texts()
    hit = tot = 0
    for lab, text in orx.items():
        t = text.lower().replace('-', '')
        for kind, w, m in results[lab][2]:
            if kind != 'code':
                continue
            m = meanings_of(w)
            term = MATCH.get(m, re.sub(r'[\[\]]', '', m).lower())
            tot += 1
            hit += term.replace('-', '') in t
    return hit, tot


def controls(results, code):
    lines = ['# Controls for decode.py (python decode.py --controls)', '']
    hit, tot = score(results, lambda w: code[w])
    lines.append(f'Real key: {hit} of {tot} code-word tokens of the nine printed telegrams have their meaning in the '
                 'printed clear text of the same telegram.')
    random.seed(1)
    words = sorted(code)
    sh = []
    for _ in range(500):
        vals = [code[w] for w in words]
        random.shuffle(vals)
        perm = dict(zip(words, vals))
        sh.append(score(results, lambda w: perm[w])[0])
    sh.sort()
    lines.append(f'Meanings shuffled among the same code words, 500 runs: min {sh[0]}, median {sh[250]}, max {sh[-1]}.')
    lines += ['', 'Time words against the time printed in the clear text:']
    orx = or_texts()
    for lab, text in orx.items():
        tw = [m for kind, w, m in results[lab][2] if kind == 'time']
        printed = re.search(r'- ([\d.]+ (?:a\.m\.|p\.m\.|noon))', text)
        lines.append(f'  {lab:4s} ledger {tw[0] if tw else "(no time word)":12s} printed {printed.group(1) if printed else "?"}')
    with open(p('controls.txt'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')
    print('\n'.join(lines))


if __name__ == '__main__':
    code, time = load_key()
    res = write(code, time)
    if '--controls' in sys.argv:
        controls(res, code)
