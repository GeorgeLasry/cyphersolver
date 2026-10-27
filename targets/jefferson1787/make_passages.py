"""Build passages.tsv for segment.py from transcription/*.tsv.

A passage is a run of consecutive code groups in one letter (a row with code '=' marks clear words and breaks
the run). Its plaintext is rebuilt from the 'plain' column: a value wholly in parentheses continues the word of
the previous group; 'word [k/n]' spreads one word over n groups; 're(turn)' and '(re)turn' both give 'return'.
Single groups that carry their own interlinear decoding, with the next group carrying another one, are also
written as 'pair' rows (TJ's decoding of that one group).
Groups read with '?' are kept as written; segment.py treats them as distinct unknown codes.
"""
import csv, glob, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
FRAC = re.compile(r'\s*[\[(](\d+)/(\d+)[\])]?\s*$')


def plain_of(rows):
    words = []
    last = None
    for r in rows:
        p = (r.get('plain') or '').strip()
        if not p:
            continue
        m = FRAC.search(p)
        if m:
            if m.group(1) != '1':
                continue
            p = FRAC.sub('', p)
        if re.fullmatch(r'\(.*\)\??', p):
            continue  # continuation of the previous word
        p = p.replace('(', '').replace(')', '').strip('[]{} ')
        if p.lower().startswith('quoted') or p.lower().startswith('not in') or 'struck' in p:
            return None
        if p == last:
            continue
        words.append(p)
        last = p
    return ' '.join(words)


def main():
    out = []
    for path in sorted(glob.glob(os.path.join(HERE, 'transcription', '*.tsv'))):
        name = os.path.basename(path)[:-4]
        rows = list(csv.DictReader(open(path, encoding='utf-8'), delimiter='\t'))
        runs, cur = [], []
        for r in rows:
            c = (r.get('code') or '').strip()
            if not c or c == '=':
                if cur:
                    runs.append(cur)
                cur = []
                continue
            cur.append(r)
        if cur:
            runs.append(cur)
        for k, run in enumerate(runs, 1):
            groups = [re.sub(r'[^0-9?]', '', r['code']) or r['code'] for r in run]
            pl = plain_of(run)
            if pl:
                out.append((f'{name}#{k}', 'aligned', ' '.join(groups), pl))
            for i, r in enumerate(run):
                il = (r.get('interlinear') or '').strip()
                nxt = (run[i + 1].get('interlinear') or '').strip() if i + 1 < len(run) else 'END'
                if il and nxt and ' ' not in il and '?' not in il:
                    out.append((f'{name}#{k}.{i + 1}', 'pair', groups[i], il))
    with open(os.path.join(HERE, 'passages.tsv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['id', 'source', 'groups', 'plain'])
        w.writerows(out)
    print(len(out), 'rows ->', os.path.join(HERE, 'passages.tsv'))


if __name__ == '__main__':
    main()
