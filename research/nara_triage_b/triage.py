"""Slice B triage of the NARA bulk scan: RG 59 items 1906-1950, plus RG 84 and RG 76.

    python research/nara_triage_b/triage.py score  > research/nara_triage_b/scored.tsv
    python research/nara_triage_b/triage.py show <naId> [n]      # print snippets of an item's best frames
    python research/nara_triage_b/triage.py phrases               # every rare-phrase / desc hit in the slice

A frame "looks like code" when most of its tokens are bare 2-5 digit groups (no decimal commas or points), the
groups are not a running sequence (page/line numbers, years, table columns), and table vocabulary is absent.
"""
import collections, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'nara_reels', 'out')

# RG 59 publications in this slice (1906-1950). '-' items are filtered by title below.
PUBS59 = {'M862', 'M367', 'M973', 'M1442', 'T1249', 'M1751', 'M1284', 'M1286', 'M1889'}
NOT_MINE_DASH = re.compile(r'Territorial|17\d\d|18[0-9]\d', re.I)

TABLE = re.compile(r'\b(total|totals|table|tabel|tableau|tabelle|cuadro|summa|summe|population|tons?|kilo\w*|'
                   r'francs?|marks?|kronen|dollars?|pesos?|rubles?|imports?|exports?|average|per cent|percent|'
                   r'revenue|mileage|class|miles|census|year|ann[ée]e|jahr|a[ñn]o|fiscal|budget|quantity|value|'
                   r'valeur|wert|rate|rates|tariff|index|page|no\.|number|application|passport|serial|grade)\b', re.I)
TEL = re.compile(r'\b(telegram|cablegram|cable|cipher|cypher|code|decode\w*|decipher\w*|paraphrase|received|'
                 r'sent|gray|green|via|commercial)\b', re.I)


def slice_hit(rg, h):
    if rg != 59:
        return True
    p = ','.join(h['microform']) or '-'
    if p in PUBS59:
        return True
    if p == '-':
        anc = ' '.join(h['ancestors'])
        return not NOT_MINE_DASH.search(h['title'] + ' ' + anc)
    return False


def feats(snip):
    toks = snip.split()
    bare = [t for t in toks if re.fullmatch(r'\d{2,5}', t)]
    dotted = [t for t in toks if re.fullmatch(r'[\d.,]+', t) and re.search(r'\d[.,]\d', t)]
    words = [t for t in toks if re.fullmatch(r'[A-Za-z]{3,}', t)]
    vals = [int(t) for t in bare]
    up = sum(1 for a, b in zip(vals, vals[1:]) if 0 < b - a <= 3)
    seq = up / max(1, len(vals) - 1)
    years = sum(1 for v in vals if 1850 <= v <= 1950)
    tab = len(TABLE.findall(snip))
    tel = len(TEL.findall(snip))
    # code words: 5-10 letter all-caps tokens that are not English-looking (rough)
    caps = [t for t in toks if re.fullmatch(r'[A-Z]{5,10}', t)]
    s = len(bare) / max(1, len(toks)) - 0.5 * seq - 0.05 * tab - 0.3 * years / max(1, len(bare)) \
        - len(dotted) / max(1, len(toks))
    return dict(bare=len(bare), toks=len(toks), seq=round(seq, 2), years=years, tab=tab, tel=tel,
                dotted=len(dotted), caps=len(caps), words=len(words), score=round(s, 3))


def load(rg):
    for line in open(os.path.join(OUT, f'rg_{rg}.jsonl'), encoding='utf-8'):
        h = json.loads(line)
        if slice_hit(rg, h):
            yield h


def score():
    sys.stdout.reconfigure(encoding='utf-8')
    print('\t'.join(['rg', 'naId', 'pub', 'flagged', 'codeish', 'best', 'title', 'parent', 'best_file', 'snip']))
    for rg in (59, 84, 76):
        items = collections.OrderedDict()
        for h in load(rg):
            if h['kind'] != 'frame':
                continue
            f = feats(h['snippet'])
            it = items.setdefault(h['naId'], dict(h=h, n=0, code=0, best=-9, bf=None))
            it['n'] += 1
            if f['score'] > 0.35:
                it['code'] += 1
            if f['score'] > it['best']:
                it['best'], it['bf'] = f['score'], h
        for naid, it in items.items():
            h, b = it['h'], it['bf']
            print('\t'.join(map(str, [rg, naid, ','.join(h['microform']) or '-', it['n'], it['code'], it['best'],
                                      h['title'][:80], ' > '.join(h['ancestors'][1:])[:80], b['file'],
                                      ' '.join(b['snippet'].split())[:160]])))


def show(naid, n=8):
    sys.stdout.reconfigure(encoding='utf-8')
    hs = []
    for rg in (59, 84, 76):
        hs += [h for h in load(rg) if str(h['naId']) == naid and h['kind'] == 'frame']
    hs.sort(key=lambda h: -feats(h['snippet'])['score'])
    if hs:
        print(hs[0]['title'], '|', ' > '.join(hs[0]['ancestors']), '|', hs[0]['microform'], len(hs), 'frames')
    for h in hs[:n]:
        f = feats(h['snippet'])
        print('--', h['file'], h['objectId'], f)
        print('  ', ' '.join(h['snippet'].split())[:400])


def phrases():
    sys.stdout.reconfigure(encoding='utf-8')
    for rg in (59, 84, 76):
        for h in load(rg):
            if h['kind'] == 'frame':
                continue
            if h['kind'] == 'phrase' and h.get('phrase', '').lower() in ('in cipher', 'in cypher'):
                continue
            print(rg, h['kind'], h['naId'], ','.join(h['microform']) or '-', h['title'][:60], '|', h.get('file'),
                  '|', h.get('phrase', ''), '|', ' '.join(h.get('snippet', h.get('desc', '')).split())[:300])


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[0] == 'score':
        score()
    elif a[0] == 'show':
        show(a[1], int(a[2]) if len(a) > 2 else 8)
    elif a[0] == 'phrases':
        phrases()
