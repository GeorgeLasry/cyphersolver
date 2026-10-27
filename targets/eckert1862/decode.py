"""Apply a cipher-book key to the code words of the ledger telegrams.

The ledgers already give each telegram in reading order (the route transposition undone); what is
left is the code-word layer. Every word that is a printed code word of the key book is replaced by
its handwritten meaning in [brackets]; the left word of a two-meaning line takes the first meaning,
the right word the second. Plain words are left as they are.

    python decode.py "mssEC 25"                # all telegrams of one ledger -> decoded/<callid>.txt
    python decode.py "mssEC 25" --stats        # code-word coverage only
"""
import collections, csv, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SUFFIX = ('ing', 'ed', 's', 'es', 'd')


def load_key(path=os.path.join(HERE, 'key_book1_mssEC43.tsv')):
    key = {}
    with open(path, encoding='utf8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            sec = (r['section'] or '').lower()
            if sec in ('route', 'numerals', 'loose leaf') or not r['meaning'] or r['struck'] == 'yes':
                continue
            m = r['meaning'].split(' | ')
            for side, w in ((0, r['left_word']), (1, r['right_word'])):
                w = (w or '').strip()
                if w and re.fullmatch(r"[A-Za-z']+", w):
                    key.setdefault(w.lower(), m[min(side, len(m) - 1)].strip())
    return key


def lookup(key, w):
    lw = w.lower()
    if lw in key:
        return key[lw]
    for s in SUFFIX:  # "Add ed or ing to Arbitrary"
        if lw.endswith(s) and lw[:-len(s)] in key:
            return key[lw[:-len(s)]] + ' +' + s
    return None


def decode(text, key):
    out, hits, words = [], 0, 0
    for tok in re.split(r'(\s+)', text):
        core = re.sub(r"^[^A-Za-z']+|[^A-Za-z']+$", '', tok)
        if not core:
            out.append(tok)
            continue
        words += 1
        v = lookup(key, core)
        if v:
            hits += 1
            out.append(f'{tok}[{v}]')
        else:
            out.append(tok)
    return ''.join(out), hits, words


def main():
    callid = sys.argv[1]
    key = load_key()
    rows = [json.loads(l) for l in open(os.path.join(HERE, 'data', 'telegrams.jsonl'), encoding='utf8')]
    rows = [r for r in rows if r['callid'] == callid]
    used = collections.Counter()
    H = W = 0
    os.makedirs(os.path.join(HERE, 'decoded'), exist_ok=True)
    lines = []
    for r in rows:
        d, h, w = decode(r['text'], key)
        H += h
        W += w
        for tok in re.findall(r"([A-Za-z']+)\[", d):
            used[tok.lower()] += 1
        lines.append(f"== {r['page']} #{r['n']}\n{d}\n")
    print(f'{callid}: {len(rows)} telegrams, {W} words, {H} replaced by the key ({H / max(W, 1):.1%})')
    print('most used:', ', '.join(f'{w}={key.get(w, "?")}:{n}' for w, n in used.most_common(30)))
    if '--stats' not in sys.argv:
        with open(os.path.join(HERE, 'decoded', callid.replace(' ', '') + '.txt'), 'w', encoding='utf8') as f:
            f.write(''.join(lines))


if __name__ == '__main__':
    main()
