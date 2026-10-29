import json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from api import api, jwt
HERE = os.path.dirname(os.path.abspath(__file__))
tok = jwt(); out, start = [], 1
while True:
    d = api("list/Records?recperpage=500&start=%d" % start, tok)
    recs = d.get("records") or []; out += recs
    print(start, len(recs), d.get("totalRecordCount"), flush=True)
    if len(recs) < 500: break
    start += 500; time.sleep(1)
json.dump(out, open(os.path.join(HERE, "list_now.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("total", len(out))
