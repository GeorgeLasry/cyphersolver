"""v4 (23 Oct 2026): insert a dated NOTES.md block before '## Remaining gaps' (else append).
    python v4_notes.py <folder> <block.md>"""
import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
p = ROOT / 'targets' / sys.argv[1] / 'NOTES.md'
s = p.read_text(encoding='utf-8'); b = pathlib.Path(sys.argv[2]).read_text(encoding='utf-8').rstrip() + '\n\n'
i = s.find('\n## Remaining gaps')
s = s[:i + 1] + b + s[i + 1:] if i >= 0 else s.rstrip() + '\n\n' + b
p.write_text(s, encoding='utf-8'); print('notes', sys.argv[1])
