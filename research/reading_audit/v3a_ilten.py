"""v3 verify (a), ilten1697/ilten1705: running reading of letters A, B, C from the clear-text-plus-gloss files.
[groups = gloss] -> the contemporary gloss; [groups = ---] (no gloss) -> [?]; '(null)' glosses dropped; the
transcriber's remarks in parentheses inside a gloss dropped; {interlined: x} -> x; {struck ...} and {.. written above ..}
dropped. Clear text unchanged.

    python research/reading_audit/v3a_ilten.py
"""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
HEAD = """# {title}: reading

Rests on: `{src}` (clear text transcribed from the GWLB master images, the code runs with the contemporary interlinear
gloss written over them). Written out for the v3 verification (23 Oct 2026) without the [groups = gloss] notation,
which the scorer takes for supplied words: each code run is replaced by its contemporary gloss as the interliner wrote
it; runs he left without a gloss are [?]; struck clear text is left out, interlined clear text kept; spelling as
written.

## Reading

"""


def conv(t):
    t = re.sub(r'\{interlined: ([^}]*)\}', r'\1', t)
    t = re.sub(r'\s*\{(?:struck[^}]*|\d+ written above \d+)\}', '', t)
    def g(m):
        v = m.group(1).strip()
        v = re.sub(r'\s*\([^)]*\)', '', v).strip()
        if v in ('---', ''):
            return '[?]' if m.group(1).strip() == '---' else ''
        return v
    t = re.sub(r'\[[\d.?]+ = ([^\]]*)\]', g, t)
    t = re.sub(r'(\w)- (\w)', r'\1\2', t)
    return re.sub(r'  +', ' ', t)


def section(path, letter):
    s = path.read_text(encoding='utf8')
    parts = re.split(r'^## ([A-D])\. ', s, flags=re.M)
    i = parts.index(letter)
    body = parts[i + 1].split('\n', 1)[1]
    lines = [l for l in body.splitlines() if l.strip() and not l.startswith('##')]
    return parts[i + 1].split('\n', 1)[0], conv(' '.join(lines))


T = ROOT / 'targets'
for folder, src, letter, out in (('ilten1697', 'letter_A_1697.txt', 'A', 'letter_A_reading.md'),
                                 ('ilten1705', 'letters_BC_1705_1706.txt', 'B', 'letter_B_reading.md'),
                                 ('ilten1705', 'letters_BC_1705_1706.txt', 'C', 'letter_C_reading.md')):
    title, body = section(T / folder / src, letter)
    (T / folder / out).write_text(HEAD.format(title=letter + '. ' + title.split(' -- ')[0], src=src) + body.strip() + '\n', encoding='utf8')
    print(out, body[:300])
