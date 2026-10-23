"""Set one outcome.texts entry to "decoded, not read" with a note, by rewriting that entry only (layout kept).

    python research/reading_audit/set_state.py <folder> <doc> "<note>"

The entry whose "doc" is <doc> is located in the text, parsed, changed (state, note; the note goes right after "doc"),
and written back in the same style: on one line if it was on one line, else indented like its first key. The rest of
the file is untouched, and the result must parse to the old data with only those two fields changed.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent


def entry_span(raw, at):
    """Start and end (exclusive) of the JSON object that contains position `at`."""
    start = raw.rfind('{', 0, at)
    dec = json.JSONDecoder()
    while start >= 0:
        try:
            obj, end = dec.raw_decode(raw, start)
            if end > at and isinstance(obj, dict) and 'doc' in obj: return start, end, obj
        except ValueError:
            pass
        start = raw.rfind('{', 0, start)
    raise SystemExit('entry not found')


def main(folder, doc, note):
    p = ROOT / 'targets' / folder / 'profile.json'
    raw = p.read_bytes().decode('utf-8')
    before = json.loads(raw)
    m = re.search(r'"doc":\s*' + re.escape(json.dumps(doc, ensure_ascii=False)) + r'\s*[,}]', raw)
    if not m: raise SystemExit(f'doc {doc!r} not found')
    start, end, obj = entry_span(raw, m.start())
    new = {}
    for k, v in obj.items():
        if k in ('state', 'note'): continue
        new[k] = v
        if k == 'doc': new['note'] = note
    new['state'] = 'decoded, not read'
    text = raw[start:end]
    if '\n' not in text:
        out_entry = json.dumps(new, ensure_ascii=False)
    else:
        nl = '\r\n' if '\r\n' in text else '\n'
        ind = re.search(r'\n([ \t]*)"', text).group(1)
        close = re.search(r'\n([ \t]*)\}\s*$', text).group(1)
        step = ind[len(close):] or ' '
        body = json.dumps(new, ensure_ascii=False, indent=len(step)).split('\n')
        out_entry = body[0] + ''.join(nl + close + line for line in body[1:])
    out = raw[:start] + out_entry + raw[end:]
    after = json.loads(out)
    tb = [t for t in before['outcome']['texts'] if t.get('doc') == doc][0]
    ta = [t for t in after['outcome']['texts'] if t.get('doc') == doc][0]
    assert {k: v for k, v in ta.items() if k not in ('state', 'note')} == {k: v for k, v in tb.items() if k not in ('state', 'note')}
    assert ta['state'] == 'decoded, not read' and ta['note'] == note
    p.write_bytes(out.encode('utf-8'))
    print(f'{folder} {doc}: decoded, not read')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
