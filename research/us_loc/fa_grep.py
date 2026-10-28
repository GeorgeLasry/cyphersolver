"""Grep LoC finding-aid PDFs (container lists) for cipher terms (Oct 2026 LoC sweep).

findingaids.loc.gov refuses scripted search (403), but each digitised collection's JSON names its EAD id(s)
and the PDF of each finding aid is published at
tile.loc.gov/storage-services/service/gdc/gdcfindingaidpdfs/<msid>/<msid>.pdf.

    LOC_GAP=6.5 python fa_grep.py            -> fa_hits.json {collection: {msid: [context lines]}}
"""
import io, json, os, re, sys, time, urllib.request
import locapi

HERE = os.path.dirname(os.path.abspath(__file__))
WORD = re.compile(r'cipher|cypher|ciphered|decipher|cryptog|code[sd]?\b|secret ink|invisible ink|sympathetic ink|nomenclat', re.I)
NOISE = re.compile(r'zip code|code of conduct|civil code|penal code|legal code|code of laws|building code|morse code|code of ethics', re.I)
KEEP = re.compile(r'papers|records|collection of|diary|correspondence|journals', re.I)


def pdf_text(msid):
    url = f'https://tile.loc.gov/storage-services/service/gdc/gdcfindingaidpdfs/{msid}/{msid}.pdf'
    cache = os.path.join(HERE, 'raw', msid + '.txt')
    if os.path.exists(cache):
        return open(cache, encoding='utf-8').read()
    wait = locapi.GAP - (time.time() - locapi._last[0])
    if wait > 0:
        time.sleep(wait)
    locapi._last[0] = time.time()
    req = urllib.request.Request(url, headers={'User-Agent': locapi.UA})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            data = r.read()
    except Exception as e:
        if getattr(e, 'code', None) == 403:
            raise locapi.Blocked(url)
        return ''
    import fitz
    doc = fitz.open(stream=io.BytesIO(data), filetype='pdf')
    txt = '\n'.join(p.get_text() for p in doc)
    open(cache, 'w', encoding='utf-8').write(txt)
    return txt


def main():
    cols = json.load(open(os.path.join(HERE, 'collections_list.json'), encoding='utf-8'))
    p = os.path.join(HERE, 'fa_hits.json')
    out = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}
    for c in cols:
        if not KEEP.search(c['title']) or c['title'] in out:
            continue
        if re.search(r'folk|music|lomax|whitman|naacp|suffrage|motion|quilt|ballet|dance', c['title'], re.I):
            continue
        try:
            d = locapi.get(c['url'].split('?')[0] + '?fo=json')
            ids = sorted(set(re.findall(r'eadmss\.(ms\d{6})', json.dumps(d))))
            res = {}
            for msid in ids[:4]:
                t = pdf_text(msid)
                lines = [ln.strip() for ln in t.splitlines() if WORD.search(ln) and not NOISE.search(ln)]
                res[msid] = {'chars': len(t), 'hits': lines[:60]}
            out[c['title']] = res
        except locapi.Blocked as e:
            print('BLOCKED', e)
            break
        except Exception as e:
            print('skip', c['title'], type(e).__name__, e)
            continue
        print(c['title'][:60], {k: len(v['hits']) for k, v in res.items()}, flush=True)
        json.dump(out, open(p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)


if __name__ == '__main__':
    main()
