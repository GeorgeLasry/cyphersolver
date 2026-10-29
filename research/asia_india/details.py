"""Fetch item-detail metadata (department, branch, file number, digitised flag) for given itemIds.

usage: python details.py <itemId> [...]   -> appends to details.jsonl
The item page embeds the record as HTML-escaped JSON; the page images are behind /Category/itemdetails/ReadContent
(POST, login required), so only metadata is read here.
"""
import html as H
import json
import re
import sys
import time

import ap

URL = 'https://www.abhilekh-patal.in/Category/ItemDetails/ItemDetails?itemId='
FIELDS = ['Name', 'Department', 'Branch', 'Year', 'FromYear', 'Place', 'Location', 'DigitizedCollection', 'Description',
          'Identifier', 'FileNumber', 'Pages', 'Category', 'FileType', 'PartNo', 'Series', 'Creator', 'Language', 'keywords']


def fetch(iid):
    h = ap.get(URL + iid)
    h = re.sub(r'data:image[^"]+', '', h)
    rec = {'itemId': iid}
    t = H.unescape(h)
    for f in FIELDS:
        m = re.search(r'"%s":(null|"(?:[^"\\]|\\.)*"|\[[^\]]*\])' % f, t)
        if m:
            try:
                rec[f] = json.loads(m.group(1))
            except Exception:
                rec[f] = m.group(1)
    m = re.search(r'name="ItemDetailsViewModel\.Name" value="([^"]*)"', h)
    if m:
        rec['Name'] = H.unescape(m.group(1))
    rec['url'] = URL + iid
    return rec


if __name__ == '__main__':
    with open('details.jsonl', 'a', encoding='utf8') as f:
        for iid in sys.argv[1:]:
            r = fetch(iid)
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
            print(json.dumps(r, ensure_ascii=False))
            time.sleep(5)
