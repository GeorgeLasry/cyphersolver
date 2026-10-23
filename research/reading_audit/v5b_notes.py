"""v5 (b): write the dated NOTES.md block of verification 5 (plain bar) into each target of v5_plainbar_b.txt, before
'## Remaining gaps' (v4_notes.py convention); nunzio1718 also gets an Escalation line.

    python research/reading_audit/v5b_notes.py [target ...]
"""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
SCR = pathlib.Path(r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\v5\b\notes')
SCR.mkdir(parents=True, exist_ok=True)
H = '**23 Oct 2026, verification 5 (plain bar; research/reading_audit/VERIFY5_BRIEF.md)**: '
T = ' Rescored with research/reading_audit/v2_score.py (plain word-list share and explicit-hole share); both figures are in each entry\'s reading_review note. Keeps read.'
B = {
 'lucini1767': "the sweep had scored decrypt_output.txt, the raw group decode. READING.md is the reading; a '## Reading' heading now marks its body (clear text from MEG's transcription with the deciphered closing passage): plain 0.771, explicit 0.914. 8107 stays open; the sentence runs on to a leaf not imaged.",
 'mercy1648': "Spanish of 1648 in period spelling (saver, saueis, uenga, tardanca, cuydado, zelo), so the explicit-hole share is the bar. reading.txt joined into running text: plain 0.429, explicit 0.821; cl/reading.txt (NoAutopilot's reading before the corrections): 0.471 / 0.941. The plain failures are period spellings, names and the trimmed-edge holes of f. 22v.",
 'mondesir1769': "Lasry's excerpts written out alone as lasry_excerpt_reading.md (the report page had been scored): plain 0.667, explicit 0.75; the failures are his [?] marks and run-together forms.",
 'portugal1667': "the text is Portuguese of 1667 (not French), so the explicit-hole share is the bar. Lasry's excerpt written out as lasry_excerpt_reading.md: explicit 1.0; the Portuguese word list does not know 1667 spelling (plain 0.0 on two sentences). Entry language set to pt.",
 'vergier1696': "Lasry's excerpt written out alone as lasry_excerpt_reading.md (the report page had been scored): plain 1.0.",
 'villardeau': "Lasry's excerpt written out alone as lasry_excerpt_reading.md (the report page had been scored): plain 1.0.",
 'villeneuve1737': "Lasry's excerpts written out alone as lasry_excerpt_reading.md (the report page had been scored): plain 0.6, explicit 1.0; failures are 1737 spellings (raport, refflection, allors), Kerim Bey and 'pu'.",
 'nunzio1736': "'## Reading' headings added to texts/423-2, 4, 6, 7, 8 and 10_reading.md, whose English headers the sweep had scored with the body: bodies plain 0.619-1.0, explicit 0.857-1.0. 423/3 had only Lasry's running text (reading_423-3.txt); texts/423-3_reading.md written from the b04 decode, word-divided: plain 0.667 (3 sentences), explicit 1.0, one run of three valueless groups.",
 'pallotto1629': "'## Reading' headings added after the header rule of texts/R294, R295, R299, R303 and R308_reading.md (the sweep had scored the English headers with the bodies): bodies plain 0.806-1.0, explicit 0.833-1.0.",
 'potocka1714': "the cipher is single words and short phrases inside clear French; each insertion put into its clear anchor (research/reading_audit/v5b_potocka.py) scores plain 0.5-1.0 and explicit 0.9-1.0 per letter section (R7529 0.5 on four phrases: the writer's spellings cete, na, loubrire). The insertions fit their anchors.",
 'r1892': "the letter is of 1795 (the folder is named for DECODE R1892). texts/p1_reading.md: plain 0.55, explicit 0.70; the plain failures are 1795 spellings (pouroit, pourez, cesseroit), names (Nagel, Vundas = Dundas), letters supplied at word ends and four unread signs. Each sentence builds.",
 'r2232': "reading.txt puts the deciphered parts in [brackets], which the scorers count as holes. Written out as reading.md with them in italics, wording unchanged: plain 0.833, explicit 0.896. reading.txt's spelling is lightly modernised (its header says so); not redone here.",
 'r2234': "reading.txt puts the deciphered parts in [brackets] and labels each line with its alphabet. Written out as reading.md with the deciphered parts in italics, wording unchanged: plain 0.818, explicit 0.879.",
 'rakoczi1707': "'## Reading' and '## Corrections' headings added to R902_reading.md (the sweep had scored header and correction list with it): body plain 0.771, explicit 0.896; failures are unread groups and names. The file's header says spelling is normalised; not redone here.",
 'ronquillo1676': "'## Reading' headings added after the titles of read/R966-R984_reading.md (14 files; the sweep had scored the notes with the readings): bodies plain 0.69-0.91 and explicit 0.90-1.0, except R982 (unmargined, read on the image) plain 0.552, explicit 0.828: its plain failures are gaps of the Spanish word list and the known soft-scan / no-key holes, about one per failing sentence; it keeps read on the reader's judgement. The readings' headers say spelling was modernised; not redone in this pass.",
 'sabran1633': "rescored the 18 French sections of lasry2022/READING.md: plain 0.519, explicit 0.715, hole rate 0.088. The writer spells by ear (secretere, trete, afaire, eloignemant) and the tentatively read name codes count as holes; the rest builds sentences.",
 'siena10': "the slip belongs to the Montepulciano campaigns of 1495-1511: older Italian, explicit-hole bar 1.0 ('presura', 'Montepulciano' the only plain failures).",
 'siena12': "the letter is Italian (Neapolitan) of 1413, not French: explicit-hole bar. reading_no12.txt (Lasry's decipherment verbatim): explicit 0.708, plain 0.25 on dialect forms. Entry language set to it and reading pointed at reading_no12.txt.",
 'sieniawski1708': "the letters are Polish (not French): explicit-hole bar. The reading is Kaczka's edition (2012, linked, not copied), checked word for word over ten lines of R7473 (sien/R7473_check.txt, key-A decode explicit 0.8). Entry language set to pl.",
 'soglia1848': "texts/plaintext.md's heading renamed '## Reading' and '## English' added before the translation (the sweep had scored plaintext_guess.txt): body plain 0.727, explicit 1.0.",
 'sp106r597': "transcription.txt is a clear instruction sheet; its prose without the digit tables: plain 0.706, explicit 0.882 (failures: the French example sentence, the digit run).",
 'sunyatsen': "the text is Chinese; the sweep had scored the English gloss. The word lists cannot score Chinese; read by the reader: five sentences, one unread character, the last word garbled.",
 'turculet1709': "the letter is Polish of 1709 (not French): explicit-hole bar. R7481_reading.txt body: explicit 1.0, plain 0.222 (small Polish word list, Latin phrases, names). The reading is in modernised Polish (9 Oct 2026); not redone here.",
 'vanreede1792': "'## Reading' and '## English' headings added to texts/R1057_decryption.md around the deciphered note: body plain 1.0.",
 'vizani1637': "the letter is Italian of 1637 (not Spanish). Satoru's reading: plain 0.333, explicit 0.667 on six sentences; the holes are the five name codes (no key material), one unread sign and 'dattone?'. Each sentence builds around the codes: only scattered codes open.",
 'wesselenyi1664': "the draft is Latin (not French): explicit-hole bar. reading.md blockquote: explicit 0.778, plain 0.222 (small Latin word list); holes are codes 60 and 64 and doubtful clear words.",
 'windischgraetz1720': "the letter is German (not French): explicit-hole bar. The 26 cipher passages, each with the clear words before it: plain 0.923, explicit 0.962.",
 'windischgraetz1720b': "the letters are German (not English): explicit-hole bar. The passages of Nos. 2, 3 and 6 in their quoted clear context: explicit 1.0 each.",
 'nunzio1718': ("the 22 despatches other than R154 and R173 had no reading file; the sweep had scored DECODE's figure tables "
   "(plain 0.0-0.33). Readings lasry/R155-R177_reading.md written (R173 excepted): Lasry's decode rows with key_extra.txt and the "
   "b22 changes, word-divided by hand beside DECODE's PLAINTEXT rows (the transcribers' copies of the contemporary interlinear "
   "decipherment, accents lost); where a group is mis-valued or the figures garbled the interlinear's word is followed, named in each "
   "file's notes (helpers research/reading_audit/v5b_nunzio_rows.py, v5b_nunzio_side.py). For R170 and R172, whose DECODE "
   "transcriptions miss figure lines and whose PLAINTEXT rows are garbled, the interlinear was read on the DECODE images "
   "(lasry/R170_decifrato.txt, R172_decifrato.txt). R163 and R177 have no interlinear on the leaves (images checked): their readings "
   "rest on the figures. Bodies score plain 0.67-1.0, explicit 0.96-1.0 (R175, three lines, plain 0.5). Found on the way: R163 is a "
   "second copy of R162 + R161; R168 ('Dup.B') of R166; R176 of R173 plus a short passage on f. 360r; R174 and R175 are the closes of "
   "passages whole in R177 and R176. Lasry groups the interlinear reads otherwise, at several places each (not adopted as key "
   "changes in this pass, for review): the 'stessi' group = volte/volta (R155, R166, R167, R170), the 'tanto' group = Armata (R158, "
   "R163) and other words, 4113 'Card.le' = conte- (contenuto, contenti, contestargli), the 'questo' group = Apostolic-, the "
   "'qualsivoglia' group = Arcivescovi (R167, R170), 'Vesconi' = Vienna, 4482 = caduto (not corrente), the date group Lasry reads 12 = 2. "
   "Open groups valued from the interlinear: 4083 udienza, 4123 distint-, 4185 impressione, 4232 occorrenza, 4357 Non, 4389 La, 4425 "
   "Stato Ecclesiastico, 4430 S.M. Cesarea, 4488 primo, 4495 ottavo, 4496 nove, 4497 dieci/decimo, 4548 dispaccio, 4917 savia."),
}
ESC = {'nunzio1718': '- [x] retry: 23 Oct 2026 (verification 5): readings written for the 22 other despatches; R170/R172 interlinear read on the DECODE images'}
if __name__ == '__main__':
    only = sys.argv[1:]
    for t, txt in B.items():
        if only and t not in only: continue
        f = SCR / f'{t}.md'
        f.write_text(H + txt + T + '\n', encoding='utf8')
        cmd = [sys.executable, str(HERE / 'v3b_notes.py'), t, str(f)]
        if t in ESC: cmd += ['--esc', ESC[t]]
        r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf8')
        print(r.stdout.strip(), r.stderr.strip()[-300:])
