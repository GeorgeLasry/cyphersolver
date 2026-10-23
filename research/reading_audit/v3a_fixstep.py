"""v3 verify (a): fix the last solution step's technique/result (splice save).

    python research/reading_audit/v3a_fixstep.py <folder> <technique> <result>
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save
T, tech, res = sys.argv[1:4]
p = load(T); s = p['solution'][-1]; s['technique'] = [tech]; s['result'] = res; save(T, p); print('fixed', T)
