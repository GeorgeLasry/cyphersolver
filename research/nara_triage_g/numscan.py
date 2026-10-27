"""Rank RG 242 numeric 'frame' hits by how much their snippet looks like a number-group cipher message.
    python research/nara_triage_g/numscan.py <rg> > research/nara_triage_g/numscan_<rg>.tsv
Score: radio/cipher vocabulary (Funkspruch, Spruch, Schluessel, Kenngruppe, Teil/Tl, Chiffre, cifra, telegram...)
plus a long run of 4-5 digit groups; table vocabulary (Battr, Stab, Summe, Kg, RM, %, decimals) counts against."""
import json, re, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
rg = sys.argv[1]
PATH = sys.argv[2] if len(sys.argv) > 2 else f'research/nara_reels/out/rg_{rg}.jsonl'
RADIO = re.compile(r'funk|spruch|schl[uü]ss|kenngr|chiff|cifr|cipher|cypher|code|telegr|ziffer|\btl\b|teile?\b|geheim|verschl|entschl|kdos', re.I)
TABLE = re.compile(r'battr|stab\b|summe|insgesamt|\bkg\b|\brm\b|%|zusammen|bestand|stärke|staerke|seite|gesamt|lfd|nummer|jahrgang|geb\.|datum', re.I)
G = re.compile(r'(?<![\d.,/:-])\d{%s}(?![\d.,/:-])' % (sys.argv[3] if len(sys.argv) > 3 else '4,5'))
out = []
for line in open(PATH, encoding='utf-8'):
    h = json.loads(line)
    if h['kind'] != 'frame':
        continue
    s = h['snippet'] or ''
    toks = s.split()
    g = 0; best = 0
    for t in toks:
        if G.fullmatch(t.strip('-=+.')):
            g += 1; best = max(best, g)
        else:
            g = 0
    dec = len(re.findall(r'\d[.,]\d', s))
    radio = len(RADIO.findall(s)); table = len(TABLE.findall(s))
    score = best + 6 * min(radio, 3) - 3 * table - dec
    if best >= 6 and score >= 10:
        out.append((score, h['microform'][0] if h['microform'] else '-', h['naId'], h['file'], best, radio, table, s[:300].replace('\t', ' ')))
out.sort(key=lambda x: -x[0])
print('score\tpub\tnaId\tfile\trun\tradio\ttable\tsnippet')
for o in out:
    print('\t'.join(map(str, o)))
