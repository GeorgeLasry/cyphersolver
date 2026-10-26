"""Walk a whole DigitArq fonds tree and save every record's full description.

python crawl.py PT/TT/MMCG <root-id>   -> crawl_PT_TT_MMCG.jsonl  (slim records, same shape as details.jsonl)

Children are listed with GET /api/docs/details/<id>?down=1&childrens=<id>&fromIndex=<n>&max=<m>
(childrens must repeat the record's own id, otherwise fromIndex/max are ignored and only 30 come back).
The search index is fuzzy and does not always surface every "Parte da carta está em cifra" item, so
fonds that turned out rich in cipher letters (MMCG, CPN) were crawled in full and filtered with filter.py.
"""
import json, sys, pathlib
from concurrent.futures import ThreadPoolExecutor
from details import get, slim

HERE = pathlib.Path(__file__).parent
BASE = "https://digitarq.arquivos.pt/api/docs/details/"
Q = "?down=1&childrens={}&fromIndex={}&max=200"


def children(rid, total_hint=None):
    out, frm = [], 0
    while True:
        d = get(BASE + rid + Q.format(rid, frm))
        if not d:
            break
        ch = (d.get("children") or {})
        res = ch.get("results") or []
        out += [c["id"] for c in res]
        frm += len(res)
        if not res or frm >= (ch.get("total") or 0):
            break
    return d, out


def main():
    name, root = sys.argv[1], sys.argv[2]
    path = HERE / ("crawl_" + name.replace("/", "_") + ".jsonl")
    done = set()
    if path.exists():
        done = {json.loads(l)["id"] for l in path.open(encoding="utf8")}
    frontier = [root]
    with path.open("a", encoding="utf8") as f, ThreadPoolExecutor(4) as ex:
        while frontier:
            results = list(ex.map(children, frontier))
            nxt = []
            for (d, kids) in results:
                if d and d["id"] not in done:
                    f.write(json.dumps(slim(d), ensure_ascii=False) + "\n")
                    done.add(d["id"])
                nxt += kids
            f.flush()
            print(len(done), "records; next level", len(nxt), file=sys.stderr, flush=True)
            frontier = nxt


if __name__ == "__main__":
    main()
