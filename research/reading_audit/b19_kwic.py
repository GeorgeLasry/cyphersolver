"""b19 (deswart1782): keyword-in-context for one or more codes in R1040 part 2 and R1036 token files.
    python research/reading_audit/b19_kwic.py <code> [<code> ...]   (env W=window, default 6)"""
import csv, os, pathlib, sys
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'deswart1782'
W = int(os.environ.get('W', 6))
for f in ('R1040_second_key_tokens.tsv', 'R1036_tokens.tsv'):
    r = list(csv.DictReader(open(T / f, encoding='utf8'), delimiter='\t'))
    v = [(x['plaintext'] or '[' + x['code'] + ']').replace(' ', '_') for x in r]
    for code in sys.argv[1:]:
        for i, x in enumerate(r):
            if x['code'] == code:
                print(f[:5], code, i + 1, ' '.join(v[max(0, i - W):i]), '<<', v[i], '>>', ' '.join(v[i + 1:i + W + 1]))
