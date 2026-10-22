"""Turn Brett Burford's per-page data (burford/<page>/signs.txt + key.json, v0.5, CC BY 4.0) into the line format of
../f276/scripts/measure.py, so his reading of fr. 15573 ff. 379r-381v is measured with the same rule as f. 276 / f. 179.

Each sign takes its key value; a two-valued sign takes the value his word decoder recorded at that occurrence
("choices", in reading order over the page), exactly as his decode/decode.py does. A single letter stays a letter, a
multi-letter value (a code or word sign: 20 = la, le_roy_de_navarre ...) becomes a word token '=value', and a sign with
no value becomes '?'. Written to read_<page>.txt and read_all.txt.

    python to_read.py
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = ['f379r', 'f379v', 'f380r', 'f380v', 'f381r', 'f381v']


def page_lines(page):
    d = os.path.join(HERE, 'burford', page)
    step = json.load(open(os.path.join(d, 'key.json'), encoding='utf-8'))['pipeline'][0]
    table, choices = step['table'], step.get('choices', {})
    used = {}
    out = []
    for raw in open(os.path.join(d, 'signs.txt'), encoding='utf-8'):
        if not raw.strip() or raw.startswith('#'):
            continue
        num, _, signs = raw.rstrip('\n').partition('\t')
        toks = []
        for s in signs.split():
            v = (table.get(s) or {}).get('v')
            if isinstance(v, list):
                k = used.get(s, 0); used[s] = k + 1
                lst = choices.get(s, [])
                v = lst[k] if k < len(lst) else None
            if not v:
                toks.append('?')
            elif len(v) == 1:
                toks.append(v)
            else:
                toks.append('=' + v.replace('_', ''))
        out.append((int(num), toks))
    return out


def main():
    allrows = []
    for p in PAGES:
        rows = page_lines(p)
        with open(os.path.join(HERE, f'read_{p}.txt'), 'w', encoding='utf-8') as f:
            f.write(f'# fr. 15573 {p[1:]}: Burford v0.5 signs through his key and recorded choices (to_read.py)\n')
            for n, toks in rows:
                f.write(f'L{n:02d}: ' + ' '.join(toks) + '\n')
        allrows += [(p, n, t) for n, t in rows]
        print(p, len(rows), 'lines', sum(len(t) for _, t in rows), 'signs')
    with open(os.path.join(HERE, 'read_all.txt'), 'w', encoding='utf-8') as f:
        f.write('# fr. 15573 ff. 379r-381v, all six pages in order (line numbers run on)\n')
        for i, (p, n, toks) in enumerate(allrows, 1):
            f.write(f'L{i:02d}: ' + ' '.join(toks) + '\n')
    print('all', len(allrows), 'lines', sum(len(t) for _, _, t in allrows), 'signs')


if __name__ == '__main__':
    main()
