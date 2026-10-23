"""nunzio1736: fraction_read after 423/5, 9, 11 were moved back to decoded, not read (22 Oct 2026)."""
import json, pathlib, re

p = pathlib.Path(__file__).resolve().parent.parent.parent / 'targets' / 'nunzio1736' / 'profile.json'
s = p.read_bytes().decode('utf-8')
m = re.search(r'"fraction_read_source":\s*("(?:[^"\\]|\\.)*")', s)
src = json.loads(m.group(1)) + (
    " Revised the same day: 423/5 (0.20 clean sentences), 423/9 and 423/11 (0.47) were moved back to decoded, not read "
    "under the 0.60 rule; with 423/1 they hold about 48% of the re-segmented decode files, so about 0.52 of the tokens "
    "are in letters that read (estimated from the decode file sizes, not re-counted).")
s = s[:m.start(1)] + json.dumps(src, ensure_ascii=False) + s[m.end(1):]
s = re.sub(r'"fraction_read":\s*0\.777', '"fraction_read": 0.52', s, count=1)
s = re.sub(r'"fraction_read_method":\s*"measured"', '"fraction_read_method": "estimated"', s, count=1)
json.loads(s)
p.write_bytes(s.encode('utf-8'))
print('ok')
