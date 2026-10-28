"""enigma_scan.py <naId> [...]: frames of cached reels (nara_reels/cache) holding Enigma-like traffic: 15+ five-letter
groups in one case whose pooled letter IC is under 0.048 (flat, as Enigma output is). Prints frame, group count, IC, the
message header (date/time/letter count/indicator) and whether the frame or its neighbours carry clear German of a
decipherment (many lowercase German words, 'Entzifferung', 'Klartext')."""
import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
C = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'nara_reels', 'cache')
DE = re.compile(r'\b(der|die|das|und|nicht|mit|von|ist|auf|für|fuer|wird|werden|nach|bei|zur|zum|den|dem|des|ein|eine)\b', re.I)


def groups(t):
    g = re.findall(r'\b[A-Za-z]{5}\b', t)
    return [x for x in g if x.isupper() or x.islower()]


def ic(gs):
    s = ''.join(gs).upper(); n = len(s)
    return sum(s.count(c) * (s.count(c) - 1) for c in set(s)) / max(1, n * (n - 1))


def scan(nid, mn=15):
    T = json.load(open(os.path.join(C, f'{nid}.txt.json'), encoding='utf-8'))
    R = json.load(open(os.path.join(C, f'{nid}.rec.json'), encoding='utf-8'))
    fn = {str(d['objectId']): d.get('objectFilename', '') for d in R.get('digitalObjects', [])}
    txt = [re.sub(r'\s+', ' ', o.get('extractedText') or '') for o in T]
    out = []
    for i, t in enumerate(txt):
        g = groups(t)
        if len(g) < mn: continue
        # drop real words before measuring
        gg = [x for x in g if not DE.fullmatch(x)]
        v = ic(gg)
        if v >= 0.048: continue
        hdr = re.findall(r'\b\d{4}\s*-\s*\d{2,3}\s*-\s*[a-zA-Z]{3}\s*[a-zA-Z]{3}\b|\b\d{1,2}\s*\.?\s*T(?:L|eil|LE)\b[^A-Z]{0,12}\d{2,3}|\b\d{1,2}\.\s?\d{1,2}\.\s?(?:19)?\d{2}\b', t)[:4]
        near = [j for j in (i - 2, i - 1, i + 1, i + 2) if 0 <= j < len(txt) and len(DE.findall(txt[j])) >= 25 and len(groups(txt[j])) < 15]
        dec = bool(re.search(r'Entziff|Klartext|entschl', t + ' '.join(txt[j] for j in near), re.I))
        out.append((fn.get(T[i]['objectId'], T[i]['objectId']), len(g), round(v, 4), hdr, [fn.get(T[j]['objectId']) for j in near], dec, t[:260]))
    return R.get('title'), out


if __name__ == '__main__':
    for nid in sys.argv[1:]:
        title, out = scan(nid)
        print(f'## {nid} {title}: {len(out)} frames')
        for f, n, v, hdr, near, dec, head in out:
            print(f'  {f} groups={n} ic={v} hdr={hdr} clear_near={near} dec={dec}')
            print('     ', head)
