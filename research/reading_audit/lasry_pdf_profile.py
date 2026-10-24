"""George Lasry's report PDFs (24 Oct 2026): point a target's outcome.texts at lasry/report/ and record the reading.
Copy of v4.py (splice saver of relabel_r0.py, one save per change) with REV dated 2026-10-24 and an `auto` step:

    python research/reading_audit/lasry_pdf_profile.py <folder> --auto [--doc '#0'] [--lang fr] [--state S] [--why TEXT]
        measures lasry/report/readable.md with v10_relabel.measure (the whole letter) and the strict share of the
        deciphered passages (bold runs plus the holes next to them, a bare ? an unread group, word? a doubtful word),
        then sets on outcome.texts[doc]: reading, translation (his excerpt translation: he gives no full one), language,
        read_share, state, note, reading_review (grade B), and appends one solution step. State: read when both
        shares reach 0.95 and the report does not call the item partly deciphered; else read in part (coherent
        sentences) unless --state says otherwise. Prints the actions; --dry stops there.
    python research/reading_audit/lasry_pdf_profile.py <folder> <actions.json>     (as v4.py)
    keys: review [{doc:'#i', note, grade?}] (keep read, rewrite reading_review), demote [{doc:'#i', note}],
          not_prose [{doc:'#i', note}],
          read, fields, documents, drop_outcome, outcome, steps

Helpers: v4_*.py.
"""
import json
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

REV = dict(by="Claude Opus 5.5", date="2026-10-24")


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
    e.pop('note', None)
    e['state'] = 'read'
    e.update(fields)
    e['reading_review'] = dict(grade=grade, **REV, note=note)
    save(T, p); print('read', T, doc)


def review(T, doc, note, grade=None):
    """keeps read: rewrite reading_review with the v3 score."""
    p = load(T)
    e = _entry(p, doc)
    rr = dict(e.get('reading_review') or {})
    g = grade or rr.get('grade') or 'B'
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


ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = "George Lasry's report PDF (24 Oct 2026)"


def strict_cipher_share(text):
    """Share of the deciphered passages that reads: bold runs and the [?]/? holes touching them."""
    import re
    body = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    body = '\n'.join(l for l in body.split('\n') if not l.startswith('#'))
    runs = re.findall(r'(?:\[\?\]\s*)*\*\*(.+?)\*\*(?:\s*\[\?\])*', body)
    near = re.findall(r'\[\?\](?=\s*\*\*)|(?<=\*\*)\s*\[\?\]', body)
    src = ' '.join(runs)
    holes = len(re.findall(r'\[\?\]|(?<![\w\]])\?(?![\w\[])', src)) + len(near)
    doubt = len(re.findall(r'(?<=\w)\?', src))
    words = len(re.findall(r'[^\W\d_]+', src.replace('[?]', ' ')))
    return (round(1 - (holes + doubt) / (words + holes), 3) if words else None), words, holes, doubt


def auto(T, doc='#0', lang=None, state=None, why='', dry=False):
    import v10_relabel as V
    rep = json.loads((ROOT / 'targets' / T / 'lasry' / 'report' / 'report.json').read_text(encoding='utf-8'))
    p = load(T); e = _entry(p, doc)
    lang = lang or e.get('language') or 'unknown'
    m = V.measure(T, {'reading': 'lasry/report/readable.md', 'language': lang})
    rs = m[1] if m else None
    cs, cw, ch, cd = strict_cipher_share((ROOT / 'targets' / T / 'lasry' / 'report' / 'readable.md').read_text(encoding='utf-8'))
    partly = 'part' in (rep.get('status') or '').lower()
    if not state:
        state = 'read' if (rs or 0) >= 0.95 and (cs is None or cs >= 0.95) and not partly else 'read in part'
    tr = ['lasry/report/translation_excerpt.md'] + [x for x in V._texts.listify(e.get('translation')) if not str(x).startswith('lasry')]
    dec = [x for x in V._texts.listify(e.get('decryption')) if x != 'lasry_entry.md' and not str(x).startswith('lasry/')]
    note = (f"{SRC}, extracted to lasry/report/ (lasry_pdf_extract.py): his full Readable text by folio is the reading; "
            f"he gives a translation of the excerpt only (lasry/report/translation_excerpt.md), no full translation. "
            f"Report status: {rep.get('status')}. Measured 24 Oct 2026: whole text {rs} (v10_relabel.measure, {m[2] if m else 0} words); "
            f"deciphered passages alone {cs} ({cw} words, {ch} unread groups, {cd} doubtful words; a bare ? counted as unread). "
            + (why + ' ' if why else '') + f"State: {state}.")
    fields = dict(reading='lasry/report/readable.md', translation=tr if len(tr) > 1 else tr[0], language=lang,
                  read_share=rs, state=state, note=note,
                  reading_review=dict(grade='B', **REV, note=f"{SRC}: full Readable text by folio (bold = deciphered), "
                                      f"read against his excerpt, his summary and the key image; whole text {rs}, deciphered "
                                      f"passages {cs}. Not re-deciphered here."))
    if dec: fields['decryption'] = dec if len(dec) > 1 else dec[0]
    elif 'decryption' in e: fields['decryption'] = 'lasry/report/readable.md'
    step = {'date': '2026-10-24', 'kind': 'reading',
            'what': f"{SRC} received and extracted to lasry/report/ (summary, key image, excerpt and translation, full "
                    f"Readable text by folio); outcome.texts now points at his full text. Read share {rs} (whole), "
                    f"{cs} (deciphered passages); state {state}.",
            'result': 'success' if state == 'read' else 'partial'}
    print(json.dumps(dict(fields=fields, step=step), ensure_ascii=False, indent=1))
    if dry: return
    set_fields(T, doc, fields)
    add_steps(T, [step])


if __name__ == '__main__':
    a = sys.argv[1:]
    if '--auto' in a:
        opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
        auto(a[0], doc=opt('--doc', '#0'), lang=opt('--lang'), state=opt('--state'), why=opt('--why', ''), dry='--dry' in a)
    else:
        run_json(a[0], a[1])
