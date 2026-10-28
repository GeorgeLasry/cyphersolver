"""Huntington library catalog (III WebPAC, catalog.huntington.org) keyword sweep.

Pages through keyword results for each term (50 per page), keeps title, bib id, location and call number,
then fetches the full record for every hit whose location or call number is a manuscript (mss...).
One request every 3 s. Writes catalog_hits.json and catalog_records.json.
"""
import html, json, os, re, time, urllib.parse, urllib.request

BASE = "https://catalog.huntington.org"
UA = "cyphersolver-archive-sweep/1.0 (historical cipher research; polite, 1 req/3s)"
HERE = os.path.dirname(os.path.abspath(__file__))
TERMS = ["cipher", "cypher", "ciphers", "cyphers", "deciphered", "decyphered", "decipher", "cryptogram",
         "nomenclator", "chiffre", "secret writing", "invisible ink", "sympathetic ink", "in cipher",
         "partly in cipher", "cipher letter", "code telegram", "cipher telegram", "ciphers and codes", "cryptography",
         "cifra", "cipher key", "in code", "cipher manuscripts", "cyphers manuscripts", "cryptography manuscripts"]
last = [0.0]


def get(path):
    wait = 5 - (time.time() - last[0])
    if wait > 0:
        time.sleep(wait)
    req = urllib.request.Request(BASE + path, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        last[0] = time.time()
        return r.read().decode("utf8", "replace")


def strip(s):
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s))).strip()


def parse_page(t):
    out = []
    for cell in t.split('class="briefcitCell"')[1:]:
        bib = re.search(r'name="save" value="(b\d+)"', cell)
        title = re.search(r'class="briefcitTitle">(.*?)</h2>', cell, re.S)
        main = re.search(r'class="briefcitDetailMain">(.*?)<div class="briefcitRatings"', cell, re.S)
        items = re.findall(r'<tr\s+class="bibItemsEntry">(.*?)</tr>', cell, re.S)
        locs = []
        for it in items:
            tds = re.findall(r"<td[^>]*>(.*?)</td>", it, re.S)
            locs.append(" | ".join(strip(x) for x in tds))
        out.append({"bib": bib and bib.group(1), "title": title and strip(title.group(1)),
                    "detail": main and strip(main.group(1))[:400], "items": locs})
    return out


def search(term):
    q = urllib.parse.quote(term)
    t = get(f"/search~S0/?searchtype=X&searcharg={q}&SORT=D")
    m = re.search(r"KEYWORDS \(\d+-\d+ of (\d+)\)", t)
    if not m:
        # single-record result or no hits
        if "No matches found" in t or "NO ENTRIES FOUND" in t.upper():
            return 0, []
        bib = re.search(r"record=(b\d+)", t)
        return (1 if bib else 0), ([{"bib": bib.group(1), "title": strip(t[:0]), "single": True}] if bib else [])
    total = int(m.group(1))
    recs = parse_page(t)
    sub = urllib.parse.quote(term)
    start = 51
    while start <= total and start <= 1000:
        p = f"/search?/X{sub}&SORT=D/X{sub}&SORT=D&SUBKEY={sub}/{start}%2C{total}%2C{total}%2CB/browse"
        recs += parse_page(get(p))
        start += 50
    return total, recs


def is_ms(r):
    s = " ".join(r.get("items", [])) + " " + (r.get("title") or "")
    return bool(re.search(r"\bmss\b|\bmss[A-Z]|Manuscripts|HM \d|\bHM\d", s, re.I) or r.get("single"))


def main():
    hp = os.path.join(HERE, "catalog_hits.json")
    hits = json.load(open(hp, encoding="utf8")) if os.path.exists(hp) else {}
    for term in TERMS:
        if term in hits:
            continue
        total, recs = search(term)
        hits[term] = {"total": total, "records": recs}
        print(term, total, sum(is_ms(r) for r in recs), flush=True)
        json.dump(hits, open(hp, "w", encoding="utf8"), indent=1, ensure_ascii=False)
    rp = os.path.join(HERE, "catalog_records.json")
    recs = json.load(open(rp, encoding="utf8")) if os.path.exists(rp) else {}
    bibs = {}
    for term, h in hits.items():
        for r in h["records"]:
            if r.get("bib") and is_ms(r):
                bibs.setdefault(r["bib"], set()).add(term)
    for bib, terms in sorted(bibs.items()):
        if bib in recs:
            continue
        t = get(f"/record={bib}~S0")
        body = re.search(r'class="bibDetail"(.*?)class="bibLinks"|class="bibDetail"(.*)', t, re.S)
        txt = strip(t)
        i = txt.find("Author")
        recs[bib] = {"terms": sorted(terms), "text": txt[max(0, i - 50): i + 4000] if i >= 0 else txt[:4000]}
        json.dump(recs, open(rp, "w", encoding="utf8"), indent=1, ensure_ascii=False)
    print("ms records:", len(recs))


if __name__ == "__main__":
    main()
