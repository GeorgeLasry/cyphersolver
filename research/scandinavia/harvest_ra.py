"""Harvest Swedish Riksarkivet search hits for cipher terms via data.riksarkivet.se/api/records (sok.riksarkivet.se/api is WAF-blocked).

    python research/scandinavia/harvest_ra.py  -> research/scandinavia/ra_hits.jsonl
"""
import json, os, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
TERMS = ['apostill*', 'tolkade', 'krypterad*', 'Geheim*', 'uttydning*', 'osynlig*', 'tolkad*', '*chiffr*', '*chiffer*', 'sympatetiskt', 'klartext', 'chiffrerade depescher', 'chiffré*', 'chiff*', 'dechiffr*', 'ziffer*', 'ciffer*', 'deciffr*', 'zifer*', 'ciphr*', 'cipher*', 'geheim*schrift', 'lönnskrift*', 'chifr*', 'chiffer', 'chiffrerad', 'chiffrerat', 'chiffrerade', 'chiffre', 'chiffres', 'ziffer', 'ziffern', 'chiffreret',
         'geheimschrift', 'cifra', 'chifferbrev', 'chiffernyckel', 'chiffernycklar', 'dechiffrering',
         'dechiffrerade', 'dechiffrerad', 'dechiffrerat', 'deciffrerade', 'deciffrerad', 'cipher', 'chiffrer', 'chifrer',
         'chiffrerede', 'chiffer-brev', 'chifferskrift', 'chiffrerade brev', 'dechiffreringar', 'chiffra', 'zyffer',
         'ziffra', 'cifferbrev', 'chiffrade', 'hemlig skrift', 'lönnskrift', 'chiffrerad skrivelse', 'nyckel chiffer']
UA = {'User-Agent': 'Mozilla/5.0 (cyphersolver research)'}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def main():
    out = os.path.join(HERE, 'ra_hits.jsonl')
    seen = set()
    if os.path.exists(out):
        for line in open(out, encoding='utf-8'):
            seen.add(json.loads(line)['id'])
    fh = open(out, 'a', encoding='utf-8')
    for t in TERMS:
        off = 0
        while True:
            url = 'https://data.riksarkivet.se/api/records?' + urllib.parse.urlencode({'text': t, 'max': 100, 'offset': off})
            try:
                d = get(url)
            except Exception as e:
                print(t, off, 'ERR', e); break
            items = d.get('items', [])
            new = 0
            for it in items:
                if it['id'] in seen:
                    continue
                seen.add(it['id']); new += 1
                md = it.get('metadata', {})
                fh.write(json.dumps({'id': it['id'], 'term': t, 'caption': it.get('caption'), 'type': it.get('type'),
                                     'ref': md.get('referenceCode'), 'date': md.get('date'),
                                     'path': ' > '.join(h['caption'] for h in md.get('hierarchy', [])),
                                     'digitised': md.get('onlyDigitisedMaterials'),
                                     'html': it.get('_links', {}).get('html')}, ensure_ascii=False) + '\n')
            fh.flush()
            print(t, off, d.get('totalHits'), len(items), 'new', new)
            off += 100
            if not items or off >= d.get('totalHits', 0) or off >= 2000:
                break
            time.sleep(0.5)


if __name__ == '__main__':
    main()
