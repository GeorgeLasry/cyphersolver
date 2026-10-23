"""b28: align haga1620 R2115 cipher spans (R2115_cipher_spans.tsv) with the reading, in order, and count letters.
    python research/reading_audit/b28_haga_align.py"""
import csv, re, pathlib
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'haga1620'
rd = (T / 'R2115_reading.md').read_text(encoding='utf-8')
body = re.search(r'^## Reading\n(.*?)^## ', rd, re.S | re.M).group(1)
body = re.sub(r'\[\?([^\]]*)\]', r' \1 ', body)          # [?word] -> word (partly carried, still a figure word)
words = [w.lower() for w in re.findall(r"[A-Za-z']+", re.sub(r'\[[^\]]*\]', ' ', body))]
rows = list(csv.DictReader(open(T / 'R2115_cipher_spans.tsv', encoding='utf-8'), delimiter='\t'))
pos = 0; n = 0; la = 0; miss = []
for r in rows:
    sp = r['decode'].lower().split()
    n += sum(map(len, sp)); la += len(r['lookalike'] or '')
    for k in range(pos, len(words)):
        if words[k:k + len(sp)] == sp: pos = k + len(sp); break
    else:
        miss.append(r['decode'])
print('spans', len(rows), 'cipher letters', n, 'look-alike letters', la, 'not found in order:', miss)
