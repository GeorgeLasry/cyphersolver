"""Search inside archive.org scans of the Huntington printed guides (BookReader full-text search).
Usage: python ia_inside.py <identifier> <server> <dir> <term> ...  ; prints page + snippet per hit."""
import json, sys, time, urllib.parse, urllib.request
ident, server, d = sys.argv[1:4]
for term in sys.argv[4:]:
    u = (f"https://{server}/fulltext/inside.php?item_id={ident}&doc={ident}&path={urllib.parse.quote(d)}"
         f"&q={urllib.parse.quote(term)}")
    r = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "cyphersolver-archive-sweep/1.0"}), timeout=60).read())
    hits = r.get("matches", [])
    print(f"## {ident} {term!r}: {len(hits)} hits")
    for m in hits:
        pg = m["par"][0].get("page") if m.get("par") else "?"
        print(f"  p{pg}: " + m["text"].replace("\n", " ").replace("{{{", "[").replace("}}}", "]")[:400])
    time.sleep(3)
