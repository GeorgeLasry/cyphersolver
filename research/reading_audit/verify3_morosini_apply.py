"""VERIFY_BRIEF pass 3, morosini1588: apply the word-by-word verdicts to texts/<R>_reading.md and _en.md.

    PYTHONUTF8=1 python research/reading_audit/verify3_morosini_apply.py [--dry]

Each edit is (record, file, prefix, old, new, suffix, kind): the text prefix+old+suffix (whitespace flexible, so it can
cross a line break) must occur exactly once in the "## Reading" (or "## Translation") section; `old` is replaced by
`new`. kind: S = word supplied ([word]), L = letter(s) supplied inside a word (w[o]rd), P = partly carried ([?word]),
R = replaced with the word the figures spell, E = English counterpart. Verdicts come from verify3_morosini_diag.py
--merge (whole letter aligned in reading order) read against the figures by hand (22 Oct 2026).
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, '..', '..', 'targets', 'morosini1588', 'texts')

E = [
    # R19
    ('R19', 'r', 'non o ', 'mancato', 'man[c]ato', ' di fare', 'L'),
    # R20
    ('R20', 'r', 'parlamento perché ', "l'hauese", "[l']hauese", ' da aprouarle', 'S'),
    ('R20', 'e', 'Parlement for ', 'it', '[it]', ' to approve', 'E'),
    ('R20', 'r', 'di N. S., ', 'si', '[s]i', ' andase cauando', 'L'),
    ('R20', 'r', 'haueuano [f. 89v] ', 'procurate', 'proc[u]rate', ' queste lettere', 'L'),
    ('R20', 'r', 'asai quello che ', 'era', 'er[a]', ' [f. 87v] suceso', 'L'),
    ('R20', 'r', 'cosa simile non ', 'apperteneua', '[?apperteneua]', ' ai', 'P'),
    ('R20', 'e', 'in such a matter it ', 'was not for', '[?was not for]', ' the people', 'E'),
    # R22
    ('R22', 'r', 'meco dela forma ', 'dela', 'del[a]', ' asolutione', 'L'),
    ('R22', 'r', 'compiacere ', 'dela', 'del[a]', ' asolutione; et io', 'L'),
    ('R22', 'r', 'duo giorni ', 'potere', 'poter', ' uscire', 'R'),
    ('R22', 'r', 'lasare il ', 'gouerno', 'goue[r]no', ' dela Prouenza', 'L'),
    # R30
    ('R30', 'r', '', 'raguagliarò', 'ragua[g]liarò', ' V. S. Ill.ma. Ho', 'L'),
    # R31
    ('R31', 'r', 'egli ', "s'habia", "s'abia", ' colpa', 'R'),
    ('R31', 'r', 'come facio ', 'con', '[con]', ' queste lettere, che credo', 'S'),
    ('R31', 'r', 'queste lettere, ', 'che', '[che]', ' credo sarano', 'S'),
    ('R31', 'e', 'as I do ', 'with', '[with]', ' this letter, which I believe', 'E'),
    ('R31', 'e', 'this letter, ', 'which', '[which]', ' I believe', 'E'),
    ('R31', 'r', 'nutiale fra ', 'il', '[il]', ' Gran Duca', 'S'),
    ('R31', 'e', 'contract between ', 'the', '[the]', ' Grand Duke', 'E'),
    # R32
    ('R32', 'r', 'S. M.tà ', 'se', '[s]e', ' ne andarà', 'L'),
    # R33
    ('R33', 'r', 'del acordo ', 'ultimam[ente]', 'ultim[a]m[ente]', ' fato a Parigi', 'L'),
    ('R33', 'r', 'de i suoi ', 'canonici', 'canon[i]ci', ', et che', 'L'),
    ('R33', 'r', 'ecetioni; che ', 'loro', '[l]oro', ' non poteuano', 'L'),
    ('R33', 'r', 'et che ', 'dispiaceria', 'dispia[c]eria', ' asai a N. S.', 'L'),
    ('R33', 'r', 'non ', 'dourebe', '[d]ourebe', ' hauere tardato', 'L'),
    ('R33', 'r', 'quanto me che il ', 'concilio', '[?concilio]', ' [fose] publicato', 'P'),
    ('R33', 'e', 'as much as I did that the ', 'Council', '[?Council]', ' [be] published', 'E'),
    ('R33', 'r', 'pii di ', 'qualsiuoglia', 'qualsiuog[l]ia', ' altro re', 'L'),
    ('R33', 'r', "et nel'", 'editto', 'edito', " d'unione", 'R'),
    ('R33', 'r', 'et nel suo ', 'ragionam[ento]', 'rag[i]onam[ento]', '', 'L'),
    ('R33', 'r', 'nel suo regno ', 'altra', 'altr[a]', ' religione', 'L'),
    ('R33', 'r', 'ela non ', 'intendeua', 'intende[u]a', ' di uolere che per forza', 'L'),
    ('R33', 'r', 'con modi ', 'destri', 'destr[i]', ' di guadagnare', 'L'),
    ('R33', 'r', 'di quello ', 'che', '[che]', ' dourò [f]are', 'S'),
    ('R33', 'e', 'Lordship on ', 'what', '[what]', ' I am to do to satisfy', 'E'),
    # R36
    ('R36', 'r', 'sodeto, partito ', 'dala', 'da[l]a', ' Regina Madre, è uenuto', 'L'),
    # R37
    ('R37', 'r', 'esa come ', 'Sua', 'S[ua]', ' Alt[ezza] potesero', 'L'),
    ('R37', 'r', "m'ha ", 'riferito', 'rifer[i]to', ' che, ragionando', 'L'),
    # R38
    ('R38', 'r', 'che lo ', 'seruirà', 'seruir[à]', ' bene', 'L'),
    ('R38', 'r', 'guerra a ', 'gli Ugonotti', "gl'Ugonotti", ' et procurare', 'R'),
    ('R38', 'r', 'zelo contra ', 'gli Ugonotti', "gl'Ugonotti", ' come', 'R'),
    ('R38', 'r', 'guerra a ', 'gli heretici', "gl'heretici", ' che a li catolici', 'R'),
    ('R38', 'r', 'ma che come ', 'padre', '[p]adre', ' comune', 'L'),
    ('R38', 'r', 'hauendo ', 'riguardo', 'ri[g]uardo', ' al ben', 'L'),
    ('R38', 'r', 'di non hauerne ', 'hauta', '[?hauta]', ' parte [f. 283v]', 'P'),
    ('R38', 'e', 'prince that he ', 'had had', 'had [?had]', ' no part', 'E'),
    ('R38', 'r', 'suo consigliere ', 'al', 'a[l]', ' sodeto sig.', 'L'),
    ('R38', 'r', 'caminare per la ', 'uia', '[?uia]', ' dela ragione', 'P'),
    ('R38', 'e', 'proceed by the ', 'way', '[?way]', ' of reason', 'E'),
    ('R38', 'r', 'uia] dela ', 'ragione', 'r[a]gione', ', di persuader', 'L'),
    ('R38', 'r', 'il suo, ', 'desiderando', 'desiderand[o]', ' molto', 'L'),
    ('R38', 'r', 'ala legatione ', 'di Auignone', "d'Auignone", ' per il sig.', 'R'),
    ('R38', 'r', 'mi ha deto sua signoria ', 'Ill.ma', 'Il[l].ma', ' che faria', 'L'),
    ('R38', 'r', 'tuta […] ', 'sodisfatione', '[?sodisfatione]', ' che desideraua', 'P'),
    ('R38', 'e', 'all the […] ', 'satisfaction', '[?satisfaction]', ' he desired', 'E'),
    ('R38', 'r', 'le ragioni che ', "l'haueuano", "l'haueua", ' moso', 'R'),
    ('R38', 'r', 'manco fauorita ', 'dala', 'dal[a]', ' M.tà di quello', 'L'),
    # R40
    ('R40', 'r', 'milia Suizeri ', 'et', '[et]', ' di oto milia', 'S'),
    ('R40', 'e', '15,000 Swiss ', 'and', '[and]', ' 8,000 Landsknechts', 'E'),
    # R41
    ('R41', 'r', 'persistendo di ', 'uolere', '[?uolere]', ' tenire quelle', 'P'),
    ('R41', 'e', 'persisting in ', 'wanting', '[?wanting]', ' to keep those places', 'E'),
    # R43
    ('R43', 'r', 'amici del duca di ', 'Guisa', '[Guisa]', ' hanno sgombrato', 'S'),
    ('R43', 'e', 'friends of the Duke of ', 'Guise', '[Guise]', ' have cleared out', 'E'),
    ('R43', 'r', 'haueua di sua signoria ', 'Ill.ma', 'Il[l].ma', ' per le parole', 'L'),
    # R44
    ('R44', 'r', 'temendo di ', 'errare', 'erare', ' in tuti modi', 'R'),
    ('R44', 'r', 'febre et un ', 'fluso', '[f]luso', ' di sangue', 'L'),
    # R45
    ('R45', 'r', 'contra li heretici quello che ', 'haueua', 'hauea', ' deto; che era', 'R'),
    ('R45', 'r', '[?sperando] di ', 'potere', 'poter', ' esere Re', 'R'),
    ('R45', 'r', 'conuiene ad un Re ', 'christianisimo', 'christianis[imo]', ', et che per', 'L'),
    ('R45', 'r', 'dechiarato inhabile et ', 'incapace', '[?incapace]', ' ala sucesione haurà', 'P'),
    ('R45', 'e', 'declared unfit and ', 'incapable', '[?incapable]', ' of the succession he', 'E'),
    # R46
    ('R46', 'r', 'del contrario ', 'conuenirà', 'conuenir[à]', ' a esere molto', 'L'),
    # R47
    ('R47', 'r', "d'insegnare ", 'agli', "agl'", ' altri non meno', 'R'),
    ('R47', 'r', 'concilio, perché, ', 'se', '[se]', ' i popoli', 'S'),
    ('R47', 'e', 'council, because, ', 'if', '[if]', ' the people', 'E'),
    ('R47', 'r', 'da tuti quelli ', "ch'hano", "c'hano", ' hauto pratica', 'R'),
    # R48
    ('R48', 'r', 'scrito a ', 'sofficienza', 'soficienza', ' a V. S.', 'R'),
    # R51
    ('R51', 'r', "d'Umala per ", 'le insolenze', "l'insolenze", ' et estorsioni', 'R'),
    # R57
    ('R57', 'r', 'per inuiarui, io ho ', 'truouato', 'trouato', ' questo portatore', 'R'),
    ('R57', 'r', 'Io ho ', 'truouato', 'trouato', ' il sig. Cesare', 'R'),
    ('R57', 'r', 'mons. di Cheseron, ', 'luogotenente', 'logotenente', ' generale per', 'R'),
    ('R57', 'r', 'humilisimi seruitori, ', 'et', '[et]', ' di esa et difenderla', 'S'),
    ('R57', 'e', 'most humble servants, ', 'and', '[and]', ' to [?…] it', 'E'),
    # R58
    ('R58', 'r', 'condoto al ', 'luogo', 'logo', ' del suplicio', 'R'),
    ('R58', 'r', "aspetare l'esercito ", 'haueuano', 'haueano', ' inuiato a rendersi', 'R'),
    ('R58', 'r', 'presto gli ', 'inuiaria', 'inuiar[i]a', ' gente', 'L'),
    ('R58', 'r', 'non hano ancora ', 'truouata', 'trouata', ' uia per', 'R'),
]


def flex(s):
    return r'\s+'.join(re.escape(p) for p in s.split(' ')) if s.strip() else ''


def section(txt, head):
    m = re.search(r'^## ' + head + r'\s*$(.*?)(?=^## |\Z)', txt, re.S | re.M)
    return m.start(1), m.end(1)


def main():
    dry = '--dry' in sys.argv
    files = {}
    bad = 0
    for rec, kind_f, pre, old, new, suf, kind in E:
        path = os.path.join(T, f'{rec}_reading.md' if kind_f == 'r' else f'{rec}_en.md')
        txt = files.get(path) or open(path, encoding='utf-8', newline='').read()
        a, b = section(txt, 'Reading' if kind_f == 'r' else 'Translation')
        sec = txt[a:b]
        lead = flex(pre.rstrip()) + (r'\s+' if pre.endswith(' ') else '')
        trail = (r'\s+' if suf.startswith(' ') else '') + flex(suf.lstrip())
        rx = re.compile(lead + '(' + flex(old) + ')' + trail)
        ms = list(rx.finditer(sec))
        if len(ms) != 1:
            print(f'!! {rec} {kind_f} {old!r}: {len(ms)} matches'); bad += 1
            continue
        s, e = ms[0].span(1)
        sec = sec[:s] + new + sec[e:]
        files[path] = txt[:a] + sec + txt[b:]
        print(f'{rec} {kind} {old} -> {new}')
    if bad:
        raise SystemExit(f'{bad} edits did not match; nothing written')
    if not dry:
        for p, t in files.items():
            open(p, 'w', encoding='utf-8', newline='').write(t)
        print('written', len(files), 'files')


if __name__ == '__main__':
    main()
