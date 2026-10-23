"""b06: align a kurtz1639 reading word by word with its decode (batch b06, REREAD_BRIEF step 3).

    python research/reading_audit/b06_align.py R3815 [...]
The stream is read/<rec>.txt (clear text in braces and deciphered runs in brackets, as decode.py writes it).
The reading body is read/<rec>_reading.md after the title line and before '## Notes'. With --para each paragraph is aligned on its own (for a reading whose pages follow the letter, not the image order).
Bracketed material
([word], [?word], [...]) is dropped; every remaining word must be found, in order, in the stream (character alignment);
words with letters the stream does not carry are listed: they need brackets or a transcription fix.
"""
import difflib, os, re, sys, unicodedata
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'targets', 'kurtz1639', 'read')


def norm(s):
    s = s.replace('ß', 'ss').replace('ẞ', 'ss')
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn').lower()
    s = s.replace('v', 'u').replace('j', 'i').replace('y', 'i')
    return re.sub(r'[^a-z]', '', s)


ORDER = {'R4645': ['P9', 'P1', 'P2', 'P6', 'P3', 'P4', 'P5', 'P7', 'P8']}   # letter order where it differs from file order


def sections(rec):
    secs, cur = [], None
    for l in open(os.path.join(T, rec + '.txt'), encoding='utf-8'):
        if l.startswith('### '):
            cur = [l.strip()[4:], []]; secs.append(cur); continue
        if cur is None: cur = ['', []]; secs.append(cur)
        cur[1].append(l)
    if rec in ORDER:
        rank = {k: i for i, k in enumerate(ORDER[rec])}
        secs.sort(key=lambda c: rank.get(c[0].rsplit('_', 1)[-1], 99))
    return [l for _, ls in secs for l in ls]


def stream(rec):
    out = []
    for l in sections(rec):
        if l.startswith('#'): continue
        l = re.sub(r'\{[^{}]*\[[^\]]*\][^{}]*\}', ' ', l)   # editorial notes such as {[blank]}, {... [not transcribed] ...}
        l = l.replace('...', '#').replace('…', '#').replace('?', '#')
        out.append(l)
    t = ''.join(out)
    t = re.sub(r'[\[\]{}]', '', t)
    return ''.join(c if c == '#' else norm(c) for c in t)


def body(rec):
    t = open(os.path.join(T, rec + '_reading.md'), encoding='utf-8').read()
    t = re.sub(r'<!--.*?-->', ' ', t, flags=re.S)
    t = t.split('\n## ')[0]
    lines = t.split('\n')
    i = next(k for k, l in enumerate(lines) if l.startswith('# '))
    return '\n'.join(lines[i + 1:])


def check(rec, verbose=True, para=False):
    if para:   # pages bound out of order: align each paragraph on its own against the whole stream
        bad = []
        for k, pb in enumerate(x for x in re.split(r'\n\s*\n', body(rec)) if x.strip()):
            bad += check_text(rec, pb, False)
        print('%s (per paragraph): %d with letters not carried by the decode' % (rec, len(bad)))
        if verbose:
            for c, h, L in bad: print('   %d/%d  %s' % (h, L, c))
        return bad
    return check_text(rec, body(rec), verbose, True)


def check_text(rec, text, verbose=True, report=False):
    s = stream(rec)
    b = re.sub(r'\[[^\]]*\]', ' ', text)
    words = [w for w in re.split(r"[\s,;:.!?()\"'’–-]+", b) if norm(w)]
    r, spans = '', []
    for w in words:
        a = len(r); r += norm(w); spans.append((w, a, len(r)))
    sm = difflib.SequenceMatcher(None, r, s, autojunk=False)
    hit = [False] * len(r)
    for blk in sm.get_matching_blocks():
        if blk.size >= 3:
            for k in range(blk.a, blk.a + blk.size): hit[k] = True
    bad = []
    for k, (w, a, e) in enumerate(spans):
        h = sum(hit[a:e]); L = e - a
        if L - h > (1 if L >= 6 else 0):
            ctx = ' '.join(x[0] for x in spans[max(0, k - 3):k]) + ' <' + w + '> ' + ' '.join(x[0] for x in spans[k + 1:k + 4])
            bad.append((ctx, h, L))
    if report: print('%s: %d words; %d with letters not carried by the decode' % (rec, len(words), len(bad)))
    if verbose:
        for c, h, L in bad: print('   %d/%d  %s' % (h, L, c))
    return bad


if __name__ == '__main__':
    para = '--para' in sys.argv
    for a in sys.argv[1:]:
        if not a.startswith('--'): check(a, para=para)
