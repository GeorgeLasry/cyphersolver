"""b09 (nuncio1566): align each '### f. <page>' section of a reading .md with its cipher page.

    python research/reading_audit/b09_align.py <transcription> <reading.md> [--full]

Runs targets/nuncio1566/reread_b09_align.py on every section (page name = section title + '.jpg') and prints the
words that disagree with the figures and the per-page counts (--full prints every word with its figures).
"""
import os, re, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
AL = os.path.join(HERE, '..', '..', 'targets', 'nuncio1566', 'reread_b09_align.py')
tr, md = sys.argv[1], sys.argv[2]
body = open(md, encoding='utf-8').read().split('## Reading', 1)[1].split('\n## ', 1)[0]
for m in re.finditer(r'### f\. (\S+)\n(.*?)(?=\n### |\Z)', body, re.S):
    page, text = m.group(1), m.group(2)
    with tempfile.NamedTemporaryFile('w', suffix='.txt', delete=False, encoding='utf-8') as f:
        f.write(text)
    out = subprocess.run([sys.executable, AL, tr, page + '.jpg', f.name], capture_output=True, text=True,
                         encoding='utf-8').stdout
    os.unlink(f.name)
    print('=== f. %s' % page)
    for line in out.splitlines():
        if '--full' in sys.argv or line.startswith('!!') or line.startswith('# cost'):
            print(line)
