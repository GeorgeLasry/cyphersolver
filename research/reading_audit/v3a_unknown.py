"""v3 verify (a): list the words of a reading body that the language's word list does not know (plain score holes).

    python research/reading_audit/v3a_unknown.py <file> <lang>
"""
import sys, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'docs')); sys.path.insert(0, str(ROOT / 'research/reading_audit')); sys.path.insert(0, str(ROOT))
import _check_reading as cr, v2_score as v2
from lang import lm
t = v2.holes(v2.body_of(pathlib.Path(sys.argv[1]).read_text(encoding='utf8')))
t = cr.CODE.sub(' ', t)
lex = cr.lexicon(sys.argv[2])
unk = [w for w in re.findall(r"[^\W\d_]+", t) if lm.norm(w, 'early').strip() not in lex and len(w) > 2]
print(len(unk), sorted(set(unk)))
