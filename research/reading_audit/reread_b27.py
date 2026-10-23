"""Re-read brief (REREAD_BRIEF.md), batch b27: esp318no94, estrada1503, exea1408, florence1429, guise1587.
Targeted profile edits with the splice saver of relabel_r0.py; one save per change.

    python research/reading_audit/reread_b27.py <folder> <actions.json>   (keys: read, fields, documents, drop_outcome, outcome, steps)

Helpers: b27_*.py, named in each target's reread log.
"""
import json
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

REV = dict(by="Claude Opus 5.5", date="2026-10-23")
# fields entries may carry "idx" (position in outcome.texts) when two entries share a doc value


def _entry(p, doc, idx=None):
    """The outcome.texts entry: by index when given (two entries can share a doc value), else the one with that doc."""
    if idx is not None:
        e = p['outcome']['texts'][idx]; assert e.get('doc') == doc, (idx, doc); return e
    e = [x for x in p['outcome']['texts'] if x.get('doc') == doc]
    assert len(e) == 1, doc
    return e[0]


def mark_read(T, doc, fields, grade, note, idx=None):
    p = load(T)
    e = _entry(p, doc, idx)
    e.pop('note', None)
    e['state'] = 'read'
    e.update(fields)
    e['reading_review'] = dict(grade=grade, **REV, note=note)
    save(T, p); print('read', T, doc)


def set_fields(T, doc, fields, idx=None):
    for k, v in fields.items():
        p = load(T)
        e = _entry(p, doc, idx)
        e[k] = v
        save(T, p)
    print('fields', T, doc, list(fields))


def add_steps(T, steps):
    for s in steps:
        p = load(T)
        p['solution'].append(s)
        save(T, p)
    print('steps', T, len(steps))


def set_outcome(T, **kw):
    for k, v in kw.items():
        p = load(T)
        if isinstance(v, list) and len(v) > 1:    # one item per save (the splice saver needs small changes)
            p['outcome'][k] = v[:1]; save(T, p)
            for x in v[1:]:
                p = load(T); p['outcome'][k].append(x); save(T, p)
            continue
        p['outcome'][k] = v
        save(T, p)
    print('outcome', T, list(kw))


def doc_field(T, doc_id, k, v):
    p = load(T)
    e = [x for x in p['documents'] if x.get('id') == doc_id][0]
    e[k] = v
    save(T, p)


def run_json(T, path):
    """Apply a json action file: {"read": [...], "fields": [...], "steps": [...], "outcome": {...}, "documents": [...]}"""
    a = json.loads(pathlib.Path(path).read_text(encoding='utf-8'))
    for r in a.get('read', []):
        mark_read(T, r['doc'], r['fields'], r['grade'], r['note'], r.get('idx'))
    for f in a.get('fields', []):
        set_fields(T, f['doc'], f['fields'], f.get('idx'))
    for d in a.get('documents', []):
        for k, v in d['set'].items():
            doc_field(T, d['id'], k, v)
    for k in a.get('drop_outcome', []):      # remove an outcome field that no longer holds
        p = load(T)
        if k in p['outcome']:
            del p['outcome'][k]; save(T, p)
    if a.get('outcome'):
        set_outcome(T, **a['outcome'])
    if a.get('steps'):
        add_steps(T, a['steps'])


if __name__ == '__main__':
    run_json(sys.argv[1], sys.argv[2])
