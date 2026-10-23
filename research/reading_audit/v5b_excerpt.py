"""v5 (b): write targets/<folder>/lasry_excerpt_reading.md from lasry_entry.md: George Lasry's excerpt text (his
report's 'Excerpt' sections, quoted verbatim, folio labels kept as section lines), under '## Reading', with a header
saying what it is, so that the scorers score his reading and not the report page around it.

    python research/reading_audit/v5b_excerpt.py <folder> "<title>"
"""
import pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
folder, title = sys.argv[1], sys.argv[2]
t = (ROOT / 'targets' / folder / 'lasry_entry.md').read_text(encoding='utf8')
parts = []
for m in re.finditer(r'^Excerpt\s*\n(.*?)(?=^Translation\s*$)', t, re.S | re.M):
    ls = m.group(1).strip().split('\n')
    lab = [l for l in ls if re.match(r'^(f\d+[rv]|p\d+$|.*lines?\s*\d)', l.strip())]
    txt = [l for l in ls if not re.match(r'^(f\d+[rv]|p\d+$|.*lines?\s*\d|BnF cipher research|\d+ / \d+|--- PDF)', l.strip())]
    parts.append((lab[0].strip() if lab else '', ' '.join(x.strip() for x in txt)))
body = '\n\n'.join(x for lab, x in parts)
labs = '; '.join(lab for lab, x in parts if lab) or 'one'
head = (f'# {title}\n\nGeorge Lasry\'s reading, as excerpted in his BnF cipher research report (lasry_entry.md, copied '
        'from the report verbatim). Written out 23 Oct 2026 (verification 5): the excerpt text only, so that it can be scored '
        'apart from the report page. Excerpts, in order: ' + labs + '. His full transcription and '
        'decryption are his and not in the repository. Marks are his: [?] unread, [x] supplied.\n\n## Reading\n\n')
out = ROOT / 'targets' / folder / 'lasry_excerpt_reading.md'
out.write_text(head + body + '\n', encoding='utf8')
print('wrote', out, len(parts), 'excerpts')
