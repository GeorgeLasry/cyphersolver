# rounds_apply.py: corrections from the improvement rounds after the Terrateig crib (notes/solve_notes.md,
# "Rounds after the crib"). Run from the vich1515 folder after crib_apply.py; edits work/v15c.txt (the split
# transcription) and work/signs.txt in place. transcriptions/n73_tokens.txt (the repo's pass-1 transcription) is
# left unchanged, so tokens.tsv still shows each token as first transcribed.
import json

# (line, position, label before, label after, basis)
TOKENS = [
    (10, 24, 'O', 'OT', 'image: o with a trailing stroke (OT), not O; lo[c]ura = locura, as printed'),
    (16, 26, 'sug', 'suq', 'image: the last letter has a q descender'),
    (18, 3, 'rue', 'rie', 'image: rie'),
    (26, 25, 'B8', 'PHI', 'image: the two-loop PHI, as at 26.21, not the 8-shaped B8; resistir, as printed'),
]
# round 2: per-token labels (a group read differently at one place, or kept unread there)
TOKENS += [
    (26, 29, 'sif', 'sifa', 'crib: resistir al rey de francia (l. 26); sif elsewhere (l. 45) stays unread'),
    (52, 7, 'ynh', 'ynhu', 'ynh = obra rests on one crib context (l. 31); l. 52 left unread'),
    (77, 20, 'yinu', 'yinpt', 'context: pero que pues nuestro Senor assi lo ha permitido (cf. the letter to the Swiss)'),
    (94, 26, 'pef', 'pefa', 'context: de aqui adelante se guarde (tentative); pef at l. 50 stays unread'),
]

# round 2: group values (value, status, basis, evidence)
GROUPS = {
    'yaz': ('pero', 'firm', 'crib+context', 'l. 14 que oy estan, pero, para con vos (crib); pero al fin Dios no desampara (42), pero he salido del cuydado (7), pero uos al papa (31)'),
    'doc': ('ui', 'firm', 'crib+context', 'l. 31 por obra ui-ere (crib: por obra viere); l. 122 triplicadas uias por mar y por tierra'),
    'ynh': ('obra', 'firm', 'crib', 'l. 31 por obra viere (crib); the token at l. 52 is kept apart (ynhu)'),
    'sifa': ('al', 'firm', 'crib', 'l. 26 resistir al rey de francia (crib)'),
    'bel': ('senor', 'firm', 'context', 'Dios nuestro Senor, ll. 83 and 103; por ser senor de lo espiritual (60); nuestro Senor (78)'),
    'xnyt': ('nuestro', 'firm', 'context', 'Dios nuestro Senor, ll. 78, 83, 103'),
    'xnl': ('mar', 'firm', 'context', 'por mar (2, 5); por mar y por tierra (122)'),
    'beq': ('tierra', 'firm', 'context', 'por X y por tierra (2); por mar y por tierra (122); l. 4 unclear'),
    'xam': ('mas', 'firm', 'context', 'no puede ser mas peligrosa (66); con mas union y conformidad (82); mas biuas fuercas (81); lo que mas (118, 123)'),
    'sen': ('ella', 'firm', 'context', 'con ellas (7); contenido en ellas (9); en ella (56); puso con ella (70)'),
    'baf': ('solo', 'firm', 'context', 'sino solo esforcarle (32); que solo ha permitido (46); no solo no la guardo (70)'),
    'xaf': ('i', 'firm', 'context', 'que uenga y (104); y con duplicadas (121); y sin dilacion (99)'),
    'xny': ('e', 'firm', 'context', 'e-scomun-, ll. 86, 88, 113'),
    'yinpt': ('pues', 'firm', 'context', 'y pues con esa ayuda de Dios (39); y que pues suycos (48); pues ... lo ha permitido (77)'),
    'yinzt': ('paz', 'firm', 'context', 'escuchar ninguna paz (64); la dicha paz no se asentara (73); alguna paz (55)'),
    'peb': ('assi', 'firm', 'context', 'nuestro Senor assi lo ha permitido (78; the letter to the Swiss has the phrase); y que assi tengo (44); haziendo lo assi (53)'),
    'dif': ('una', 'firm', 'context', 'alg-una paz (55); sin dilacion alg-una (99); mencion alg-una (121)'),
    'sof': ('defension', 'firm', 'context', 'la defension y conseruacion (101, 112); a la defension de (115)'),
    'xnp': ('mucho', 'firm', 'context', 'ha muchos anos que desean los franceses (62); de no tener muchos dias (8)'),
    'zuf': ('quiere', 'firm', 'context', 'pues suycos quieren tornar (48); y lo quieren (63)'),
    'sy': ('estado', 'firm', 'context', 'al estado de la yglesia (67); apoderarse del estado (58)'),
    'yae': ('otro', 'firm', 'crib+context', 'faltando los otros confederados (114; Terrateig quotes the phrase); en otro tal yerro (95; the letter to the Swiss)'),
    'pefa': ('aqui', 'tentative', 'context', 'de aqui adelante se guarde (94)'),
    # round 3
    'piq': ('bien', 'firm', 'context', 'que considere bien que si alguna paz (54-55); que mire bien su S[antida]d (73)'),
}

SIGNS = {
    'PSI': ('l', 'crib: echarle (27.13), the only PSI token; t was a solver choice on this one token'),
}

split = [l.split() for l in open('work/v15c.txt')]
for ln, pos, old, new, why in TOKENS:
    assert split[ln - 1][pos - 1] == old, (ln, pos, split[ln - 1][pos - 1], old)
    split[ln - 1][pos - 1] = new
open('work/v15c.txt', 'w').write('\n'.join(' '.join(l) for l in split) + '\n')

G = json.load(open('keys/groups.json'))
for k, (v, st, b, ev) in GROUPS.items():
    G[k] = {'value': v, 'status': st, 'basis': b}
json.dump(G, open('keys/groups.json', 'w'), ensure_ascii=False, indent=1)
open('keys/groups.txt', 'w').write(' '.join(f'{k}={v["value"].replace(" ", "_")}' for k, v in G.items()) + '\n')

S = dict(kv.split('=') for kv in open('work/signs.txt').read().split())
for k, (v, why) in SIGNS.items():
    S[k] = v
open('work/signs.txt', 'w').write(' '.join(f'{k}={v}' for k, v in S.items()) + '\n')
print('tokens relabelled:', len(TOKENS), '; groups set:', len(GROUPS), '; sign values set:', len(SIGNS))

# keep the published sign keys in step with work/signs.txt
J = json.load(open('keys/signs.json'))
for k, v in S.items():
    if k in J or k in SIGNS: J[k] = v
json.dump(J, open('keys/signs.json', 'w'), ensure_ascii=False, indent=1)
open('keys/signs.txt', 'w').write(' '.join(f'{k}={v}' for k, v in S.items()) + '\n')
