# Re-reading log, R46 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R46_decryption.txt` (character-model segmentation of DECODE's
transcription D1711, KaJo, Dec 2015, under Meister no. 40) scored 0.69: the Council of Trent passage was mostly
legible, Morosini's long complaint about the Pope's displeasure much less so ("lioentiati nostri", "iosue si credito").

## 1. Is there a text already?

- DECODE images: 7 cipher pages (381r–384r) and 2 "cleartext" images (despatches in clear, not a decipherment).
- Tempesti (1754) II, book IX (scratch OCR ll. 1636–1660, 3005–3030) quotes Montalto's cipher of 16 December 1588 on the
  Trent clause, which this letter answers, and then Morosini's reply "con cifra de' 24 Gennaro" [1589]: a close
  paraphrase of 382v ("Mi dolgo in estremo che N. S. si mostri mal sodisfatto di me … tanto lontani non sol dal
  probabile ma anche dal possibile … con maggior ualore et prudenza di me"). It dates the letter (Blois, 24 January 1589)
  and confirms the catchword: 382v's catchword 2 1 5 0 9 1 1 is "[u]alor(e)", and Tempesti's text after "ualore et
  prudenza di me" ("non l'havrebbe però servito … taluno in Roma si mostra mal soddisfatto di me …") is not on 383r,
  which goes on with other matter — so a leaf of the cipher is missing between 382v and 383r. Used for sense and
  date only; no word was taken from it.
- The transcriber noted that the page order might be wrong (catchword on 382v). Checked on the image: the catchword
  "2 1 5 0 9 1 1" at the foot of 382v matches no page in the record; 383r begins with "…ere magiore autorità". The order
  381r–384r is kept; a leaf is missing between 382v and 383r (see Tempesti above; outside blocker for that junction).

## 2. Word decode and hand re-parsing (R46_corrections.tsv, 64 rows)

- One transcription line was wrong: 382r l. 12 repeats the end of l. 13; the image gives "… Serenis. di Sauoia [?scrita] a
  V. S. Ill.ma, che mi [i]nuiò con le sue di tre di otobre". `R46_transcription_corrected.txt` carries this line
  (used for the alignment).
- Numbers in plain figures: "di 24 del pasato", "di 23 d'otobre", "di 1[8?] di Nouembre".
- Codes with displaced or missing dots: 161 (et quanto), 216 (auiso, dot on the 6), 167 + 19 (decoder: code 1671); 111
  written 1111. Codes written with a wrong first figure, consistently: 265 for 165 (three times) and 267 for 167.
- The figures give 26 for "et" four times (381r l. 14, 381v l. 20, 383v l. 7, 383r l. 1 "et dominio"); 4 for 14 (h)
  twice (hora, honore).
- Abbreviations with 8: santis. piedi, prontam., chiaram., altram.; m without 8: liberam., fedelm.
- Vocabulary gaps where the figures were right: esortauo, patti, uisum est Spiritui Sancto et nobis, Sanlis, guarda
  sigilo, riesce, comandata, uiueza, d'aquistarmi, sconsolatisimo, reflesso, saprei, disgustato, discusarmi, diceria.
- Image checks (crops, scratchpad only): 382r ll. 10–13 (the repeated line), 382v ll. 19–21 and 383r l. 1 (catchword).

## 3. Alignment

`python reread_b00_align.py R46 --trans ../../targets/morosini1588/texts/R46_transcription_corrected.txt`:
`TOTAL R46: 1304 words, 1 supplied, 7 partly` after these fixes from the first run: three page markers moved to where
the page breaks fall inside words (pr|oposte, scons|olatisimo, scriuen|do), "publi[c]are" bracketed, "ad esere" →
"a esere", "temere" → "temer". The remaining flags ("di" and "cifre" at code 219, medesme, conuenirà) are carried.

## Result

Before: 0.69. After: 0.81 clean-sentence share on the "## Reading" body (hole rate 0.076). By hand: 10 unread stretches
([…]), 6 partly carried words, 1,300 words; the letter reads as continuous sentences. Grade A-: sentences hold
throughout; the holes are short; one transcription line corrected from the image.

## Still open, and why

- 381r l. 3 opening; 381v l. 20 ("2 6 2 1 7 1 1 9 5 4" before ocasione); 382v ll. 5–6 ("4 5 1 7 2 0 1 7 1"); 383r l. 4
  ("2 0 5 4 9 1 7 1"); 383v ll. 3 and 13; the last line of 384r: no parse under the slips tried (not re-checked on the
  image).
- The junction 382v/383r: a leaf probably missing (catchword mismatch) — outside blocker.
- 384r ends in mid-sentence (the rest of the letter is not in the record).

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

Each hole located (`research/reading_audit/r2p_holes.py`), its line looked at on the image (scratchpad
`reread/r2p/crops`; the pages are clean), cancellation strokes looked for, the figures parsed (`r2p_parseall.py`).
Withdrawn:
- 383r l. 2 "Se poi […] riesce": the lone figure there is struck through with two strokes by the encipherer (a
  cancellation, as on R40): no word stands between "poi" and "riesce".
Left, with blockers:
- 381r l. 3 "[…] con l": "9 2 0 5 2 7 3 1715^. 8" (best parse "omciuit"). Blocker: no-key-material.
- 381r l. 15 "et nobis [?et] replicandole in": "8 2 6". Blocker: no-key-material.
- 381r l. 18 "lasciò di publi[c]are nei Stati": "7 0 3 7 2 4 5 0 1 7 2 1 0 0 5" (best parse "publiare"). Blocker: no-key-material.
- 381v l. 20 "suo regno [?et] che pregaua": "2 6". Blocker: no-key-material.
- 381v l. 20 "che pregaua [?dar] […]": "6 2 1 7 1 1 9 5 4" (best parse "dixos"). Blocker: no-key-material.
- 382r l. 15 "cifre di 1[8?] di Nouembre": "1 8". Blocker: too-short.
- 382v l. 5-6 "particolari fastidiosi […] tanto lontani": "4 5 1 7 2 0 | 1 7 1" (best parse "simi"). Blocker: no-key-material.
- 382v l. 9 "posi hauere [?le] prestata alcuna": "0 5". Blocker: no-key-material.
- 382v l. 20 "con magior […]": "8 3". Blocker: too-short.
- 383r l. 1 "[…] ere magiore": "3 7". Blocker: too-short.
- 383r l. 4 "o da […] né uoglia": "2 0 5 4 9 1 7" (best parse "msoi"). Blocker: no-key-material.
- 383v l. 3 "ationi mie […] prego con": "8 1 7 1 0 5 6" (best parse "ilt"). Blocker: no-key-material.
- 383v l. 7 "il Re [?et] il regno": "8 2 6". Blocker: no-key-material.
- 383v l. 10 "del contrario conuenir[à] a esere": "1 9 3 7 3 5 0 1 1 7 0 0" (best parse "conuenir"). Blocker: no-key-material.
- 383v l. 13 "N S […] Et per": "9 2 2 0 0 3 5" (best parse "oamfe"). Blocker: no-key-material.
- 384r l. 8 "ma l un[o] et l": "1 7 3 0 1" (best parse "un"). Blocker: no-key-material.
- 384r l. 16-17 "altram[ente] auisata […]": "8 4 2 0 1 0 9 2 7 | 196^. 1 7 3 4 2 0 0 7 0 7 2 2 1 0 0" (best parse "mnoai[sauoia]riscarpiaar"). Blocker: no-key-material.
Result: 1 hole withdrawn (a cancelled figure); 18 left, each with its blocker.
