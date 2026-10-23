"""b33 (richelieu): decode the cipher runs Avenel printed (targets/richelieu/texts/ff87-89_avenel_figures.txt) with the key
recovered here (final.py KEY, with 39 = et per Avenel's footnotes), to check his decipherment run by run.

    python research/reading_audit/b33_rl_decode.py
"""
import re, pathlib
T = pathlib.Path(__file__).resolve().parents[2] / 'targets/richelieu/texts/ff87-89_avenel_figures.txt'
KEY = {'10': 'c', '11': 'b', '12': 'g', '13': 'p', '14': 'l', '15': 'o', '16': 'r', '17': 'f', '18': 't', '19': 'a',
       '20': 'd', '21': 'i', '22': 'n', '23': 'h', '24': 'm', '25': 's', '26': 'u', '27': 'e', '28': 'q', '29': 'a',
       '30': 'e', '31': 'i', '32': 'o', '33': 'u', '34': 'a', '35': 'e', '36': 'i', '37': 'o', '38': 'u',
       '39': '+et+', '40': '+de+', '42': '+la+'}
for line in T.read_text(encoding='utf-8').splitlines():
    if line.startswith('#') or not line.strip(): continue
    for run in re.findall(r'\[([^\]]+)\]', line):
        out = []
        for t in run.split():
            if t == '|': out.append(' | '); continue
            dbl = t.startswith('~'); t = t.lstrip('~')
            v = KEY.get(t, '[%s]' % t)
            out.append(v * 2 if dbl and len(v) == 1 else (v.strip('+') * 2 if dbl else v))
        print('%-70s -> %s' % (run[:70], ''.join(out).replace('+', ' ').strip()))
