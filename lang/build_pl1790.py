"""Build the late-18th-century Polish corpus for the pl-1790 model.

Polish letters of the 1780s-90s spell j as i before a vowel at the start of a word or between vowels (iest, iuż,
moie), and as y after a vowel before a consonant or at the end of a word, and after a consonant (wczoray, tey,
Rossya, negocyacya). No sizeable corpus of the period is at hand, so the 19th-century Gutenberg texts of pl-modern are
respelled by those rules, and the clear despatches of Deboli transcribed for target deboli1789 (ZbPop 419) are added
three times over as in-period text. Output: lang/corpora/pl-1790.txt.  Run: python -m lang.build_pl1790
"""
import glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, 'corpora', 'pl-1790.txt')
V = 'aąeęioóuy'


def respell(t):
    t = re.sub(rf'\bj(?=[{V}])', 'i', t)
    t = re.sub(rf'\bJ(?=[{V}])', 'I', t)
    t = re.sub(rf'(?<=[{V}])j(?=[{V}])', 'i', t)
    t = re.sub(r'j', 'y', t)
    return t.replace('J', 'Y')


def main():
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)
    from lang import corpora
    base = respell(corpora.text(['pl-gutenberg']))
    clear = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'targets', 'deboli1789', 'clear', '*.txt'))):
        lines = [l for l in open(f, encoding='utf-8') if not l.startswith('#')]
        clear.append(re.sub(r'\[struck:[^\]]*\]|\[\?\]', ' ', ''.join(lines)))
    text = base + '\n' + '\n'.join(clear) * 3
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write(text)
    print(OUT, len(base), 'chars respelled +', len(clear), 'clear despatches')


if __name__ == '__main__':
    main()
