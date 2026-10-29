"""Europeana Record API (demo key) restricted to Venetian / Veneto data providers, cipher terms.
Writes dl/eu_hits.json and prints title | provider | id.
"""
import json, urllib.request, urllib.parse, time, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROVIDERS = ["New Manuscript Library, Veneto Region", "Marciana National Library",
             "Fondazione Giorgio Cini", "Fondazione Querini Stampalia", "Museo Correr",
             "Archivio di Stato di Venezia"]
TERMS = ["cifra", "cifre", "cifrato", "cifrata", "cifrate", "cifrati", "\"in cifra\"", "decifrazione", "deciferazione",
         "decifrata", "decifrato", "deciferata", "zifra", "ziffra", "cifrario", "chiave", "chiavi", "\"caratteri segreti\"",
         "crittografia", "steganografia", "\"scrittura segreta\"", "alfabeto", "occulta"]


def q(query, qf, cursor="*"):
    p = {"wskey": "api2demo", "query": query, "qf": qf, "rows": 100, "cursor": cursor, "profile": "standard"}
    url = "https://api.europeana.eu/record/v2/search.json?" + urllib.parse.urlencode(p, doseq=True)
    time.sleep(0.5)
    return json.load(urllib.request.urlopen(url, timeout=60))


def main():
    hits = {}
    for prov in PROVIDERS:
        for t in TERMS:
            try:
                r = q(t, [f'DATA_PROVIDER:"{prov}"'])
            except Exception as e:
                print("ERR", prov, t, e, file=sys.stderr); continue
            n = r.get("totalResults", 0)
            if n:
                print(f"## {prov} / {t}: {n}")
            for it in r.get("items", []):
                hits.setdefault(it["id"], {"id": it["id"], "title": it.get("title"), "provider": it.get("dataProvider"),
                                           "year": it.get("year"), "desc": it.get("dcDescription"),
                                           "link": it.get("guid"), "terms": []})["terms"].append(t)
    json.dump(list(hits.values()), open(os.path.join(HERE, "dl", "eu_hits.json"), "w", encoding="utf8"), ensure_ascii=False, indent=1)
    print(len(hits), "distinct")


if __name__ == "__main__":
    main()
