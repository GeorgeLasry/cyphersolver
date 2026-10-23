"""v6: put a modernised reading back into the writer's spelling, word by word, from a period source text.

    python v6_align.py <reading> <lang> <source.txt> [<source2.txt> ...] [--apply] [--strip-accents]

The '## Reading' body (or, with no such heading, everything after the first blank line that follows an HTML comment
or '#' header lines) is walked word by word against the source words (the contemporary decipherment / margin as
written, the printed edition as printed, or the clear transcription), aligned with difflib on folded word forms
(case, accents, u/v, i/j/y, b/v in Spanish, h, double letters, ...). Where a reading word and the aligned source
word are the same word (fold equal, or close: similarity >= 0.75 on the folded forms) and differ in spelling, the
source form is taken; the reading's capital is kept on the first letter. Words inside [ ] { } ⟨ ⟩ < > are left
alone, so holes, brackets and code glosses are kept. A pair that is not the same word is never changed: it is
listed as 'differs' for review (the source may show another word). --strip-accents also takes editorial accents
off reading words that no source word carries (for cipher text in a language whose writer used none).

Prints every change and every 'differs' pair; --apply writes the body back.
"""
import difflib, re, sys, pathlib, unicodedata

BR = r'\[[^\]\n]*\]|\{[^}\n]*\}|⟨[^⟩\n]*⟩|<[^>\n]*>'


def deacc(s):
    keep = {'ñ': '\0', 'Ñ': '\1'}
    for k, v in keep.items():
        s = s.replace(k, v)
    s = ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))
    return s.replace('\0', 'ñ').replace('\1', 'Ñ')


def fold(w, lang, vowels=True):
    s = deacc(w.lower()).replace('ñ', 'n').replace('ſ', 's').replace('ß', 'ss')
    s = re.sub(r'[^a-z]', '', s)
    if lang == 'es':
        s = s.replace('v', 'b').replace('h', '').replace('y', 'i').replace('z', 'c').replace('ç', 'c')
        s = s.replace('x', 'j')
        s = re.sub(r'qu(?=[ei])', 'c', s).replace('q', 'c')
        s = s.replace('ge', 'je').replace('gi', 'ji')
        s = s.replace('ph', 'f').replace('th', 't')
    elif lang == 'la':
        s = s.replace('j', 'i').replace('v', 'u').replace('ae', 'e').replace('oe', 'e').replace('y', 'i')
        s = s.replace('ti', 'ci').replace('h', '').replace('mn', 'n')
    else:
        s = s.replace('v', 'u').replace('j', 'i').replace('y', 'i').replace('w', 'u')
        if lang == 'fr':
            s = re.sub(r's(?=[bcdfgjklmnpqtv])', '', s)
        if lang == 'en':
            s = s.rstrip('e') or s
            s = s.replace('ck', 'k').replace('ph', 'f').replace('gh', 'g').replace('ie', 'i').replace('ea', 'e')
    return re.sub(r'(.)\1+', r'\1', s) if vowels else re.sub(r'([^aeiou])\1+', r'\1', s)


def body_span(t):
    m = re.search(r'(^## Reading[^\n]*\n)(.*?)(?=^## |\Z)', t, re.S | re.M)
    if m:
        return m.start(2), m.end(2)
    m = re.search(r'-->[ \t]*\n', t)                          # carpio/ronquillo: after the HTML comment header
    if m:
        s0 = m.end()
        mt = re.match(r'\s*# [^\n]*\n', t[s0:])               # and its title line
        if mt:
            s0 += mt.end()
        m2 = re.search(r'^## ', t[s0:], re.M)
        return s0, (s0 + m2.start()) if m2 else len(t)
    return 0, len(t)


def source_words(paths, ocr=False):
    out = []
    for p in paths:
        t = pathlib.Path(p).read_text(encoding='utf8')
        if ocr:
            t = t.replace('ſ', 's')
        t = '\n'.join(l for l in t.split('\n') if not l.startswith('#'))
        t = re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', t)               # words broken at the line end
        t = re.sub(r'\[[^\]\n]*\]|<[^>\n]*>|\{[^}\n]*\}', ' ', t)   # illegible / uncertain marks are not spellings
        out += re.findall(r"(?<![\w])[^\W\d_]+", t)
    return out


def main(a):
    apply = '--apply' in a
    strip = '--strip-accents' in a
    lexf = [x.split('=', 1)[1] for x in a if x.startswith('--lexicon=')]
    ocr = '--ocr' in a          # source is OCR of an old print: f may be a long s; first letters must agree
    angle = '--angle' in a      # also respell words in ⟨ ⟩ (clear text given from the same print)
    skip = set(x.split('=', 1)[1] for x in a if x.startswith('--skip='))   # source forms judged OCR errors by hand
    a = [x for x in a if not x.startswith('--')]
    rd, lang, srcs = a[0], a[1], a[2:]
    p = pathlib.Path(rd)
    t = p.read_text(encoding='utf8')
    s0, s1 = body_span(t)
    body = t[s0:s1]
    br = BR.replace('|⟨[^⟩\\n]*⟩', '') if angle else BR
    masked = re.sub(br, lambda m: ' ' * len(m.group(0)), body.replace('⟨', ' ').replace('⟩', ' ') if angle else body)
    toks = [(m.start(), m.end(), m.group(0)) for m in re.finditer(r"(?<![\w])[^\W\d_]+", masked) if m.group(0) not in ('º', 'ª')]
    S = source_words(srcs, ocr) if srcs else []
    LEX = None
    if lexf:                     # word counts of the whole print: an OCR form that is not the same word must recur
        from collections import Counter
        LEX = Counter(w.lower() for w in source_words(lexf, ocr))
    F = (lambda w: fold(w, lang).replace('f', 's')) if ocr else (lambda w: fold(w, lang))
    A = [F(w) for _, _, w in toks]
    B = [F(w) for w in S]
    sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
    rep, differs, matched = {}, [], set()

    abbrev = []

    def take(i, j):
        w, s = toks[i][2], S[j]
        if s in skip:
            abbrev.append((w, s + ' (OCR error, by hand)')); return
        fw, fs = F(w), F(s)
        if ocr and (fw[:1] != fs[:1] or (fw != fs and difflib.SequenceMatcher(None, fw, fs).ratio() < 0.8)):
            abbrev.append((w, s)); return
        if ocr and (any(c.isupper() for c in s[1:]) and not w.isupper() or (len(s) == 1 and s != w)):
            abbrev.append((w, s)); return              # OCR noise: small capitals, J for I
        if ocr and fw != fs and LEX is not None and LEX.get(s.lower(), 0) < 2:
            abbrev.append((w, s + ' (once in the print: OCR?)')); return
        if ocr:                                    # an OCR f where the reading has s is a long s
            sl, wl = list(s), w.lower()
            for op, x1, x2, y1, y2 in difflib.SequenceMatcher(None, wl, s.lower(), autojunk=False).get_opcodes():
                if op == 'replace' and x2 - x1 == y2 - y1:
                    for k in range(x2 - x1):
                        if wl[x1 + k] == 's' and s[y1 + k].lower() == 'f':
                            sl[y1 + k] = 's'
            s = ''.join(sl)
        if fw != fs and (len(fw) <= 4 or len(fs) < len(fw) - 1):   # short words: only the same word; a shorter
            abbrev.append((w, s)); return                          # source form is an abbreviation, not a spelling
        matched.add(i)
        if w == s:
            return
        if w[:1].isupper():
            s = s[:1].upper() + s[1:]
        elif w[:1].islower() and not w.isupper():
            s = s[:1].lower() + s[1:]
        if s != w:
            rep[i] = s

    for op, a1, a2, b1, b2 in sm.get_opcodes():
        if op == 'equal':
            for k in range(a2 - a1):
                take(a1 + k, b1 + k)
        elif op == 'replace':
            sub = difflib.SequenceMatcher(None, A[a1:a2], B[b1:b2], autojunk=False)
            # pair greedily in order by similarity
            j = b1
            for i in range(a1, a2):
                best = None
                for jj in range(j, min(b2, j + 4)):
                    r = difflib.SequenceMatcher(None, A[i], B[jj]).ratio()
                    if ocr and A[i][:1] != B[jj][:1]:
                        r = 0
                    if r >= 0.75 and (best is None or r > best[0]):
                        best = (r, jj)
                if best:
                    take(i, best[1]); j = best[1] + 1
                else:
                    differs.append((toks[i][2], ' '.join(S[b1:b2])))
    if strip:
        for i, (_, _, w) in enumerate(toks):
            if i not in matched and i not in rep and deacc(w) != w:
                rep[i] = deacc(w)
    for i in sorted(rep):
        print(f'  {toks[i][2]} -> {rep[i]}')
    seen = set()
    for w, s in abbrev:
        print(f'  kept (abbreviated or other word in the source): {w!r} | {s!r}')
    for w, s in differs:
        if (w, s) in seen:
            continue
        seen.add((w, s))
        print(f'  differs: {w!r} | source: {s[:80]!r}')
    cov = len(matched) / max(1, len(toks))
    print(f'{rd}: {len(rep)} respelt, {len(toks)} words, {cov:.0%} aligned to the source')
    if apply and rep:
        b = body
        for i in sorted(rep, reverse=True):
            x0, x1, _ = toks[i]
            b = b[:x0] + rep[i] + b[x1:]
        p.write_text(t[:s0] + b + t[s1:], encoding='utf8')


if __name__ == '__main__':
    main(sys.argv[1:])
