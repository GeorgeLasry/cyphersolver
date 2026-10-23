"""b06: decode kurtz1639 R3812 with key.json plus the proposed corrections below, writing read/R3812.txt.

    python research/reading_audit/b06_r3812_decode.py
key.json is not edited (proposals for the parent session); this wrapper applies them for R3812 only.
  38 = d (key.json: g): every occurrence in R3812 reads d (und, feindt, landt, tausendt, wird, freundt, die,
       folgendem, ad congressum ...), and the same holds in every other letter (kwic over all nine).
"""
import os, sys
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'targets', 'kurtz1639')
sys.path.insert(0, HERE)
os.chdir(HERE)
import decode
OVERRIDE = {'38': 'd'}
h, s = decode.loadkey()
s.update(OVERRIDE)
open(os.path.join(HERE, 'read', 'R3812.txt'), 'w', encoding='utf-8').write(decode.decode_record('R3812', h, s))
print('read/R3812.txt written with', OVERRIDE)
