"""Helper for the relabel brief, list relabel_1 (22 Oct 2026). Load/save profile.json keeping its format.

  python research/reading_audit/relabel_helper_r1.py show <folder>
  from relabel_helper_r1 import load, save, step
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]


def load(folder):
    f = ROOT / 'targets' / folder / 'profile.json'
    raw = f.read_bytes().decode('utf-8')
    crlf = '\r\n' in raw
    s = raw.replace('\r\n', '\n')
    p = json.loads(s)
    ea = json.dumps(p, indent=1, ensure_ascii=True) + '\n' == s
    trail = s.endswith('\n')
    return p, (crlf, ea, trail)


def save(folder, p, fmt):
    crlf, ea, trail = fmt
    s = json.dumps(p, indent=1, ensure_ascii=ea) + ('\n' if trail else '')
    if crlf: s = s.replace('\n', '\r\n')
    (ROOT / 'targets' / folder / 'profile.json').write_bytes(s.encode('utf-8'))


def step(p, what, result='failed', technique=('language-model scoring', 'statistical test')):
    st = {'date': '2026-10-22', 'kind': 'verification', 'what': what, 'result': result,
          'technique': list(technique)}
    # match the key order / extra fields of existing steps where possible
    p.setdefault('solution', []).append(st)
    return st


def review(grade, note):
    return {'grade': grade, 'by': 'Claude (reading audit)', 'date': '2026-10-22', 'note': note}


def show(folder):
    p, fmt = load(folder)
    o = p['outcome']
    print('fmt', fmt)
    for k in ('class', 'method', 'key', 'fraction_read', 'fraction_read_method', 'fraction_read_source',
              'fraction_coherent', 'notes'):
        print(f'{k}: {o.get(k)}')
    for i, t in enumerate(o.get('texts') or []):
        print(f'--- texts[{i}]', json.dumps({k: v for k, v in t.items() if k != 'summary'}, ensure_ascii=False))
    print('last step:', (p.get('solution') or [{}])[-1])
    print('documents:', [(d.get('id'), (d.get('length') or {}).get('tokens')) for d in p.get('documents') or []])


if __name__ == '__main__':
    if sys.argv[1] == 'show': show(sys.argv[2])


def _rw(path, fn):
    p = ROOT / path
    raw = p.read_bytes().decode('utf-8')
    crlf = '\r\n' in raw
    s = fn(raw.replace('\r\n', '\n'))
    if crlf: s = s.replace('\n', '\r\n')
    p.write_bytes(s.encode('utf-8'))


def notes(folder, block, gaps=(), anchor=None):
    """Insert the dated audit block after the first 'Status:' paragraph (or before `anchor`), and gap lines
    at the top of '## Remaining gaps' (created before '## Escalation' or at the end if missing)."""
    def fn(s):
        b = block.strip('\n') + '\n\n'
        if anchor:
            assert anchor in s, anchor
            s = s.replace(anchor, b + anchor, 1)
        else:
            i = s.find('\nStatus:')
            if i < 0: i = s.find('\n**Status')
            assert i >= 0, 'no Status line'
            j = s.find('\n\n', i + 1)
            s = s[:j + 2] + b + s[j + 2:]
        if gaps:
            g = ''.join('- ' + x + '\n' for x in gaps)
            if '\n## Remaining gaps\n' in s:
                k = s.index('\n## Remaining gaps\n') + len('\n## Remaining gaps\n')
                if s[k:k + 1] == '\n': k += 1
                s = s[:k] + g + s[k:]
            elif '\n## Escalation' in s:
                k = s.index('\n## Escalation')
                s = s[:k] + '\n## Remaining gaps\n' + g + s[k:]
            else:
                s = s.rstrip('\n') + '\n\n## Remaining gaps\n' + g
        return s
    _rw(f'targets/{folder}/NOTES.md', fn)


def page(slug, reps):
    def fn(s):
        for a, b in reps:
            assert a in s, a
            s = s.replace(a, b)
        return s
    _rw(f'docs/{slug}.html', fn)
