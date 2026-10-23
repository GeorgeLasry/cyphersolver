"""Set outcome.fraction_read and append a sentence to fraction_read_source, by targeted text edit (layout kept).

    python research/reading_audit/set_fraction.py <folder> <value> <measured|estimated> "<sentence to append>"
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent


def main(folder, value, method, sentence):
    p = ROOT / 'targets' / folder / 'profile.json'
    s = p.read_bytes().decode('utf-8')
    before = json.loads(s)
    s = re.sub(r'("fraction_read":\s*)[0-9.]+|("fraction_read":\s*)"[^"]*"', lambda m: (m.group(1) or m.group(2)) + value, s, count=1)
    m = re.search(r'"fraction_read_source":\s*("(?:[^"\\]|\\.)*")', s)
    if m:
        src = json.loads(m.group(1)) + ' ' + sentence
        s = s[:m.start(1)] + json.dumps(src, ensure_ascii=False) + s[m.end(1):]
    else:
        s = re.sub(r'("fraction_read":\s*[0-9.]+)', lambda mm: mm.group(1) + ', "fraction_read_source": ' + json.dumps(sentence, ensure_ascii=False), s, count=1)
    if re.search(r'"fraction_read_method":\s*"[^"]*"', s):
        s = re.sub(r'"fraction_read_method":\s*"[^"]*"', f'"fraction_read_method": "{method}"', s, count=1)
    after = json.loads(s)
    assert after['outcome']['fraction_read'] == float(value)
    p.write_bytes(s.encode('utf-8'))
    print(folder, value)


if __name__ == '__main__':
    main(*sys.argv[1:5])
