"""List file units under a series (ancestorNaId) with titles and dates; write raw/series_<id>.tsv."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import client
HERE = os.path.dirname(os.path.abspath(__file__))
def walk(sid, maxn=3000, extra=None):
    out, page = [], 1
    while True:
        p = dict(ancestorNaId=sid, limit=100, page=page)
        if extra: p.update(extra)
        d = client.search(**p)
        if not d or 'body' not in d: break
        hits = d['body']['hits']['hits']; total = d['body']['hits']['total']['value']
        for h in hits:
            r = h['_source'].get('record') or {}
            yr = [x.get('year') for x in (r.get('inclusiveStartDate'), r.get('coverageStartDate')) if isinstance(x, dict)]
            out.append((r.get('naId'), r.get('levelOfDescription'), yr[0] if yr else '', len(r.get('digitalObjects') or []),
                        (r.get('title') or '').replace('\t', ' '), (r.get('scopeAndContentNote') or '')[:300].replace('\n', ' ').replace('\t', ' ')))
        if not hits or len(out) >= min(total, maxn): break
        page += 1
    return out, total
if __name__ == '__main__':
    sid = sys.argv[1]; q = sys.argv[2] if len(sys.argv) > 2 else None
    rows, total = walk(sid, extra={'q': q} if q else None)
    with open(os.path.join(HERE, 'raw', f'series_{sid}{"_q" if q else ""}.tsv'), 'w', encoding='utf-8') as fh:
        for r in rows: fh.write('\t'.join(map(str, r)) + '\n')
    print(sid, 'total', total, 'got', len(rows))
