"""Append rows found in Paz, Catalogo III (Flandes, 1915) and Catalogo V (Patronato Real, 1912).

Source: Google Books full view, page text (output=text) scanned for 'cifr' in the built-in browser,
26 Oct 2026. Run once; it refuses to add a title twice.
"""
import json
from pathlib import Path

P = Path(__file__).with_name('candidates.json')
FL = 'https://books.google.com/books?id=GXdKAQAAMAAJ'
PR = 'https://books.google.com/books?id=V0hQAQAAMAAJ'
SN = ('Scored from the printed-catalogue description during the Oct 2026 PARES (AGS) sweep '
      '(research/pares_ags/); not viewed')


def row(**k):
    base = dict(seen='catalogue', source='PARES (AGS) sweep', score_note=SN)
    base.update(k)
    order = ['year', 'date', 'title', 'correspondents', 'place', 'language', 'region', 'period', 'shelfmark',
             'folio_note', 'cls', 'status', 'why', 'importance', 'solvability', 'difficulty', 'score_note',
             'verify', 'links', 'seen', 'source', 'prior_art']
    return {f: base[f] for f in order}


NEW = [
    row(year=1583, date='1582-1583',
        title='Alexander Farnese, Prince of Parma: letters in cipher, Flanders correspondence 1582-83',
        correspondents='Alexander Farnese, Prince of Parma → Philip II', place='Low Countries', language='Spanish',
        region='Low Countries', period='1560-1589',
        shelfmark='AGS, Estado, leg. 587 (Paz, Catálogo III, entry 587, A. 1582-83)',
        folio_note='"Cartas en cifra del Príncipe de Parma"; number and folios not given', cls='B',
        status=('Paz, Catálogo III (Flandes, 1915) p. 37: "Cartas en cifra del Príncipe de Parma"; no descifrado '
                'noted (the catalogue notes them elsewhere). known.py: no hits for "Estado, 587"; Parma/Farnese hits '
                'are unrelated items. Legajo number read from the catalogue margin numbering; confirm on PARES.'),
        why="Parma's own cipher despatches of the reconquest years, on Anjou, England and Scotland.",
        importance=4, solvability=2, difficulty=3,
        verify=('Find EST,LEG,587 on PARES when the 429 clears; check for images and for descifrados filed with the '
                "cipher originals; Parma's keys are in AGS and on Tomokiyo's cryptiana Spanish pages."),
        links=[{'label': 'Paz, Catálogo III (1915), Google Books p. 37', 'href': FL + '&pg=PA37&q=cifra'}],
        prior_art=('open as far as checked (26 Oct 2026: catalogue gives no decipherment; repo no hits). '
                   "Historians use Parma's despatches widely, so descifrados may exist in the same legajo.")),
    row(year=1575, date='1574-1576',
        title='Luis de Requesens, Comendador mayor de Castilla: cipher letters from Flanders',
        correspondents='Luis de Requesens → Philip II', place='Low Countries', language='Spanish',
        region='Low Countries', period='1560-1589',
        shelfmark='AGS, Estado, leg. 563 (Paz, Catálogo III, entry before 564)',
        folio_note='"Cartas cifradas del Comendador mayor de Castilla"; number not given', cls='B',
        status=('Paz, Catálogo III (1915) p. 29: "Cartas cifradas del Comendador mayor de Castilla" (Requesens, '
                "governor 1573-76); no descifrado noted. known.py 'Requesens' hits only this README's note on "
                "Leone's study of his Italian legajos (Estado 899-902). Legajo read from the margin numbering."),
        why="Requesens's governorship of the Netherlands (Breda talks, mutinies, Zierikzee) in his own cipher.",
        importance=4, solvability=2, difficulty=3,
        verify="PARES EST,LEG,563; check for descifrados; compare with Leone's Requesens key (Estudios Románicos 34, 2025).",
        links=[{'label': 'Paz, Catálogo III (1915), Google Books p. 29', 'href': FL + '&pg=PA29&q=cifradas'}],
        prior_art=("possibly studied: Leone (Estudios Románicos 34, 2025) worked on Requesens's ciphers from his "
                   'Italian posts; Flanders letters not checked (26 Oct 2026)')),
    row(year=1542, date='1541-1543',
        title="'Mr. de San Vicente', imperial ambassador in France: cipher correspondence with Charles V and Granvelle",
        correspondents="Imperial ambassador in France ('Mr. de San Vicente') → Charles V, Granvelle and others",
        place='France', language='unknown (Spanish or French)', region='France', period='1497-1559',
        shelfmark='AGS, Estado, leg. 499 or 500 (Paz, Catálogo III, A. 1541-43)',
        folio_note='"Correspondencia cifrada"; size not given', cls='B',
        status=('Paz, Catálogo III (1915) p. 4: "Correspondencia cifrada del embajador en Francia Mr. de San Vicente '
                'con el Emperador, con Granvela, etc."; no descifrado noted. known.py "San Vicente", "Saint-Vincent", '
                '"Estado 499": no hits. Legajo ambiguous in the OCR (499 appears mid-entry).'),
        why='Imperial diplomacy in France before the 1542 war, in the ambassador\'s own cipher.',
        importance=3, solvability=2, difficulty=3,
        verify="PARES EST,LEG,499/500; check Luo 2021 (Charles V letters; keys in Estado 1.1.1) for this ambassador's key.",
        links=[{'label': 'Paz, Catálogo III (1915), Google Books p. 4', 'href': FL + '&pg=PA4&q=cifrada'}],
        prior_art='unknown; Luo 2021 may hold the key (checked 26 Oct 2026: not in repo)'),
    row(year=1675, date='c. 1674-1676',
        title='Spy Francisco Vannó: his letters and the cipher he used, with interrogations and death sentence',
        correspondents='Francisco Vannó (spy) → unknown', place='Low Countries', language='unknown',
        region='Low Countries', period='1651-1700',
        shelfmark='AGS, Estado, leg. 2126 (Paz, Catálogo III; number from the margin, confirm)',
        folio_note='"Instrucción ... cartas suyas, cifra de que se servía"; size not given', cls='A',
        status=('Paz, Catálogo III (1915) p. 120: "Instrucción que se ocupó al espía Francisco Vannó, cartas suyas, '
                'cifra de que se servía, interrogatorios hechos al mismo y sentencia de muerte contra él." The key '
                'seems to be in the bundle; whether the letters are enciphered is not stated. known.py "Vanno": no '
                'relevant hits.'),
        why="A captured spy's letters with his seized key, from the Dutch War; the key should make any cipher letters readable.",
        importance=2, solvability=3, difficulty=2,
        verify='PARES EST,LEG,2126; confirm the letters are enciphered and pair them with the key.',
        links=[{'label': 'Paz, Catálogo III (1915), Google Books p. 120', 'href': FL + '&pg=PA120&q=cifra'}],
        prior_art='open (checked 26 Oct 2026: repo no hits; no web check)'),
    row(year=1500, date='undated (late 15th / early 16th c.)',
        title='Document in cipher with an English cover, not deciphered (Patronato Real, England papers)',
        correspondents='unknown (Anglo-Spanish correspondence of the Puebla period)', place='England (probably)',
        language='unknown', region='England', period='1497-1559',
        shelfmark='AGS, Patronato Real (Paz, Catálogo V, no. 4715; PTR legajo/doc to map)',
        folio_note='2 hoj. fol., in poor condition', cls='B',
        status=('Paz, Catálogo V Patronato Real (1912) no. 4715: "Documento en cifra con sobre inglés. S. f. Ni '
                'descifrado. 2 hoj. fol., en mal estado de conservación." No. 4716 is Catherine, Princess of Wales, '
                'to Dr Puebla. catalogue.json already has three PTR leg. 52 Puebla-code items; this one\'s PARES DOC '
                'number is unknown, so it may coincide with one of them: check before merging.'),
        why="An undeciphered Anglo-Spanish cipher of the Henry VII / Catherine of Aragon years; Puebla's Roman-numeral code (key PTR leg. 52 doc. 33) is the first key to try.",
        importance=3, solvability=3, difficulty=2,
        verify='Map Paz no. 4715 to PTR,LEG,<n>,DOC.<m> on PARES; compare with the PTR leg. 52 rows in catalogue.json; view images.',
        links=[{'label': 'Paz, Catálogo V (1912), Google Books', 'href': PR + '&pg=PT2&q=cifra'}],
        prior_art='open as far as checked (26 Oct 2026: catalogue says not deciphered; Bergenroth CSP Spain i not grepped)'),
    row(year=1520, date='Nov-Dec 1520',
        title='Lope Hurtado de Mendoza to Charles V on the Comunidades: one of seven letters in cipher',
        correspondents='Lope Hurtado de Mendoza → Charles V', place='Medina de Rioseco / Tordesillas',
        language='Spanish', region='Spain', period='1497-1559',
        shelfmark='AGS, Patronato Real (Paz, Catálogo V, no. 189; PTR legajo/doc to map)',
        folio_note='7 letters, 17 hoj. fol. + 1 en 4.°; one letter in cipher', cls='B',
        status=('Paz, Catálogo V (1912) no. 189: "Cartas (Siete) de Lope Hurtado de Mendoza á S. M. ... Una carta '
                'ológr. y otra en cifra." No descifrado noted. The repo has his 1522-24 Rome ciphers '
                '(lopehurtado1522, lopehurtado1523) but not this 1520 letter (known.py).'),
        why='A royalist cipher report from inside the Comunidades revolt; the writer\'s later cipher is already broken here.',
        importance=3, solvability=3, difficulty=2,
        verify='Map no. 189 to PTR,LEG,<n>,DOC on PARES; try the targets/lopehurtado1522 key; grep Danvila MHE 35-40.',
        links=[{'label': 'Paz, Catálogo V (1912), Google Books p. 29-32', 'href': PR + '&pg=PA29&q=cifra'}],
        prior_art="open as far as checked (26 Oct 2026: repo has his 1522-24 ciphers only; Danvila's Comunidades volumes not grepped)"),
    row(year=1546, date='10 Jun 1546',
        title='Charles V: instruction to the Cardinal of Trent (Madruzzo), entirely in cipher',
        correspondents='Charles V → Cristoforo Madruzzo, Cardinal of Trent', place='Regensburg',
        language='Spanish', region='Central Europe', period='1497-1559',
        shelfmark='AGS, Patronato Real (Paz, Catálogo V, no. 1521; PTR legajo/doc to map)',
        folio_note='8 hoj. fol., signed by Charles V, "Toda en cifra"', cls='B',
        status=('Paz, Catálogo V (1912) no. 1521: "Instruccion de lo que vos el Reverendisimo Cardenal de Trento '
                'haveys de dezir negociar y tractar con [Vela] de nuestra parte. Ratisbona 10 Junio 1546. Firma de '
                'Carlos V. Toda en cifra." Footnote: "Lo subrayado en cifra. La palabra [Vela] no consta en la '
                'clave": the cataloguer had a key and read at least the title; no descifrado listed. known.py '
                '"Cardenal de Trento", "Madruzzo": no hits.'),
        why="Charles V's secret instructions for Madruzzo's mission to Paul III on the eve of the Schmalkaldic War.",
        importance=4, solvability=3, difficulty=2,
        verify=('Map no. 1521 to PTR legajo/doc on PARES; find the key the cataloguer used (Luo 2021, Estado 1.1.1); '
                'check Corpus documental de Carlos V ii for a printed text.'),
        links=[{'label': 'Paz, Catálogo V (1912), Google Books p. 194', 'href': PR + '&pg=PA194&q=cifra'}],
        prior_art='possibly printed (CDCV ii prints many 1546 instructions); not checked (26 Oct 2026)'),
]

d = json.loads(P.read_text(encoding='utf8'))
titles = {r['title'] for r in d}
added = [r for r in NEW if r['title'] not in titles]
d.extend(added)
P.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
print(f'added {len(added)}; total {len(d)}')
