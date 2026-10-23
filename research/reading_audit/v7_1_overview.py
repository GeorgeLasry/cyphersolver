"""v7 translate list 1: overview of each entry (decryption file, words, language, reading)."""
import json, sys, pathlib, re
R = pathlib.Path(__file__).resolve().parents[2]
rows = [l.split('\t') for l in (R/'research/reading_audit/v7_translate_1.txt').read_text(encoding='utf8').splitlines() if l.strip()]
for f, i, d in rows:
    p = json.loads((R/'targets'/f/'profile.json').read_text(encoding='utf8'))
    e = p['outcome']['texts'][int(i)]
    dec = e.get('decryption')
    decs = dec if isinstance(dec, list) else [dec]
    info = []
    for x in decs:
        if not x: info.append('NONE'); continue
        if str(x).startswith('http'): info.append('URL'); continue
        fp = R/'targets'/f/x
        if fp.exists():
            t = fp.read_text(encoding='utf8', errors='replace')
            info.append(f'{x}:{len(t.split())}w')
        else: info.append(f'{x}:MISSING')
    print(f, i, e.get('doc'), '|', e.get('state'), '|', e.get('language'), '| rd=', e.get('reading'), '| tr=', e.get('translation'), '|', ' '.join(info))
