"""b04: align each Spagna 423 reading word by word with its decode (texts/423-<n>_decode_b04.txt running decode).
Every unbracketed word of the reading must be found, in order, in the decode stream; words not found are listed
(they would be supplied words that need brackets). Usage: python b04_align.py <n> [...]"""
import re, sys, os, unicodedata
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'targets', 'nunzio1736', 'texts')
def norm(s):
    s = unicodedata.normalize('NFD', s); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = s.lower().replace('v', 'u').replace('j', 'i')
    return re.sub(r'[^a-z]', '', s)
def stream(n):
    t = open(os.path.join(T, '423-%d_decode_b04.txt' % n), encoding='utf8').read()
    t = t.split('Running decode:')[1].replace('\n', '')
    t = re.sub(r'\[\?[^\]]*\]', '#', t)          # probable values: bracketed in the reading too
    t = re.sub(r'\{(1\d{3})\}', '#', t)            # open groups
    t = re.sub(r'\{([^}]*)\}', r'\1', t)
    t = re.sub(r'<[^>]*>', '#', t)
    t = t.replace('(che)', 'che')
    return ''.join(c if c == '#' else norm(c) for c in t)
def body(n):
    t = open(os.path.join(T, '423-%d_reading.md' % n), encoding='utf8').read()
    lines = t.split('\n'); out = []; on = False
    for l in lines:
        if l.startswith('## '): break
        if not on:
            if l.strip() == '' and any(x.startswith('Marks') or x.startswith('[..]') for x in out[-3:] if True) : pass
        out.append(l)
    # body = text after the first blank line following the "Marks" paragraph
    i = max(k for k, l in enumerate(out) if l.startswith('Marks') or l.startswith('[..] = '))
    while out[i].strip(): i += 1
    return ' '.join(out[i:])
def check(n, verbose=True):
    import difflib
    s = stream(n); b = body(n)
    b = re.sub(r'\[[^\]]*\]', ' ', b)               # drop bracketed material
    words = [w for w in re.split(r"[\s,;:.…'’]+", b) if norm(w)]
    r = ''; spans = []
    for w in words:
        a = len(r); r += norm(w); spans.append((w, a, len(r)))
    sm = difflib.SequenceMatcher(None, r, s, autojunk=False)
    hit = [False] * len(r)
    for blk in sm.get_matching_blocks():
        if blk.size >= 3:
            for k in range(blk.a, blk.a + blk.size): hit[k] = True
    bad = []
    for w, a, e in spans:
        h = sum(hit[a:e]); L = e - a
        # a nomenclator stem may lack the last one or two letters of the word
        if L - h > (2 if L >= 4 else 0):
            k = [x[0] for x in spans].index(w) if False else spans.index((w, a, e))
            bad.append((' '.join(x[0] for x in spans[max(0, k - 3):k]) + ' [' + w + '] ' + ' '.join(x[0] for x in spans[k + 1:k + 4]), h, L))
    print('423/%d: %d words; %d with letters not carried by the decode' % (n, len(words), len(bad)))
    if verbose:
        for w, h, L in bad: print('   %-16s %d/%d letters carried' % (w, h, L))
    return bad
if __name__ == '__main__':
    for a in sys.argv[1:]: check(int(a))
