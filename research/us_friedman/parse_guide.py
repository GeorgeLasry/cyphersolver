"""Split Sheldon's "The Friedman Collection: An Analytical Guide" (Marshall Foundation, Sept 2014; Wayback copy)
into items and list those that look like ciphertexts (cryptograms, cipher letters, unsolved messages).

Input: cache/guide.txt (text of the 646-page PDF). Output: cache/items.json, cache/hits.txt
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
t = open(os.path.join(HERE, "cache", "guide.txt"), encoding="utf8").read()
t = re.sub(r"\n=== p(\d+)\n\d+ *\n", r"\n[[p\1]]\n", t)

parts = re.split(r"\n\s*(Items?\s+[0-9][0-9.,\-\s/a-z&]*?)(?=\s{2,}|\n|[A-Z“\"])", t)
items = []
page = 1
for k in range(1, len(parts) - 1, 2):
    head, body = parts[k].strip(), parts[k + 1]
    pm = re.findall(r"\[\[p(\d+)\]\]", parts[k - 1])
    if pm:
        page = int(pm[-1])
    items.append({"item": head, "page": page, "text": re.sub(r"\s+", " ", re.sub(r"\[\[p\d+\]\]", " ", body)).strip()})
json.dump(items, open(os.path.join(HERE, "cache", "items.json"), "w", encoding="utf8"), ensure_ascii=False, indent=0)

KEY = re.compile(r"cryptogram|unsolved|undeciphered|not (been )?solved|never (been )?solved|unread|unbroken|"
                 r"cipher (letter|message|text|document|manuscript)|coded (letter|message)|in cipher|enciphered|"
                 r"secret writing|sent (to|him) (for|a)|submitted|challenge|puzzle|treasure|mystery|"
                 r"solution was|could not|no solution|attempt(s|ed)? to (solve|decipher)|decipher", re.I)
DROP = re.compile(r"Voynich|Beale|Shakespeare|Bacon|Kryptos|Zodiac|Dorabella", re.I)
with open(os.path.join(HERE, "cache", "hits.txt"), "w", encoding="utf8") as f:
    n = 0
    for it in items:
        if KEY.search(it["text"]):
            n += 1
            flag = " [famous]" if DROP.search(it["text"]) else ""
            f.write(f"## {it['item']} (p.{it['page']}){flag}\n{it['text'][:900]}\n\n")
print(len(items), "items;", n, "keyword hits")
