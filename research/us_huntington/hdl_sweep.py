"""Huntington Digital Library (CONTENTdm) keyword sweep for cipher material.

Public dmwebservices API, one request every 3 s. Writes hdl_hits.json (raw hits per term)
and hdl_items.json (item info for each distinct top-level object outside the Eckert collection).
Usage: python hdl_sweep.py
"""
import json, os, sys, time, urllib.parse, urllib.request

BASE = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = "cyphersolver-archive-sweep/1.0 (historical cipher research; polite, 1 req/3s)"
HERE = os.path.dirname(os.path.abspath(__file__))
TERMS = ["cipher", "cypher", "ciphers", "cyphers", "ciphered", "cyphered", "decipher", "decypher",
         "deciphered", "decyphered", "code", "cryptogram", "nomenclator", "chiffre", "secret writing",
         "invisible ink", "sympathetic ink", "in cipher", "cifra", "cypher key", "telegraphic code", "coded"]
last = [0.0]


def get(q):
    wait = 3 - (time.time() - last[0])
    if wait > 0:
        time.sleep(wait)
    req = urllib.request.Request(BASE + q, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        last[0] = time.time()
        return json.loads(r.read().decode("utf8"))


def search(term):
    t = urllib.parse.quote(term.replace(" ", "+"), safe="+")
    out, start = [], 1
    while True:
        d = get(f"dmQuery/all/CISOSEARCHALL^{t}^all^and/title!date!descri!subjec/title/1024/{start}/0/0/0/0/json")
        recs = d.get("records", [])
        out += recs
        total = int(d["pager"]["total"])
        start += 1024
        if start > total or not recs:
            return total, out


def main():
    hits_path = os.path.join(HERE, "hdl_hits.json")
    hits = json.load(open(hits_path, encoding="utf8")) if os.path.exists(hits_path) else {}
    for term in TERMS:
        if term in hits:
            continue
        total, recs = search(term)
        hits[term] = {"total": total, "records": recs}
        print(term, total, flush=True)
        json.dump(hits, open(hits_path, "w", encoding="utf8"), indent=0)
    # distinct top-level objects, Eckert excluded
    tops = {}
    for term, h in hits.items():
        for r in h["records"]:
            coll = r["collection"].strip("/")
            if coll == "p16003coll11":
                continue
            p = r["parentobject"]
            ptr = r["pointer"] if p in (-1, "-1") else int(p)
            tops.setdefault((coll, ptr), set()).add(term)
    items_path = os.path.join(HERE, "hdl_items.json")
    items = json.load(open(items_path, encoding="utf8")) if os.path.exists(items_path) else {}
    for (coll, ptr), terms in sorted(tops.items()):
        key = f"{coll}/{ptr}"
        if key in items:
            items[key]["terms"] = sorted(terms)
            continue
        try:
            info = get(f"dmGetItemInfo/{coll}/{ptr}/json")
        except Exception as e:  # noqa
            info = {"error": str(e)}
        info = {k: v for k, v in info.items() if v not in ({}, "", None)}
        info["terms"] = sorted(terms)
        items[key] = info
        json.dump(items, open(items_path, "w", encoding="utf8"), indent=1, ensure_ascii=False)
    json.dump(items, open(items_path, "w", encoding="utf8"), indent=1, ensure_ascii=False)
    print("distinct objects:", len(items))


if __name__ == "__main__":
    main()
