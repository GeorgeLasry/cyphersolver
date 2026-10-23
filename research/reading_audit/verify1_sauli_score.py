"""verify1 (sauli1579): cut each R19x reading to its body (from the first '## ' section; headings, header comment and
the closing 'Alignment notes' pointer removed) into the scratchpad and score it with docs/_check_reading.py.
    python research/reading_audit/verify1_sauli_score.py <scratch_dir> R190 ..."""
import pathlib, re, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
T = ROOT / 'targets' / 'sauli1579' / 'texts'
out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
for doc in sys.argv[2:]:
    s = (T / f'{doc}_reading.md').read_text(encoding='utf8')
    s = re.sub(r'<!--.*?-->', '', s, flags=re.S)
    s = s[s.index('\n## '):] if '\n## ' in s else s[s.index('\n# '):]  # R194 has no sections: body follows the title
    lines = [l for l in s.splitlines() if not l.startswith('#') and not l.startswith('Alignment notes')]
    p = out / f'{doc}_body.md'
    p.write_text('\n'.join(lines) + '\n', encoding='utf8')
    r = subprocess.run([sys.executable, str(ROOT / 'docs' / '_check_reading.py'), '--file', str(p)],
                       capture_output=True, text=True, encoding='utf8', cwd=ROOT)
    print('==', doc); print(r.stdout.strip()[-600:])
