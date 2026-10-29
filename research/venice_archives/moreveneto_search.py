"""Search ASVe's moreveneto (Arianna4, asve.arianna4.cloud) GraphQL endpoint for cipher terms.

Query shape copied from the site's own request (search box + "Cerca in tutti i campi delle schede").
Writes dl/mv_<term>.json and prints id | label | breadcrumb.
Usage: python -I moreveneto_search.py term [term ...]
"""
import json, sys, urllib.request, os, time

URL = "https://asve.arianna4.cloud//apollo/"
HERE = os.path.dirname(os.path.abspath(__file__))

Q = """{ search(searchParameters: { totalCount: 0 gallery: false
 facets: [{ id: "query" type: "value" },{ id: "query-all" type: "value" data: [{ label: "x" value: "1" counter: null }] }]
 page: { offset: %(off)d limit: %(lim)d }
 results: { order: { type: "score" key: "_score" direction: "DESC" } fields: [{ id: "description" highlight: true limit: 400 }] }
 filters: [{ facetId: "query" value: %(term)s searchIn: [{ key: "label.ngrams" operator: "LIKE" }] },
           { facetId: "query-all" value: "1" searchIn: [{ key: "label.ngrams^5,text^4,fields.*^3" operator: "=" }] }] })
 { totalCount results { items {
   ... on Entity { id label typeOfEntity }
   ... on Item { id label title subTitle text breadcrumbs { label link } fields { ... on KeyValueField { key value } } }
 } } } }"""


def search(term, off=0, lim=100):
    body = json.dumps({"query": Q % {"term": json.dumps(term), "off": off, "lim": lim}}).encode()
    req = urllib.request.Request(URL, data=body, headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"})
    for k in range(4):
        try:
            time.sleep(1.5)
            return json.load(urllib.request.urlopen(req, timeout=60))
        except Exception as e:
            print('  retry', k, e, file=sys.stderr); time.sleep(10 * (k + 1))
    return {}


def main():
    for term in sys.argv[1:]:
        out, off = [], 0
        while True:
            r = search(term, off)
            s = r.get("data", {}).get("search") or {}
            items = (s.get("results") or {}).get("items") or []
            out += items
            tot = s.get("totalCount") or 0
            off += 100
            if off >= tot or not items or off >= 1000:
                break
        json.dump({"term": term, "total": tot, "items": out}, open(os.path.join(HERE, "dl", f"mv_{term.replace(' ', '_')}.json"), "w", encoding="utf8"), ensure_ascii=False, indent=1)
        print(f"## {term}: {tot}")
        for it in out:
            bc = " > ".join(b["label"] for b in (it.get("breadcrumbs") or []))
            print(" ", it.get("id"), "|", (it.get("label") or it.get("title") or "")[:120], "|", bc[:160])


if __name__ == "__main__":
    main()
