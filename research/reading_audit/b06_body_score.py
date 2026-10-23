"""b06: score only the body of read/<rec>_reading.md (title to '## Notes', header comment cut) with _check_reading.py.
    python research/reading_audit/b06_body_score.py R3811
"""
import os, re, subprocess, sys, tempfile
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
for rec in sys.argv[1:]:
    t = open(os.path.join(ROOT, 'targets', 'kurtz1639', 'read', rec + '_reading.md'), encoding='utf-8').read()
    t = re.sub(r'<!--.*?-->', '', t, flags=re.S).split('\n## ')[0]
    t = '\n'.join(l for l in t.split('\n') if not l.startswith('# '))
    f = os.path.join(tempfile.gettempdir(), 'b06_body_%s.md' % rec)
    open(f, 'w', encoding='utf-8').write(t)
    out = subprocess.run([sys.executable, os.path.join(ROOT, 'docs', '_check_reading.py'), '--file', f],
                         capture_output=True, text=True, encoding='utf-8', env=dict(os.environ, PYTHONUTF8='1')).stdout
    m = {k: re.search(r'"%s":\s*([0-9.]+)' % k, out) for k in ('sentences', 'clean', 'clean_share', 'words', 'hole_rate')}
    print(rec, {k: (v.group(1) if v else None) for k, v in m.items()})
