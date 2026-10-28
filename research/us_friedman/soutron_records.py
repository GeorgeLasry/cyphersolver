"""Fetch Marshall Foundation library (Soutron portal) record pages by CID and print the metadata.

Usage: python -I soutron_records.py 1785-1835 1900-1912 ...   (writes cache/records.json)
Polite: one request every 3 s, stops on 403/429.
"""
import html, json, re, sys, time, urllib.request, os

UA = "cyphersolver-research/1.0 (historical cipher catalogue sweep)"
BASE = "https://library.marshallfoundation.org/portal/Default/en-US/RecordView/Index/{}"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "cache", "records.json")


def parse(h):
    t = re.sub(r"<script.*?</script>|<style.*?</style>", " ", h, flags=re.S)
    t = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t)))
    i = t.find("CID:")
    j = t.find("Contact:", i)
    title = re.search(r'"og:title","ContentAttr":"content","ContentValue":"([^"]*)', h)
    objs = sorted(set(re.findall(r"objectId=(\d+)&(?:amp;)?ownerType=0&(?:amp;)?ownerId=(\d+)", h)))
    return {"title": html.unescape(title.group(1)) if title else "", "meta": t[i:j].strip() if i >= 0 else "",
            "objects": [o for o, _ in objs]}


def main():
    ids = []
    for a in sys.argv[1:]:
        if "-" in a:
            x, y = map(int, a.split("-"))
            ids += range(x, y + 1)
        else:
            ids.append(int(a))
    data = json.load(open(OUT, encoding="utf8")) if os.path.exists(OUT) else {}
    for cid in ids:
        if str(cid) in data:
            continue
        req = urllib.request.Request(BASE.format(cid), headers={"User-Agent": UA})
        try:
            h = urllib.request.urlopen(req, timeout=60).read().decode("utf8", "replace")
        except urllib.error.HTTPError as e:
            print(cid, "HTTP", e.code)
            if e.code in (403, 429):
                break
            time.sleep(3)
            continue
        rec = parse(h)
        data[str(cid)] = rec
        print(cid, rec["title"], "|", rec["meta"][:200], "| obj", rec["objects"])
        json.dump(data, open(OUT, "w", encoding="utf8"), ensure_ascii=False, indent=1)
        time.sleep(3)


if __name__ == "__main__":
    main()
