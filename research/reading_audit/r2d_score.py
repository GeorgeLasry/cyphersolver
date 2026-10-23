"""r2d (23 Oct 2026): v2 score of a Spagna 423 or Morosini reading body (header paragraph and '## ' sections cut,
abbreviations V.S. N.S. S. Mons. Sig. Card. Ecc. de-dotted so they do not cut sentences).

    python research/reading_audit/r2d_score.py <reading.md> [lang]     SHOW=1 prints the body scored
"""
import os, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'docs')); sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / 'research' / 'reading_audit'))
import _check_reading as cr
from v2_score import holes, score


def body(path):
    s = pathlib.Path(path).read_text(encoding='utf8')
    m = re.search(r'^## Reading[^\n]*\n(.*?)(?=^## |\Z)', s, re.S | re.M)
    if m:
        s = m.group(1)
    else:
        s = s.split('\n## ')[0]
        ls = s.split('\n')
        ks = [k for k, l in enumerate(ls) if l.startswith('Marks') or l.startswith('[..] = ')]
        if ks:
            i = max(ks)
            while i < len(ls) and ls[i].strip():
                i += 1
            s = '\n'.join(ls[i:])
    s = re.sub(r'\b(V|N|S|Ecc|Mons|Sig|Card|Ill|Rev|Em|Mgr|Sr|Sra|D|Dn|Ma|Md|Mag|Ex|Exa|Va|Su|Vra|V\.?M|S\.?M)\.\s*(?=\S)', r'\1 ', s)
    return s


if __name__ == '__main__':
    f, lang = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else 'it')
    b = holes(body(f))
    if os.environ.get('SHOW'): print(b)
    cr.lexicon(lang)
    p, h = score(b, lang, False), score(b, lang, True)
    print(f'{f}: plain {p["clean_share"]} ({p["clean"]}/{p["sentences"]}), explicit holes {h["clean_share"]} '
          f'({h["clean"]}/{h["sentences"]}), hole rate {h["hole_rate"]}, words {h["words"]}')
