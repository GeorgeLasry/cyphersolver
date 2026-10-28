"""Test archive.org dictionary editions against the page.row anchors.

For each edition: fetch its hOCR search text, page index and printed page numbers,
then count how many anchors (page, word) put the word on that printed page,
also trying constant page offsets in case the edition's pagination differs.
Usage: python test_editions.py CACHE_DIR ID [ID ...]
"""
import gzip, json, os, re, sys, urllib.request
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def anchors():
    out = []
    for line in open(os.path.join(HERE, 'dict_refs_from_wordbank.tsv'), encoding='utf-8'):
        ref, word = line.rstrip('\n').split('\t')
        m = re.match(r'(\d+)\.\[(\d+)\]([-=^])', ref)
        word = word.strip('?').lower()
        if m and m.group(3) != '^' and word.isalpha():
            out.append((int(m.group(1)), int(m.group(2)), m.group(3), word))
    return sorted(set(out))


def fetch(cache, ident, suffix):
    path = os.path.join(cache, ident + suffix)
    if not os.path.exists(path):
        url = f'https://archive.org/download/{ident}/{ident}{suffix}'
        urllib.request.urlretrieve(url, path)
    data = open(path, 'rb').read()
    return gzip.decompress(data) if suffix.endswith('.gz') else data


def pages(cache, ident):
    text = fetch(cache, ident, '_hocr_searchtext.txt.gz').decode('utf-8', 'replace')
    index = json.loads(fetch(cache, ident, '_hocr_pageindex.json.gz'))
    leaves = [text[a:b].lower() for a, b, *_ in index]
    try:
        nums = json.loads(fetch(cache, ident, '_page_numbers.json'))['pages']
        printed = {}
        for p in nums:
            if str(p.get('pageNumber', '')).isdigit():
                printed.setdefault(int(p['pageNumber']), p['leafNum'])
    except Exception:
        printed = {}
    return leaves, printed


def score(ident, cache):
    leaves, printed = pages(cache, ident)
    words = [set(re.findall(r'[a-z]+', t)) for t in leaves]
    an = anchors()
    # leaf offset fit: anchor page p is on leaf p + k
    best = Counter()
    for p, r, col, w in an:
        for k in range(-5, 60):
            leaf = p + k
            if 0 <= leaf < len(words) and w in words[leaf]:
                best[k] += 1
    k, hits = best.most_common(1)[0] if best else (None, 0)
    hit_pn = sum(1 for p, r, col, w in an if p in printed and printed[p] < len(words) and w in words[printed[p]])
    rows = [(p, w) for p, r, col, w in an if 0 <= p + k < len(words) and w in words[p + k]]
    return dict(id=ident, leaves=len(leaves), anchors=len(an), offset=k, hits=hits,
                hits_printed=hit_pn, max_printed=max(printed) if printed else None,
                sample=rows[:8])


if __name__ == '__main__':
    cache = sys.argv[1]
    for ident in sys.argv[2:]:
        try:
            print(json.dumps(score(ident, cache)), flush=True)
        except Exception as e:
            print(json.dumps(dict(id=ident, error=repr(e))), flush=True)
