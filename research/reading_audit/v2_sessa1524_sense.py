"""v2 verify sweep: sessa1524 R9873, mark as holes the words that rest on a sense-only key value (flagged 'review' in
texts/r9873-r9898_reread_log.md section 3: sur/luc parte, tt plural s, reb dezi-, cer teni, lar miento, gom quatro,
qu o, dis servido, gul si, nuf gente), found by their (a)-line contexts in r9873_cipher.txt. Writes a scratch copy.

    python v2_sessa1524_sense.py <out.md>
"""
import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
t = (ROOT / 'targets/sessa1524/r9873_reading.md').read_text(encoding='utf8')
NL = chr(10) * 2
REPL = [  # (context in the reading, replacement); each must occur exactly as often as listed
    ('el exercito por esas partes.\n\n[clear', 'el exercito por [?] [?].\n\n[clear', 1),        # f80v tt sur
    ('He lo tornado a dezir', 'He lo tornado a [?]', 1),                                        # reb
    ('porque teniendose por amigo', 'porque [?] por amigo', 1),                                 # cer
    ('para el sostenimiento del exercito, tanto', 'para el [?] del exercito, tanto', 1),        # cer lar
    ('los dichos quatro mill ducados', 'los dichos [?] mill ducados', 1),                       # gom
    ('y otros quatro mill embiara', 'y otros [?] mill embiara', 1),                             # gom
    ('que por esas partes ni por', 'que por esas [?] ni por', 1),                               # luc
    ('no se haze ninguno de', 'no se haze [?] de', 1),                                          # qu
    ('se as[…ag] servido', 'se as[…ag] [?]', 1),                                                # dis
    ('matrimonios] y crecimiento', 'matrimonios] y [?]', 1),                                    # lar
    ('Y si la paz veniesse', 'Y [?] la paz veniesse', 1),                                       # gul
    ('o pretenderan si', 'o pretenderan [?]', 1),                                               # gul
    ('Y si V.Md. deliberase', 'Y [?] V.Md. deliberase', 1),                                     # gul
    ('y a sus servidores', 'y a sus [?]', 1),                                                   # dis
    ('el exercito por esas partes.' + NL + 'Y con esto', 'el exercito por [?] [?].' + NL + 'Y con esto', 1),  # f86r tt sur
    ('disolver la gente', 'disolver la [?]', 1),                                                # nuf
    ('no si se ha de hazer', 'no [?] se ha de hazer', 1),                                       # gul
    ('por esas fronteras', 'por [?] fronteras', 1),                                             # tt
    ('grand descaymiento', 'grand [?]', 1),                                                     # lar
    ('para el sostenimiento de lo de', 'para el [?] de lo de', 1),                              # lar
]
n = 0
for a, b, k in REPL:
    c = t.count(a)
    assert c == k, (a, c)
    if a != b: t = t.replace(a, b); n += 1
pathlib.Path(sys.argv[1]).write_text(t, encoding='utf8')
print('replaced', n, 'contexts')
