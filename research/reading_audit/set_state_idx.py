"""Set outcome.texts[<idx>] to "decoded, not read" with a note and no reading_review, by rewriting that entry only.

    python research/reading_audit/set_state_idx.py <folder> <idx> "<note>"

For entries that share a "doc" value (set_state.py matches the first one). Layout of the rest of the file is kept.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent


def main(folder, idx, note):
    idx = int(idx)
    p = ROOT / 'targets' / folder / 'profile.json'
    raw = p.read_bytes().decode('utf-8')
    before = json.loads(raw)
    target = before['outcome']['texts'][idx]
    dec = json.JSONDecoder()
    # walk the texts array to the idx-th object
    m = re.search(r'"texts":\s*\[', raw)
    pos, n = m.end(), -1
    while True:
        pos = raw.index('{', pos)
        obj, end = dec.raw_decode(raw, pos)
        n += 1
        if n == idx:
            assert obj == target
            start = pos
            break
        pos = end
    new = {}
    for k, v in obj.items():
        if k in ('state', 'note', 'reading_review'): continue
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
    ta = after['outcome']['texts'][idx]
    assert ta['state'] == 'decoded, not read' and 'reading_review' not in ta
    assert len(after['outcome']['texts']) == len(before['outcome']['texts'])
    p.write_bytes(out.encode('utf-8'))
    print(f'{folder} [{idx}]: decoded, not read')


if __name__ == '__main__':
    main(*sys.argv[1:4])
