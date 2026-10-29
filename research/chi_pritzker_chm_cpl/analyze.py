"""Grep cached finding aids (raw/pmml/*.pdf, raw/cpl/*.txt) for cipher terms; write hits.txt and counts.json."""
import glob, re, json, collections, sys
import pymupdf

TERMS = {
    "cipher": r"cipher", "cypher": r"cypher", "decipher": r"decipher", "cryptogram": r"cryptogram",
    "crypto": r"cryptograph|cryptolog", "code message": r"code[ds]? (message|letter|telegram|cable|dispatch)|coded (message|letter)",
    "code book": r"code ?book|code book", "secret writing": r"secret writing|secret ink|invisible ink|sympathetic ink",
    "secret code": r"secret code", "in code": r"\bin code\b|\bcoded\b|encoded|encrypt|enciph",
    "signal code": r"signal code|signal book|wigwag|semaphore", "northwest conspiracy": r"northwest(ern)? conspiracy|camp douglas|sons of liberty",
    "telegram": r"telegraph cipher|military telegraph",
}
docs = {}
for f in glob.glob("raw/pmml/*.pdf"):
    try:
        d = pymupdf.open(f)
        docs["pmml:" + f.split("/")[-1].split("\\")[-1]] = re.sub(r"\s+", " ", " ".join(p.get_text() for p in d))
    except Exception as e:
        docs["pmml:" + f] = ""
for f in glob.glob("raw/cpl/*.txt") + glob.glob("raw/cplfa/*.txt"):
    t = open(f, encoding="utf8").read()
    u, _, body = t.partition("\n")
    docs["cpl:" + u] = re.sub(r"\s+", " ", body)

counts = collections.defaultdict(lambda: collections.Counter())
out = []
for name, t in sorted(docs.items()):
    inst = name.split(":")[0]
    for k, rx in TERMS.items():
        ms = list(re.finditer(rx, t, re.I))
        if ms:
            counts[inst][k] += len(ms)
            counts[inst][k + " (docs)"] += 1
            for m in ms[:4]:
                out.append("%s | %s | %s" % (name, k, t[max(0, m.start() - 200): m.end() + 250]))
open("hits.txt", "w", encoding="utf8").write("\n".join(out))
json.dump({k: dict(v) for k, v in counts.items()}, open("counts.json", "w"), indent=1)
print({i: sum(1 for n in docs if n.startswith(i)) for i in ("pmml", "cpl")})
for i, c in counts.items():
    print(i, dict(c))
