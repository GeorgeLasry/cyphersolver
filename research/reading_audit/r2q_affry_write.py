"""r2q (23 Oct 2026): write affry1757/read/R1054_reading.md and R1064_reading.md from the Fagel register clear copies
(v5a_affry_reg.py output saved in the scratchpad), with the places where the figures give another word than the register
followed (SUBS: register text -> reading, reason). Every substitution is asserted to apply once.
    PYTHONUTF8=1 python research/reading_audit/r2q_affry_write.py"""
import pathlib, textwrap
ROOT = pathlib.Path(__file__).resolve().parents[2]
SCR = pathlib.Path(r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\r2q')

# --- R1054: the cipher page (DECODE image I5511, the only page of the record) ends inside the sentence on the gout.
R1054_CUT = ' J\'espere malgé cela'
R1054_SUBS = [
    ("n'a point ordonné au Cte. d'Estreés", "n'a point ordonné à M. le Maréchal d'Estreés",
     "groups 402 196 878 185 (à, m, le, maréchal; 185 = maréchal also in R1064 'M. le Marechal de Belle Isle'); DECODE "
     "transcribed '878^6', which the parse had split into 8 and 786; the register (and Bussemaker) have 'au Cte.' "
     "(d'Estrées was made maréchal de France in February 1757)"),
    ("pour la sureté de la communication du Royaume", "pour la sureté de sa communication du Royaume",
     "group 10 = sa (11 other occurrences at sa); 'du' has no group of its own and is the register's"),
    ("que je le voudrois.", "que par le [...]",
     "the page ends with 197 306 628 (que, par, le); 306 = par at 34 other places; the register's 'que je le voudrois' "
     "has no group for 'je' or 'voudrois' here, and the letter goes on on a page that is not on the DECODE record"),
]
# --- R1064: the whole register entry; its clear postscript is in clear on the last cipher page too.
R1064_SUBS = [
    ("qui écrivoit de Londres au (-) ne et soit Mr de Quintin,", "qui écrivoit de Londres au Senechal de Quintin,",
     "groups 739 1127 134 1136 582 219 1044 580 588 141: au se-ne-cha-l de qui-n-ti-n. The clerk left a blank, wrote "
     "'ne' and 'soit', dotted them for deletion and interlined 'et' (62R, checked on the scan): he did not make out "
     "the title. 1136 = cha also in R1054 'Champ'"),
    ("ne consentiront pas à une Operation", "ne consentiront point à une Operation",
     "group 948 = point (also 'le point de jalousie' in this letter, 'On ne dit point' in R1054)"),
    ("j'ai vû combien il est important", "j'ai vû combien il étoit important",
     "group 842 = étoit/été, never est"),
    ("cet encouragemen ne", "cet encouragement ne", "word cut at the binding on 63L; group 308 = ment"),
    ("cette Grace n'est pas un Traité", "cette Grace n'est point un Traité", "group 948 = point"),
    ("l'au roit crû", "l'auroit crû", "line break in the register"),
    ("dans l'in stant", "dans l'instant", "line break in the register"),
    ("ou de le taire si Elle", "ou de la taire si Elle",
     "groups 583 172 1017 (la, ta, re); the scan (63L) has 'ou de Se taire', not 'le taire' as WAINUT's transcription"),
    ("Correspondance avec avec lui.", "Correspondance avec lui.", "catchword 'avec' at the foot of 63L repeated on 63R"),
    ("du 10. Janvier du dit jour", "du 18. Janvier du dit jour",
     "the scan (63R) has '18.', not '10.' as WAINUT's transcription; the cipher groups (978 634 114) have no value"),
    ('"Les Srs Joseph " du Perieux', '"Les Srs Joseph du Perieux', "the clerk's quotation marks at each line start"),
    ('Maurepas, " de Bourdeaux', 'Maurepas, de Bourdeaux', "the same"),
    ('Clement " Omeri', 'Clement Omeri', "the same"),
    ('Imbert, " Capitaine', 'Imbert, Capitaine', "the same"),
    ('natif " de la dite', 'natif de la dite', "the same"),
    ('Bourdeaux, " pour un Mois."', 'Bourdeaux, pour un Mois."', "the same"),
    ("Vous remarqué que le Passeport regardoit et le Chirurgien,",
     "Vous remarquerez que le Passeport regardoit les deux Capitaines et le Chirurgien,",
     "groups 1017 718 1116 (re, [718], rés) give 'remarquerez'; then 282 936 380 265 729 460 172 516 134 797 "
     "(re-garde-oit les deux ca-pi-ta[-]ne-s): the figures carry 'les deux Capitaines', which the clerk left out (the "
     "'et' after 'regardoit' is dotted on 63R)"),
    ("Montaran # et", "Montaran et", "footnote mark"),
    ("Ouvrage ## auquel", "Ouvrage auquel", "footnote mark"),
    ("J'espere que vous en Serez content. dans une Enveloppe addressée à Mr de Montaran.",
     "J'espere que vous en Serez content. [Notes in the register:] La Lettre de N: à Son Oncle van Oller étoit "
     "enfermée dans une Enveloppe addressée à Mr de Montaran. [The work:] La Verité des Faits.",
     "the clerk's two footnotes (63R), which the joiner drops because they begin with '#'"),
]

L = {
 'R1054': dict(
    date='19 July 1757 (to Bernis, "B.")',
    where='inv. 5186 scans 248R-249L (margin "Dat: 19. Juïllet 1757. A: à B:")',
    agree='319 of the 364 keyed groups stand at the register\'s word (0.876; shuffled key values 0.144, max 0.206), '
          'from first group to last',
    cover='The DECODE record has one cipher page (image I5511, 372 groups); it ends inside the sentence on the gout '
          '("... autant de monde que par le"), and the rest of the letter is not on the record. The reading covers that '
          'page; the register\'s continuation is given below the reading',
    cut=R1054_CUT, subs=R1054_SUBS),
 'R1064': dict(
    date='1 February 1757 (no. 136, to Rouillé)',
    where='inv. 5186 scans 62R-63R (margin "No 136. Dat: 1. Fevrier 1757. A: à R:")',
    agree='996 of the 1,201 keyed groups stand at the register\'s word (0.829; shuffled key values 0.153, max 0.180). '
          'The cipher is written in numbered paragraphs set out of order on the five pages (read/R1064.md); the '
          'register gives them in order, which is followed here. The postscript ("Je joins ici deux Lettres ...") is in '
          'clear on the last cipher page as well',
    cover='', cut=None, subs=R1064_SUBS),
}

for r, d in L.items():
    t = (SCR / f'reg_{r}.txt').read_text(encoding='utf-8').strip()
    rest = ''
    if d['cut']:
        i = t.index(d['cut']); rest = t[i:].strip(); t = t[:i]
    for a, b, _ in d['subs']:
        assert t.count(a) == 1, (r, a, t.count(a)); t = t.replace(a, b)
    head = (f'Rests on: the contemporary clear copy of this despatch in the Fagel register, Nationaal Archief 1.10.29 '
            f'{d["where"]}, transcribed by WAINUT (21 Oct 2026, `wainut/register_clear.txt`) and checked line by line '
            f'against the NA IIIF scans 23 Oct 2026 (r2q). The register is the deciphered text of the same letter: with '
            f'this folder\'s key (`wainut/align_register.py`, `wainut/align/{r}.tsv`), {d["agree"]}. ')
    if d['cover']:
        head += d['cover'] + '. '
    head += (f'The reading follows the register in the clerk\'s spelling, except where the figures give another word; '
             f'those places are listed under "Figures over the register" and in `{r}_reread_log.md`. Groups the '
             f'register passes over without a word are listed in the log, not put into the reading. The keyed decode '
             f'this replaces is `{r}.md`.')
    out = f'# {r} - d\'Affry, The Hague, {d["date"]}: reading\n\n' + textwrap.fill(head, 118)
    out += '\n\n## Reading\n\n' + textwrap.fill(t, 118) + '\n'
    if rest:
        out += ('\n## Rest of the letter (register only, not on this record\'s image)\n\n'
                + textwrap.fill('[...] que je le voudrois. ' + rest, 118) + '\n')
    out += '\n## Figures over the register\n\n'
    for a, b, why in d['subs']:
        out += textwrap.fill(f'- "{b}" for the register\'s "{a}": {why}.', 118, subsequent_indent='  ') + '\n'
    (ROOT / 'targets/affry1757/read' / f'{r}_reading.md').write_text(out, encoding='utf-8')
    print(r, len(t.split()), 'words')
