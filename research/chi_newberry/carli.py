"""Search the Newberry CONTENTdm collections on collections.carli.illinois.edu (dmQuery, all fields)."""
import json, sys, time, requests
UA = {'User-Agent': 'cyphersolver research (catalogue sweep)'}
B = 'https://collections.carli.illinois.edu/digital/bl/dmwebservices/index.php?q='
COLLS = ['nby_chicago', 'nby_eeayer', 'nby_graff', 'nby_mms', 'nby_dig', 'nby_pullman', 'nby_rrlife', 'nby_music', 'nby_cgs']
def q(coll, term):
    t = term.replace(' ', '+')
    u = f'{B}dmQuery/{coll}/CISOSEARCHALL^{t}^all^and/title!date!descri/nosort/200/1/0/0/0/0/json'
    r = requests.get(u, headers=UA, timeout=60)
    if r.status_code in (403, 429): sys.exit('STOP %s' % r.status_code)
    return r.json()
if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    out = open('carli_hits.jsonl', 'a', encoding='utf-8')
    for term in sys.argv[1:]:
        for c in COLLS:
            try: d = q(c, term)
            except Exception as e: print('ERR', c, term, e); time.sleep(3); continue
            recs = d.get('records', []); tot = d.get('pager', {}).get('total')
            print(f'{term!r} {c} total={tot}')
            for x in recs:
                x['coll'] = c; x['term'] = term; out.write(json.dumps(x, ensure_ascii=False) + '\n')
                print('   ', x.get('pointer'), '|', str(x.get('date'))[:20], '|', str(x.get('title'))[:110])
            time.sleep(3)
