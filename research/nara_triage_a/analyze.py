"""Per cached item: find code frames in the full OCR, name the code family by its signature groups, try the known keys.

    python analyze.py <naId> [...]        # summary per code frame
    python analyze.py <naId> --decode F   # decode frame number F (e.g. 0206) with every key, print side by side
"""
import json, os, re, sys, csv
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
CACHE = os.path.join(ROOT, 'research', 'nara_reels', 'cache')
YEAR = re.compile(r'^1[6-9]\d\d$')
SIG = {  # family: {group: word}
    'jqa': {'1385': 'the', '1576': 'of', '668': 'and', '1384': 'that', '1401': 'I'},
    'armstrong972': {'972': 'the', '1354': 'of'},
    'pinckney': {'1651': 'the', '133': 'of', '1343': 'and', '244': 'to', '1578': 'that'},
    'code11': {'1196': 'the', '1199': 'to', '1508': 'of', '1140': 'and', '708': 'that'},
}


def load_keys():
    keys = {}
    k = {}
    for line in open(os.path.join(ROOT, 'targets', 'jqa', 'code_table.tsv'), encoding='utf-8'):
        if line.startswith('#'):
            continue
        p = line.rstrip('\n').split('\t')
        if len(p) > 1 and p[0].isdigit():
            k[p[0]] = p[1]
    keys['jqa'] = k
    k = {}
    for kk, v in json.load(open(os.path.join(ROOT, 'targets', 'armstrong', 'code972_partial.json'), encoding='utf-8')).items():
        k[kk] = v[0]
    keys['armstrong972'] = k
    k = {}
    for line in open(os.path.join(ROOT, 'targets', 'erving1807aug', 'key_pinckney.tsv'), encoding='utf-8'):
        if line.startswith('#'):
            continue
        p = line.rstrip('\n').split('\t')
        if len(p) > 1 and p[0].isdigit():
            k[p[0]] = (p[1] or (p[2] if len(p) > 2 else '')) or '?'
    keys['pinckney'] = k
    k = {}
    for line in open(os.path.join(ROOT, 'targets', 'jefferson1787', 'key.tsv'), encoding='utf-8'):
        p = line.rstrip('\n').split('\t')
        if len(p) > 1 and p[0].isdigit():
            k[p[0]] = p[1]
    keys['code11'] = k
    return keys


def frames(naid):
    rec = json.load(open(os.path.join(CACHE, f'{naid}.rec.json'), encoding='utf-8'))
    txt = json.load(open(os.path.join(CACHE, f'{naid}.txt.json'), encoding='utf-8'))
    names = {o['objectId']: (o['objectFilename'], o['objectUrl']) for o in rec.get('digitalObjects') or []}
    for o in txt:
        fn, url = names.get(o['objectId'], (o['objectId'], ''))
        yield fn, url, o.get('extractedText') or ''


def groups(text):
    toks = text.split()
    g = [t.rstrip('.,;:-_') for t in toks]
    nums = [x for x in g if re.fullmatch(r'\d{1,4}', x) and not YEAR.match(x)]
    words = [t for t in toks if re.fullmatch(r'[A-Za-z]{3,}[.,;:]?', t)]
    return nums, words


def family(nums):
    sc = {f: sum(1 for x in nums if x in s) for f, s in SIG.items()}
    best = max(sc, key=sc.get)
    return best if sc[best] >= 2 else '?', sc


def summary(naid):
    rec = json.load(open(os.path.join(CACHE, f'{naid}.rec.json'), encoding='utf-8'))
    print(f"## {naid} {rec.get('title')}")
    for fn, url, text in frames(naid):
        nums, words = groups(text)
        big = [x for x in nums if len(x) >= 3]
        if len(big) < 15 or len(nums) < 0.3 * (len(nums) + len(words)):
            continue
        fam, sc = family(nums)
        print(f"  {fn} groups={len(nums)} words={len(words)} fam={fam} {sc}")


def decode(naid, frame):
    keys = load_keys()
    for fn, url, text in frames(naid):
        if frame in fn:
            nums, words = groups(text)
            print(url)
            for f, k in keys.items():
                hit = sum(1 for x in nums if x in k)
                print(f'[{f}] {hit}/{len(nums)}:', ' '.join(k.get(x, f'<{x}>') for x in nums)[:900])
            print('OCR:', ' '.join(text.split())[:1500])


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    a = sys.argv[1:]
    if '--decode' in a:
        decode(a[0], a[a.index('--decode') + 1])
    else:
        for n in a:
            if os.path.exists(os.path.join(CACHE, f'{n}.txt.json')):
                summary(n)
            else:
                print('## not cached', n)
