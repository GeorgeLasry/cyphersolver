"""verify1 (carpio1677): apply the word-by-word verification edits (22 Oct 2026) to read/R*_reading.md and the
matching read/R*_en.md. Each edit is (file, old phrase, new phrase); whitespace in the phrase matches any run of
whitespace (line breaks kept as they were where possible); each old phrase must match exactly once.

Readings: [w] = supplied (neither the key decode nor DECODE's margin transcription carries it), [?w] = partly
carried, replacements take the word of the source (margin or key decode).

    python research/reading_audit/verify1_carpio_mark.py
"""
import pathlib
import re

R = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'carpio1677' / 'read'

EDITS = [
    # R1002: margin "y qye esta no? defau? an arbitrio", key "no de ra ba n": no "me"
    ('R1002_reading.md', 'éstas no me dejaban', 'éstas no [me] dejaban'),
    # key "de ci r a {8} ra V.S." (a-o-ra = ahora), margin "al I? aora": no "hasta"
    ('R1002_reading.md', 'decir a V.S. hasta ahora', 'decir a V.S. [hasta] ahora'),
    # key "que ha go la se", margin "que ha*ga se": the verb is not settled (hablase?)
    ('R1002_reading.md', 'que hable a Su', 'que [?hable] a Su'),
    # margin "le mismo que al dia", key "que ma di a": "al", not "el"
    ('R1002_reading.md', 'lo mismo que el día', 'lo mismo que al día'),
    ('R1002_en.md', 'to speak to His Beatitude', 'to [?speak] to His Beatitude'),
    ('R1002_en.md', 'and that they left me no discretion', 'and that they left [me] no discretion'),
    ('R1002_en.md', 'nor can I yet tell Your Lordship', 'nor can I [yet] tell Your Lordship'),
    # R1003: key "si en d p re ci so", margin "si en pr**crifo": siendo preciso
    ('R1003_reading.md', 'pues si es preciso que', 'pues siendo preciso que'),
    ('R1003_en.md', 'consequences: if this mishap forces a\nchange in the plan of the winter quarters, the Duke of Lorraine having to recross the Rhine, then I',
     'consequences, since this mishap must bring a\nchange in the plan of the winter quarters, the Duke of Lorraine having to recross the Rhine; but I'),
    # R1006: key "bo l bi s [80] l ta": "la" only perhaps inside the unread group [80]
    ('R1006_reading.md', 'volvió la vuelta', 'volvió [?la] vuelta'),
    # R1007 (no margin transcription on DECODE; key decode only)
    ('R1007_reading.md', 'nación en esta corte,', 'nación [?en] esta [corte],'),
    ('R1007_reading.md', 'de que por mi parte', 'de que [por] mi parte'),
    ('R1007_reading.md', 'que pide la justicia', 'que [?pide] la justicia'),
    ('R1007_reading.md', 'esperando la respuesta', 'esperando una respuesta'),
    ('R1007_en.md', 'has received at this court.', 'has received [?at] this [court].'),
    ('R1007_en.md', 'although for my\npart I have', 'although [for my\npart] I have'),
    ('R1007_en.md', 'that the justice on my side calls for', 'that the justice on my side [?calls for]'),
    ('R1007_en.md', 'I am waiting for the answer of the viceroy', 'I am waiting for an answer from the viceroy'),
    # R1008: key "me es ga x go", margin "une? vean?": partly
    ('R1008_reading.md', 'me lleguen las órdenes de Su', 'me [?lleguen] las órdenes de Su'),
    ('R1008_en.md', 'orders reach me', 'orders [?reach] me'),
    # R1011
    ('R1011_reading.md', 'logrado con ella que se', 'logrado [con] [ella] que se'),
    ('R1011_reading.md', 'no se trata de castigar', 'no se [?trata] [?de] castigar'),
    ('R1011_reading.md', 'tampoco de la averiguación', 'tampoco [de] [la] averiguación'),
    ('R1011_reading.md', 'en Civitavecchia levantaron', 'en [?Civitavecchia] levantaron'),
    ('R1011_en.md', 'and having thereby got the populace', 'and having [thereby] got the populace'),
    ('R1011_en.md', 'not only is there no move to punish the\nseditious, there is none to find out the truth either',
     'not only is there [?no move] to punish the\nseditious, there is [none] to find out the truth either'),
    ('R1011_en.md', 'were at Civitavecchia', 'were at [?Civitavecchia]'),
]


def apply():
    for fn, old, new in EDITS:
        if old == new:
            continue
        f = R / fn
        s = f.read_text(encoding='utf8')
        pat = r'\s+'.join(re.escape(x) for x in old.split())
        ms = list(re.finditer(pat, s))
        if not ms and re.search(r'\s+'.join(re.escape(x) for x in new.split()), s):
            continue  # already applied
        assert len(ms) == 1, (fn, old, len(ms))
        m = ms[0]
        # keep the original whitespace layout: map words of new onto the matched span's separators
        seps = re.findall(r'\s+', m.group(0))
        nw = new.split()
        if len(nw) == len(seps) + 1:
            rep = ''.join(w + (seps[k] if k < len(seps) else '') for k, w in enumerate(nw))
        else:
            rep = new
        s = s[:m.start()] + rep + s[m.end():]
        f.write_text(s, encoding='utf8', newline='')
        print('ok', fn, '|', old.replace('\n', ' '), '->', new.replace('\n', ' '))


if __name__ == '__main__':
    apply()
