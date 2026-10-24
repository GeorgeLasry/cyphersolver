"""Riksarkivet sweep: title search via data.riksarkivet.se/api/records for cipher words."""
import json, time, urllib.request, urllib.parse, re
TERMS = ["chiffer","chiffrerad","chiffrerade","chifferbrev","chiffernyckel","chiffernycklar","chiffre","chiffres",
         "dechiffrering","dechiffrerade","dechiffrerad","cifra","geheimschrift","nomenklator","nomenclator",
         "chifferskrift","chiffrer","dechiffr*","chiffer*","ziffer","cipher","déchiffré"]
out = {}
for t in TERMS:
    off = 0
    while True:
        u = "https://data.riksarkivet.se/api/records?" + urllib.parse.urlencode({"text": t, "max": 100, "offset": off})
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "curl/8.0", "Accept": "application/json"}), timeout=60))
        except Exception as e:
            print(t, off, "ERR", e); break
        items = d.get("items", [])
        for it in items:
            m = it.get("metadata", {})
            rec = out.setdefault(it["id"], {"id": it["id"], "terms": [], "caption": it.get("caption"),
                "type": it.get("type"), "objectType": it.get("objectType"),
                "referenceCode": m.get("referenceCode"), "date": m.get("date"),
                "hierarchy": " > ".join(h["caption"] for h in m.get("hierarchy", [])),
                "institution": ", ".join(a["caption"] for a in m.get("archivalInstitution", [])),
                "digitised": m.get("onlyDigitisedMaterials"), "url": it.get("_links", {}).get("html")})
            if t not in rec["terms"]: rec["terms"].append(t)
        print(t, off, d.get("totalHits"), len(items))
        off += 100
        if not items or off >= d.get("totalHits", 0) or off >= 1000: break
        time.sleep(0.5)
def year(s):
    y = re.findall(r"\b(1[0-9]{3})\b", s or ""); return int(y[0]) if y else None
rows = sorted(out.values(), key=lambda r: (year(r["date"]) or 9999))
for r in rows: r["year"] = year(r["date"])
json.dump(rows, open(__file__.replace("harvest.py", "hits.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(rows), "unique;", sum(1 for r in rows if r["year"] and r["year"] < 1950), "pre-1950")
