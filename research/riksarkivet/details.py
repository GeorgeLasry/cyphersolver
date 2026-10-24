"""Fetch skos:note / title for each pre-1900 non-flag hit from the json-ld record."""
import json, urllib.request, re
rows = json.load(open("hits.json", encoding="utf-8"))
H = {"User-Agent": "curl/8.0"}
for r in rows:
    r.pop("detail_err", None)
    if not r["year"] or r["year"] >= 1950 or "Fanritningar" in r["hierarchy"]: continue
    try:
        s = urllib.request.urlopen(urllib.request.Request("https://data.riksarkivet.se/archive/%s.jsonld" % r["id"], headers=H), timeout=60).read().decode("utf-8")
    except Exception as e:
        r["detail_err"] = str(e); continue
    d = json.loads(s)
    notes = []
    for g in d.get("@graph", []):
        for k in ("skos:note", "rico:scopeAndContent", "rico:title", "schema:name", "rico:descriptiveNote"):
            v = g.get(k)
            if isinstance(v, str): notes.append(v)
            elif isinstance(v, list): notes += [x for x in v if isinstance(x, str)]
    r["note"] = " | ".join(dict.fromkeys(notes))
    r["digitised_any"] = "digital" in s.lower()
    print(r["date"], r["referenceCode"], "||", r["note"][:500].replace("\n", " "))
json.dump(rows, open("hits.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
