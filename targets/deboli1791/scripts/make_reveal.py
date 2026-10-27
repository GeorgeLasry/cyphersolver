"""Build docs/reveal/deboli1791.json from align/002.tsv: the opening of despatch 002, each cipher group with the value
the contemporary decipherment gives it. Word spaces are taken from the clear sentence in the '# ' comment lines."""
import json, re, sys

N = int(sys.argv[1]) if len(sys.argv) > 1 else 110
tokens, sentence, pos = [], '', 0
for line in open('align/002.tsv', encoding='utf8'):
    line = line.rstrip('\n')
    if line.startswith('# ') and not line.startswith('# 002') and not line.startswith('# Punctuation'):
        sentence, pos = line[2:], 0
        continue
    if line.startswith('#') or not line.strip():
        continue
    g, _, v = line.partition('\t')
    unc = '[' in v
    val = re.sub(r'\s*\[.*?\]', '', v).strip()
    cls = 'unk' if val in ('?', '') else ('unc' if unc else '')
    p = val
    if val not in ('?', '') and sentence:
        i = sentence.lower().find(val.lower(), pos)
        if i >= 0 and i - pos <= 3:
            pos = i + len(val)
            if val in ',.;:' or (pos < len(sentence) and not sentence[pos].isalpha()):
                p += ' '
                while pos < len(sentence) and sentence[pos] == ' ':
                    pos += 1
        else:
            p += ' '
    tok = {"g": g, "p": p if cls != 'unk' else '?'}
    if cls:
        tok["cls"] = cls
    tokens.append(tok)
    if len(tokens) >= N and val in ('.', ';'):
        break
out = {
    "slug": "deboli1791",
    "anchor": "the-check",
    "title": "St Petersburg, 7 January 1791: the opening of despatch 002",
    "caption": "The first lines of Deboli's cipher despatch of 7 January 1791 (AGAD Zbiór Popielów 5, k. 6), each group with the value given to it by the King's cabinet's decipherment (Zbiór Popielów 421, k. 302).",
    "unit": "code groups",
    "key_note": "Polish syllabic code (code A): words, syllables and letters, with groups for punctuation (1786 = comma, 1775 = full stop). Values from the contemporary decipherment, aligned here; dotted = the split of a word between groups is uncertain.",
    "tokens": tokens,
}
json.dump(out, open('../../docs/reveal/deboli1791.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(tokens), ''.join(t['p'] for t in tokens))
