"""b16 (wotton1585): align a modernised reading word by word with its diplomatic transcription and list every reading
word the transcription does not carry. Struck words (~~...~~) are dropped from the transcription first (the reading
follows the last state of the draft); interlined ^{...} words are kept. Spelling is compared loosely (u/v, i/j/y,
doubled letters, final e, -eth/-s, vowels) because the reading modernises. Supplied [word], doubtful [?word], [..],
{code = gloss} and header lines (#) are skipped. Usage: b16_wotton_align.py READING TRANSCRIPTION"""
import re, sys, difflib


def key(w):
    w = w.lower().replace('v', 'u').replace('j', 'i').replace('y', 'i').replace('ph', 'f')
    w = re.sub(r'(.)\1+', r'\1', w)
    w = re.sub(r'(eth|es|s|e|ed|d)$', '', w)
    c = re.sub(r'[aeiou]', '', w)
    return c or w


ABBR = {'h': 'honour', 'm': 'maiesti', 'mty': 'maiesti', 'k': 'king', 'll': 'lords', 'l': 'lord', 'fr': 'france',
        'wch': 'which', 'w': 'which', 'mr': 'master', 'pre': 'prior', 'p': 'prior', 'cou': 'court', 'hou': 'house',
        'joh': 'iohnstone', 'b': 'blantire', 'la': 'laird', 'art': 'article', 'post': 'postscript'}
NUM = {'six': '6000', 'thousand': '6000', 'five': '500', 'hundred': '100', 'three': '3', 'four': '4'}


def trans_words(path):
    t = open(path, encoding='utf8').read()
    t = '\n'.join(l.split(' ', 1)[1] if re.match(r'p\d\.\d+ ', l) else '' for l in t.splitlines())
    t = re.sub(r'~~.*?~~', ' ', t)
    t = re.sub(r'\[(?:folio|right|centre|margin)[^\]]*\]', ' ', t)
    out = []
    for w in re.findall(r"[A-Za-z]+|\d+", t.replace('w.ch', 'wch').replace('M.ty', 'Mty')):
        out.append(ABBR.get(w.lower(), w))
    return out


def reading_words(path):
    t = '\n'.join(l for l in open(path, encoding='utf8').read().splitlines() if not l.startswith('#'))
    toks = []
    for m in re.finditer(r"\{[^}]*\}|\[[^\]]*\]|[A-Za-z]+(?:'s)?", t):
        s = m.group(0)
        if s.startswith('{'):
            num = re.match(r'\{(\d+)', s)
            toks.append(('code', num.group(1) if num else s))
        elif s.startswith('['):
            toks.append(('skip', s))
        else:
            toks.append(('word', s[:-2] if s.endswith("'s") else s))
    return toks


def main(rp, tp):
    tw = trans_words(tp)
    tk = [key(w) for w in tw]
    toks = reading_words(rp)
    rk = []
    for kind, w in toks:
        if kind == 'word':
            rk.append(key(NUM.get(w.lower(), w)))
        elif kind == 'code':
            rk.append(key(w))
        else:
            rk.append(None)
    seq = [k for k in rk if k is not None]
    idx = [i for i, k in enumerate(rk) if k is not None]
    sm = difflib.SequenceMatcher(None, seq, tk, autojunk=False)
    carried = set()
    for a, b, n in sm.get_matching_blocks():
        for j in range(n):
            carried.add(idx[a + j])
    # second chance: a word anywhere in the transcription within a short window counts (draft insertions move words)
    tset = set(tk)
    loose = []
    unc = []
    for i, (kind, w) in enumerate(toks):
        if rk[i] is None or i in carried:
            continue
        if rk[i] in tset:
            loose.append(w)
        else:
            unc.append(w)
    words = sum(1 for k, _ in toks if k in ('word', 'code'))
    print(f'{rp}: {words} words/codes; carried in order {len(carried)}; carried out of order {len(loose)}; '
          f'not carried {len(unc)}')
    if loose:
        print('  out of order (interlineations):', ' '.join(loose))
    if unc:
        print('  NOT CARRIED:', ' '.join(unc))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
