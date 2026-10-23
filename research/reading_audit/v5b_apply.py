"""v5 (b): build the per-target action files for v5_b.py (a copy of v4.py) from the decisions of verification 5, list b
(v5_plainbar_b.txt), and apply them. Every row keeps read; a reading_review note gets the v5 check appended (existing
notes are kept); nunzio1718's 22 entries get the readings written in this pass (lasry/R155-R177_reading.md).

    python research/reading_audit/v5b_apply.py [--dry] [target ...]
"""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SCR = pathlib.Path(r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\v5\b\actions')
SCR.mkdir(parents=True, exist_ok=True)
V5 = 'v5 check 23 Oct 2026 (plain bar, VERIFY5_BRIEF): '


def entry(t, i):
    return json.loads((ROOT / 'targets' / t / 'profile.json').read_text(encoding='utf8'))['outcome']['texts'][i]


def rev(t, i, note, grade=None, fields=None):
    """keep read: append the v5 note to the existing reading_review note (or start one)."""
    e = entry(t, i)
    old = (e.get('reading_review') or {}).get('note', '')
    full = (old.rstrip() + ' ' if old else '') + V5 + note
    r = dict(doc=f'#{i}', note=full)
    g = grade or (e.get('reading_review') or {}).get('grade')
    if g: r['grade'] = g
    out = {'review': [r]}
    if fields: out['fields'] = [dict(doc=f'#{i}', fields=fields)]
    return out


def step(what, result='worked', kind='verification', tech=('statistical test', 'manual reconstruction')):
    return dict(date='2026-10-23', kind=kind, technique=list(tech), what=what, result=result)


A = {}


def add(t, d):
    a = A.setdefault(t, {})
    for k, v in d.items():
        a.setdefault(k, []).extend(v)


# ---------------------------------------------------------------- single-file false alarms and older spellings
add('lucini1767', rev('lucini1767', 0,
    "the sweep scored decrypt_output.txt, the raw group decode (plain 0.0, explicit 1.0). The reading is READING.md (MEG's "
    "clear transcription with the deciphered closing passage); a '## Reading' heading now marks its body: plain 0.771 "
    "(27/35), explicit holes 0.914, hole rate 0.026. Sentences hold; 8107 open and the sentence runs on to a leaf not imaged. "
    "Keeps read.", grade='A', fields={'reading': 'READING.md', 'language': 'it'}))
add('mercy1648', rev('mercy1648', 0,
    "Spanish of 1648 in period spelling (saver, deven, saueis, uenga, tardanca, summo, cuydado, zelo, embian, paresca), so "
    "the explicit-hole share is the bar. reading.txt (line-numbered) joined into running text (v5b_lines.py): plain 0.429 "
    "(12/28), explicit holes 0.821 (23/28), hole rate 0.058; the plain failures are those spellings, names (Cheureuse, "
    "Brandenburg, Burgstorf, Barneton), gaps of the Spanish word list (fuisteis, regimientos) and the trimmed-edge holes of "
    "f. 22v. Sentences hold. Keeps read.", grade='A', fields={'reading': 'reading.txt'}))
add('mercy1648', rev('mercy1648', 1,
    "the record of NoAutopilot's reading before the eight corrections (entry 0 is the verified reading). Spanish of 1648 in "
    "period spelling: explicit-hole bar. cl/reading.txt joined (v5b_lines.py): plain 0.471 (8/17), explicit holes 0.941 "
    "(16/17), hole rate 0.029; plain failures are period spellings and names. Keeps read.", grade='B',
    fields={'reading': 'cl/reading.txt'}))
for t, lang, sc, why in [
        ('mondesir1769', 'fr', 'plain 0.667 (8/12), explicit holes 0.75 (9/12), hole rate 0.041',
         "the failures are Lasry's own [?] marks and run-together forms (maccorder, largent)"),
        ('vergier1696', 'fr', 'plain 1.0 (7/7), explicit holes 1.0, hole rate 0.012', 'no sentence fails'),
        ('villardeau', 'fr', 'plain 1.0 (3/3), explicit holes 1.0, hole rate 0.0', 'no sentence fails'),
        ('villeneuve1737', 'fr', 'plain 0.6 (9/15), explicit holes 1.0 (15/15), hole rate 0.021',
         "the failures are 1737 spellings (raport, refflection, allors, conpromis), Kerim Bey and 'pu', which the word list lacks"),
        ('portugal1667', 'pt', 'explicit holes 1.0 (2/2), plain 0.0 (2 sentences; the Portuguese word list does not know 1667 spelling: pareceo, aquelle, nam)',
         'Portuguese of 1667, not French: the explicit-hole share is the bar')]:
    e = entry(t, 0)
    add(t, rev(t, 0,
        f"the sweep scored lasry_entry.md, the report page with English contents, key and translation. George Lasry's "
        f"excerpt written out alone as lasry_excerpt_reading.md (his text verbatim, folio labels in the header): {sc}; {why}. "
        f"The reading is Lasry's (his full decryption is not in the repository); the excerpt reads as sentences. Keeps read.",
        grade='A', fields={'reading': 'lasry_excerpt_reading.md', 'language': lang}))
# nunzio1736
for i, n, sc in [(1, 2, 'plain 0.824 (14/17), explicit holes 0.882, hole rate 0.034'),
                 (3, 4, 'plain 0.9 (9/10), explicit holes 1.0, hole rate 0.014'),
                 (5, 6, 'plain 1.0 (11/11), explicit holes 1.0, hole rate 0.008'),
                 (6, 7, 'plain 0.619 (13/21), explicit holes 0.857, hole rate 0.078'),
                 (7, 8, 'plain 0.778 (7/9), explicit holes 0.889, hole rate 0.044'),
                 (9, 10, 'plain 0.757 (28/37), explicit holes 0.919, hole rate 0.039')]:
    add('nunzio1736', rev('nunzio1736', i,
        f"the sweep scored the whole file, English header and notes included. A '## Reading' heading now marks the body of "
        f"texts/423-{n}_reading.md: {sc}. The plain failures are open groups and the Italian word list's gaps. Keeps read."))
add('nunzio1736', rev('nunzio1736', 2,
    "the sweep scored texts/reading_423-3.txt, Lasry's running text with {codes} and a ???? run (plain 0.429, explicit "
    "0.857). Written out as texts/423-3_reading.md from the b04 decode, word-divided (the passage is one sentence, opening "
    "mid-sentence): plain 0.667 (2/3), explicit holes 1.0, hole rate 0.03; one run of three valueless groups ('sicuro di "
    "[...] lode e merito'). Keeps read.", grade='A', fields={'reading': 'texts/423-3_reading.md', 'state': 'read'}))
# pallotto1629
for i, r, sc in [(8, 294, 'plain 0.833 (20/24), explicit holes 0.833'), (9, 295, 'plain 1.0 (15/15), explicit holes 1.0'),
                 (13, 299, 'plain 0.857 (12/14), explicit holes 0.929'), (17, 303, 'plain 0.806 (29/36), explicit holes 0.861'),
                 (22, 308, 'plain 0.947 (18/19), explicit holes 0.947')]:
    add('pallotto1629', rev('pallotto1629', i,
        f"Italian of 1629: plain bar. The sweep scored the whole file with its English header; a '## Reading' heading now "
        f"follows the header's rule in texts/R{r}_reading.md: body {sc}. Keeps read."))
# potocka1714
for i, r, sc in [(0, 'R7525', 'plain 0.857 (6/7), explicit 1.0'), (2, 'R7527', 'plain 0.885 (23/26), explicit 1.0'),
                 (3, 'R7528', 'plain 1.0 (5/5), explicit 1.0'), (4, 'R7529', "plain 0.5 (2/4; the failures are the writer's spellings cete, na, loubrire and a standalone code), explicit 1.0"),
                 (5, 'R7530', 'plain 1.0 (5/5), explicit 1.0'), (6, 'R7534', 'plain 1.0 (2/2), explicit 1.0'),
                 (7, 'R7535', 'plain 0.917 (11/12), explicit 1.0'), (8, 'R7536', 'plain 0.8 (8/10), explicit 0.9')]:
    add('potocka1714', rev('potocka1714', i,
        f"the sweep scored all of reading.md (every letter's insertions with cipher numbers and labels). Each cipher insertion "
        f"of section {r} put into its clear anchor phrase (research/reading_audit/v5b_potocka.py): {sc}. The insertions fit "
        f"the clear text they sit in; no sentence of cipher alone is expected. Keeps read."))
add('r1892', rev('r1892', 0,
    "the letter is of 1795 (the folder is named for DECODE R1892), French: plain bar. texts/p1_reading.md body: plain 0.55 "
    "(11/20), explicit holes 0.70 (14/20), hole rate 0.104. The plain failures: 1795 spellings (pouroit, pourez, cesseroit, "
    "dépences), names (Nagel, Vundas = Dundas), letters supplied at word ends ('flatte[r]', 'elle[s]', counted as holes) and "
    "four unread signs; each sentence builds. Keeps read."))
add('r2232', rev('r2232', 0,
    "the sweep scored decrypt_raw.txt. reading.txt brackets the deciphered parts, which the scorers count as holes; written out "
    "as reading.md with them in italics, wording unchanged: plain 0.833 (40/48), explicit holes 0.896, hole rate 0.033. "
    "reading.txt's spelling is lightly modernised (4 Oct 2026, its header says so); not redone in this pass. Keeps read.",
    grade='B', fields={'reading': 'reading.md', 'language': 'fr', 'state': 'read'}))
add('r2234', rev('r2234', 0,
    "the sweep scored decrypt_raw.txt. reading.txt brackets the deciphered parts (scored as holes) and labels each line with "
    "its alphabet; written out as reading.md with the deciphered parts in italics, wording unchanged: plain 0.818 (27/33), "
    "explicit holes 0.879, hole rate 0.057; the failures are numbers, names (Salm, Osnabruck, Degelmann) and three unread "
    "places. Keeps read.", grade='A', fields={'reading': 'reading.md', 'language': 'fr', 'state': 'read'}))
add('rakoczi1707', rev('rakoczi1707', 0,
    "French of 1707: plain bar. The sweep scored R902_reading.md whole (header and correction list with it). '## Reading' "
    "and '## Corrections' headings added: body plain 0.771 (37/48), explicit holes 0.896, hole rate 0.051; failures are "
    "unread groups and names (Slupce, Gorlitz, Lubben, Posnanie, Stettin, Rehnskiöld). The file's header says spelling is "
    "normalised; not redone here. Keeps read.", grade='B', fields={'reading': 'R902_reading.md', 'language': 'fr', 'state': 'read'}))
for i, r, sc in [(0, 966, 'plain 0.885 (23/26), explicit 1.0'), (1, 967, 'plain 0.844 (27/32), explicit 1.0'),
                 (2, 968, 'plain 0.913 (21/23), explicit 1.0'), (3, 969, 'plain 0.88 (22/25), explicit 1.0'),
                 (8, 974, 'plain 0.744 (29/39), explicit 1.0'), (9, 975, 'plain 0.746 (53/71), explicit 1.0'),
                 (10, 976, 'plain 0.708 (17/24), explicit 1.0'), (11, 977, 'plain 0.76 (19/25), explicit 1.0'),
                 (12, 978, 'plain 0.73 (46/63), explicit 0.984'), (13, 979, 'plain 0.778 (49/63), explicit 0.984'),
                 (15, 981, 'plain 0.725 (58/80), explicit 1.0'), (17, 983, 'plain 0.694 (50/72), explicit 0.903'),
                 (18, 984, 'plain 0.708 (34/48), explicit 0.958')]:
    add('ronquillo1676', rev('ronquillo1676', i,
        f"Spanish of 1676: plain bar. The sweep scored read/R{r}_reading.md with its notes; a '## Reading' heading now follows "
        f"the title: body {sc}. Keeps read."))
add('ronquillo1676', rev('ronquillo1676', 16,
    "Spanish of 1678: plain bar. '## Reading' heading added after the title of read/R982_reading.md: body plain 0.552 (16/29), "
    "explicit holes 0.828 (24/29), hole rate 0.082. The plain failures are gaps of the Spanish word list (progresos, "
    "infelicidad, irresolución, experimentamos, sorprendidos) and the explicit holes the known ones (soft scan; no key "
    "material for dul, al, lop, fin, 109, bc), about one per failing sentence; the sentences build. Keeps read."))
add('sabran1633', rev('sabran1633', 0,
    "French of 1631-35, where the plain share is a bar too; but this writer spells by ear (secretere, trete, afaire, "
    "eloignemant, munitionere, gouuernet) and the name codes read tentatively count as holes. Rescored: the 18 '### French' "
    "sections plain 0.519 (277/534), explicit holes 0.715, hole rate 0.088 (as at v3). The plain failures are those "
    "spellings, names (Garbarin, Sauli, Fiasque, Monaco, Valence) and the name-code holes (no key material). Sentences hold. "
    "Keeps read."))
add('siena10', rev('siena10', 0,
    "the slip is undated but of the Montepulciano campaigns of 1495-1511 (NOTES): older Italian, so the explicit-hole share "
    "is the bar (1.0); 'presura' and 'Montepulciano' are the only plain failures. Keeps read."))
add('siena12', rev('siena12', 0,
    "the letter is Italian (Neapolitan, 1413), not French: older spelling, explicit-hole bar. reading_no12.txt (Lasry's "
    "decipherment verbatim): explicit holes 0.708 (17/24), plain 0.25 (dialect forms: vuie, doe, pigliole, mamole, legiptima); "
    "the holes are his [?] signs and the name signs. Sentences hold. Keeps read.", grade='A',
    fields={'reading': 'reading_no12.txt', 'language': 'it', 'state': 'read'}))
add('sieniawski1708', rev('sieniawski1708', 0,
    "Polish of 1709-14, not French: the explicit-hole share is the bar. The reading is Kaczka's printed edition (Danubius "
    "2012, linked, not copied); the project's check of R7473 p. 17 (sien/R7473_check.txt) matches it word for word over ten "
    "lines, the key-A decode lines explicit 0.8 (4/5; the hole a part-word at the line break). Keeps read (read from "
    "existing decipherment).", grade='A', fields={'language': 'pl', 'state': 'read'}))
add('soglia1848', rev('soglia1848', 0,
    "the sweep scored plaintext_guess.txt (the code decoder's output). texts/plaintext.md is the reading; its heading renamed "
    "'## Reading' and '## English' added before the translation: body plain 0.727 (8/11), explicit holes 1.0, hole rate 0.043. "
    "Keeps read.", fields={'reading': 'texts/plaintext.md'}))
add('sp106r597', rev('sp106r597', 0,
    "English of c. 1731: plain bar. transcription.txt is a clear instruction sheet with digit tables; its prose (tables and "
    "syllable rows cut): plain 0.706 (12/17), explicit holes 0.882; the failures are the French example sentence and the "
    "digit run. Keeps read.", grade='A', fields={'reading': 'transcription.txt', 'language': 'en', 'state': 'read'}))
add('sunyatsen', rev('sunyatsen', 0,
    "the text is Chinese; the sweep scored the English gloss as English. The word lists cannot score Chinese; read by the "
    "reader: five sentences, one unread character (翼□) and the last word garbled, 港 restored from a Morse slip (grade M). "
    "Sentences hold. Keeps read.", grade='A', fields={'reading': 'texts/swatow_decryption.md', 'language': 'zh', 'state': 'read'}))
add('turculet1709', rev('turculet1709', 0,
    "Polish of 1709, not French: explicit-hole bar. R7481_reading.txt body (header and notes cut): explicit holes 1.0 (9/9), "
    "plain 0.222 (the Polish word list is small and splits at ł; Latin phrases; names). Rests on the decode checked against "
    "the interlinear gloss and the fair copy on p. 3. The reading is in modernised Polish (9 Oct 2026); not redone here. "
    "Keeps read.", grade='B', fields={'reading': 'R7481_reading.txt', 'language': 'pl', 'state': 'read'}))
add('vanreede1792', rev('vanreede1792', 0,
    "French of 1792: plain bar. The sweep scored texts/R1057_decryption.md whole (figures and English included); '## Reading' "
    "now marks the deciphered note and '## English' the translation: body plain 1.0 (4/4), explicit 1.0, hole rate 0.017. "
    "Keeps read.", grade='A', fields={'reading': 'texts/R1057_decryption.md', 'language': 'fr', 'state': 'read'}))
add('vizani1637', rev('vizani1637', 0,
    "the letter is Italian of 1637 (not Spanish): plain bar. Satoru's reading as quoted in texts/f292_decryption.md: plain "
    "0.333 (2/6), explicit holes 0.667 (4/6), hole rate 0.096, 73 words. The holes are the five name codes (231, 31, 36, 198, "
    "227; no key material), one unread sign and 'dattone?'; the plain failures add Beria and 'patiarchato'. Each sentence "
    "builds around the codes: only scattered codes open. Keeps read.", grade='A',
    fields={'reading': 'texts/f292_decryption.md', 'language': 'it', 'state': 'read'}))
add('wesselenyi1664', rev('wesselenyi1664', 0,
    "Latin, not French: explicit-hole bar. reading.md blockquote (bold marks and struck words out): explicit holes 0.778 "
    "(7/9), plain 0.222 (the Latin word list is small); the holes are codes 60 and 64 and doubtful clear words. Keeps read.",
    grade='A', fields={'reading': 'reading.md', 'language': 'la', 'state': 'read'}))
add('windischgraetz1720', rev('windischgraetz1720', 0,
    "German, not French: explicit-hole bar. The 26 cipher passages of dec_R5017_letter.md, each with the clear words before it "
    "(research/reading_audit/v5b_wtable.py): plain 0.923 (24/26), explicit 0.962. Keeps read.", grade='A',
    fields={'reading': 'dec_R5017_letter.md', 'language': 'de', 'state': 'read'}))
for i, n, sc in [(0, 2, 'plain 1.0 (3/3), explicit 1.0'), (1, 3, 'plain 1.0 (4/4), explicit 1.0'),
                 (2, 6, 'explicit 1.0 (4/4), plain 0.5 (Beretti, convenienz, inutili et honorifico)')]:
    add('windischgraetz1720b', rev('windischgraetz1720b', i,
        f"German, not English: explicit-hole bar. The cipher passages of No. {n} in dec_R5018_letters.md put into their quoted "
        f"clear context (research/reading_audit/v5b_w18.py): {sc}. Keeps read.", grade='A',
        fields={'language': 'de', 'state': 'read'}))

# ---------------------------------------------------------------- nunzio1718: readings written in this pass
NZ = {  # idx: (R, before plain, before explicit, after, grade, extra)
    1: (155, 0.119, 1.0, 'plain 1.0 (22/22), explicit 1.0, hole rate 0.004', 'A', ''),
    2: (156, 0.1, 0.959, 'plain 0.878 (79/90), explicit 0.989, hole rate 0.005', 'A', ' Two despatches of 8 Feb.'),
    3: (157, 0.0, 0.8, 'plain 0.8 (4/5), explicit 1.0', 'A', ''),
    4: (158, 0.092, 0.971, 'plain 0.886 (70/79), explicit 1.0, hole rate 0.001', 'A', ''),
    5: (159, 0.143, 0.929, 'plain 0.667 (4/6), explicit 1.0, hole rate 0.014', 'A', ''),
    6: (160, 0.083, 0.917, 'plain 0.75 (3/4), explicit 0.75, hole rate 0.061', 'A', ' Three sentences, the failures dates.'),
    7: (161, 0.114, 0.914, 'plain 0.923 (12/13), explicit 1.0', 'A', ''),
    8: (162, 0.097, 0.935, 'plain 0.895 (17/19), explicit 1.0, hole rate 0.004', 'A', ''),
    9: (163, 0.308, 0.615, 'plain 0.896 (43/48), explicit 0.958, hole rate 0.017', 'B',
        ' No PLAINTEXT rows on this record: it is a second copy of R162 and R161, runs further than R162, and the part found '
        'only here rests on its figures alone (two open codes, one garbled run).'),
    10: (164, 0.125, 0.917, 'plain 1.0 (7/7), explicit 1.0', 'A', ''),
    11: (165, 0.036, 1.0, 'plain 0.923 (12/13), explicit 1.0', 'A', ''),
    12: (166, 0.176, 0.912, 'plain 1.0 (14/14), explicit 1.0', 'A', ' The same despatch as R168 (its duplicate).'),
    13: (167, 0.158, 0.959, 'plain 0.911 (214/235), explicit 0.996, hole rate 0.006', 'A', ' 2,758 words.'),
    14: (168, 0.314, 0.971, 'plain 1.0 (14/14), explicit 1.0', 'A', " 'Dup.B' of R166; its own PLAINTEXT rows are garbled, R166 carries the garbled places."),
    15: (169, 0.163, 0.977, 'plain 0.842 (16/19), explicit 1.0', 'A', ''),
    16: (170, 0.22, 0.947, 'plain 0.69 (29/42), explicit 0.857, hole rate 0.059', 'B',
         ' About nineteen cipher lines are missing from DECODE\'s figure transcription and the PLAINTEXT rows are garbled there: '
         'those places are [...]; the interlinear on the DECODE images would close them.'),
    17: (171, 0.101, 1.0, 'plain 1.0 (29/29), explicit 1.0', 'A', ''),
    18: (172, 0.129, 0.952, 'plain 0.684 (13/19), explicit 0.895, hole rate 0.047', 'B',
         ' Several garbled runs in figures and PLAINTEXT rows alike left [...].'),
    20: (174, 0.0, 1.0, 'plain 1.0 (2/2), explicit 1.0', 'A', ' The close of the sentence that R177 gives whole.'),
    21: (175, 0.0, 0.778, 'plain 0.5 (1/2), explicit 1.0, 16 words', 'A',
         ' Three lines, the close of the passage on f. 360r of R176; too short for the share to mean much; the clause builds.'),
    22: (176, 0.0, 0.8, 'plain 0.846 (22/26), explicit 0.962, hole rate 0.014', 'B',
         ' No PLAINTEXT rows: a second copy of R173 (read from its interlinear) plus a short passage on f. 360r; garbled places '
         'carried by R173.'),
    23: (177, 0.333, 1.0, 'plain 1.0 (3/3), explicit 1.0', 'A', ' No PLAINTEXT rows; one sentence, one unread run before \'mani\'.'),
}
for i, (r, bp, be, after, g, extra) in NZ.items():
    n = r - 153
    add('nunzio1718', {'read': [dict(doc=f'#{i}', grade=g, fields={'reading': f'lasry/R{r}_reading.md', 'language': 'it'},
        note=(V5 + f"the sweep scored lasry/364D-{n}.txt, DECODE's figure table with Lasry's decode rows (plain {bp}, explicit "
              f"{be}); no reading had been written. Reading lasry/R{r}_reading.md built: Lasry's rows with key_extra.txt and "
              "the b22 key changes, word-divided by hand line by line beside DECODE's PLAINTEXT rows (the transcriber's copy of "
              "the contemporary interlinear decipherment, accents lost), the interlinear followed where a group is mis-valued "
              "or the figures garbled (named in the file's notes). Body: " + after + '.' + extra + ' Read.'))]})

STEPS = {
    'nunzio1718': [step("Verification 5 (plain bar, 23 Oct 2026): the 22 despatches other than R154/R173 had no reading file; "
        "the sweep had scored the DECODE figure tables (plain 0.0-0.33). Readings lasry/R155-R177_reading.md written: Lasry's "
        "decode rows with key_extra.txt and the b22 changes, word-divided by hand beside DECODE's PLAINTEXT rows (copies of the "
        "contemporary interlinear decipherment); helpers research/reading_audit/v5b_nunzio_rows.py, v5b_nunzio_side.py. Found: "
        "R163 = second copy of R162+R161, R168 = duplicate of R166, R176 = second copy of R173 (+ f. 360r), R174/R175 = closes of "
        "passages whole in R177/R176; Lasry's 'stessi' group stands for 'volte' (4 places), 'tanto' for 'Armata' (2), 4113 "
        "'Card.le' for 'conte-', 4482 for 'caduto'; not adopted. All 22 score plain 0.68-1.0 except R175 (16 words, 0.5); R170 "
        "keeps [...] gaps where ~19 figure lines are missing from DECODE's transcription.", tech=('manual reconstruction', 'plaintext matching', 'statistical test'))],
}
GEN = ("Verification 5 (plain bar, 23 Oct 2026): {what} Rescored with research/reading_audit/v2_score.py; all entries keep read; "
       "reading_review notes record both scores.")
for t, what in {
    'lucini1767': "the sweep had scored decrypt_output.txt (raw decode); READING.md given a '## Reading' heading, body plain 0.771, explicit 0.914.",
    'mercy1648': "Spanish of 1648 in period spelling, so the explicit-hole share is the bar: reading.txt joined 0.429 plain / 0.821 explicit; cl/reading.txt 0.471 / 0.941.",
    'mondesir1769': "Lasry's excerpt written out as lasry_excerpt_reading.md (plain 0.667, explicit 0.75).",
    'portugal1667': "the text is Portuguese of 1667 (explicit-hole bar); Lasry's excerpt written out as lasry_excerpt_reading.md (explicit 1.0).",
    'vergier1696': "Lasry's excerpt written out as lasry_excerpt_reading.md (plain 1.0).",
    'villardeau': "Lasry's excerpt written out as lasry_excerpt_reading.md (plain 1.0).",
    'villeneuve1737': "Lasry's excerpt written out as lasry_excerpt_reading.md (plain 0.6, explicit 1.0).",
    'nunzio1736': "'## Reading' headings added to texts/423-2, 4, 6, 7, 8, 10_reading.md (bodies plain 0.619-1.0); texts/423-3_reading.md written from the b04 decode (plain 0.667, explicit 1.0).",
    'pallotto1629': "'## Reading' headings added to texts/R294, R295, R299, R303, R308_reading.md (bodies plain 0.806-1.0).",
    'potocka1714': "each cipher insertion put into its clear anchor (v5b_potocka.py): sections plain 0.5-1.0, explicit 0.9-1.0.",
    'r1892': "the letter is of 1795; texts/p1_reading.md plain 0.55, explicit 0.70; failures are period spellings, names and supplied word endings.",
    'r2232': "reading.txt's brackets mark the deciphered parts, not holes; written out as reading.md with italics (plain 0.833, explicit 0.896).",
    'r2234': "reading.txt's brackets mark the deciphered parts; written out as reading.md with italics (plain 0.818, explicit 0.879).",
    'rakoczi1707': "'## Reading' and '## Corrections' headings added to R902_reading.md (body plain 0.771, explicit 0.896).",
    'ronquillo1676': "'## Reading' headings added after the titles of read/R966-R984_reading.md (14 files; bodies plain 0.552-0.913, explicit 0.828-1.0).",
    'sabran1633': "18 French sections rescored: plain 0.519, explicit 0.715; plain failures are the writer's phonetic spelling, names and name-code holes.",
    'siena10': "the slip is of 1495-1511: older Italian, explicit-hole bar (1.0).",
    'siena12': "the letter is Italian (Neapolitan) of 1413: explicit-hole bar; reading_no12.txt explicit 0.708.",
    'sieniawski1708': "the letters are Polish (explicit-hole bar); the reading is Kaczka's edition, checked over ten lines (explicit 0.8).",
    'soglia1848': "texts/plaintext.md heading renamed '## Reading', '## English' added (body plain 0.727, explicit 1.0).",
    'sp106r597': "the instruction sheet's prose scored without its tables: plain 0.706, explicit 0.882.",
    'sunyatsen': "the text is Chinese; not scorable by the word lists; read by the reader (one unread character, last word garbled).",
    'turculet1709': "the letter is Polish of 1709 (explicit-hole bar): R7481_reading.txt body explicit 1.0.",
    'vanreede1792': "'## Reading' and '## English' headings added to texts/R1057_decryption.md (body plain 1.0).",
    'vizani1637': "the letter is Italian of 1637; Satoru's reading plain 0.333, explicit 0.667, the holes five name codes without key material, one sign and 'dattone?'.",
    'wesselenyi1664': "the draft is Latin (explicit-hole bar): reading.md blockquote explicit 0.778.",
    'windischgraetz1720': "German (explicit-hole bar): the 26 passages in their clear context plain 0.923, explicit 0.962.",
    'windischgraetz1720b': "German (explicit-hole bar): passages in their clear context explicit 1.0 for Nos. 2, 3, 6.",
}.items():
    STEPS.setdefault(t, []).append(step(GEN.format(what=what)))
for t, s in STEPS.items():
    add(t, {'steps': s})

if __name__ == '__main__':
    only = [a for a in sys.argv[1:] if not a.startswith('--')]
    for t, a in A.items():
        if only and t not in only: continue
        f = SCR / f'{t}.json'
        f.write_text(json.dumps(a, ensure_ascii=False, indent=1), encoding='utf8')
        if '--dry' in sys.argv:
            print('dry', t, {k: len(v) for k, v in a.items()}); continue
        r = subprocess.run([sys.executable, str(HERE / 'v5_b.py'), t, str(f)], capture_output=True, text=True, encoding='utf8')
        print(t, (r.stdout.strip().splitlines() or [''])[-1], r.stderr.strip()[-600:])
