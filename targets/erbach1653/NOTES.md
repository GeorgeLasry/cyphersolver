# Erbach-Fürstenau to Ludwig VI, 1654-1670 (HStAD D 4 Nr. 248/3)

Catalogue no. 569. Count Georg Ernst zu Erbach (1629-1669) to Landgrave Ludwig VI of Hesse-Darmstadt, 39 letters,
"z.T. chiffrierte Briefe", alchemical matter (Dr Johann Tack). Hessisches Staatsarchiv Darmstadt, D 4 Nr. 248/3,
Arcinsys detail id v4503719, DDB item LU6DLFTL56RRNJ4YNHQMGDTPKEJFNC4G. Finding-aid date range 1654-1670.

**Result (27 Oct 2026): all three cipher letters deciphered.** The cipher is a letter-position book cipher: each
pair a,b is the b-th letter of line a of a rhymed German Lord's Prayer ("O Vatter aller frommen / geheiligt werd
dein nahm / las dein reich zu uns kommen / dein will der mach uns zahm / gib brod vergib die sund / kein args das
hertz entzunde / los uns aus aller nott"). The key verse was rebuilt from cribs taken from a contemporary Latin
outline of the long letter, filmed beside it. 610 pairs: 591 (96.9%) read as the key gives them, the other 19
are neighbouring-cell slips by the writer that the sense corrects; statistical validation passes.

## Sources and access

- Scans: 78 JPGs (3500 px, microfilm frames of open double pages), served openly by the archive at
  `https://digitalisate-he.arcinsys.de/hstad/d_4/248--3/hstad_d_4_nr_248--3_NNN.jpg` (licence CC BY / CC0 per
  the DDB EDM record). The Archivportal-D item page sits behind an Anubis bot check; the DDB API
  `https://api.deutsche-digitale-bibliothek.de/2/items/<id>/edm` lists the image URLs without it
  (`src/ddb_edm.xml`, `src/urls_248-3.txt`). Images in `img/` (git-ignored). Images 000-027 are film 1, 028-029
  film cards, 030-038 a second filming of 001-009, 039-077 the rest.
- Candidate key material fetched the same way into `key/` (git-ignored); neither is the key:
  - D 4 Nr. 141/2 (7 images): "Alphabete und Chiffren einer Geheimschrift" for Georg II and Cardinal Friedrich,
    1652 and 1658.
  - D 4 Nr. 239/1 (258 images, 000-107 viewed as contact sheets): Ludwig VI's "Notizen und verstreute
    Aktenstücke" Bd. 2. Images 008-011 hold a Thirty Years' War homophonic number table headed "Hamburg ..."
    (values 10-166 under a 24-letter alphabet) with a German letter deciphered above the line ("ambassadeur de
    France", "regimenter", "König") and code lists 135-242 (Embassadeur de ... a Hamburg, Minden, Salvius, armée
    de Weimar, Comte d'Eberstein, armée de Hesse, armée suédoise) and 157-230. That is 1640s Georg II material
    and belongs with the catalogue's Georg II entry, not here. 108-257 not viewed.

## Where the cipher is (survey, work/survey_A.md and survey_B.md)

Only three letters carry cipher, all from the 1666 series addressed "à Stokholm":
- 003 = 032: No. 1, Fürstenau 22 Mar 1666, two runs, 25 pairs (`ct_003.txt`).
- 006 = 035: No. 2, 27 Apr [1666], one run of 14 pairs (`ct_006.txt`).
- 004 = 033: undated two-page letter, 571 pairs (`ct_004.txt`), with the Latin outline slip.
Images 039-077 (Dec 1658 - Apr 1660 letters, mostly endorsed "an D. Tacken", and Ludwig's replies) have no cipher:
only an anagram signature ("J. Strenuus Segrego" = Georgius Ernestus), Ludwig's "Tuus Totus 666" (LUDOVICUS in
Roman numerals) and cover names in a 1654 allegory (Pan, Bacchus, Neptune, Diana). The finding aid's
"z.T. chiffrierte Briefe" refers to the three 1666 letters.

## The system and the key

Pairs written "a,b." inline in German or Latin text, words often closed by a vertical stroke "|". a = line of
the key verse (1-8), b = letter position in that line, counting letters only. Rows used: 1-19, 1-21, 1-23, 1-22,
2-18, 1-24, 1-18, and row 8 only at 8,1 (p) and 8,3 (x). The writer scans forward along a line (runs such as
1,10 1,11 1,12 or 3,20 3,22 3,23), so the same plaintext letter takes many cells: 123 distinct cells in 610
pairs.

`key.txt` holds the verse as rebuilt. Each row's spelling is fixed only where a cell is used; unused letters
come from the verse wording. Row 8 is known only as "p?x". The verse is a rhymed Lord's Prayer; no printed
source was found by web search (27 Oct), so its author is not identified.

## How it was deciphered (27 Oct 2026)

1. Transcribed letter 004 from rotated, enlarged crops (`work/p004/`), checked against the second filming (033).
2. A plain homophonic anneal on 124 cells (`solve.py`, Latin 5-gram) did not converge: about 4.6 tokens per cell.
3. The slip filmed beside 004 (`work/slip_004.png`) is a Latin outline of the letter in a contemporary hand:
   "Status turbulentus ...; Bell. Electorale; onerosa ... quotidie crescens; Regimen ... filii(?); pericula
   ..., tam ... subditorum quam ...; subditorum fiducia; divisio bonorum ...; defectus fidelitatis", and on the
   lower flap a near-verbatim gloss of the Hic quaeritur passage ("... salutem Ecclesiae subditorum ... sine
   laesione conscientiae et offensione Dei haec omnia possit deserere et mercenariorum directioni oves suas
   submittere ‡ ac sic periculis jamdum praevisis ...").
4. Cribs from it ("turbulentus", "defectus", "dominus cui deus salutem ecclesie", "conscientie et offensione
   dei", "mercenariorum", "oves suas", "periculis") gave about 80 cells (`key_cells.tsv`, `partial.py`). Letters
   in the same row began to spell words: row 4 "dein will ... uns", row 3 "las dein reich zu uns", row 7 "los uns
   aus aller not", row 1 "o vatter aller frommen". The rest of each row followed from the verse.
5. The whole text was deciphered with the verse key unchanged (`decode.py`). Of 80 crib cells, four disagreed
   with the verse, all crib guesses of mine ("ecclesie" is spelled with e, etc.).
6. Letters No. 1 and No. 2 deciphered with the same key.
7. Validation (`validation.tsv`, `docs/_validate.py`, Latin model): reading -2.390 per letter, random keys
   -4.598 (sd 0.206, z 10.7), shuffled refit -2.641 (max -2.589), verdict pass.

## The reading

`reading_004.md` (edition and translation), `reading_003_006.md`, raw output `decrypt_*.txt`, pair by pair in
`reading.tsv`. Letter 004 gives eight reasons why Erbach cannot leave his county and hand it to others: the
troubled state of the Empire, the electors' war nearby, his wife's illness, his brothers about to take up
government (by connivance and a dispensation of age) with youthful counsels, his subjects' trust in him, the
division of property with his brothers, and the councillors' want of loyalty; then asks whether a lord to whom
God entrusted church, subjects, house and wife may abandon them and "put his sheep under hirelings" (John 10:12).
No. 1 mentions "unsers vorhabens" and changes since; No. 2 says the division of property is due in May or June.

Letter 004 is undated. No. 2 (27 Apr 1666) says Erbach has already sent "meine rationes" by letter and hopes Ludwig
will find them "relevant genug" and not accuse him of inconstancy; with the shared cipher and subject (the division
of property) this makes 004 the reasons letter, written before 27 April 1666.

## Remaining gaps

- words in the clear German frame of the three letters (not cipher), marked [?] and [..] in clear_text.md -
  blocker: illegible; microfilm frame, Kurrent at about 25 px per line; the archive holds only this film
- pair 11 of letter No. 2 (read 7,7, sense needs an s) and the clause p1.11 "nich wie sche[X]rts[X]s" (blots in
  the manuscript) - blocker: illegible; ink blots over the cipher, same on both filmings

## Escalation

- [x] siblings: all 78 images of the file surveyed; the two other cipher letters (Nos. 1 and 2) read with the
  same key
- [x] clear-pages: the Latin slip filmed with letter 004 is the contemporary outline; used as the crib
- [x] known-keys: Hesse-Darmstadt keys D 4 Nr. 141/2 (Georg II and Cardinal Friedrich, 1652/1658) and the 1640s
  number table in D 4 Nr. 239/1 checked; neither is this system
- [x] print: web searches (German and English) for an edition or study of the letters and for the verse: none
- [x] key-rebuild: key verse rebuilt from cribs and the rows' own text; every pair has a value
- [x] retry: every slip re-checked on the second filming (033, 032, 035); the 19 slips are listed in
  reading_004.md and reading_003_006.md

## Prior work

- 26 Oct 2026 web searches (German and English; Erbach, Ludwig VI, Tack, Geheimschrift, Chiffre, Alchemie): no
  edition, study or decipherment of these letters found. The catalogue's own check (known.py) found none.
- The slip shows the long letter was read, at least in outline, at the time. It gave the cribs.

## Log

- 26 Oct 2026: worktree off origin/main; scans and both key files downloaded; survey of all 78 images.
- 26-27 Oct 2026: 004 transcribed; anneal failed; slip cribs; key verse rebuilt; all three letters deciphered;
  validation pass.
