"""Verification 5 (a): plain-bar rows (v5_plainbar_a.txt). Copy of v4.py (via reread_b35.py, v3_b.py) with by-index review/demote.
Targeted profile edits with the splice saver of relabel_r0.py; one save per change.

    python research/reading_audit/v4.py <folder> <actions.json>
    keys: review [{doc:'#i', note, grade?}] (keep read, rewrite reading_review), demote [{doc:'#i', note}],
          not_prose [{doc:'#i', note}],
          read, fields, documents, drop_outcome, outcome, steps

Helpers: v5a_*.py (v5a_body.py scores a cut body and lists the unknown words).
"""
import json
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

REV = dict(by="Claude Opus 5.5", date="2026-10-23")


def _entry(p, doc):
    """doc may be the doc value, or '#<index>' to pick outcome.texts by index (b35: when doc values are shared)."""
    if isinstance(doc, str) and doc.startswith('#'):
        return p['outcome']['texts'][int(doc[1:])]
    e = [x for x in p['outcome']['texts'] if x.get('doc') == doc]
    assert len(e) == 1, doc
    return e[0]


def mark_read(T, doc, fields, grade, note):
    p = load(T)
    e = _entry(p, doc)
    if e.get('state') not in (None, 'read'):      # v5: drop the note only when the state changes to read
        e.pop('note', None)
    e['state'] = 'read'
    e.update(fields)
    rr = e.get('reading_review') or {}
    if rr.get('note') and 'v5 check' not in rr['note']:
        note = note + ' Earlier: ' + rr['note']
    e['reading_review'] = dict(grade=grade, **REV, note=note)
    save(T, p); print('read', T, doc)


def review(T, doc, note, grade=None):
    """keeps read: rewrite reading_review with the v3 score."""
    p = load(T)
    e = _entry(p, doc)
    rr = dict(e.get('reading_review') or {})
    g = grade or rr.get('grade') or 'B'
    if rr.get('note') and 'v5 check' not in rr['note']:
        note = note + ' Earlier: ' + rr['note']          # v5: keep the earlier review note after the new one
    e['reading_review'] = dict(grade=g, **REV, note=note)
    save(T, p); print('review', T, doc)


def demote(T, doc, note):
    """state -> decoded, not read with a note; reading_review removed."""
    p = load(T)
    e = _entry(p, doc)
    e.pop('reading_review', None)
    save(T, p)
    p = load(T); e = _entry(p, doc)
    e['state'] = 'decoded, not read'
    e['note'] = note
    save(T, p); print('demote', T, doc)


def not_prose(T, doc, note):
    """v4: state -> not prose (a word, names: no sentence expected) with a note; reading_review removed."""
    p = load(T)
    e = _entry(p, doc)
    e.pop('reading_review', None)
    save(T, p)
    p = load(T); e = _entry(p, doc)
    e['state'] = 'not prose'
    e['note'] = note
    save(T, p); print('not prose', T, doc)


def set_fields(T, doc, fields):
    for k, v in fields.items():
        p = load(T)
        e = _entry(p, doc)
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
    for r in a.get('review', []):
        review(T, r['doc'], r['note'], r.get('grade'))
    for r in a.get('demote', []):
        demote(T, r['doc'], r['note'])
    for r in a.get('not_prose', []):
        not_prose(T, r['doc'], r['note'])
    for r in a.get('read', []):
        mark_read(T, r['doc'], r['fields'], r['grade'], r['note'])
    for f in a.get('fields', []):
        set_fields(T, f['doc'], f['fields'])
    for d in a.get('documents', []):
        for k, v in d['set'].items():
            doc_field(T, d['id'], k, v)
    for k in a.get('drop_outcome', []):      # b26: remove an outcome field that no longer holds
        p = load(T)
        if k in p['outcome']:
            del p['outcome'][k]; save(T, p)
    if a.get('outcome'):
        set_outcome(T, **a['outcome'])
    if a.get('steps'):
        add_steps(T, a['steps'])


if __name__ == '__main__':
    run_json(sys.argv[1], sys.argv[2])
