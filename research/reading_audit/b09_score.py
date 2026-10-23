"""b09: score only the '## Reading' body (section headings '### f. ...' removed) of targets/nuncio1566/texts/<rec>_reading.md
with _check_reading.py.     python research/reading_audit/b09_score.py R85 R86 ...  [--en] (score <rec>_en.md instead)
"""
import os, re, subprocess, sys, tempfile
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
en = '--en' in sys.argv
for rec in [a for a in sys.argv[1:] if not a.startswith('--')]:
    t = open(os.path.join(ROOT, 'targets', 'nuncio1566', 'texts', rec + ('_en.md' if en else '_reading.md')), encoding='utf-8').read()
    t = t.split('## Reading', 1)[1] if '## Reading' in t else t.split('\n', 1)[1]
    t = t.split('\n## ', 1)[0]
    t = '\n'.join(l for l in t.split('\n') if not l.startswith('#'))
    f = os.path.join(tempfile.gettempdir(), 'b09_body_%s.md' % rec)
    open(f, 'w', encoding='utf-8').write(t)
    out = subprocess.run([sys.executable, os.path.join(ROOT, 'docs', '_check_reading.py'), '--file', f],
                         capture_output=True, text=True, encoding='utf-8', env=dict(os.environ, PYTHONUTF8='1')).stdout
    m = {k: re.search(r'"%s":\s*([0-9.]+)' % k, out) for k in ('sentences', 'clean', 'clean_share', 'words', 'hole_rate')}
    print(rec, {k: (v.group(1) if v else None) for k, v in m.items()})
