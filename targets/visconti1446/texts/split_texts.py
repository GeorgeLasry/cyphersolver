"""Per slip: write f<n>_signs.txt (sign tokens, one cipher line per row) from f<n>_tokens.tsv, and f<n>_reading.md /
f<n>_en.md from the continuous-plaintext and English-summary sections of f<n>.md. Run from this folder.

    python split_texts.py            # all slips with a tokens file
"""
import glob, re, os

def section(md, names):
    parts = re.split(r'^## ', md, flags=re.M)
    for p in parts[1:]:
        head = p.split('\n', 1)[0].lower()
        if any(head.startswith(n) for n in names):
            return p.split('\n', 1)[1].strip()
    return None

for tok in sorted(glob.glob('f*_tokens.tsv')):
    n = tok.split('_')[0]
    rows = [l.rstrip('\n').split('\t') for l in open(tok, encoding='utf-8')]
    if rows and rows[0][:1] == ['line']:
        rows = rows[1:]
    lines = {}
    for r in rows:
        if len(r) >= 2:
            lines.setdefault(r[0], []).append(r[1])
    with open(f'{n}_signs.txt', 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(' '.join(v) for v in lines.values()) + '\n')
    md = open(f'{n}.md', encoding='utf-8').read() if os.path.exists(f'{n}.md') else ''
    title = md.split('\n', 1)[0].lstrip('# ').strip()
    it = section(md, ['continuous plaintext', 'plaintext'])
    en = section(md, ['english summary', 'summary'])
    if it:
        open(f'{n}_reading.md', 'w', encoding='utf-8').write(f'# {title}: reading\n\n{it}\n')
    if en:
        open(f'{n}_en.md', 'w', encoding='utf-8').write(f'# {title}: English\n\n{en}\n')
    print(n, len(rows), 'tokens', len(lines), 'lines', 'reading' if it else 'NO READING', 'en' if en else 'NO EN')
