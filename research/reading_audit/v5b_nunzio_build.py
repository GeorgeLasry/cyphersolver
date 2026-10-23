"""v5 (b): nunzio1718 - build lasry/R<nnn>_reading.md from the DECODE transcriber's PLAINTEXT rows (their copy of the
contemporary interlinear decipherment) in lasry/364D-<n>.txt, checked against Lasry's decode row of each figure line.

    python research/reading_audit/v5b_nunzio_build.py <n> [--write] [--show]

* A PLAINTEXT row is paired with the figure line that follows it. A figure line with no PLAINTEXT row before it is
  reported (MISSING) and filled from Lasry's decode row of that line, word-divided by hand later (marked <<L: ...>>
  in the draft; the draft is not written while any remain unless --write-anyway).
* A word the transcriber marked doubtful ('word?', '?word') is kept unbracketed when its letters occur in Lasry's
  decode of the same or a neighbouring figure line (the figures carry it), else it becomes [?word]. A bare '?' is [?].
* Letters with accents that DECODE's file dropped are not restored (the transcriber's copy lost them: 'pi' = piu,
  'gi' = gia, a lone 'e' lost entirely); abbreviations are kept as written.
"""
import pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
LAS = ROOT / 'targets' / 'nunzio1718' / 'lasry'


def letters(s):
    return re.sub(r'[^a-z]', '', s.lower().replace('u/v', 'u').replace('v', 'u').replace('j', 'i'))


def dec_letters(l):
    out = ''
    for t in l.split('|')[0].split():
        if t == '_' or '?' in t or t.startswith('<'): continue
        out += letters(t.split('/')[0])
    return out


def build(n):
    ls = (LAS / f'364D-{n}.txt').read_text(encoding='utf8', errors='replace').splitlines()
    figs = []          # (plaintext or None, decode letters, decode raw)
    pend = None
    for i, l in enumerate(ls):
        m = re.match(r'^<PLAINTEXT \w+ (.*)>\s*$', l)
        if m:
            if pend is not None: figs.append((pend, '', ''))       # two PLAINTEXT rows in a row
            pend = m.group(1).strip(); continue
        if re.match(r'^[\d ?\-]+\|\s*$', l) and i + 1 < len(ls):
            figs.append((pend, dec_letters(ls[i + 1]), ls[i + 1].split('|')[0]))
            pend = None
    if pend is not None: figs.append((pend, '', ''))
    words, miss, kept, brk = [], 0, 0, 0
    for k, (pt, dl, raw) in enumerate(figs):
        if pt is None:
            miss += 1
            words.append('<<L: ' + re.sub(r'\s+', ' ', raw.replace(' _ ', ' ').replace('u/v', 'u')).strip() + '>>')
            continue
        near = ''.join(f[1] for f in figs[max(0, k - 1):k + 2])
        for w in pt.split():
            if '?' not in w:
                words.append(w); continue
            core = w.replace('?', '')
            if not letters(core):
                words.append('[?]'); brk += 1; continue
            if len(letters(core)) >= 2 and letters(core) in near:
                words.append(core); kept += 1
            else:
                words.append(f'[?{core}]'); brk += 1
    body = ' '.join(words)
    return body, miss, kept, brk, len(figs)


if __name__ == '__main__':
    n = int(sys.argv[1])
    body, miss, kept, brk, nf = build(n)
    print(f'364D-{n} R{153 + n}: figure lines {nf}, missing PLAINTEXT {miss}, doubtful words confirmed by the figures {kept}, bracketed {brk}')
    if '--show' in sys.argv: print(body)
    if '--write' in sys.argv:
        out = HERE.parents[1] / 'research' / 'reading_audit' / 'v5b_tmp' / f'R{153 + n}_draft.md'
        out.parent.mkdir(exist_ok=True)
        out.write_text(body + '\n', encoding='utf8')
        print('draft', out)
