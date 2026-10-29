"""Apply the 1798 page,word values (table_1798.tsv, from align.py) to the 1802 letters ct_212.txt and ct_217.txt.

Each group is looked up in the 1798 table: a word value, a letter value, or nothing. Groups with no 1798 value
are shown as [page,word:X-Y], where X-Y is the stretch of the alphabet the page falls in, judged from the letter
groups (A=1 ... U=398, Z=440); the vocabulary is roughly alphabetical, so this narrows the word. Runs of letter
groups are joined into the spelled word. Writes decode_212.txt, decode_217.txt and prints coverage.

    python targets/jones1802/apply.py
"""
import bisect
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from align import cipher_tokens  # noqa: E402


# Letter groups that occur only in 1802, each fixed by the spelled names it completes (not from 1798):
# B 28,1 (A-B-DULLAH, B-AGDAD, DEAR-B-EKIR); H 174,7 (ABDULLA-H, ASTRAC-H-AN); K 213,8 (K-ARAPET, DEARBE-K-IR,
# K-ARS); M 228,45 (M-ERDIN, ERZEROU-M, TO-M-ANS); Z 440,72 (ER-Z-EROUM); Y 439,66 (BA-Y-EZEED); F 141,67
# (SE-F-LIS = Teflis, three times); second codes: C 49,10 (ASTRA-C-HAN), N 249,48 / 249,45 (MERDI-N, ERIVA-N),
# O 256,10 and A 56,11 (C-O-NST-A-N, Constantinople), L 215,3 (PHI-L-IPI), H 147,7 (P-H-ILIPOOS), P 265,63.
LETTERS_1802 = {'28,1': 'b', '174,7': 'h', '213,8': 'k', '228,45': 'm', '440,72': 'z', '439,66': 'y',
                '141,67': 'f', '49,10': 'c', '249,48': 'n', '249,45': 'n', '256,10': 'o', '56,11': 'a',
                '215,3': 'l', '147,7': 'h', '265,63': 'p',
                '1,45': 'a'}  # DE-A-RBEND (Derbend, spelled like DEARBEKIR); faded, read on a 1400-px crop


def load_table():
    words, letters = {}, {}
    for line in (HERE / 'table_1798.tsv').read_text(encoding='utf-8').splitlines()[1:]:
        g, w, c, p = line.split('\t')
        if w.startswith('['):
            letters[g] = w[1:-1]
        elif c != '-' and (g not in words or int(c) > words[g][1]):
            words[g] = (w, int(c))
    return {g: w for g, (w, c) in words.items()}, letters


def heads(letters):
    """(page, letter) for the lowest page each letter group sits on, sorted."""
    return sorted((int(g.split(',')[0]), l) for g, l in letters.items())


def bracket(page, hs):
    pages = [p for p, _ in hs]
    i = bisect.bisect_right(pages, page)
    lo = hs[i - 1][1] if i else 'a'
    hi = hs[i][1] if i < len(hs) else 'z'
    return lo.upper() if lo == hi else f'{lo.upper()}-{hi.upper()}'


def decode(path, words, letters, hs):
    toks = cipher_tokens(path)
    out, run = [], []
    n_groups = n_word = n_letter = n_letter02 = 0
    unknown = []

    def flush():
        if run:
            out.append(''.join(run).upper())
            run.clear()
    for t in toks:
        if t[0] == 'w':
            flush()
            out.append(t[1])
            continue
        g = t[1]
        suf = t[2] if len(t) > 2 else ''
        n_groups += 1
        base = ','.join(g.split(',')[:2])
        if g in letters:
            n_letter += 1
            run.append(letters[g])
            continue
        if g in LETTERS_1802:
            n_letter02 += 1
            run.append(LETTERS_1802[g])
            continue
        flush()
        w = words.get(g) or words.get(base)
        if w:
            n_word += 1
            out.append(w + ('+' + suf if suf else ''))
        else:
            page = int(g.split(',')[0])
            unknown.append(g)
            out.append(f'[{g}{"+" + suf if suf else ""}:{bracket(page, hs)}]')
    flush()
    return out, n_groups, n_word, n_letter, n_letter02, unknown


def load_proposals():
    """proposals.tsv: values for groups with no 1798 value, from alphabet stretch plus context, graded H/M/L."""
    props = {}
    for line in (HERE / 'proposals.tsv').read_text(encoding='utf-8').splitlines()[1:]:
        g, w, grade, _ = line.split('\t', 3)
        if w != '?':
            props[g] = (w, grade)
    return props


def retry(words, letters, props):
    """Second pass: the 1798 values, the 1802 letters and the proposals together. H proposals print plain,
    M in {braces}, L in {braces?}; groups with no value stay [group]. Writes reading_<n>.txt, prints shares."""
    for name in ('217', '212'):
        out, run, cnt = [], [], {'1798w': 0, '1798l': 0, '1802l': 0, 'H': 0, 'M': 0, 'L': 0, 'open': 0}

        def flush():
            if run:
                out.append(''.join(run).upper())
                run.clear()
        for t in cipher_tokens(HERE / f'ct_{name}.txt'):
            if t[0] == 'w':
                flush()
                out.append(t[1])
                continue
            g, suf = t[1], ('+' + t[2] if len(t) > 2 else '')
            base = ','.join(g.split(',')[:2])
            if g in letters or g in LETTERS_1802 or (g in props and props[g][0].startswith('[')):
                cnt['1798l' if g in letters else '1802l' if g in LETTERS_1802 else 'H'] += 1
                run.append(letters.get(g) or LETTERS_1802.get(g) or props[g][0][1:-1])
                continue
            flush()
            if g in words or base in words:
                cnt['1798w'] += 1
                out.append((words.get(g) or words[base]) + suf)
            elif g in props:
                w, grade = props[g]
                cnt[grade] += 1
                out.append({'H': w, 'M': '{' + w + '}', 'L': '{' + w + '?}'}[grade] + suf)
            else:
                cnt['open'] += 1
                out.append(f'[{g}]')
        flush()
        n = sum(cnt.values())
        text = re.sub(r'(.{1,110})(?:\s+|$)', r'\1\n', ' '.join(out))
        (HERE / f'reading_{name}.txt').write_text(
            f'# ct_{name}.txt read with the 1798 values, the 1802 letters and proposals.tsv (apply.py).\n'
            '# plain = 1798 value, spelled letters or grade-H proposal; {word} = grade M; {word?} = grade L;\n'
            '# [group] = no value. Suffixes shown as +ed etc.\n' + text, encoding='utf-8')
        print(f'{name} retry: {n} groups; ' + ', '.join(f'{k} {v} ({v / n:.0%})' for k, v in cnt.items()))


def main():
    words, letters = load_table()
    hs = heads(letters)
    if '--retry' in sys.argv:
        return retry(words, letters, load_proposals())
    for name in ('217', '212'):
        out, n, nw, nl, nl2, unk = decode(HERE / f'ct_{name}.txt', words, letters, hs)
        text = ' '.join(out)
        text = re.sub(r'(.{1,110})(?:\s+|$)', r'\1\n', text)
        (HERE / f'decode_{name}.txt').write_text(
            f'# ct_{name}.txt with the 1798 values (apply.py). [group:X-Y] = no 1798 value; X-Y = alphabet stretch.\n'
            + text, encoding='utf-8')
        print(f'{name}: {n} groups; 1798 word values {nw} ({nw / n:.0%}), 1798 letter values {nl} ({nl / n:.0%}), '
              f'letters fixed by 1802 names {nl2} ({nl2 / n:.0%}), no value {len(unk)} ({len(unk) / n:.0%}; '
              f'{len(set(unk))} distinct)')
        print('   1798 word groups used:', sorted({g for g in words} & {t[1] for t in cipher_tokens(
            HERE / f'ct_{name}.txt') if t[0] == 'g'}))


if __name__ == '__main__':
    sys.exit(main())
