"""Harvest DigitArq (digitarq.arquivos.pt) simple-search hits for cipher terms.

Endpoint (found from the Next.js bundle, Oct 2026):
  GET https://digitarq.arquivos.pt/api/docs/search?query=<q>&fromIndex=<n>&max=<m>
  -> {"results": [...], "total": N}; results carry referenceCode, titles, dates, filesCount, id.
Item page: https://digitarq.arquivos.pt/documentDetails/<id>

archiveCode=ANTT restricts to Torre do Tombo. Writes hits.jsonl (one line per unique id, with the terms that matched). Keeps all archives;
filter PT/TT/ afterwards.
"""
import json, sys, time, urllib.parse, urllib.request, pathlib

HERE = pathlib.Path(__file__).parent
OUT = HERE / "hits.jsonl"
BASE = "https://digitarq.arquivos.pt/api/docs/search?"

# The search is fuzzy (cifra also hits Cufra, Citra), so every term is harvested in full for
# archiveCode=ANTT (Torre do Tombo) and the hits are filtered later on the full description.
TERMS = sys.argv[1:] or [
    "cifra", "cifras", "cifrada", "cifradas", "cifrado", "cifrados", "em cifra", "decifrada",
    "decifrado", "decifrar", "decifra", "chave da cifra", "caracteres", "letra secreta",
    "criptografia", "cifrar", "contracifra", "cyfra", "zifra", "cartas cifradas", "carta cifrada",
    "cifra de", "decifrada", "cifradas", "chaves de cifra", "segredo cifra",
]


def get(url):
    for i in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "cyphersolver research"}), timeout=90) as r:
                return json.load(r)
        except Exception as e:
            print("retry", url, e, file=sys.stderr)
            time.sleep(3 * (i + 1))
    return None


def main():
    seen = {}
    if OUT.exists():
        for line in OUT.open(encoding="utf8"):
            r = json.loads(line)
            seen[r["id"]] = r
    for term in TERMS:
        n = 0
        frm = 0
        total = None
        while True:
            d = get(BASE + urllib.parse.urlencode({"query": term, "fromIndex": frm, "max": 100, "archiveCode": "ANTT"}))
            if not d:
                break
            total = d.get("total")
            res = d.get("results") or []
            for r in res:
                rid = r["id"]
                rec = seen.get(rid) or {
                    "id": rid,
                    "ref": (r.get("referenceCode") or {}).get("value") or r.get("value"),
                    "archive": r.get("archiveCode"),
                    "level": (r.get("descriptionLevel") or {}).get("value"),
                    "d1": (r.get("dateInitial") or {}).get("value"),
                    "d2": (r.get("dateFinal") or {}).get("value"),
                    "title": " | ".join(t["value"] for t in r.get("titles") or []),
                    "files": r.get("filesCount"),
                    "terms": [],
                }
                if term not in rec["terms"]:
                    rec["terms"].append(term)
                seen[rid] = rec
            n += len(res)
            frm += len(res)
            if not res or frm >= (total or 0) or frm >= 5000:
                break
            time.sleep(0.5)
        print(term, "total", total, "fetched", n, file=sys.stderr)
        with OUT.open("w", encoding="utf8") as f:
            for r in seen.values():
                f.write(json.dumps(r, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
