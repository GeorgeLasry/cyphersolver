"""v3 verify (b): insert a dated NOTES.md block before '## Remaining gaps' (else append); optionally add a line at the
end of the Remaining gaps and Escalation sections.

    python research/reading_audit/v3b_notes.py <folder> <block.md> [--gap "- line"] [--esc "- [x] line"] [--status "Status: ..."]

--status replaces the first 'Status:' line in the first forty lines (or inserts one after the title).
"""
import argparse, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[2]


def add_to_section(s, head, line):
    i = s.find('\n' + head)
    if i < 0:
        return s.rstrip() + f'\n\n{head}\n{line}\n'
    j = s.find('\n## ', i + 1)
    j = len(s) if j < 0 else j
    body = s[:j].rstrip('\n')
    rest = s[j:].lstrip('\n')
    return body + '\n' + line + '\n' + ('\n' + rest if rest else '')


a = argparse.ArgumentParser()
a.add_argument('folder'); a.add_argument('block')
a.add_argument('--gap', action='append', default=[]); a.add_argument('--esc', action='append', default=[])
a.add_argument('--status')
o = a.parse_args()
f = ROOT / 'targets' / o.folder / 'NOTES.md'
s = f.read_text(encoding='utf8')
b = pathlib.Path(o.block).read_text(encoding='utf8').strip() + '\n\n'
i = s.find('\n## Remaining gaps')
s = s[:i + 1] + b + s[i + 1:] if i >= 0 else s.rstrip() + '\n\n' + b
for g in o.gap:
    s = add_to_section(s, '## Remaining gaps', g)
for e in o.esc:
    s = add_to_section(s, '## Escalation', e)
if o.status:
    ls = s.split('\n')
    k = next((n for n, l in enumerate(ls[:40]) if l.startswith('Status:')), None)
    if k is None:
        ls.insert(2, o.status + '\n')
    else:
        ls[k] = o.status
    s = '\n'.join(ls)
f.write_text(s, encoding='utf8', newline='')
print('notes', o.folder)
