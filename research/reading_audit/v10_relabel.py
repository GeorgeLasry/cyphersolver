"""v10 (24 Oct 2026): apply the README read bar to every document marked read.

The 22-23 Oct audit marked a document "read" when it built coherent sentences (about 0.60 clean sentences). The
project's read bar is stricter: 95% of the words read as sense. This pass measures read_share = 1 - (explicit holes + doubtful
words) / (words + holes), counted after v2_score.holes, (every [?word], supplied [word], {?}, part-word, unread sign and unvalued code is a hole)
for every entry whose state is read, records it in the entry, and moves entries under 0.95 to "read in part".

    python research/reading_audit/v10_relabel.py            dry run: tsv on stdout, summary on stderr
    python research/reading_audit/v10_relabel.py --apply    write the profiles

Entries with no local text to measure (external pointers, unspaced scripts) are left as they are and listed.
Each changed profile gets one solution step. Only the touched entries are rewritten; the rest keeps its layout.
"""
import json, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'docs')); sys.path.insert(0, str(ROOT / 'research' / 'reading_audit'))
import _texts, v2_score as v2
import _check_reading as cr

BAR = 0.95
NUM = re.compile(r'^\s*(?:[A-Z]?\d+[a-z]?|[A-Z]\d+\.\d+)[.:)]?\s+')
STEP_RE = re.compile(r'\n([ \t]*)\{')


def running(text):
    """Reading body as running text: line labels cut and words broken at a line end joined, when the file is numbered."""
    body = v2.body_of(text)
    lines = [l for l in body.split('\n') if l.strip()]
    if lines and sum(bool(NUM.match(l)) for l in lines) > 0.5 * len(lines):
        out = ''
        for l in lines:
            if l.lstrip().startswith(('#', '==')): continue
            l = NUM.sub('', l).strip()
            out = out[:-1] + l if out.endswith('-') else (out + ' ' + l if out else l)
        return out
    return body


WORD = re.compile(r'[^\W\d_]+')


def share(text):
    """(words read, holes) on the reading body: holes are the explicit markers left by v2_score.holes ([?] for every
    [?word], supplied [word], {?}, part-word, unread sign and unvalued code) plus each doubtful word marked (?).
    Markdown tables, headings and notes after the reading are not counted."""
    body = running(text)
    body = '\n'.join(l for l in body.split('\n') if not l.lstrip().startswith(('|', '#', '>')))
    b = v2.holes(body)
    holes = b.count('[?]')
    doubtful = len(re.findall(r'\(\?\)', b))
    words = len(WORD.findall(b.replace('[?]', ' ')))
    return words, holes, doubtful


def measure(folder, t):
    lang = (t.get('language') or '').split('-')[0]
    if lang in ('zh', 'ja'): return None
    files = _texts.listify(t.get('reading')) or _texts.listify(t.get('decryption'))
    best = None
    for r in files:
        f = ROOT / 'targets' / folder / str(r)
        if str(r).startswith('http') or not f.is_file() or f.suffix.lower() in ('.pdf', '.json', '.tsv'): continue
        words, holes, doubtful = share(f.read_text(encoding='utf8', errors='replace'))
        if words < 5: continue
        rs = round(1 - (holes + doubtful) / (words + holes), 3)   # a doubtful word is already among the words
        if best is None or rs > best[1]: best = (str(r), rs, words)
    return best


def rewrite_entry(raw, idx, fn):
    """Apply fn(dict) to outcome.texts[idx], rewriting only that object in the file's own style."""
    dec = json.JSONDecoder()
    m = re.search(r'"texts":\s*\[', raw)
    pos, n = m.end(), -1
    while True:
        pos = raw.index('{', pos)
        obj, end = dec.raw_decode(raw, pos)
        n += 1
        if n == idx:
            start = pos
            break
        pos = end
    new = fn(dict(obj))
    text = raw[start:end]
    if '\n' not in text:
        out = json.dumps(new, ensure_ascii=False)
    else:
        nl = '\r\n' if '\r\n' in text else '\n'
        ind = re.search(r'\n([ \t]*)"', text).group(1)
        close = re.search(r'\n([ \t]*)\}\s*$', text).group(1)
        step = ind[len(close):] or ' '
        body = json.dumps(new, ensure_ascii=False, indent=len(step)).split('\n')
        out = body[0] + ''.join(nl + close + line for line in body[1:])
    return raw[:start] + out + raw[end:]


def add_step(raw, step):
    """Append one step to the top-level "solution" list, in the list's own style."""
    d = json.loads(raw)
    if not isinstance(d.get('solution'), list) or not d['solution']: return raw
    m = re.search(r'"solution":\s*\[', raw)
    dec = json.JSONDecoder()
    pos, last_end = m.end(), None
    while True:
        j = raw.find('{', pos)
        k = raw.find(']', pos)
        if j == -1 or (k != -1 and k < j): break
        _, e = dec.raw_decode(raw, j)
        last_end = pos = e
    if last_end is None: return raw
    ind = STEP_RE.search(raw[m.end():last_end])
    nl = '\r\n' if '\r\n' in raw else '\n'
    item = json.dumps(step, ensure_ascii=False)
    piece = (',' + nl + ind.group(1) + item) if ind else (', ' + item)
    out = raw[:last_end] + piece + raw[last_end:]
    assert len(json.loads(out)['solution']) == len(d['solution']) + 1
    return out


def main(apply):
    print('folder\tidx\tdoc\tfile\twords\tread_share\tstate_now')
    changed, unmeasured = {}, []
    for p in sorted((ROOT / 'targets').glob('*/profile.json')):
        raw = p.read_bytes().decode('utf-8')
        d = json.loads(raw)
        o = d.get('outcome') or {}
        if o.get('texts_withheld'): continue
        moves = []
        for i, t in enumerate(o.get('texts') or []):
            if _texts.entry_state(t) != 'read': continue
            m = measure(p.parent.name, t)
            doc = '/'.join(map(str, _texts.listify(t.get('doc'))))
            if m is None:
                unmeasured.append((p.parent.name, i, doc))
                continue
            f, rs, words = m
            st = 'read' if rs >= BAR else 'read in part'
            print(f'{p.parent.name}\t{i}\t{doc}\t{f}\t{words}\t{rs}\t{st}')
            moves.append((i, rs, st, f))
        if not moves: continue
        changed[p.parent.name] = moves
        if not apply: continue
        for i, rs, st, f in moves:
            def fn(e, rs=rs, st=st, f=f):
                e['read_share'] = rs
                if st == 'read in part':
                    e['state'] = 'read in part'
                    note = (f'24 Oct 2026: {rs * 100:.1f}% of the words of {f} read as sense (v2_score explicit holes); '
                            'coherent sentences but under the 95% read bar, so read in part.')
                    e['note'] = (e['note'] + ' ' + note) if e.get('note') else note
                return e
            raw = rewrite_entry(raw, i, fn)
        n_part = sum(1 for m in moves if m[2] == 'read in part')
        if n_part:
            raw = add_step(raw, {'date': '2026-10-24', 'kind': 'verification',
                                 'what': f'Read bar applied per document (v10): {n_part} of {len(moves)} documents marked '
                                         'read measure under 95% of words read as sense (v2_score explicit holes) and are '
                                         'now read in part; read_share recorded for each.',
                                 'result': 'partial'})
        json.loads(raw)
        p.write_bytes(raw.encode('utf-8'))
    n = sum(len(v) for v in changed.values())
    part = sum(1 for v in changed.values() for m in v if m[2] == 'read in part')
    print(f'# measured {n} read entries in {len(changed)} targets; {part} under 0.95 -> read in part; '
          f'{len(unmeasured)} not measurable: ' + ', '.join(f'{a}#{b}' for a, b, _ in unmeasured), file=sys.stderr)


if __name__ == '__main__':
    main('--apply' in sys.argv)
