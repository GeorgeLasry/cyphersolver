"""v2 verify sweep (23 Oct 2026): score a reading body with every conjectural or supplied word counted as a hole.

    python v2_score.py <file> [lang]       file: a reading (body after '## Reading', else the whole file)

Before scoring, every bracket that marks a conjecture or a supplied word becomes one explicit hole per word it holds:
[word?] [?word] [x?] [word] (lower-case, i.e. not a resolved code such as [SUA MAESTA]) and part-words like
[ne]glect. Prints the plain score (_check_reading word list) and the explicit-hole score (b17 HOLES=1).
"""
import os, re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'docs')); sys.path.insert(0, str(ROOT))
import _check_reading as cr


def body_of(t):
    m = re.search(r'^## Reading[^\n]*\n(.*?)(?=^## |\Z)', t, re.S | re.M)
    return m.group(1) if m else t


def holes(t):
    def rep(m):
        inner = m.group(1)
        if re.fullmatch(r'[\s\d.?…*+-]*', inner) or len(inner.strip()) <= 2:   # [Π] [R] [#]: one unread sign
            return '[?]'
        if '?' in inner or inner == inner.lower():
            n = max(1, len(re.findall(r'[^\W\d_]+', inner)))
            return ' '.join(['[?]'] * n)
        return m.group(0)
    t = re.sub(r'\[(?:l|ll|f|ff|fol|p|pp|c|line|page)\.?\s*[\divxlcrv,\s–-]+\]', ' ', t, flags=re.I)   # [l. 12] [f. 79v]: markers
    t = re.sub(r'\{([^}\n]*\?[^}\n]*|[\s.…]*)\}',lambda m: rep(re.match(r'(.*)', m.group(1))), t)   # {?} {?word} {…}: unread
    t = re.sub(r'\[([^\]\n]*)\]', rep, t)
    t = re.sub(r'(\w*)\[\?\](\w*)', lambda m: '[?]' if (m.group(1) or m.group(2)) else m.group(0), t)
    return t


def score(text, lang, all_known):
    saved = cr._LEX.get(lang)
    if all_known:
        class _All(dict):
            def __contains__(self, k): return True
        cr._LEX[lang] = _All()
    try:
        return cr.score_text(text, lang)
    finally:
        if all_known:
            if saved is None: cr._LEX.pop(lang, None)
            else: cr._LEX[lang] = saved


if __name__ == '__main__':
    f, lang = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else 'en')
    b = holes(body_of(pathlib.Path(f).read_text(encoding='utf8')))
    if os.environ.get('SHOW'): print(b)
    cr.lexicon(lang)
    p, h = score(b, lang, False), score(b, lang, True)
    print(f'{f}: plain {p["clean_share"]} ({p["clean"]}/{p["sentences"]}), explicit holes {h["clean_share"]} '
          f'({h["clean"]}/{h["sentences"]}), hole rate {h["hole_rate"]}, words {h["words"]}')
