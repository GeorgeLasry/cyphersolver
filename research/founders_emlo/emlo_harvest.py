"""Harvest EMLO (Early Modern Letters Online) works that mention cipher/code, via its open Solr cores.

    python research/founders_emlo/emlo_harvest.py

Writes research/founders_emlo/emlo_hits.json: one record per work with author, recipient, date, abstract,
keywords, notes (comments core) and manifestations (repository + shelfmark).
"""
import json, os, time, urllib.parse, urllib.request

BASE = 'https://emlo.bodleian.ox.ac.uk/solr/'
HERE = os.path.dirname(os.path.abspath(__file__))
TERMS = ['cipher', 'ciphers', 'ciphered', 'cypher', 'cyphers', 'cyphered', 'decipher', 'deciphered', 'decyphered',
         'chiffre', 'chiffres', 'chiffré', 'chiffrée', 'cijfer', 'cijfers', 'Geheimschrift', 'cifra', 'cifrado',
         'ziffer', 'Chiffren', 'Ziffern', '"in code"', 'nomenclator', 'cryptography', 'steganography', 'zyfer', 'cyffer']


def get(core, params):
    url = BASE + core + '/select?' + urllib.parse.urlencode(params, doseq=True)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (cyphersolver research sweep)'})
    for i in range(3):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.load(r)
        except Exception as e:  # noqa
            time.sleep(3 * (i + 1))
    raise RuntimeError(url)


def main():
    works = {}
    for t in TERMS:
        start = 0
        while True:
            d = get('works', {'q': t, 'rows': 200, 'start': start, 'wt': 'json'})
            docs = d['response']['docs']
            for doc in docs:
                w = works.setdefault(doc['uuid'], doc)
                w.setdefault('_terms', [])
                if t not in w['_terms']:
                    w['_terms'].append(t)
            n = d['response']['numFound']
            print(t, n, flush=True)
            start += 200
            if start >= n or start >= 3000:
                break
            time.sleep(0.5)
    # notes (comments core) that mention cipher, mapped back to their works
    extra = set()
    for t in TERMS:
        d = get('comments', {'q': t, 'rows': 1000, 'wt': 'json'})
        print('comments', t, d['response']['numFound'], flush=True)
        for c in d['response']['docs']:
            for wu in c.get('bibo_annotates-work', []) or []:
                extra.add((wu.split('/')[-1], t))
    for wid, t in sorted(extra):
        if wid in works:
            if t not in works[wid]['_terms']:
                works[wid]['_terms'].append(t)
            continue
        d = get('works', {'q': 'uuid:"%s"' % wid, 'rows': 1, 'wt': 'json'})
        for doc in d['response']['docs']:
            doc['_terms'] = ['note:' + t]
            works[wid] = doc
    # comments and manifestations
    def fetch_uris(core, uris):
        out = {}
        uris = list(uris)
        for i in range(0, len(uris), 40):
            chunk = uris[i:i + 40]
            q = ' OR '.join('uri:"%s"' % u.replace('http://localhost/', '//emlo.bodleian.ox.ac.uk/').split('/')[-1] for u in chunk)
            ids = ' OR '.join('"%s"' % u.split('/')[-1] for u in chunk)
            d = get(core, {'q': 'uuid:(%s)' % ids, 'rows': 100, 'wt': 'json'})
            for doc in d['response']['docs']:
                out[doc['uuid']] = doc
            time.sleep(0.3)
        return out
    com = set(); man = set()
    for w in works.values():
        com.update(w.get('comments', []) or [])
        com.update(w.get('ox_isAnnotatedBy-comment', []) or [])
        man.update(w.get('manifestations', []) or [])
    comments = fetch_uris('comments', com) if com else {}
    manifs = fetch_uris('manifestations', man) if man else {}
    for w in works.values():
        cids = set((w.get('comments') or []) + (w.get('ox_isAnnotatedBy-comment') or []))
        w['_notes'] = [comments.get(c.split('/')[-1], {}) for c in cids]
        w['_manifs'] = [manifs.get(m.split('/')[-1], {}) for m in (w.get('manifestations') or [])]
    json.dump(list(works.values()), open(os.path.join(HERE, 'emlo_hits.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=0)
    print('works', len(works), 'comments', len(comments), 'manifestations', len(manifs))


if __name__ == '__main__':
    main()
