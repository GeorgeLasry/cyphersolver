# crib_apply.py: applies the values settled by Terrateig's quotation of the letter (Política en Italia del Rey
# Católico, 1963, pp. 631-634; see notes/solve_notes.md, "The Terrateig crib") to the keys and to the split
# transcription. Run from the vich1515 folder; writes work/v15c.txt (the split transcription with per-token crib
# labels), and updates keys/groups.json, keys/groups.txt and work/signs.txt.
#   basis "crib": the value is read off the aligned quotation (ll. 6-31)
#   basis "crib+context": as crib, and every other occurrence of the group reads with it
#   basis "context": not in the quotation; set from the other occurrences or a parallel passage (tentative)
import json

G = json.load(open('keys/groups.json'))

GROUPS = {   # label: (value, status, basis)
    # changed firm values
    'seg': ('dicha', 'firm', 'crib+context'),        # was s: la dicha capitulacion, la dicha paz (13 of 13 read)
    'soo': ('esto', 'firm', 'crib+context'),         # was do: pues en esto, de todo esto, estoy, estos dias (8 of 8)
    # unread or tentative groups now settled
    'be': ('suycos', 'firm', 'crib+context'),        # suyços: locura de suyços, el Emperador y yo y suyços (5)
    'beo': ('toda', 'firm', 'crib+context'),         # todas las cosas, toda vez, toda la Xpiandad (4)
    'dam': ('ya', 'firm', 'crib+context'),           # se hayan, vos haya (5)
    'dah': ('uos', 'firm', 'crib+context'),          # para con vos, el vos haya, vos al Papa (3)
    'tir': ('iunta', 'firm', 'crib+context'),        # se juntase, juntarse, juntamente (3)
    'zuy': ('rey de francia', 'firm', 'crib+context'),  # al rey de Francia (5)
    'poz': ('capitan general', 'firm', 'crib+context'),
    'bon': ('tanto', 'firm', 'crib+context'),
    'yom': ('principe', 'firm', 'crib+context'),
    'xez': ('ninguna', 'firm', 'crib+context'),
    'pab': ('ahunque', 'firm', 'crib+context'),
    'pib': ('assimismo', 'firm', 'crib+context'),
    'sey': ('fue', 'firm', 'crib+context'),
    'xnz': ('necesidad', 'firm', 'crib+context'),
    'gak': ('con', 'firm', 'crib'),                  # concertarse (the quotation has contentarse)
    'soq': ('francia', 'firm', 'crib+context'),      # con Francia; Luys de Francia muerto
    'xaz': ('ninguno', 'firm', 'crib'),
    'dik': ('voluntad', 'firm', 'crib'),
    'bip': ('tiene', 'firm', 'crib'),
    'yee': ('otra', 'firm', 'crib'),
    'sem': ('exercito', 'firm', 'crib'),
    'nab': ('lo', 'firm', 'crib'),
    'oso': ('e', 'firm', 'crib'),
    'ip': ('mucho', 'firm', 'crib'),
    'rue': ('confederado', 'firm', 'crib'),          # one token; probably rie misread
    'sug': ('franceses', 'firm', 'crib'),            # one token; probably suq misread
    'ral': ('con', 'firm', 'crib'),                  # one token; probably rak misread
    # tentative values the quotation confirms
    'rie': ('confederado', 'firm', 'crib+context'), 'suq': ('franceses', 'firm', 'crib+context'),
    'xin': ('mal', 'firm', 'crib+context'), 'yem': ('papa', 'firm', 'crib+context'),
    'bay': ('uisorrey', 'firm', 'crib+context'), 'sio': ('esta', 'firm', 'crib+context'),
    'san': ('ello', 'firm', 'crib+context'), 'xad': ('lo', 'firm', 'crib+context'),
    'pnk': ('ayuda', 'firm', 'crib+context'), 'yed': ('obligado', 'firm', 'crib+context'),
    'suh': ('emperador', 'firm', 'crib+context'),
    # second groups under one label (split per token, like sin/sim)
    'yinz': ('paz', 'firm', 'crib+context'),         # yin read paz
    'yinp': ('pues', 'firm', 'crib+context'),        # yin read pues
    'ynbp': ('para', 'firm', 'crib+context'),        # ynb read para (no son para haver plazer; para con vos; para ello)
    'xnyn': ('nuestro', 'firm', 'crib'),             # xny read nuestro (nuestro exercito)
    'xnyt': ('nuestro', 'tentative', 'context'),     # Dios nuestro Señor (the parallel letter to the Swiss)
    'siml': ('el', 'firm', 'crib'),                  # sim read el (en el peligro, con el / que el Emperador)
    'yinpt': ('pues', 'tentative', 'context'),       # yin outside the quotation, read pues by context
    'yinzt': ('paz', 'tentative', 'context'),        # yin outside the quotation, read paz by context
}
for k, (v, st, b) in GROUPS.items():
    G[k] = {'value': v, 'status': st, 'basis': b}
for k in ('sin', 'sim', 'ynb', 'xny'):
    G.setdefault(k, {}).setdefault('basis', 'context')
G.pop('yin', None)   # no token keeps the unsplit label (see CONTEXT below)
json.dump(G, open('keys/groups.json', 'w'), ensure_ascii=False, indent=1)
open('keys/groups.txt', 'w').write(' '.join(f'{k}={v["value"].replace(" ", "_")}' for k, v in G.items()) + '\n')

# signs: SL = ll (maravillado; dello); ZHq = q before -uisiere/-uiere (two crib tokens) and ZHqt the same by
# position (tentative); LAMu = u (pura)
S = dict(kv.split('=') for kv in open('work/signs.txt').read().split())
S['SL'] = 'll'; S['ZHq'] = 'q'; S['ZHqt'] = 'q'; S['LAMu'] = 'u'   # ZHqt is tentative (renotate.py TENT_SIGNS)
open('work/signs.txt', 'w').write(' '.join(f'{k}={v}' for k, v in S.items()) + '\n')

# per-token labels (line, position within the line, label as split before, new label)
TOKENS = [
    (9, 26, 'Xs', 'Xr'), (10, 19, 'Xs', 'Xr'), (15, 21, 'Xs', 'Xz'), (21, 21, 'Xr', 'Xz'), (23, 3, 'Xr', 'Xz'),
    (26, 4, 'Xr', 'Xz'), (29, 17, 'Xs', 'Xz'),
    (13, 19, 'sin', 'sim'), (20, 27, 'sin', 'sim'), (27, 3, 'sin', 'sim'), (27, 8, 'sin', 'sim'),
    (28, 15, 'sim', 'sin'), (13, 20, 'sim', 'siml'), (23, 21, 'sim', 'siml'), (26, 6, 'sim', 'siml'),
    (13, 8, 'yin', 'yinp'), (19, 23, 'yin', 'yinp'), (18, 15, 'yin', 'yinz'), (22, 19, 'yin', 'yinz'),
    (28, 20, 'yin', 'yinz'),
    (14, 12, 'ynb', 'ynbp'), (27, 21, 'ynb', 'ynbp'),
    (11, 19, 'xny', 'xnyn'),
    (26, 12, 'ZH', 'ZHq'), (29, 1, 'ZH', 'ZHq'), (29, 26, 'LAM', 'LAMu'),
]
TOKENS += [
    (6, 18, 'ynb', 'ynbp'),     # no son para haver plazer: Terrateig's quotation word for word (p. 631)
]
CONTEXT = [  # not in the quotation: tentative values from the same position or the parallel letter
    (61, 18, 'ZH', 'ZHqt'),     # lo que [q]uisiere
    (78, 1, 'xny', 'xnyt'), (83, 18, 'xny', 'xnyt'), (103, 14, 'xny', 'xnyt'),   # Dios nuestro Señor
    # yin outside the quotation: its old value es is withdrawn (the quotation shows paz and pues); by context:
    (36, 4, 'yin', 'yinpt'), (39, 13, 'yin', 'yinpt'), (48, 3, 'yin', 'yinpt'),        # pues
    (55, 6, 'yin', 'yinzt'), (64, 5, 'yin', 'yinzt'), (73, 2, 'yin', 'yinzt'),         # paz
    (68, 7, 'yin', 'yinu'), (77, 20, 'yin', 'yinu'), (85, 15, 'yin', 'yinu'),          # either: left unread
]
split = [l.split() for l in open('work/v15x.txt')]
for ln, pos, old, new in TOKENS + CONTEXT:
    assert split[ln - 1][pos - 1] == old, (ln, pos, split[ln - 1][pos - 1], old)
    split[ln - 1][pos - 1] = new
open('work/v15c.txt', 'w').write('\n'.join(' '.join(l) for l in split) + '\n')
print('groups set:', len(GROUPS), '; tokens relabelled:', len(TOKENS), 'by the crib,', len(CONTEXT), 'by context')
