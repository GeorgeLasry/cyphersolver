"""verify2 (alessandrino1568): align a reading with the figures of all its cipher pages at once (R101 runs over
291r and 291v), reusing targets/alessandrino1568/reread_aless_align.py, and print the words the figures do not carry.
Each listed word is then looked up by hand in the contemporary decipherment (texts/R*_decifrato_*.txt).

    python research/reading_audit/verify2_aless_align.py <transcription> <reading.md> <image> [<image> ...]
"""
import importlib.util
import pathlib
import sys

T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'alessandrino1568'
spec = importlib.util.spec_from_file_location('ra', T / 'reread_aless_align.py')
ra = importlib.util.module_from_spec(spec)
sys.argv_saved = sys.argv
spec.loader.exec_module(ra)


def main(tr, rd, *imgs):
    pages = dict(ra.parse(str(T / tr)))
    items = []
    for im in imgs:
        items += pages[im]
    text = (T / rd).read_text(encoding='utf-8').split('## Reading', 1)[1].split('\n## ', 1)[0]
    words = ra.words_of(text)
    c, path, tgt = ra.align(items, words)
    lines, bad, _ = ra.show(items, words, path, tgt)
    print('\n'.join(l for l in lines if l.startswith('!!') or ALL))
    print('# cost %.1f; %d words, %d disagree' % (c, len(words), len(bad)))


ALL = '-a' in sys.argv
if __name__ == '__main__':
    main(*[a for a in sys.argv[1:] if a != '-a'])
