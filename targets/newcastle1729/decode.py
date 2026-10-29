"""Apply codetable.tsv to the report (transcription/report_61005_tokens.txt).

Writes two files in decryption/:
  report_61005_decode.txt  per manuscript line, the groups with the table value under each ("?" after a value =
                           grade M, [n] = group not in the table, _ = a null or stop group);
  report_61005_raw.txt     the same values run together as a word stream, one manuscript line per line, with
                           [n] for an open group and [?value] for a grade M value. reading.py checks the
                           hand-made reading (report_61005_reading.txt) against this stream.
and prints the coverage: groups with a firm value, with a doubtful one, and open.

    python decode.py
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_table():
    table = {}
    for line in open(os.path.join(HERE, 'codetable.tsv'), encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        group, value, grade = line.rstrip('\n').split('\t')[:3]
        table[group] = (value, grade)
    return table


def report_lines():
    for line in open(os.path.join(HERE, 'transcription', 'report_61005_tokens.txt'), encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        label, *groups = line.split()
        yield label, groups


def raw_stream(table):
    """Yield (label, [(group, token)]) where token is the value, '[?value]' for grade M, '[n]' for an open group."""
    for label, groups in report_lines():
        toks = []
        for g in groups:
            if g not in table:
                toks.append((g, f'[{g}]'))
            else:
                v, grade = table[g]
                toks.append((g, v if grade == 'H' else f'[?{v}]'))
        yield label, toks


def main():
    table = load_table()
    out, raw = [], []
    firm = doubt = opened = nulls = 0
    for label, toks in raw_stream(table):
        cells = []
        for g, t in toks:
            if g not in table:
                opened += 1
                cells.append((g, t))
            else:
                v, grade = table[g]
                if v == '_':
                    nulls += 1
                elif grade == 'H':
                    firm += 1
                else:
                    doubt += 1
                cells.append((g, v + ('' if grade == 'H' else '?')))
        widths = [max(len(g), len(v)) for g, v in cells]
        out.append(label + '  ' + ' '.join(g.ljust(w) for (g, _), w in zip(cells, widths)))
        out.append(' ' * len(label) + '  ' + ' '.join(v.ljust(w) for (_, v), w in zip(cells, widths)))
        raw.append(label + ' ' + ' '.join(t for g, t in toks if g not in table or table[g][0] != '_'))
    total = firm + doubt + opened + nulls
    summary = (f'report groups: {total}; firm value {firm}, doubtful value (grade M) {doubt}, '
               f'null/stop group {nulls}, open {opened}; with any value {firm + doubt + nulls} '
               f'({(firm + doubt + nulls) / total:.1%})')
    os.makedirs(os.path.join(HERE, 'decryption'), exist_ok=True)
    open(os.path.join(HERE, 'decryption', 'report_61005_decode.txt'), 'w', encoding='utf-8').write(
        '# Report (mssBLA 191 p. 5) decoded group by group with codetable.tsv (decode.py).\n'
        '# Under each group: its table value; "?" after a value = grade M; [n] = group not in the table.\n'
        + '\n'.join(out) + '\n\n' + summary + '\n')
    open(os.path.join(HERE, 'decryption', 'report_61005_raw.txt'), 'w', encoding='utf-8').write(
        '# Raw word stream of the report, one manuscript line per line (decode.py). [n] = open group,\n'
        '# [?value] = grade M value, null/stop groups left out; syllables are not yet joined into words.\n'
        + '\n'.join(raw) + '\n')
    print(summary)


if __name__ == '__main__':
    main()
