"""v3 verify (b): cut the running text of one document out of a reading file and score it with v2_score.

    python research/reading_audit/v3b_body.py <file> <lang> [--start REGEX] [--end REGEX] [--keep-markers] [--show]

The body runs from the first line matching --start (exclusive; default '## Reading') to the first line matching --end
(exclusive; default the next '## ' heading or 'Files:' line). Line/folio markers such as [l. 12], [f. 173v], [p. 3],
[fol. 2], [L12] and the stop code written as [44] by matignon1586 are removed before scoring unless --keep-markers
(v2_score would count each as a hole). The cut body is written to the v3 scratch folder and scored there.
"""
import argparse, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
SCR = pathlib.Path(r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\v5\b')

MARK = re.compile(r'\[(?:l|ll|line|f|fol|p|pp|L|ln)\.?\s*[\dIVXivx]+[rv]?(?:[-â€“]\d+)?\]', re.I)


def cut(text, start, end):
    lines = text.splitlines()
    i0 = 0
    if start:
        for i, l in enumerate(lines):
            if re.search(start, l):
                i0 = i + 1; break
        else:
            sys.exit(f'no start {start!r}')
    out = []
    for l in lines[i0:]:
        if end and re.search(end, l):
            break
        out.append(l)
    return '\n'.join(out)


def main():
    a = argparse.ArgumentParser()
    a.add_argument('file'); a.add_argument('lang')
    a.add_argument('--start', default=r'^## Reading'); a.add_argument('--end', default=r'^(## |Files:)')
    a.add_argument('--keep-markers', action='store_true'); a.add_argument('--stop', default=None,
                   help='a stop-code number written in brackets, removed (e.g. 44)')
    a.add_argument('--out', default=None); a.add_argument('--show', action='store_true')
    o = a.parse_args()
    t = pathlib.Path(o.file).read_text(encoding='utf8')
    b = cut(t, o.start, o.end)
    if not o.keep_markers:
        b = MARK.sub(' ', b)
    b = re.sub(r'(?m)^#+ .*$', '', b)   # inner headings would end v2_score's body
    if o.stop:
        b = b.replace(f'[{o.stop}]', ' ')
    SCR.mkdir(parents=True, exist_ok=True)
    out = SCR / (o.out or (pathlib.Path(o.file).stem + '_body.md'))
    out.write_text('## Reading\n' + b + '\n', encoding='utf8')
    if o.show:
        print(b)
    r = subprocess.run([sys.executable, str(HERE / 'v2_score.py'), str(out), o.lang], capture_output=True, text=True,
                       encoding='utf8')
    print(r.stdout.strip() or r.stderr[-2000:])


if __name__ == '__main__':
    main()
