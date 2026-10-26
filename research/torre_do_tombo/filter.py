"""Filter details.jsonl to records whose title or description really mentions cipher, up to 1950.

python filter.py [details.jsonl crawl_*.jsonl ...] > filtered.txt   (one block per record, sorted by date)
"""
import json, re, sys, pathlib

HERE = pathlib.Path(__file__).parent
RX = re.compile(r"\b(de)?(cifr|cyfr|zifr|zyfr|cifer|cypher|cipher|chiffr|criptogr|letra secreta|"
                r"caracteres secretos|contra-?cifra|chave d[ae] cifra)\w*", re.I)
NEG = re.compile(r"\bcifra(s)? de (\d|réis|reis)|\bcifrões?\b", re.I)


def year(d):
    try:
        return int((d or "")[:4])
    except ValueError:
        return None


def main():
    files = sys.argv[1:] or ["details.jsonl"]
    rows = {}
    for fn in files:
        for l in (HERE / fn).open(encoding="utf8"):
            r = json.loads(l)
            rows[r["id"]] = r
    rows = list(rows.values())
    out = []
    for r in rows:
        text = " | ".join([*r["titles"], r.get("description") or "", r.get("history") or ""])
        if not RX.search(text):
            continue
        y = year(r["d1"])
        if y and y > 1950:
            continue
        out.append((y or 9999, r, text))
    out.sort(key=lambda t: (t[0], t[1]["ref"]))
    print(len(rows), "records;", len(out), "mention cipher, <=1950 or undated", file=sys.stderr)
    for y, r, text in out:
        print(f"{r['ref']}  {r['d1']}..{r['d2']}  lvl={r['level']} img={r['hasImages']} rep={r['nrep']} kids={r['children']} lang={','.join(r['languages'])}")
        print(f"   id={r['id']} quota={'; '.join(q for q in r['quota'] if q)}")
        print(f"   parent={r['parent']} {r['parent_title'][:80]}")
        print("   " + re.sub(r"\s+", " ", text)[:1200])


if __name__ == "__main__":
    main()
