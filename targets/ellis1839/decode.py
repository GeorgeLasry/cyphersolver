"""Decode this folder's transcription with the JQA code table (../jqa/code_table.tsv, used unchanged). The code is
in the shared script ../appleton1823/decode.py (same output, same options); this file only points it at this folder:

    python decode.py ellis1839_transcription.txt              group-by-group decryption, line by line
    python decode.py ellis1839_transcription.txt --controls   wrong-key controls

Python standard library only.
"""
import os, runpy, sys

HERE = os.path.dirname(os.path.abspath(__file__))
if len(sys.argv) > 1 and not os.path.isabs(sys.argv[1]):
    sys.argv[1] = os.path.join(HERE, sys.argv[1])
runpy.run_path(os.path.join(HERE, '..', 'appleton1823', 'decode.py'), run_name='__main__')
