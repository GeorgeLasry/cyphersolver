"""lasry_import (24 Oct 2026): George Lasry's permission ("you can use the decryption I give in DECODE for items I
deciphered, with attribution"). Targeted splices of one outcome.texts entry (relabel_r0 load/save, as v4.py), the
lasry credit, one solution step, and a dated NOTES block.

    python research/reading_audit/lasry_import.py <folder> <actions.json>
    actions: {doc: '#i' or doc value, add_decryption: [paths], reading, translation, language,
              state, read_share (measured here if omitted and reading given), grade, review_note, note,
              step: str, step_result, notes_block: str, credit_doc: str, fraction_read, fraction_read_source, cls}
"""
import json, sys, pathlib, datetime
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save, ROOT  # noqa: E402
import v10_relabel as v10  # noqa: E402

CREDIT = "George Lasry (decryption on DECODE, used with his permission, 24 Oct 2026)"


def main(T, A):
    p = load(T)
    o = p['outcome']
    texts = o['texts']
    d = A['doc']
    e = texts[int(d[1:])] if str(d).startswith('#') else [x for x in texts if x.get('doc') == d][0]
    dec = e.get('decryption')
    dec = [] if dec is None else (dec if isinstance(dec, list) else [dec])
    for f in A.get('add_decryption', []):
        if f not in dec: dec.append(f)
    if dec: e['decryption'] = dec if len(dec) > 1 else dec[0]
    for k in ('reading', 'translation', 'language'):
        if A.get(k): e[k] = A[k]
    if A.get('state'):
        e['state'] = A['state']
    rs = A.get('read_share')
    if rs is None and e.get('reading'):
        m = v10.measure(T, e)
        rs = m[1] if m else None
    if rs is not None: e['read_share'] = rs
    if A.get('grade'):
        e['reading_review'] = dict(grade=A['grade'], by='Claude Opus 5.5', date='2026-10-24', note=A['review_note'])
    if 'note' in A:
        if A['note']: e['note'] = A['note']
        else: e.pop('note', None)
    for k in ('fraction_read', 'fraction_read_source'):
        if k in A: o[k] = A[k]
    if A.get('cls'): o['class'] = A['cls']
    cr = o.setdefault('credits', [])
    lc = [c for c in cr if c.get('who') == 'lasry']
    tag = 'used with his permission, 24 Oct 2026'
    if lc:
        if tag not in lc[0].get('note', ''):
            lc[0]['note'] = (lc[0].get('note', '') + '; ' if lc[0].get('note') else '') + CREDIT
    else:
        cr.append({'who': 'lasry', 'role': 'key or decipherment used', 'note': CREDIT + (': ' + A['credit_doc'] if A.get('credit_doc') else ''),
                   'date': '2026-10-24', 'source': A.get('credit_source', 'DECODE record files')})
    if A.get('step'):
        p['solution'].append({'date': '2026-10-24', 'kind': A.get('step_kind', 'reading'), 'what': A['step'],
                              'result': A.get('step_result', 'partial')})
    save(T, p)
    if A.get('notes_block'):
        n = ROOT / 'targets' / T / 'NOTES.md'
        s = n.read_text(encoding='utf8')
        lines = s.split('\n')
        i = 1
        while i < len(lines) and (lines[i].strip() == '' or lines[i].startswith('Status:')): i += 1
        lines.insert(i, A['notes_block'] + '\n')
        n.write_text('\n'.join(lines), encoding='utf8', newline='')
    print(T, d, e.get('state'), rs)


if __name__ == '__main__':
    main(sys.argv[1], json.loads(pathlib.Path(sys.argv[2]).read_text(encoding='utf8')))
