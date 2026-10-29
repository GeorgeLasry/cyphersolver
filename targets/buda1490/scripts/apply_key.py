"""Decode a transcription of DL 46150 with the buda1489 key and score the result with lang/.

Usage (from the repo root): python targets/buda1490/scripts/apply_key.py transcription/p2.txt
Written for the moment images exist; not run on real data yet (there is no transcription).
Reuses targets/buda1489/decode.py for the sign->value table and lang/ for the language check.
"""
import sys, pathlib, importlib.util
root = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(root))
spec = importlib.util.spec_from_file_location("dec", root / "targets/buda1489/decode.py")
dec = importlib.util.module_from_spec(spec); spec.loader.exec_module(dec)
from lang import lm
def main(path):
    text = pathlib.Path(path).read_text(encoding="utf-8")
    out = dec.decode(text) if hasattr(dec, "decode") else text
    print(out)
    print(lm.best_language(out))
if __name__ == "__main__":
    main(sys.argv[1])
