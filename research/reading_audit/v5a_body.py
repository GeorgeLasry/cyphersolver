"""v5a (23 Oct 2026): cut a reading body, score it with v2_score (plain and explicit-hole) and, with --holes, list the
words the plain word list does not know, per failing sentence (to judge names/abbreviations vs real holes).

    python research/reading_audit/v5a_body.py <file> <lang> [--start RE] [--end RE] [--lines] [--holes] [--show]

--start: first line matching is excluded and the body follows (default '## Reading' if present, else whole file);
--end: stop at the first line matching (default '^(## |Files:)'). --lines: line-numbered reading (v3b_lines rules).
Markdown headings, HTML comments and folio/line markers are cut. Body written to scratchpad reread/v5/.
"""
import argparse, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'docs')); sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(HERE))
import _check_reading as cr
import v2_score as v2
SCR = pathlib.Path(r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\v5')
MARK = re.compile(r'\[(?:l|ll|line|f|fol|p|pp|L|ln)\.?\s*[\dIVXivx]+[rv]?(?:[-–]\d+[rv]?)?\]', re.I)


def cut(text, start, end):
    lines = text.splitlines(); i0 = 0
    if start is None and any(re.match(r'^## Reading', l) for l in lines): start = r'^## Reading'
    if start:
        for i, l in enumerate(lines):
            if re.search(start, l): i0 = i + 1; break
        else: sys.exit(f'no start {start!r}')
    out = []
    for l in lines[i0:]:
        if end and re.search(end, l): break
        out.append(l)
    return '\n'.join(out)


def main():
    a = argparse.ArgumentParser()
    a.add_argument('file'); a.add_argument('lang')
    a.add_argument('--start', default=None); a.add_argument('--end', default=r'^(## |Files:)')
    a.add_argument('--lines', action='store_true'); a.add_argument('--holes', action='store_true')
    a.add_argument('--show', action='store_true'); a.add_argument('--out', default=None)
    o = a.parse_args()
    t = pathlib.Path(o.file).read_text(encoding='utf8')
    t = re.sub(r'<!--.*?-->', ' ', t, flags=re.S)
    b = cut(t, o.start, o.end)
    b = MARK.sub(' ', b)
    b = re.sub(r'(?m)^#+ .*$', '', b)
    if o.lines:
        s = ''
        for l in b.splitlines():
            if l.startswith('==') or not l.strip(): continue
            l = re.sub(r'^\s*\d+[a-z]?\s+', '', l).strip()
            s = s[:-1] + l.lstrip('-') if s.endswith('-') else (s + ' ' + l if s else l)
        b = s
    SCR.mkdir(parents=True, exist_ok=True)
    out = SCR / (o.out or (pathlib.Path(o.file).resolve().parent.parent.name + '_' + pathlib.Path(o.file).stem + '_body.md'))
    out.write_text('## Reading\n' + b + '\n', encoding='utf8')
    if o.show: print(b)
    hb = v2.holes(b)
    cr.lexicon(o.lang)
    p, h = v2.score(hb, o.lang, False), v2.score(hb, o.lang, True)
    print(f'{out.name}: plain {p["clean_share"]} ({p["clean"]}/{p["sentences"]}), explicit {h["clean_share"]} '
          f'({h["clean"]}/{h["sentences"]}), hole rate {h["hole_rate"]}, words {h["words"]}')
    if o.holes:
        lex = cr.lexicon(o.lang)
        text = cr.CODE.sub(' CODEWORD ', cr.clean_text(hb))
        for s in cr.sentences(re.sub(r'\|[^|\n]*\|', ' [?] ', text)):
            ws = [(w, g) for tok in s for w, g in cr.words_of(tok)]
            unk = [w for w, g in ws if g or not (w in lex or w == 'codeword')]
            if len(unk) > max(1, len(ws) // 10):
                print(f'  [{len(unk)}/{len(ws)}] ' + ', '.join(unk))


if __name__ == '__main__':
    main()
