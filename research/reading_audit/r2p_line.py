"""r2p (23 Oct 2026), morosini1588: print transcription line(s) of a page as figures (dotted codes as NNN^.).

    python research/reading_audit/r2p_line.py R17 234r 1 [2]
"""
import os, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reread_b00_align as A

rec, page = sys.argv[1], sys.argv[2].lstrip('0').lower()
l1 = int(sys.argv[3]); l2 = int(sys.argv[4]) if len(sys.argv) > 4 else l1
F = A.page_items(rec)[page]
for ln in range(l1, l2 + 1):
    print(f'{page} l.{ln}: ' + ' '.join(x['val'] + ('^.' if x['kind'] == 'N' else '') + ('?' if x.get('unc') else '')
                                         for x in F if x['line'] == ln))
