"""Manus Online (ICCU) search API: POST /o/manus-api/titles-search-post (form fields as the site sends them).
Harvests every page for each query and keeps records held in Venice (title starts "Venezia,").
Usage: python -I manus_search.py "<query>" [AND|ONLY|OR]
Appends to dl/manus_hits.json.
"""
import json, os, re, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
API = "https://manus.iccu.sbn.it/o/manus-api/titles-search-post"


def page(q, mode, n):
    body = urllib.parse.urlencode({"monocampo": q, "n": "v", "monocampo:tipo": mode, "page": n}).encode()
    req = urllib.request.Request(API, data=body, headers={"Content-Type": "application/x-www-form-urlencoded",
                                                          "X-Requested-With": "XMLHttpRequest", "User-Agent": "Mozilla/5.0"})
    for k in range(3):
        try:
            time.sleep(1.0)
            txt = urllib.request.urlopen(req, timeout=60).read().decode("utf8", "replace")
            return json.loads(txt, strict=False)
        except Exception as e:
            print("retry", k, e, file=sys.stderr); time.sleep(8)
    return {}


def main():
    q = sys.argv[1]; mode = sys.argv[2] if len(sys.argv) > 2 else "AND"
    path = os.path.join(HERE, "dl", "manus_hits.json")
    hits = json.load(open(path, encoding="utf8")) if os.path.exists(path) else {}
    r = page(q, mode, 1); d = r.get("data", {})
    pages = d.get("pagination", {}).get("total", 1); total = d.get("total")
    print(f"## {q} [{mode}]: {total} records, {pages} pages")
    kept = 0
    for n in range(1, pages + 1):
        if n > 1:
            d = page(q, mode, n).get("data", {})
        for it in d.get("results", []):
            t = it["title"]["text"]
            if t.startswith("Venezia"):
                h = hits.setdefault(it["id"], {"id": it["id"], "title": t, "info": it["title"]["info"], "queries": []})
                if q not in h["queries"]:
                    h["queries"].append(q)
                kept += 1
    json.dump(hits, open(path, "w", encoding="utf8"), ensure_ascii=False, indent=1)
    print(f"   kept {kept} Venice records")


if __name__ == "__main__":
    main()
