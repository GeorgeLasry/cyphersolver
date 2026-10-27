"""Build the telegram corpus from the harvested Decoding the Civil War transcriptions.

Reads data/items/*.jsonl (harvest.py), splits each page's transcription into telegrams at blank
lines, and writes:
  data/telegrams.jsonl   one row per telegram: item, callid, ledger title, page, n, text
  ledgers.tsv            per item: callid, title, pages, transcribed pages, telegrams, words
  codewords.tsv          capitalised words used as code (in a cipher-book word list) per ledger

    python corpus.py
"""
import collections, glob, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ITEMS = os.path.join(HERE, 'data', 'items')


def telegrams(transc):
    blocks = re.split(r'\n\s*\n', transc.replace('\r', ''))
    return [b.strip() for b in blocks if len(b.split()) >= 4]


def main():
    vocab = set()
    vf = os.path.join(HERE, 'book1_words.txt')
    if os.path.exists(vf):
        vocab = {w.strip() for w in open(vf, encoding='utf8') if w.strip() and not w.startswith('#')}
    rows, ledgers, codes = [], [], collections.defaultdict(collections.Counter)
    for f in sorted(glob.glob(os.path.join(ITEMS, '*.jsonl'))):
        pages = [json.loads(l) for l in open(f, encoding='utf8')]
        if not pages:
            continue
        p0 = pages[0]
        n_tel = n_words = n_tr = 0
        for p in pages:
            if p['transc'].strip():
                n_tr += 1
            for k, t in enumerate(telegrams(p['transc'])):
                rows.append(dict(item=p['item'], callid=p['callid'], page=p['pagetitle'], n=k + 1, text=t))
                n_tel += 1
                n_words += len(t.split())
                for w in re.findall(r'\b[A-Z][a-z]+\b', t):
                    if w in vocab:
                        codes[p0['callid']][w] += 1
        ledgers.append((p0['callid'], p0['item'], p0['title'], len(pages), n_tr, n_tel, n_words))
    with open(os.path.join(HERE, 'data', 'telegrams.jsonl'), 'w', encoding='utf8') as out:
        for r in rows:
            out.write(json.dumps(r, ensure_ascii=False) + '\n')
    key = lambda l: int(re.sub(r'\D', '', l[0]) or 0)
    with open(os.path.join(HERE, 'ledgers.tsv'), 'w', encoding='utf8') as out:
        out.write('callid\titem\ttitle\tpages\ttranscribed_pages\ttelegrams\twords\n')
        for l in sorted(ledgers, key=key):
            out.write('\t'.join(map(str, l)) + '\n')
    if vocab:
        with open(os.path.join(HERE, 'codewords.tsv'), 'w', encoding='utf8') as out:
            out.write('callid\tcode_tokens\tdistinct\ttop\n')
            for c in sorted(codes, key=lambda c: int(re.sub(r'\D', '', c) or 0)):
                top = ' '.join(f'{w}:{n}' for w, n in codes[c].most_common(25))
                out.write(f'{c}\t{sum(codes[c].values())}\t{len(codes[c])}\t{top}\n')
    tr = [l for l in ledgers if l[4]]
    print(len(ledgers), 'items,', len(tr), 'with transcriptions,',
          sum(l[5] for l in tr), 'telegram blocks,', sum(l[6] for l in tr), 'words')


if __name__ == '__main__':
    main()
