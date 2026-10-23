"""b12: write the body of a reading file (comment header, # lines and the notes section cut) to a scratch file and score it."""
import re, subprocess, sys
src, out = sys.argv[1], sys.argv[2]
t = open(src, encoding='utf8').read()
t = re.split(r'^## ', t, flags=re.M)[0]
t = re.sub(r'<!--.*?-->', '', t, flags=re.S)
t = '\n'.join(l for l in t.split('\n') if not l.startswith('#'))
open(out, 'w', encoding='utf8').write(t)
r = subprocess.run([sys.executable, 'docs/_check_reading.py', '--file', out], capture_output=True, text=True, encoding='utf8')
print(src, ' '.join(l.strip() for l in r.stdout.split('\n') if re.search(r'"(sentences|clean|clean_share|hole_rate)"', l)))
