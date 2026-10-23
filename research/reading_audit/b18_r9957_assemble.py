"""b18: assemble the R9957 reading body from the run files of forks A, B, C (R9957_runs_A/B/C.md).

Each run becomes one paragraph: (clear words before, as transcribed from the image) decode (clear words after).
Writes the body to stdout; the header, the f. 9r decipherment section and the notes are added by hand.
    python research/reading_audit/b18_r9957_assemble.py > body.md
"""
import re, pathlib, sys
D = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'charles1536' / 'texts'
FIELD = re.compile(r'^(?:- )?(Clear before|Before[^:]*|Decode|Clear after|After[^:]*|Signs|Notes|Luo)\s*:\s*(.*)$')

def runs(f):
    cur = None; field = None
    for line in (D / f).read_text(encoding='utf8').split('\n'):
        if re.match(r'^#{2,3} Run', line):
            if cur: yield cur
            cur = {'head': line.lstrip('#').strip()}; field = None; continue
        if re.match(r'^#{1,3} ', line):
            if cur: yield cur
            cur = None; field = None; continue
        if cur is None: continue
        m = FIELD.match(line)
        if m:
            k = m.group(1).lower()
            field = 'before' if k.startswith(('clear before', 'before')) else 'after' if k.startswith(('clear after', 'after')) else k
            cur[field] = m.group(2).strip(); continue
        if not line.strip():
            field = None; continue
        if field in ('before', 'after', 'decode') and not line.startswith('- '):
            cur[field] += ' ' + line.strip()
    if cur: yield cur

def clean_clear(t, tail):
    t = re.sub(r'\([^)]*\)', ' ', t)                       # remarks such as (0006, fork A)
    q = re.findall(r'"([^"]*)"', t)
    t = ' '.join(q) if q else t
    t = t.replace('|', ' ')
    parts = re.split(r'\.\.\.|…', t)
    t = parts[-1] if tail else parts[0]
    w = t.split()
    return ' '.join(w[-8:] if tail else w[:8]).strip(' .,;')

for f in ('R9957_runs_A.md', 'R9957_runs_B.md', 'R9957_runs_C.md'):
    for r in runs(f):
        d = r.get('decode', '').replace('|', '').replace('  ', ' ').strip()
        d = re.sub(r'\s*\((?:[^)]*)\)\s*', ' ', d) if d.startswith('(') and False else d
        if not d:
            print(f'<!-- {r["head"]}: no decode -->'); continue
        b = clean_clear(r.get('before', ''), True); a = clean_clear(r.get('after', ''), False)
        print(f'<!-- {r["head"]} -->')
        print(((f'({b}) ' if b else '') + d + (f' ({a})' if a else '')).replace('  ', ' ') + '\n')
