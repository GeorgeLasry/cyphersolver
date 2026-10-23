"""v5 (b): r2232 / r2234 - write <folder>/reading.md from reading.txt, where the deciphered parts are in [brackets]
(which the scorers take for holes). In reading.md the deciphered parts are in *italics*; real holes keep their marks
([..] -> [...], '[word?]' -> '[?word]', ... kept); page/line labels [P2], [D] dropped from the running text; the
words themselves unchanged.

    python research/reading_audit/v5b_italics.py <folder> <skip header lines> "<header paragraph>"
"""
import pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
folder, skip, head = sys.argv[1], int(sys.argv[2]), sys.argv[3]
src = (ROOT / 'targets' / folder / 'reading.txt').read_text(encoding='utf8').splitlines()
title = src[0]
body = '\n'.join(src[skip:])
body = re.sub(r'^\[(P\d|[DGLNR])\]\s*', '', body, flags=re.M)
body = body.replace('[..]', '[...]')
body = re.sub(r'\[([^\]\n?]+?)\?\]', lambda m: '[?' + m.group(1) + ']', body)


def ital(m):
    inner = m.group(1)
    if inner.startswith('?') or inner in ('...',) or re.fullmatch(r'\.\.\.|\d+', inner):
        return m.group(0)
    if inner in ('in clear', 'signature, clear, not read'):
        return '(' + inner + ')'
    return '*' + inner.replace('\n', '*\n*') + '*'


body = re.sub(r'\[([^\]]+)\]', ital, body, flags=re.S)
out = ROOT / 'targets' / folder / 'reading.md'
out.write_text(f'# {title}\n\n{head}\n\n## Reading\n\n{body.strip()}\n', encoding='utf8')
print('wrote', out)
