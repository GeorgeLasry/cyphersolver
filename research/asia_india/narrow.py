"""Narrow-query harvest that needs no paging: each query's first page (10 items) under four sort orders.

PaginationScroll drew HTTP 403 from the WAF on 28 Oct 2026 after the first parallel harvest, so this script
uses only AdvanceSearchV3 first pages. Output: hits/narrow.jsonl (one line per item per query).
usage: python narrow.py
"""
import json
import sys
import time
import urllib.parse

import ap

SORTS = ['dc.date.issued,asc', 'dc.date.issued,desc', 'dc.title,asc', 'dc.title,desc']

KW = ['Kabul', 'Amir', 'Russian', 'German', 'Persia', 'Bokhara', 'Kashgar', 'Tibet', 'Nepal', 'Mandalay', 'Japanese',
      'Turkish', 'Berlin', 'Bolshevik', 'communist', 'Ghadr', 'revolutionary', 'conspiracy', 'agent', 'spy', 'intercepted',
      'seized', 'Maharaja', 'Sindia', 'Holkar', 'Mysore', 'Lahore', 'Sikh', 'French', 'mutilated', 'unintelligible', 'key',
      'native', 'Persian', 'Resident']
QUERIES = [({'title': w}) for w in ['cypher letter', 'letters in cypher', 'written in cypher', 'written in cipher',
    'key to the cypher', 'secret code', 'code book', 'undecyphered', 'undeciphered', 'decypher', 'decipher',
    'intercepted telegram', 'intercepted message', 'intercepted wireless', 'wireless intercept', 'secret characters',
    'secret writing', 'invisible ink', 'sympathetic ink', 'cryptograph', 'cryptography', 'code words',
    'Hindu German conspiracy', 'German plot', 'Silk letter', 'cipher letter', 'communist code', 'anarchist code']]
QUERIES += [{'title': t, 'keywords': k} for t in ['cypher', 'cipher'] for k in KW]
QUERIES += [{'keywords': 'cipher'}, {'keywords': 'cypher'}, {'keywords': 'decipher'}, {'subject': 'cypher'}, {'subject': 'cipher'},
            {'title': 'code', 'keywords': 'Ghadr'}, {'title': 'code', 'keywords': 'German'}, {'title': 'code', 'keywords': 'conspiracy'},
            {'title': 'secret', 'keywords': 'cypher'}, {'title': 'letter', 'keywords': 'cypher'}, {'title': 'letter', 'keywords': 'cipher'},
            {'title': 'رمز'}, {'title': 'Tippoo'}, {'title': 'Tipu', 'keywords': 'cypher'}, {'title': 'Carnatic', 'keywords': 'cypher'},
            {'title': 'Ghadr', 'keywords': 'cipher'}, {'title': 'Ghadr', 'keywords': 'code'}, {'title': 'Ghadr', 'keywords': 'key'},
            {'title': 'conspiracy', 'keywords': 'cipher'}, {'title': 'conspiracy', 'keywords': 'cypher'},
            {'title': 'intercepted', 'keywords': 'cypher'}, {'title': 'intercepted', 'keywords': 'cipher'}, {'title': 'intercepted', 'keywords': 'code'}]


def main():
    out = open('hits/narrow.jsonl', 'a', encoding='utf8')
    log = open('narrow.log', 'a', encoding='utf8')
    done = {}
    try:
        for l in open('narrow.log', encoding='utf8'):
            k, n, _ = l.rstrip('\n').split('\t')
            done[k] = int(n)
    except FileNotFoundError:
        pass
    for q in QUERIES:
        for s in SORTS:
            key = '&'.join(f'{f}={v}' for f, v in q.items()) + '|' + s
            if key in done:
                n_done = done[key]
                if n_done <= 10 or (n_done <= 20 and s == SORTS[1]):
                    break
                continue
            p = {f: v + ',contains' for f, v in q.items()}
            p['sort'] = s
            h = ap.get(ap.BASE + 'AdvanceSearchV3?' + urllib.parse.urlencode(p))
            n = ap.total(h)
            rs = ap.parse(h)
            for r in rs:
                r['_q'] = key
                r['_total'] = n
                out.write(json.dumps(r, ensure_ascii=False) + '\n')
            out.flush()
            log.write(f'{key}\t{n}\t{len(rs)}\n'); log.flush()
            print(key, n, len(rs), flush=True)
            if n >= 0 and n <= 10:
                break  # one sort suffices
            if n <= 20 and s == SORTS[1]:
                break  # date asc + desc cover all
            if n < 0:
                break
            time.sleep(4)


if __name__ == '__main__':
    main()
