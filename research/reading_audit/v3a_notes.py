"""v3 verify (a): insert a dated NOTES.md block before '## Remaining gaps' (else append).

    python research/reading_audit/v3a_notes.py <folder> <block.md>
"""
import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
f = ROOT / 'targets' / sys.argv[1] / 'NOTES.md'
s = f.read_text(encoding='utf8')
b = pathlib.Path(sys.argv[2]).read_text(encoding='utf8').strip() + '\n\n'
i = s.find('\n## Remaining gaps')
s = s[:i + 1] + b + s[i + 1:] if i >= 0 else s.rstrip() + '\n\n' + b
f.write_text(s, encoding='utf8', newline='')
print('notes', sys.argv[1])
