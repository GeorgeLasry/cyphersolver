"""CPL digital collections (CONTENTdm cdm16818.contentdm.oclc.org): term counts and hits per collection."""
import subprocess, json, time, urllib.parse, collections

HOST = "https://cdm16818.contentdm.oclc.org"
terms = ["cipher", "cypher", "ciphered", "in cipher", "decipher", "cryptogram", "code message", "code telegram",
         "code book", "coded", "secret writing", "secret code", "invisible ink", "Confederate cipher", "signal code",
         "Northwest Conspiracy", "cryptography", "enciphered", "Camp Douglas", "secret service"]


def get(u):
    r = subprocess.run(["curl", "-sL", "-m", "90", "-A", "Mozilla/5.0 (research; polite)", u], capture_output=True).stdout
    try:
        return json.loads(r)
    except Exception:
        return None


cols = get(HOST + "/digital/api/collections")
json.dump(cols, open("cpl_cdm_collections.json", "w"), indent=1)
res = {}
for t in terms:
    d = get("%s/digital/api/search/collection/all/searchterm/%s/field/all/mode/all/conn/and/maxRecords/100"
            % (HOST, urllib.parse.quote(t)))
    time.sleep(3)
    if not d:
        print(t, "ERR", flush=True)
        continue
    items = [(i["collectionAlias"], i["itemId"], i["title"]) for i in d["items"]]
    res[t] = {"total": d["totalResults"], "items": items}
    c = collections.Counter(a for a, _, _ in items)
    print(t, d["totalResults"], dict(c), flush=True)
json.dump(res, open("cpl_cdm_hits.json", "w"), indent=1)
