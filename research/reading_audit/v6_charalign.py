"""v6: put a modernised reading of cipher text back into the spelling the cipher gives (the key's letter values).

    python v6_charalign.py <reading> <lang> <stream.txt> [--apply] [--keep-accents]

<stream.txt> is the key decode as one letter stream (read2/R*.txt style: '#' lines skipped, [x] = group with no
value, dropped; {v} = a value, kept as letters). The reading body ('## Reading' section, else after the HTML comment
header) is aligned letter by letter with the stream (difflib, accents off, ñ = n). For each reading word, the stream
letters aligned to it are taken as its spelling when they are the same word in another spelling (v6_align.fold equal,
plus m/n before b/p): tomaban -> tomavan, así -> assi, debía -> devia. A ñ of the reading is kept where the stream
has n (the key does not distinguish them). A word whose stream letters are another word or a cipher slip keeps its
form, without editorial accents (the cipher carries none) unless --keep-accents. Words in [ ] { } ⟨ ⟩ < > are left
alone. Prints the changes; --apply writes the body back.
"""
import difflib, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from v6_align import fold as _fold, deacc, body_span, BR  # noqa: E402


def fold(w, lang):
    s = _fold(w, lang, vowels=False)   # a doubled vowel is a cipher slip, not a spelling
    if lang == 'es':
        s = re.sub(r'm(?=[bp])', 'n', s)
    return s


def lite(c):
    return deacc(c.lower()).replace('ñ', 'n')


def stream_letters(path):
    t = pathlib.Path(path).read_text(encoding='utf8')
    t = re.split(r'^# margin', t, flags=re.M)[0]          # read2 files: the DECODE margin follows; it is not the cipher
    t = '\n'.join(l for l in t.split('\n') if not l.startswith('#'))
    t = re.sub(r'\[[^\]]*\]', '', t)
    t = re.sub(r'[{}]', '', t)
    return [c for c in t if c.isalpha()]


def main(a):
    apply, keep = '--apply' in a, '--keep-accents' in a
    keepform = '--keep-uv-ij' in a
    a = [x for x in a if not x.startswith('--')]
    rd, lang, sp = a
    p = pathlib.Path(rd)
    t = p.read_text(encoding='utf8')
    s0, s1 = body_span(t)
    body = t[s0:s1]
    masked = re.sub(BR, lambda m: ' ' * len(m.group(0)), body)
    toks = [(m.start(), m.end(), m.group(0)) for m in re.finditer(r"[^\W\d_]+", masked) if m.group(0) not in ('º', 'ª')]
    S = stream_letters(sp)
    sl = ''.join(lite(c) for c in S)
    rch, rtok = [], []
    for i, (_, _, w) in enumerate(toks):
        for c in w:
            rch.append(lite(c)); rtok.append(i)
    rl = ''.join(rch)
    sm = difflib.SequenceMatcher(None, rl, sl, autojunk=False)
    got = {}
    for op, a1, a2, b1, b2 in sm.get_opcodes():
        if op == 'equal' or (op == 'replace' and a2 - a1 == b2 - b1):
            for k in range(a2 - a1):
                got.setdefault(rtok[a1 + k], []).append(S[b1 + k].lower())
        elif op == 'insert' and a1 > 0 and a1 < len(rtok) and rtok[a1 - 1] == rtok[a1]:   # inside a word only
            got.setdefault(rtok[a1], []).append(''.join(S[b1:b2]).lower())
        elif op == 'replace':
            if rtok[a1] == rtok[a2 - 1]:
                got.setdefault(rtok[a1], []).append(''.join(S[b1:b2]).lower())
    rep, n_cipher = {}, 0
    for i, (_, _, w) in enumerate(toks):
        cand = ''.join(got.get(i, []))
        new = None
        def slip(c, w=w):   # a doubled letter the word does not have (other than ss/ll), or q without u: a cipher slip
            wl = lite(w)
            if any(c[k] == c[k + 1] and (c[k] not in 'sl' or k == len(c) - 2) and c[k:k + 2] not in wl
                   for k in range(len(c) - 1)):
                return True
            return bool(re.search(r'q(?!u)', c))
        if cand and fold(cand, lang) == fold(w, lang) and cand != lite(w) and not slip(cand):
            # keep the reading's ñ where the stream has n
            if 'ñ' in w.lower():
                out = list(cand)
                m2 = difflib.SequenceMatcher(None, w.lower(), cand, autojunk=False)
                for op, x1, x2, y1, y2 in m2.get_opcodes():
                    if op == 'replace' and x2 - x1 == y2 - y1:
                        for k in range(x2 - x1):
                            if w.lower()[x1 + k] == 'ñ' and cand[y1 + k] == 'n':
                                out[y1 + k] = 'ñ'
                cand = ''.join(out)
            if keepform:          # u/v and i/j are letter forms the key does not separate: keep the reading's
                out = list(cand)
                m3 = difflib.SequenceMatcher(None, lite(w), cand, autojunk=False)
                for op, x1, x2, y1, y2 in m3.get_opcodes():
                    if op == 'replace' and x2 - x1 == y2 - y1:
                        for k in range(x2 - x1):
                            if {lite(w)[x1 + k], cand[y1 + k]} in ({'u', 'v'}, {'i', 'j'}):
                                out[y1 + k] = w.lower()[x1 + k]
                cand = ''.join(out)
            if keep:              # --keep-accents: the reading's accented letters stay where the stream has the base letter
                out = list(cand)
                wl = w.lower()
                m4 = difflib.SequenceMatcher(None, ''.join(lite(c) for c in wl), cand, autojunk=False)
                for op, x1, x2, y1, y2 in m4.get_opcodes():
                    if op == 'equal':
                        for k in range(x2 - x1):
                            out[y1 + k] = wl[x1 + k]
                cand = ''.join(out)
            if cand == w.lower():
                cand = None
            new = cand
            n_cipher += 1 if cand else 0
        elif not keep and deacc(w) != w:
            new = deacc(w)
        if new is None and not keep and deacc(w) != w:
            new = deacc(w)
        if new is not None:
            if w[:1].isupper():
                new = new[:1].upper() + new[1:]
            if w.isupper() and len(w) > 1:
                new = new.upper()
            if new != w:
                rep[i] = new
    for i in sorted(rep):
        print(f'  {toks[i][2]} -> {rep[i]}')
    print(f'{rd}: {len(rep)} changed ({n_cipher} respelt from the stream), {len(toks)} words, '
          f'{sum(1 for i in range(len(toks)) if got.get(i))/max(1,len(toks)):.0%} aligned')
    if apply and rep:
        b = body
        for i in sorted(rep, reverse=True):
            x0, x1, _ = toks[i]
            b = b[:x0] + rep[i] + b[x1:]
        p.write_text(t[:s0] + b + t[s1:], encoding='utf8')


if __name__ == '__main__':
    main(sys.argv[1:])
