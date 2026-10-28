"""Fetch the OCR text of a digitised NARA description and print the pages that match a pattern.
    python research/chi_nara/ocr.py <naId> [regex]"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import client
def text(naid):
    objs, page = [], 1
    while True:
        d = client.get(f'extractedText/{naid}?limit=1000&page={page}')
        if not d: break
        objs += d.get('digitalObjects') or []
        if len(objs) >= (d.get('total') or 0) or not d.get('digitalObjects'): break
        page += 1
    return objs
if __name__ == '__main__':
    naid = sys.argv[1]; pat = re.compile(sys.argv[2] if len(sys.argv) > 2 else r'cipher|cypher|decod|in code|secret ink|invisible', re.I)
    objs = text(naid)
    print(naid, len(objs), 'objects')
    for i, o in enumerate(objs):
        t = o.get('extractedText') or o.get('text') or ''
        if not isinstance(t, str): t = json.dumps(t)
        for m in pat.finditer(t):
            s = t[max(0, m.start()-250): m.end()+250].replace('\n', ' ')
            print(f'--- obj {i} {o.get("objectFilename") or o.get("objectId")}:', s)
