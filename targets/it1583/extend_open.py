"""Escalation pass on the unresolved sign classes of Lasry's 1446 key (lasry2026/ctts/key.txt).

For every class still '?' (and the provisional l / n / in), try each single-letter value, each word value of the key
(che con per qva se et in) and 'null', with every other token kept at its CTTS value, and score the whole text of
both letters with the lang/ it-cinquecento model (spaces dropped; unread tokens split the text). Prints, per class,
its occurrences, the best values and their margin over the next. A value is only a candidate: one-sign classes that
occur once or twice cannot be fixed this way.

    python targets/it1583/extend_open.py
"""
import json, pathlib, sys, collections
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from lang import lm

ED = json.loads((HERE / 'lasry2026/edition.json').read_text(encoding='utf-8'))
M = lm.load('it-cinquecento', order=4, spaces=False)

seq = []   # (label, value) per cipher token, None between rows and at clear boxes
for doc in ED['documents']:
    for row in doc['rows']:
        for b in row['boxes']:
            if b['label'] == '[Plaintext]': seq.append(None); continue
            seq.append((b['label'], b['value']))
        seq.append(None)

def score(key):
    tot = n = 0; cur = ''
    def flush(s):
        nonlocal tot, n
        x = M.encode(lm.norm(s, 'early', spaces=False))
        if len(x) >= 4: tot += M.score_idx(x); n += len(x) - 3
    for t in seq + [None]:
        if t is None or key.get(t[0], t[1]) == '?':
            if cur: flush(cur)
            cur = ''; continue
        v = key.get(t[0], t[1]); cur += '' if v == '-' else v
    return tot / n if n else -9, tot

base = {}
counts = collections.Counter(t[0] for t in seq if t)
openc = sorted({t[0] for t in seq if t and (t[1] == '?' or t[1] in ('l', 'n', 'in') and t[0] in ('(8)', '(24)', '(16)'))},
               key=lambda l: -counts[l])
cands = list('abcdefghilmnopqrstvz') + ['che', 'con', 'per', 'qva', 'se', 'et', 'in', '-']
_, b0 = score(base)
print(f'baseline total log-prob {b0:.1f}')
for lab in openc:
    res = sorted(((score({lab: v})[1], v) for v in cands), reverse=True)
    best, nxt = res[0], res[1]
    cur = next(t[1] for t in seq if t and t[0] == lab)
    print(f'{lab:6} x{counts[lab]:<3} now {cur:4} best {best[1]:4} ({best[0]-b0:+.1f})  next {nxt[1]:4} ({nxt[0]-b0:+.1f})  margin {best[0]-nxt[0]:.1f}')
