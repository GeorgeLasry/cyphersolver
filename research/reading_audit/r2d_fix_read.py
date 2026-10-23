"""r2d (23 Oct 2026): carry the key corrections read off the clear copies (texts/b04_key_additions.txt, r2d block:
26 = del, 80 = dal, 1219 = ora, 1201 = ancora, 1236 = quando, 1239 = quell, 1449 = ecclesiastic, 1229 = perche, 1231 = pero,
1699 = pregiudizi, 1818 = ragguagli, ...) into the readings of the letters already read (423/2, 4, 6, 7, 8, 10).
Each replacement is an exact, unique string of the reading; the decode it rests on is texts/423-<n>_decode_b04.txt.
"""
import pathlib
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'nunzio1736' / 'texts'
FIX = {
 2: [("in [?esse] comprese", "in quelle comprese"), ("l'amarezza a l'animo mio, [?massime]", "l'amarezza dell'animo mio, massime"),
     ("dei [1960] e [1985]a passato", "dei [1960] e [1985] del passato"),
     ("gli affari a la S. Sede", "gli affari della S. Sede"), ("cos[ì] [?contrario]", "cos[ì] contrario"),
     ("assai nuovo [?anche] che", "assai nuovo ancora che"), ("gli interessi a la S. Sede.", "gli interessi della S. Sede."),
     ("[?Se] ella sappia", "Quando ella sappia"), ("nella difesa a le ragioni", "nella difesa delle ragioni")],
 4: [("la situazione a le nostre", "la situazione delle nostre"), ("Ministri a carattere", "Ministri del carattere"),
     ("Mons. [1513]a[?Consiglio]", "Mons. Governatore del Consiglio"), ("più sani [?consigli]", "più sani consigli"),
     ("dei [1952] a lo scorso", "dei [1952] dello scorso"), ("spinosissime [?occasioni]", "spinosissime congiunture")],
 6: [("visitato nel [1582]", "visitato dal [1582]"), ("prevaluto [?essa] Corte", "prevaluto quella Corte"),
     ("[?massime] nel nuovo", "massime nel nuovo"), ("in tre [?Segretari]", "in tre Segretari"),
     ("deliberazioni, [?se], venendo", "deliberazioni, quando, venendo"), ("[1204] sembrerebbe ancora molto", "benchè sembrerebbe ora molto")],
 7: [("li continui aggravi che", "li continui pregiudizi che"), ("giunta a padronato ai diritti a la S. Sede e a [l']ecclesiastica\nlibertà",
      "giunta del padronato ai diritti della S. Sede e a quella\nlibertà"), ("ha [?sempre] da tempi", "ha avuto da tempi"),
     ("[?benefici] [1449], e li Vescovi\n[?anche] essi", "[?benefici] ecclesiastici, e li Vescovi\nancora essi"),
     ("la rovina a l'autorità", "la rovina dell'autorità"), ("e a la potestà\n[1449]a in", "e della potestà\necclesiastica in"),
     ("prendere anch[e] li rimedii", "prendere però li rimedii"), ("usare a la sua paterna", "usare della sua paterna"),
     ("Brev[e], a qual[e] si manda", "Brev[e], del qual[e] si manda"), ("copia, affinché faccia", "copia, perchè faccia"),
     ("Regni, a tenore parimente\na l'annessa", "Regni, del tenore parimente\ndell'annessa"),
     ("V.S. affinché sia", "V.S. perchè sia"), ("intacco a la sua", "intacco della sua"),
     ("[?confessore] a la\nmedesima", "[?confessore] della\nmedesima")],
 8: [("che informi di\ntutt[o] [1601] d'Avila", "che ragguagli di\ntutt[o] Mons. Vescovo d'Avila"),
     ("in [1636] di [1845];", "in [1636] di [?rispondere];"), ("procuri [?anche] destramente", "procuri ancora destramente"),
     ("quali [?effetti]", "quali effetti"), ("informandomi minutamente", "ragguagliandomi minutamente")],
 10: [("dei [1957]a passato", "dei 12 del passato"), ("pubblicazione a[l] medesim[o] sia\nnato nelle [?rimostra]nze",
       "pubblicazione del medesim[o] sia\nnato dalle rappresentanze"), ("nasce nel vedere", "nasce dal vedere"),
      ("rapporti a [1844]i", "rapporti a risoluzioni"), ("a questa ancora fossero [?già] convinti", "a questa ora fossero costì convinti"),
      ("degli uni e a l'altre", "degli uni e dell'altre"), ("attentati a\nle Corti", "attentati delle\nCorti"),
      ("per via a le teste", "per via delle teste"), ("una a le più ingiuste", "una delle più ingiuste"),
      ("pensioni a la Corte di Napoli; e ancora\nal riferire", "pensioni della Corte di Napoli; e ora\nal riferire"),
      ("altre tante false [?rimostra]nze", "altre tante false rappresentanze"), ("insussistenti [?rimostra]nze", "insussistenti rappresentanze"),
      ("Avverta anche che", "Avverta però che"), ("[?però] per altro", "mentre per altro"),
      ("non [?essendo]vi chi", "non essendovi chi"), ("l'osservare ancora questi", "l'osservare ora questi"),
      ("[?Se] [?anche] [?S.M.] le", "Quando ancora S.M. le"), ("[1843]i sicuri", "riscontri sicuri"),
      ("stato di aggravio alla", "stato di pregiudizio alla"), ("nomina [1864]ndo ai", "nomina significando ai")],
}
for n, reps in FIX.items():
    p = T / f'423-{n}_reading.md'
    s = p.read_text(encoding='utf8')
    s, sep, notes = s.partition(chr(10) + '## Notes')   # the reading body only; the notes keep the 22 Oct wording
    for a, b in reps:
        assert s.count(a) == 1, (n, a, s.count(a))
        s = s.replace(a, b)
    p.write_text(s + sep + notes, encoding='utf8')
    print(n, len(reps), 'replacements')
