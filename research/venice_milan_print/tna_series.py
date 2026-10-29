"""TNA Discovery API: cipher terms within the Italian State Papers series (SP 99 Venice, SP 85 Italian States, SP 98 Tuscany, SP 79 Genoa, SP 92 Savoy, SP 93 Sicily-Naples)."""
import json, subprocess, time, urllib.parse
U = "https://discovery.nationalarchives.gov.uk/API/search/records"
out = open("tna_italy_hits.jsonl", "w", encoding="utf-8")
seen = set()
for series in ["SP 99", "SP 85", "SP 98", "SP 79", "SP 92", "SP 93", "SP 104"]:
    for term in ["cipher", "cypher", "decipher", "decypher", "cifra", "zifra", "chiffre", "deciphered", "characters"]:
        p = {"sps.searchQuery": term, "sps.recordSeries": series, "sps.resultsPageSize": 100, "sps.page": 1}
        r = subprocess.run(["curl", "-s", "-m", "60", U + "?" + urllib.parse.urlencode(p), "-H", "Accept: application/json"], capture_output=True)
        try:
            j = json.loads(r.stdout.decode("utf8"))
        except Exception:
            print(series, term, "ERR", r.stdout[:100]); continue
        n = 0
        for rec in j.get("records", []):
            if not rec.get("reference", "").startswith(series): continue
            n += 1
            if rec["id"] in seen: continue
            seen.add(rec["id"])
            out.write(json.dumps({k: rec.get(k) for k in ["id", "reference", "title", "description", "coveringDates"]}, ensure_ascii=False) + "\n")
        print(series, term, j.get("count"), n)
        time.sleep(1)
