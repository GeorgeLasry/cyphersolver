"""Fetch full DigitArq records for the harvested hits (hits.jsonl -> details.jsonl).

  GET https://digitarq.arquivos.pt/api/docs/details/<id>
returns titles, description (scope and content), dates, languages, present quota, parent, rootParent,
hasImages. Incremental: ids already in details.jsonl are skipped.
"""
import json, sys, time, urllib.request, pathlib

HERE = pathlib.Path(__file__).parent
HITS = HERE / "hits.jsonl"
OUT = HERE / "details.jsonl"
URL = "https://digitarq.arquivos.pt/api/docs/details/"


def get(url):
    for i in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "cyphersolver research"}), timeout=90) as r:
                return json.load(r)
        except Exception as e:
            print("retry", url, e, file=sys.stderr)
            time.sleep(3 * (i + 1))
    return None


def v(x):
    return (x or {}).get("value") if isinstance(x, dict) else None


def slim(d):
    return {
        "id": d["id"],
        "ref": v(d.get("referenceCode")) or d.get("value"),
        "old_id": d.get("old_id"),
        "level": v(d.get("descriptionLevel")),
        "d1": v(d.get("dateInitial")),
        "d2": v(d.get("dateFinal")),
        "titles": [t.get("value") for t in d.get("titles") or []],
        "description": v(d.get("description")),
        "history": v(d.get("history")),
        "quota": [i.get("value") for i in d.get("identifiers") or []],
        "languages": [l.get("value") for l in d.get("languages") or []],
        "hasImages": d.get("hasImages"),
        "hasRep": d.get("hasPublishedRepresentations") or d.get("hasRepresentations"),
        "nrep": (d.get("relatedRepresentations") or {}).get("total"),
        "children": (d.get("children") or {}).get("total"),
        "parent": v(d.get("parent")),
        "parent_title": " | ".join(t.get("value") or "" for t in ((d.get("parent") or {}).get("titles") or [])),
        "root": v(d.get("rootParent")),
        "root_title": " | ".join(t.get("value") or "" for t in ((d.get("rootParent") or {}).get("titles") or [])),
        "extra": {k: d[k] for k in ("scopeContent", "notes", "note", "physicalCharacteristics", "relatedMaterial")
                  if k in d and d[k]},
    }


def main():
    done = set()
    if OUT.exists():
        done = {json.loads(l)["id"] for l in OUT.open(encoding="utf8")}
    ids = [json.loads(l) for l in HITS.open(encoding="utf8")]
    ids = [h for h in ids if h["id"] not in done and (h.get("ref") or "").startswith("PT/TT")]
    print(len(ids), "to fetch", file=sys.stderr)
    from concurrent.futures import ThreadPoolExecutor
    with OUT.open("a", encoding="utf8") as f, ThreadPoolExecutor(4) as ex:
        for k, d in enumerate(ex.map(lambda h: get(URL + h["id"]), ids)):
            if d:
                f.write(json.dumps(slim(d), ensure_ascii=False) + "\n")
                f.flush()
            if k % 100 == 0:
                print(k, file=sys.stderr, flush=True)


if __name__ == "__main__":
    main()
