"""Frames with telegram/cable vocabulary plus >= 8 bare 4-5 digit groups (code-number telegrams).
    python research/nara_triage_b/telegrams.py > research/nara_triage_b/telegrams.tsv"""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from triage import load
sys.stdout.reconfigure(encoding='utf-8')
TEL = re.compile(r'telegra|cable|cipher|cypher|decode|decipher|chiffr|code', re.I)
EX = re.compile(r'Lincoln|Marshals|Aqueduct|Diplomatic Instructions|Subject-Numeric|Mongoose')
for rg in (59, 84, 76):
    for h in load(rg):
        if h['kind'] != 'frame' or EX.search(' '.join(h['ancestors'])):
            continue
        s = h['snippet']
        if not TEL.search(s):
            continue
        g = [t for t in s.split() if re.fullmatch(r'\d{4,5}', t) and not (1850 <= int(t) <= 1950)]
        if len(g) < 6:
            continue
        print('\t'.join(map(str, [rg, h['naId'], ','.join(h['microform']) or '-', h['file'], h['objectId'], len(g),
                                  h['words'], h['title'][:60], ' '.join(s.split())[:400]])))
