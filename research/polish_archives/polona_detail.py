"""Fetch full Polona records for manuscript hits in polona_hits.jsonl and keep those whose text really mentions a cipher.

    python research/polish_archives/polona_detail.py   # writes polona_cipher.jsonl
"""
import json, os, re, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
RX = re.compile(r'szyfr|\bcyfr[ąaey]\b|chiffr|ziffer|geheimschrift|\bcifr|kryptogra|tajnopis|nomenklator', re.I)


def get(uid):
    url = f'https://polona.pl/api/search-service/search/{uid}'
    with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'cyphersolver research sweep'}),
                                timeout=60) as r:
        return json.load(r)


def main():
    out = []
    for line in open(os.path.join(HERE, 'polona_hits.jsonl'), encoding='utf-8'):
        f = json.loads(line)
        mt = ' '.join(f.get('metatype') or []).lower()
        if not ('rękopis' in mt or 'listy' in mt or 'list' == mt or 'dokument' in mt):
            continue
        if 'muzycz' in mt:
            continue
        try:
            d = get(f['id'])
        except Exception as e:
            print('ERR', f['id'], e); continue
        fields = {}
        for grp in ('basicFields', 'expandedFields', 'hiddenFields'):
            for k, v in (d.get(grp) or {}).items():
                fields[k] = v.get('values')
        text = json.dumps(fields, ensure_ascii=False)
        hits = [text[max(0, m.start() - 200):m.end() + 200] for m in RX.finditer(text)]
        if hits:
            out.append({'id': f['id'], 'fields': fields, 'snippets': hits})
            print('HIT', f['id'][:8], (fields.get('title') or [''])[0][:100])
        time.sleep(0.3)
    with open(os.path.join(HERE, 'polona_cipher.jsonl'), 'w', encoding='utf-8') as fh:
        for o in out:
            fh.write(json.dumps(o, ensure_ascii=False) + '\n')
    print(len(out), 'records mention a cipher')


if __name__ == '__main__':
    main()
