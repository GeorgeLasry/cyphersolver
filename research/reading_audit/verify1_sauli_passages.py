"""verify1 (sauli1579): list the cipher passages ({...}) of each R19x reading, numbered, for the word-by-word check.
    python research/reading_audit/verify1_sauli_passages.py R190 [R191 ...]"""
import pathlib, re, sys
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'sauli1579' / 'texts'
for doc in sys.argv[1:]:
    s = (T / f'{doc}_reading.md').read_text(encoding='utf8')
    s = re.sub(r'<!--.*?-->', '', s, flags=re.S)
    print('==', doc)
    for i, m in enumerate(re.finditer(r'\{([^}]*)\}', s), 1):
        pre = s[max(0, m.start() - 40):m.start()].replace('\n', ' ')
        print(f'{i:3d} ...{pre[-40:]}| {{{" ".join(m.group(1).split())}}}')
