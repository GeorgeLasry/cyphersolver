"""Write texts/<letter>_decryption.txt and texts/<letter>_reading.txt for every letter, and outcome.texts.

Decryption: each code group with its reading and grade, one line per manuscript line (from reading.tsv and the
transcription's image/line columns). Reading: the coded words in order, a word spread over several groups written
once; unread groups stay as [number]. The two hand-written files for 4 Jul 1787 and Barclay's footnotes are kept.
Run after make_reading.py.
"""
import csv, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from make_profile import DOCS  # noqa: E402
KEEP = {'tj_17870704', 'barclay_17870703'}
SUMMARY = {
    'barclay_17860410': "Barclay reports from Madrid that Lamb's mission to Algiers has failed: no peace without a larger sum, and the Dey refuses to treat.",
    'tj_17870925': "Jefferson tells Carmichael of Smith's mission to Portugal, the failure to march into Holland, and a possible triple alliance of France, Austria and Russia.",
    'tj_17870928': "Jefferson's postscript to Adams that France is arranging with the two empires; written by mistake in the Barclay code, which Adams could not read.",
    'tj_17871215': "A test line: the opening of Jefferson's letter of 14 June 1787 put into code so that Carmichael could check his copy of the code.",
    'carmichael_17880508': "Carmichael explains that his cipher was wrong, has had no official news from America, and sketches Floridablanca's tactics against Eden.",
    'carmichael_17880529': "Carmichael on the Swedish armaments, the Russian minister's suspicion of England, and a British ship carrying war stores to the Turks.",
    'tj_17880603': "Jefferson on Littlepage, the survey for a canal across the isthmus of Panama, and the new French minister's quarrel over etiquette.",
    'carmichael_17880605': "Carmichael on a Spanish ordinance meant to force a custom house on Biscay.",
    'carmichael_17880724': "Carmichael on the 1360/1363 error in his cipher, Littlepage, and Campomanes and Ulloa on the Panama canal.",
    'tj_17881225': "Jefferson asks Carmichael what is being concerted between the Spanish court and the Kentucky settlers.",
    'carmichael_17890126': "Carmichael on a French agent sent to visit the American back settlements and on Gayoso, sent as governor of the Natchez.",
    'tj_17890809': "Jefferson asks whether the provinces of Spain begin to talk of their rights, and reports Brabant in commotion.",
    'short_17891009': "Short on the October days: a party of the Duke of Orleans suspected of tampering with Lafayette's troops, and the royal family at the mercy of a mob.",
    'short_17891025': "Short on Mirabeau abandoning the Orleans party and seeking the ministry through Lafayette.",
    'short_17891028': "Short mentions the ransom of the American prisoners at Algiers.",
    'tj_17910411': "Jefferson urges Carmichael to work for a joint front against the British navigation act and for the free navigation of the Mississippi.",
}


def word(r):
    w = r.strip()
    w = re.sub(r'\s*[\[(]\d+/[\d?]+[\])]?.*$', '', w)
    return w.replace('(', '').replace(')', '').strip()


def same(a, b):
    return b is not None and a.rstrip('?') == b.rstrip('?')


def main():
    rows = list(csv.DictReader(open(os.path.join(HERE, 'reading.tsv'), encoding='utf-8'), delimiter='\t'))
    tr = {}
    for name in {r['letter'] for r in rows}:
        t = list(csv.DictReader(open(os.path.join(HERE, 'transcription', name + '.tsv'), encoding='utf-8'),
                                delimiter='\t'))
        tr[name] = [x for x in t if (x.get('code') or '').strip() not in ('', '=')]
    os.makedirs(os.path.join(HERE, 'texts'), exist_ok=True)
    prof = json.load(open(os.path.join(HERE, 'profile.json'), encoding='utf-8'))
    keep = [t for t in prof['outcome'].get('texts', []) if t['doc'] in KEEP]
    texts = []
    order = [d['id'] for d in prof['documents']]
    for name in order:
        if name in KEEP:
            texts += [t for t in keep if t['doc'] == name]
            continue
        rs = [r for r in rows if r['letter'] == name]
        lines, cur, key = [], [], None
        words, last = [], None
        n = rd = 0
        for r, t in zip(rs, tr[name]):
            k = (t.get('image'), t.get('line'))
            if k != key and cur:
                lines.append(cur); cur = []
            key = k
            if r['grade'] == 'x':
                cur.append(f"{r['code']}[excluded]")
                continue
            n += 1
            rdg = r['reading']
            if rdg:
                rd += 1
                cur.append(f"{r['code']}[{rdg} {r['grade']}]")
                w = word(rdg)
                if w and not same(w, last):
                    words.append(w); last = w
            else:
                cur.append(f"{r['code']}[?]")
                words.append(f"[{r['code']}]"); last = None
        if cur:
            lines.append(cur)
        dec = os.path.join('texts', name + '_decryption.txt')
        rdp = os.path.join('texts', name + '_reading.txt')
        doc = next(d for d in prof['documents'] if d['id'] == name)
        with open(os.path.join(HERE, dec), 'w', encoding='utf-8') as f:
            f.write(f"# {doc['shelfmark']}\n# each group with its reading and grade (H contemporary decoding or clear sheet, "
                    f"C attested elsewhere, M editors' reading only, I conjecture); one line per manuscript line\n")
            for l in lines:
                f.write(' '.join(l) + '\n')
        with open(os.path.join(HERE, rdp), 'w', encoding='utf-8') as f:
            f.write(' '.join(words) + '\n')
        texts.append({'doc': name, 'label': DOCS[name][0],
                      'transcription': doc['length']['file'], 'decryption': dec.replace(os.sep, '/'),
                      'reading': rdp.replace(os.sep, '/'), 'summary': SUMMARY[name], 'language': 'en',
                      'read_share': round(rd / n, 3) if n else 0.0,
                      'state': 'read' if n and rd / n >= 0.95 else 'read in part'})
    prof['outcome']['texts'] = texts
    prof['outcome']['key_file'] = 'key.tsv'
    json.dump(prof, open(os.path.join(HERE, 'profile.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    open(os.path.join(HERE, 'profile.json'), 'a', encoding='utf-8').write('\n')
    print(len(texts), 'texts')


if __name__ == '__main__':
    main()
