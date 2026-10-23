"""r2k: v2_score with unvalued signs <V> <4#> and unvalued bracketed sign labels [XX] [oo] also counted as holes.

    python r2k_score.py <file> [lang]
"""
import re, sys, pathlib, os
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import v2_score as v
import _check_reading as cr


def strict(t):
    t = re.sub(r'<[^<>\n]{1,6}>', '[?]', t)            # <V> <K> <4#> <e>: unvalued sign
    t = re.sub(r'\[(XX|oo|OO|[A-Z]{1,2}|[A-Z]#)\]', '[?]', t)   # [XX] sign labels
    return t


if __name__ == '__main__':
    f, lang = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else 'de')
    b = strict(v.holes(v.body_of(pathlib.Path(f).read_text(encoding='utf8'))))
    b = v.holes(b)
    if os.environ.get('SHOW'): print(b)
    cr.lexicon(lang)
    p, h = v.score(b, lang, False), v.score(b, lang, True)
    print(f'{f}: strict plain {p["clean_share"]} ({p["clean"]}/{p["sentences"]}), explicit holes {h["clean_share"]} '
          f'({h["clean"]}/{h["sentences"]}), hole rate {h["hole_rate"]}, words {h["words"]}')
