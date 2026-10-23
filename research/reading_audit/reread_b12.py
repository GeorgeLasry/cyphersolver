"""b12 (acciaiuoli1757, balbases1677): profile.json edits after the 22 Oct 2026 re-read. The two files are written
by json.dumps(indent=1, ensure_ascii=False), so loading, changing and dumping keeps the layout byte for byte
(checked before use). Saved after each step.

    python research/reading_audit/reread_b12.py <target> <step>
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]


def load(t):
    p = ROOT / 'targets' / t / 'profile.json'
    s = p.read_bytes().decode('utf-8')
    return p, json.loads(s), s.endswith('\n')


def save(p, d, nl):
    p.write_bytes((json.dumps(d, indent=1, ensure_ascii=False) + ('\n' if nl else '')).encode('utf-8'))


REV = dict(by='Claude Opus 5.5', date='2026-10-22')


def mark_read(t, match, fields, grade, note):
    p, d, nl = load(t)
    hit = [e for e in d['outcome']['texts'] if match in e.get('label', '')]
    assert len(hit) == 1, (match, len(hit))
    e = hit[0]
    e.pop('state', None); e.pop('note', None)
    e.update(fields)
    e['reading_review'] = dict(grade=grade, **REV, note=note)
    save(p, d, nl); print('read', t, match)


def add_steps(t, steps):
    p, d, nl = load(t)
    d['solution'] += steps
    save(p, d, nl); print('steps', t, len(steps))


def set_outcome(t, **kw):
    p, d, nl = load(t)
    for k, v in kw.items(): d['outcome'][k] = v
    save(p, d, nl); print('outcome', t, list(kw))


if __name__ == '__main__':
    t, step = sys.argv[1], sys.argv[2]
    import importlib.util
    spec = importlib.util.spec_from_file_location('b12steps', ROOT / 'research' / 'reading_audit' / 'reread_b12_steps.py')
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    m.STEPS[(t, step)]()
