"""Write candidates.json for the venice_milan_print sweep (Oct 2026) from the rows_*.py modules in this folder."""
import json, os, sys, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
FIELDS = ["year", "date", "title", "correspondents", "place", "language", "region", "period", "shelfmark", "folio_note",
          "cls", "status", "why", "importance", "solvability", "difficulty", "score_note", "verify", "links", "seen",
          "source", "prior_art", "decode_ids"]
rows = []
for mod in ["rows_sforza", "rows_print", "rows_outside"]:
    if os.path.exists(os.path.join(HERE, mod + ".py")):
        rows += importlib.import_module(mod).ROWS
out = []
for r in rows:
    missing = [f for f in FIELDS if f not in r and f != "decode_ids"]
    assert not missing, (r.get("title"), missing)
    out.append({f: r[f] for f in FIELDS if f in r})
json.dump(out, open(os.path.join(HERE, "candidates.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out), "rows")
