"""Builds candidates.json for the South Cone / Andes sweep (Oct 2026). Rows are hand-written from the hits
of atom.py / aleph_cl.py / the printed-archive greps; see README.md."""
import json, os

SRC = 'South Cone / Andes archives sweep'
NOTE = 'Scored from the archive description during the Oct 2026 South Cone/Andes sweep (research/latam_southcone/); '

ROWS = [
    {
        "year": 1850,
        "date": "13 Feb 1850 (letter in a file of 1849-1853)",
        "title": "Benito Varela, Paraguayan foreign minister → Manuel Moreira de Castro, consul general in Rio: letter with numeric cipher passages",
        "correspondents": "Benito Varela (Ministro de Relaciones Exteriores, Paraguay, under Carlos Antonio López) → Manuel Moreira de Castro (consul general, later plenipotentiary of Paraguay at the court of Brazil)",
        "place": "Asunción",
        "language": "Spanish",
        "region": "Americas",
        "period": "1801-1900",
        "shelfmark": "Asunción, Archivo Nacional de Asunción, Colección Rio Branco, ANA-AHRP-PY-558-1-31 (ex Biblioteca Nacional do Rio de Janeiro I-29,25,23), item 13",
        "folio_note": "PDF of 98 images; the cipher letter is on images 41-42 (0-based 41/42): clear Spanish with about 12 runs of dot-separated numbers (1-116, e.g. '9.27.7.33.15.3', '37.3.1.27.7.33.9'), roughly 60-80 cipher tokens, plus a sign like a barred circle. Other letters in the file are clear.",
        "cls": "C",
        "status": "ANA description, item 13: 'se refiere a otros asuntos que no pueden ser identificados por estar escritos en código cifrado' (i.e. the cataloguer could not read it). Viewed on the scan 28 Oct 2026: numeric substitution (letters or syllables) inside a clear letter about Brazil, Rio Grande and Buenos Aires. Not on DECODE, not in the repo.",
        "why": "Cipher of Carlos Antonio López's foreign ministry with its agent in Rio on the eve of the 1850 Paraguay-Brazil alliance against Rosas; Paraguayan state ciphers of this period are hardly known.",
        "importance": 3, "solvability": 3, "difficulty": 2,
        "score_note": NOTE + "the cipher page was viewed on the scan.",
        "verify": "Transcribe images 41-42 of the PDF; small numbers mostly odd suggest a letter table with homophones or a syllabary; context (Rosas, Brazil, Rio Grande, Urquiza) gives cribs. Look for further Varela/Moreira letters in the Rio Branco collection (ANA-AHRP 558-*) using the same numbers.",
        "links": [
            {"label": "ANA catalogue record", "href": "https://riobranco.archivonacional.gov.py/index.php/correspondencia-entre-el-ministro-de-relaciones-exteriores-de-la-republica-del-paraguay-y-el-senor-manuel-moreira-de-castro-primeramente-consul-y-despues-plenipotenciario-del-paraguay"},
            {"label": "PDF of the file (98 images)", "href": "https://riobranco.archivonacional.gov.py/uploads/r/archivo-nacional-de-asuncion/8/3/5/8353484cf68d7a80d9ddbfe3c3bee098b13c26efaa58f1bacbc368e0c6755294/ANA-AHRP-PY_-_558-1-31.compressed.pdf"},
        ],
        "seen": "image",
        "source": SRC,
        "prior_art": "open (checked 28 Oct 2026: repo ledgers, DECODE list, Cryptoole snapshot; web search on Paraguayan/López ciphers found nothing)",
    },
]

# ---- Archivo Nacional Histórico de Chile, Aleph base ARNES ("Archivo especial"): Archivo Santa María and
# Archivo Fernández Larraín, item-level records. Records whose note says "Texto en clave" with no
# transcription attached. 142 sibling telegrams in the same fonds have the transcription attached, and the
# fonds holds the key sheets (A3039, B4931), so these are class A on paper; none is digitised online.
ALEPH = 'http://www.bncatalogo.cl/F/?func=direct&local_base=ARNES&doc_number='
ASM_NOTE = ('Not digitised online (no 856 link in the MARC record). The same fonds holds 142 cipher telegrams '
            'of 1879-1886 with transcriptions attached and two key sheets: A3039 "Código para escribir en clave" '
            '(ca. 1880) and B4931 "Claves telegráficas a utilizar con Lynch, Altamirano, Novoa y todas las '
            'legaciones chilenas en el extranjero" (ca. 1883, 10 p.).')


def asm(year, date, title, corr, place, sm, sysno, note, why, imp=3, solv=2, diff=2, cls='A', lang='Spanish',
        extra_links=()):
    links = [{"label": f"ANH Chile catalogue record {sysno}", "href": ALEPH + sysno}] + list(extra_links)
    return {
        "year": year, "date": date, "title": title, "correspondents": corr, "place": place, "language": lang,
        "region": "Americas", "period": "1801-1900",
        "shelfmark": sm, "folio_note": note, "cls": cls,
        "status": "Archivo Nacional de Chile catalogue (Aleph ARNES) note: '" + note.split(' | ')[0] +
                  "', no transcription noted (the catalogue does note one on most sibling telegrams). " + ASM_NOTE +
                  " Not on DECODE, not in the repo (checked 28 Oct 2026).",
        "why": why, "importance": imp, "solvability": solv, "difficulty": diff,
        "score_note": NOTE + "not viewed.",
        "verify": "Request scans from the Archivo Nacional Histórico (Santiago); read with the key sheets A3039/B4931 of the same fonds, calibrated on the transcribed sibling telegrams.",
        "links": links, "seen": "catalogue", "source": SRC,
        "prior_art": "open (checked 28 Oct 2026: repo ledgers, DECODE list, Cryptoole snapshot; web search on War of the Pacific ciphers found no study of the Santa María telegrams)",
    }


ROWS += [
    asm(1880, "8 Apr - 31 Dec 1880",
        "Nicolás de Piérola, supreme chief of Peru: letter-book of correspondence to various authorities, in cipher (62 pp.)",
        "Nicolás de Piérola (Jefe Supremo of Peru) → various Peruvian authorities",
        "Lima", "Santiago, Archivo Nacional Histórico, Archivo Santa María A6000 (Aleph sys. 000006000)", "000006000",
        "Texto en clave | 62 p. letter-book; how the Peruvian copybook reached President Santa María's papers is not stated (presumably captured at Lima, Jan 1881)",
        "A whole wartime letter-book of Peru's dictator during the Chilean advance on Lima; if the cipher is Peruvian and unread, it is the largest Peruvian ciphertext of the War of the Pacific.",
        imp=4, solv=2, diff=3, cls='B'),
    asm(1882, "29 May 1882",
        "Patricio Lynch, commander of the Chilean occupation of Peru → President Domingo Santa María, telegram in cipher",
        "Patricio Lynch Zaldívar → Domingo Santa María González", "Lima",
        "Santiago, Archivo Nacional Histórico, Archivo Santa María B1441 (in 'Lynch, Novoa y otros, enero 1882 a octubre 1883')",
        "000011441", "Texto en clave | 1 p.",
        "Occupation-era reporting from Lima to the Chilean president during the Peruvian resistance (Cáceres' Sierra campaign)."),
    asm(1882, "1 Jun 1882",
        "Patricio Lynch → President Santa María, telegram in cipher with a copy attached",
        "Patricio Lynch Zaldívar → Domingo Santa María González", "Lima",
        "Santiago, Archivo Nacional Histórico, Archivo Santa María B1403", "000011403",
        "Texto en clave, adjunta copia | 2 p.; the attached 'copia' may be a clear copy (then read at the time) or a second cipher copy",
        "Occupation-era reporting from Lima, during the Sierra campaign.", solv=2),
    asm(1883, "29 Jan 1883",
        "Patricio Lynch → President Santa María and → Minister of War Carlos Castellón: two telegrams in cipher of the same day",
        "Patricio Lynch Zaldívar → Domingo Santa María González; → Carlos Castellón", "Lima",
        "Santiago, Archivo Nacional Histórico, Archivo Santa María B1487 and B1488", "000011487",
        "Texto en clave | 1 p. each; two records (sys. 000011487, 000011488)",
        "Lynch's reports in the months before the Ancón negotiations with Iglesias.",
        extra_links=[{"label": "record B1488", "href": ALEPH + "000011488"}]),
    asm(1883, "6 Sep 1883",
        "Jovino Novoa, Chilean plenipotentiary in Peru → President Santa María, telegram partly in cipher",
        "Jovino Novoa → Domingo Santa María González", "Lima",
        "Santiago, Archivo Nacional Histórico, Archivo Santa María B1591", "000011591",
        "Parte del texto está en clave | 1 p.",
        "Novoa negotiated the Treaty of Ancón (Oct 1883); a ciphered report from the weeks before signature."),
    asm(1883, "6 Nov 1883",
        "Unsigned telegram from Lima → José Manuel Balmaceda (Minister of the Interior / Foreign Affairs), in cipher, incomplete",
        "unknown (Chilean authorities in Lima) → José Manuel Balmaceda Fernández", "Lima",
        "Santiago, Archivo Nacional Histórico, Archivo Santa María B3181 (in 'Lynch, Novoa y otros, noviembre 1883 a junio 1884')",
        "000013181", "Texto en clave, incompleto | 1 p.",
        "Report from occupied Lima days after the Treaty of Ancón, addressed to the future president.", imp=2, solv=1),
    asm(1883, "Dec 1883",
        "Patricio Lynch → President Santa María, telegram in cipher, incomplete",
        "Patricio Lynch Zaldívar → Domingo Santa María González", "unknown (Lima?)",
        "Santiago, Archivo Nacional Histórico, Archivo Santa María B3922", "000013922",
        "Texto en clave e incompleto | 1 p.", "Lynch's report during the evacuation phase after Ancón.", imp=2, solv=1),
    asm(1884, "21 Feb 1884",
        "Patricio Lynch and Jovino Novoa → President Santa María: two telegrams in cipher of the same day from Chorrillos",
        "Patricio Lynch Zaldívar; Jovino Novoa → Domingo Santa María González", "Chorrillos (Peru)",
        "Santiago, Archivo Nacional Histórico, Archivo Santa María B3960 (Lynch) and B3958 (Novoa)", "000013960",
        "Texto en clave | 1 p. + 2 p.; two records (sys. 000013960, 000013958)",
        "Reports from the occupation command and the Chilean plenipotentiary as Iglesias' government was being installed.",
        extra_links=[{"label": "record B3958 (Novoa)", "href": ALEPH + "000013958"}]),
    asm(1879, "1 Jul 1879",
        "Jorge Huneeus → Domingo Santa María (then minister in the field at Antofagasta), telegram in cipher",
        "Jorge Huneeus → Domingo Santa María González", "Valparaíso",
        "Santiago, Archivo Nacional Histórico, Archivo Santa María B9821 (in 'Correspondencia telegráfica, mayo a agosto 1879')",
        "000019821", "Texto en clave | 1 p.",
        "First months of the War of the Pacific, between the Iquique battle and the Antofagasta campaign.", imp=2),
    asm(1879, "29 Jul 1879",
        "President Aníbal Pinto → Domingo Santa María at Antofagasta: two telegrams in cipher (one incomplete)",
        "Aníbal Pinto Garmendia → Domingo Santa María González", "Valparaíso",
        "Santiago, Archivo Nacional Histórico, Archivo Santa María B9882 and B9877", "000019882",
        "Texto en clave; Texto incompleto en clave | 1 p. each; two records (sys. 000019882, 000019877)",
        "The president's ciphered instructions to his minister at the front during the Huáscar crisis of 1879.",
        imp=3, extra_links=[{"label": "record B9877", "href": ALEPH + "000019877"}]),
    asm(1830, "undated (between 1817 and 1841)",
        "José Antonio Rodríguez Aldea → Bernardo O'Higgins, letter partly in cipher (6 ff.), with a printed 'Expreso al Virrey de Popayán'",
        "José Antonio Rodríguez Aldea → Bernardo O'Higgins", "unknown",
        "Santiago, Archivo Nacional Histórico, Archivo Fernández Larraín vol. 39, p. 15 (Aleph sys. 000029316)", "000029316",
        "Texto parcialmente en clave | 6 ff.; the catalogue dates it '[19-' (undated); Rodríguez Aldea was O'Higgins' finance minister 1820-23 and corresponded with him in Peruvian exile until 1841",
        "A ciphered letter from O'Higgins' closest minister; his circle's ciphers (Logia Lautaro, exile plotting from Peru) are hardly documented.",
        imp=3, solv=1, diff=3, cls='C'),
]

UY_INV = 'https://www.gub.uy/ministerio-educacion-cultura/sites/ministerio-educacion-cultura/files/2026-01/COLECCI%C3%93N%20PIVEL%20DEVOTO.pdf'
ROWS += [
    {
        "year": 1903, "date": "c. 1897-1904 (neighbouring items 1903-1904)",
        "title": "Cipher telegram in the papers of Aparicio Saravia, leader of the Nationalist (Blanco) revolutions of 1897 and 1904",
        "correspondents": "unknown → Aparicio Saravia (presumed)",
        "place": "unknown (Uruguay)", "language": "Spanish", "region": "Americas", "period": "1901-1950",
        "shelfmark": "Montevideo, Archivo General de la Nación, Colección Pivel Devoto, 'Aparicio Saravia. Documentos de carácter particular - Revolución de Río Grande del Sur - Revolución de 1897 y 1904', Estantería 51, Estante 4, Caja 43, carpeta 155, doc. 36 (f. 85)",
        "folio_note": "doc. 36 'Telegrama cifrado en mal estado. 1 folio' (f. 85); the same folder holds doc. 13 'Clave remitida a Aparicio Saravia por el Director del Partido Nacional' (10 typed ff., ff. 23-33), doc. 45 'Para descifrar - Para cifrar' (f. 144) and doc. 48 'Texto - Clave. Nombres' (ff. 149-150)",
        "cls": "A",
        "status": "AGN Uruguay inventory of the Colección Pivel Devoto (PDF, inventory p. 217): 'Telegrama cifrado en mal estado'. The key sheets of the Partido Nacional are in the same folder, so it is probably readable; whether a clear copy exists is not stated. Not digitised online. Not on DECODE, not in the repo.",
        "why": "Ciphered traffic of the last Uruguayan civil war (1904, Masoller); the party's own keys survive with it, so it is a test case rather than a hard break.",
        "importance": 2, "solvability": 2, "difficulty": 1,
        "score_note": NOTE + "not viewed.",
        "verify": "Ask the AGN Uruguay for scans of carpeta 155 ff. 23-33, 85, 144, 149-150; apply the party key to the telegram.",
        "links": [{"label": "AGN Uruguay inventory, Colección Pivel Devoto (PDF)", "href": UY_INV}],
        "seen": "catalogue", "source": SRC,
        "prior_art": "open (checked 28 Oct 2026: repo ledgers, DECODE list; no web search)",
    },
    {
        "year": 1927, "date": "1926-1940 (three volumes)",
        "title": "Intendencia de Antofagasta, received communications including confidential 'criptogramas' from the Ministries of the Interior and Foreign Affairs",
        "correspondents": "Chilean Ministries of the Interior, Foreign Affairs, War, Fomento, Justice → Intendente of Antofagasta",
        "place": "Santiago → Antofagasta", "language": "Spanish", "region": "Americas", "period": "1901-1950",
        "shelfmark": "Santiago, Archivo Nacional de la Administración / Histórico, Fondo Intendencia de Antofagasta, 'Comunicaciones recibidas' 1926-1927, 1928-1929, 1928-1940 (Aleph sys. 000050868, 000050870, 000050871)",
        "folio_note": "volume-level records: 'oficios, telegramas y criptogramas reservados y confidenciales'; number of cipher telegrams unknown",
        "cls": "C",
        "status": "Archivo Nacional de Chile catalogue (Aleph) mentions 'criptogramas' in three volumes of the Antofagasta intendancy; no key or decipherment mentioned. Not digitised online. Not on DECODE, not in the repo.",
        "why": "Chilean interior-ministry cipher traffic to the nitrate north under Ibáñez (1927-31), the Tacna-Arica settlement of 1929 and the 1931-32 crises; Chilean state codes of the period are unstudied.",
        "importance": 2, "solvability": 1, "difficulty": 3,
        "score_note": NOTE + "volume-level catalogue only; not viewed.",
        "verify": "Consult the three volumes at the Archivo Nacional; count the cipher telegrams and look for clear copies or a key in the same series.",
        "links": [{"label": "record 1926-1927", "href": "http://www.bncatalogo.cl/F/?func=direct&local_base=ARCHIVO_NACIONAL&doc_number=000050868"},
                  {"label": "record 1928-1940", "href": "http://www.bncatalogo.cl/F/?func=direct&local_base=ARCHIVO_NACIONAL&doc_number=000050871"}],
        "seen": "catalogue", "source": SRC,
        "prior_art": "open (checked 28 Oct 2026: repo ledgers, DECODE list; no web search)",
    },
]

# ---- Biblioteca Nacional de Chile, manuscripts (Aleph base BNC01 on bncatalogo.cl; Sala Medina / Archivo
# Balmaceda papers). Item-level notes; none has a digital-object link and BND search finds no scan.
BNC = 'http://www.bncatalogo.cl/F/?func=direct&local_base=BNC01&doc_number='
KEYS_1891 = ('The library also holds "[Códigos y claves antibalmacedistas] 1891" (3 ff., sys. 001156140), "[Códigos y claves '
             'de grupo congresista] 1891" (sys. 001156145) and a Legation list of the keys sent to Paris, 15 Jun 1891 '
             '(sys. 001083798); the government (Balmacedist) key is not catalogued.')


def bnc(year, date, title, corr, place, sm, sysnos, note, status, why, imp=2, solv=1, diff=2, cls='C',
        period='1801-1900', lang='Spanish', verify=None):
    return {
        "year": year, "date": date, "title": title, "correspondents": corr, "place": place, "language": lang,
        "region": "Americas", "period": period,
        "shelfmark": sm, "folio_note": note, "cls": cls,
        "status": status + " Not digitised online (no link in the record; BND search finds no scan). Not on DECODE, not in the repo (checked 28 Oct 2026).",
        "why": why, "importance": imp, "solvability": solv, "difficulty": diff,
        "score_note": NOTE + "not viewed.",
        "verify": verify or "Request scans from the Biblioteca Nacional de Chile (Sección Manuscritos); compare with the 1891 key sheets held there.",
        "links": [{"label": f"BN Chile catalogue record {s}", "href": BNC + s} for s in sysnos],
        "seen": "catalogue", "source": SRC,
        "prior_art": "open (checked 28 Oct 2026: repo ledgers, DECODE list; web search on 1891 civil-war ciphers found no study)",
    }


ROWS += [
    bnc(1891, "8 and 16 Feb 1891",
        "Villegas (Antofagasta) → President José Manuel Balmaceda: two telegrams in letter cipher, civil war of 1891",
        "Villegas → José Manuel Balmaceda", "Antofagasta",
        "Santiago, Biblioteca Nacional de Chile, manuscritos, Hoja 14398-B and 14398-A (Aleph sys. 001162221, 001162218)",
        ["001162221", "001162218"],
        "1 f. and 2 ff.; opening words given by the cataloguer: 'Y j h _ t v t b...' and 'Estimo que- Z t K y K J K u b_son_...' (letter cipher mixed into clear text)",
        "BN Chile catalogue: 'Mensaje escrito en clave'; no translation noted. " + KEYS_1891,
        "Reports to the president from the nitrate north as it fell to the Congressist navy (Feb 1891).",
        imp=3, solv=2, diff=2),
    bnc(1891, "14, 16 and 20 (two) Jan 1891",
        "Claudio Vicuña Guerrero (Valparaíso) → President Balmaceda: four telegrams partly in cipher at the outbreak of the 1891 civil war",
        "Claudio Vicuña Guerrero → José Manuel Balmaceda", "Valparaíso",
        "Santiago, Biblioteca Nacional de Chile, manuscritos, Hoja 14470-128, 14470-127, 14470-114, 14470-94 (Aleph sys. 001171959, 001171956, 001171724, 001171638)",
        ["001171959", "001171956", "001171724", "001171638"],
        "1, 3, 1 and 1 ff.; 14 Jan: 'El resto del mensaje está redactado en clave' (the ships in the bay, Blanco and Huáscar); 16 Jan: facts 'expresa en clave'; 20 Jan: 'Telegrama en clave'",
        "BN Chile catalogue notes the cipher parts; no translation noted except 'las frases finales pueden ser vinculadas a la traducción' on 14 Jan. " + KEYS_1891,
        "Balmaceda's minister and later presidential candidate reporting the fleet's revolt at Valparaíso in its first days.",
        imp=3, solv=2, diff=2),
    bnc(1891, "20 Apr and 29 Jun 1891",
        "Admiral Oscar Viel (Valparaíso) → President Balmaceda: two telegrams in cipher on the 'insubordinados'",
        "Oscar Viel Toro → José Manuel Balmaceda", "Valparaíso",
        "Santiago, Biblioteca Nacional de Chile, manuscritos, Hoja 14470-2 (sys. 001168747) and an unnumbered 2-page telegram (sys. 001081085)",
        ["001168747", "001081085"],
        "1 f. and 2 pp.; 'El contenido está en clave'; 'Telegrama cifrado ... sobre asuntos de la Guerra Civil'",
        "BN Chile catalogue: content in cipher, no translation noted. Viel's own letter to Julio Haase, Valparaíso 9 Jun 1891 (sys. 001081115), sends 'detalles sobre el código Oscar y cómo descifrarlo', a probable key description. " + KEYS_1891,
        "Balmacedist naval command at Valparaíso during the civil war.", imp=3, solv=2, diff=2, cls='B',
        verify="Request scans of the two telegrams and of Viel's letter to Haase (sys. 001081115) describing the 'código Oscar'."),
    bnc(1891, "14 and 20 Jan 1891",
        "Provincial telegrams partly in cipher to Balmaceda and the army secretary: Alejandro Morán (Rancagua) and Manuel J. Jarpa (Talca)",
        "Alejandro Morán → José Manuel Balmaceda; Manuel J. Jarpa → Secretario General del Ejército", "Rancagua; Talca",
        "Santiago, Biblioteca Nacional de Chile, manuscritos, Hoja 14455-F (sys. 001168257) and Hoja 14465-H (sys. 001168489)",
        ["001168257", "001168489"],
        "1 f. each; Morán opens 'z x h...', 'Texto en clave; traducción parcial'; Jarpa 'En clave se anota ... un mensaje'",
        "BN Chile catalogue: Morán's text in cipher with only a partial translation; Jarpa's cipher line not translated. " + KEYS_1891,
        "Short telegrams, but they share the government system with the Villegas, Vicuña and Viel items and give partial cribs.",
        imp=1, solv=2, diff=2),
    bnc(1891, "1891",
        "José Manuel Balmaceda: autograph note written in cipher during the civil war",
        "José Manuel Balmaceda → unknown", "unknown (Santiago?)",
        "Santiago, Biblioteca Nacional de Chile, manuscritos, 1 unnumbered leaf (Aleph sys. 001054112)", ["001054112"],
        "1 f., autograph; 'Documento escrito en clave durante la Guerra Civil por José Manuel Balmaceda'",
        "BN Chile catalogue; no transcription noted. " + KEYS_1891,
        "The president's own cipher in the war that ended with his suicide.", imp=3, solv=1, diff=2),
    bnc(1891, "23 Aug - 1 Sep 1891",
        "'Marco' → Claudio Matte (Berlin): 22 telegrams partly in cipher on watching the property and persons of the Balmaceda administration",
        "'Marco' (pseudonym) → Claudio Matte Pérez", "unknown → Berlin",
        "Santiago, Biblioteca Nacional de Chile, manuscritos, pieces 19981-20002 (Aleph sys. 000486117)", ["000486117"],
        "22 ff., typed telegram forms completed by hand in blue pencil; 'Telegramas con información en clave'",
        "BN Chile catalogue: information in cipher; no decipherment noted. Claudio Matte was the Congressist agent in Germany; the Congressist code sheets (sys. 001156145, 001156140) are in the same library.",
        "Congressist intelligence on Balmacedist assets abroad at the end of the civil war (Balmaceda resigned 29 Aug).",
        imp=2, solv=2, diff=2, cls='A',
        verify="Request scans of pieces 19981-20002 and of the 'Códigos y claves' sheets (sys. 001156140/001156145); try the Congressist code first."),
    bnc(1837, "18 Oct 1837",
        "Luis José Orbegoso, president of North Peru → Andrés de Santa Cruz, Protector of the Peru-Bolivian Confederation: letter with information in cipher (contemporary copy)",
        "Luis José Orbegoso → Andrés de Santa Cruz", "Lima",
        "Santiago, Biblioteca Nacional de Chile, manuscritos, 2 ff. (Aleph sys. 000608379)", ["000608379"],
        "2 ff., manuscript transcription; 'Da a conocer el movimiento de tropas; en clave proporciona información'",
        "BN Chile catalogue: part in cipher; it is a contemporary transcription (possibly an intercepted copy, given its place in a Chilean library); no decipherment noted.",
        "Confederation correspondence in the weeks after the Chilean expedition's Paucarpata treaty; a Peruvian or Bolivian state cipher of the 1830s.",
        imp=3, solv=1, diff=3),
    bnc(1825, "undated ('[18--?]'; filed under Uruguay, independence 1810-1828)",
        "Allegorical code letter 'No. 1. La Estrella de la Banda Oriental y vos merse ambas se unen y ofrecen mutuamente servir a Sn. Miguel...', with its key",
        "unknown → unknown", "unknown",
        "Santiago, Biblioteca Nacional de Chile, manuscritos, bound volume pp. 349, 343-344, with piece 75 (the key) (Aleph sys. 000103674)",
        ["000103674"],
        "2 parts; 'La pieza 75, corresponde a las claves para poder descifrar la carta descrita'; bound with a letter of 3 Jun 1843 from Lima to 'Canónigo Albano'",
        "BN Chile catalogue: a cover-name letter ('el Santo se mueve de cuando en cuando de una parte de los cielos') whose key is bound with it; whether anyone has applied the key is not recorded.",
        "A conspiratorial cover-name letter of the Río de la Plata independence era ('San Miguel' may be José Miguel Carrera, who plotted from Montevideo 1817-1820).",
        imp=2, solv=2, diff=1, cls='A',
        verify="Request scans of pp. 343-349 and piece 75; apply the key."),
    bnc(1921, "23 Mar 1921",
        "Antonio Huneeus Valdés (Paris) → Chilean government: telegram in cipher on the Upper Silesia plebiscite",
        "Antonio Huneeus Valdés → Chilean Foreign Ministry (presumed)", "Paris",
        "Santiago, Biblioteca Nacional de Chile, manuscritos, Hoja 15522 (Aleph sys. 001118451)", ["001118451"],
        "1 f., 'Copia original de telegrama manuscrito. Telegrama escrito en clave'",
        "BN Chile catalogue: 'Telegrama escrito en clave'; the summary (opinion on the Upper Silesia plebiscite) suggests a decipherment or plain draft exists alongside.",
        "Chilean diplomatic code of 1921 (Huneeus at the League of Nations, the Tacna-Arica question before the League).",
        imp=1, solv=1, diff=3, period='1901-1950'),
]

if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, 'candidates.json'), 'w', encoding='utf-8') as fh:
        json.dump(ROWS, fh, ensure_ascii=False, indent=1)
    print(len(ROWS), 'rows')
