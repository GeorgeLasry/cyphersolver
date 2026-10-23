"""Batch b02 (fiesque1567): bracket the words of the readings that the figures do not carry (coordinator's sweep,
22 Oct 2026). Each edit is a phrase with the target word in {}; the word becomes [word] (supplied) or [?word]
(partly carried). Words are matched across line breaks; each phrase must match exactly once.

    python research/reading_audit/reread_b02_mark.py
"""
import collections
import pathlib
import re

R = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'fiesque1567' / 'read'

# (doc, phrase, kind) kind: 's' = supplied [w], 'p' = partly carried [?w]
EDITS = [
    ('1569-10-20', 'Il {dict} depuis', 's'),
    ('1569-10-20', 'Erfort {pour} traicter', 'p'),
    ('1569-10-20', 'promis {m\'advertir.}', 'p'),
    ('1569-10-20', 'faisoit {levée} de gens', 'p'),
    ('1569-10-20', 'qu\'il n\'y {a} aulcun', 's'),
    ('1569-10-20', 'fondement; {et} qu\'il a donné', 'p'),
    ('1569-10-20', 's\'il {advient} quelque', 'p'),
    ('1567-10', 'sçait {comme} il a eu', 'p'),
    ('1567-10', 'rien {a} dire', 'p'),
    ('1567-10', 'jusques a {ce} qu\'on', 'p'),
    ('1567-10', 'Depuis {il} m\'a dict', 's'),
    ('1567-10', 'y faict {a} Constantinoble', 's'),
    ('1567-10', 'bien {estre} que cest', 'p'),
    ('1567-10', 'l\'aisnée, {il} vouldroict', 's'),
    ('1568-01-21', 'sçavoir {comme} vous', 'p'),
    ('1568-03-06', 'n\'est {que} {trop} vray', 'p'),
    ('1568-03-06', 'amys {de} ceulx du', 's'),
    ('1568-03-06', 'cause, {comme} il vous', 'p'),
    ('1568-03-06', 'longueur {de} ceste guerre', 's'),
    ('1568-03-06', 'du Roy, {comme} je vous', 'p'),
    ('1568-03-06', 'veoir, {comme} je vous', 'p'),
    ('1568-03-06', 'Flandres. {Il} a envoyé', 's'),
    ('1568-03-06', 'apprendre. Il {est} bien vray', 'p'),
    ('1568-02-15', 'qu\'il {a} avec le prince', 's'),
    ('1568-02-15', 'Allemaigne, {car} il a desja', 'p'),
    ('1568-02-15', 'pied {pour} estre prests', 'p'),
    ('1568-06-12', 'guieres {a} arriver', 'p'),
    ('1568-07-17', 'lequel {n\'est} encores party', 'p'),
    ('1568-07-17', 'demeure de {la} deliberation', 's'),
    ('1568-07-17', 'pouvoir {pour} la delivrance', 'p'),
    ('1568-08-14', 'que je {vous} ay escrist', 'p'),
    ('1568-08-14', 'd\'Allemaigne {pour} le bien', 'p'),
    ('1568-08-14', 'et {s\'en} allera', 'p'),
    ('1568-08-14', 'Et {quand} a son retour', 'p'),
    ('1568-08-14', 'advertir {pour} vous en adviser', 'p'),
    ('1568-08-14', 'qu\'il {n\'estoit} encores asseuré', 'p'),
    ('1568-08-14', 'escriviez {comme} avez', 'p'),
    ('1568-09-04k', 'bon, {et} que {vous} estiez', 'p'),
    ('1568-09-04k', 'amitié {et} intelligence', 'p'),
    ('1568-09-04k', 'tirer {a} ceste heure', 'p'),
    ('1568-09-04k', 'homme a {rencontré} le courrier', 'p'),
    ('1568-09-04k', 'conseil {est} si saige', 'p'),
    ('1568-09-04k', 'Flandres, {me} semble', 's'),
    ('1568-09-04k', 'car {il} l\'ayme', 'p'),
    ('1568-09-04k', 'est {d\'avoir} esté {adverty} que les princes', 'p'),
    ('1568-09-04k', 'de {leurs} vies', 'p'),
    ('1568-09-04q', 'on {a} apporté', 'p'),
    ('1568-09-04q', 'empeschement {pour} separer', 'p'),
    ('1568-09-04q', 'y en {a} aulcuns', 's'),
    ('1568-12-02', ', {et} qu\'il [vous] plaira', 'p'),
    ('1568-12-02', 'comme {je} me doibs', 'p'),
    ('1569-01-14', 'Il {a} arrivé', 's'),
    ('1569-01-14', 'dict {que} ce mariaige', 'p'),
    ('1569-01-14', 'Saxe {donnast} sa fille', 'p'),
    ('1569-03-02', 'advisé {que} monsieur', 'p'),
    ('1569-03-02', 'qu\'il {a} faict doubler', 's'),
    ('1569-09-10', 'Espaigne {pour} [?se] condouloir', 'p'),
    ('1569-09-10', '{pour} s\'embarquer, {et} que madame', 'p'),
    ('1569-09-10', 's\'embarqueroict {pour} aller', 'p'),
    ('1569-09-10', 'aisnée, {et} de la tireroit', 'p'),
    ('1569-09-10', 'plaisir, {pour} le desir', 'p'),
    ('1569-09-10', 'qualité {pour} demander', 'p'),
    ('1569-09-10', 'resolu, {et} qu\'il vous envoyera', 'p'),
    ('1569-09-10', 'gentilzhommes {pour} {vous} faire entendre', 's'),
    ('1569-09-10', 'faire {entendre} la bonne volunté', 'p'),
    ('1569-09-10', 'qu\'il {vous} porte', 'p'),
    ('1569-09-10', 'pleu {me} commander', 'p'),
    ('1569-09-10', 'conservation de {vostre} estat', 'p'),
    ('1569-09-10', 'et que {pour} plusieurs raisons', 'p'),
    ('1569-09-10', 'coeur, {et} vous fera', 'p'),
    ('1569-10-01', 'je {vous} ay escript que', 'p'),
    ('1569-10-01', 'de {vos} {affaires,} dont', 'p'),
    ('1569-10-01', 'Poictiers, {et} desire', 'p'),
    ('1569-10-15', 'ennemys, {et} de les secourir', 'p'),
    ('1569-10-29', 'comme {vous} estiez prest', 'p'),
    ('1569-10-29', 'Dieu {vous} a donnée', 'p'),
]


def apply():
    count = collections.Counter()
    for doc, phrase, kind in EDITS:
        f = R / f'{doc}_reading.md'
        s = f.read_text(encoding='utf8')
        parts = re.split(r'(\{[^}]*\})', phrase)
        pat, repl, n = '', [], 0
        for part in parts:
            if not part.strip():
                if part: pat += r'\s+'
                continue
            toks = part.strip().split(' ') if not part.startswith('{') else [part]
            for k, tok in enumerate(toks):
                if pat and not pat.endswith(r'\s+'):
                    pat += r'\s+'
                if tok.startswith('{'):
                    w = tok[1:-1]
                    pat += '(' + re.escape(w) + ')'
                    n += 1
                else:
                    pat += re.escape(tok)
            if part.endswith(' ') and not part.startswith('{'):
                pat += r'\s+'
        pat = re.sub(r'(\\s\+)+', r'\\s+', pat)
        ms = list(re.finditer(pat, s))
        assert len(ms) == 1, (doc, phrase, len(ms))
        m = ms[0]
        out, last = [], m.start()
        for g in range(1, n + 1):
            w = m.group(g)
            trail = ''
            while w and w[-1] in '.,;:':
                trail = w[-1] + trail; w = w[:-1]
            out.append(s[last:m.start(g)] + ('[' + w + ']' if kind == 's' else '[?' + w + ']') + trail)
            last = m.end(g)
        s = s[:m.start()] + ''.join(out) + s[last:]
        f.write_text(s, encoding='utf8', newline='')
        count[doc] += n
    return count


if __name__ == '__main__':
    for d, c in sorted(apply().items()):
        print(d, c)
