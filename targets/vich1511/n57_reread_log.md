# Re-reading log, N.57 (22-23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b16)

## Starting point

Reading audit (22 Oct): decoded, not read. `n57_transcription_v2_decoded.txt` / `n57_decode_v4.txt` were decoder
output with a space around every code group ("lo s de nro tcampo"), wrong letters and 22 bracketed groups in 35
lines. `_check_reading.py --file`: 0.302 (v2 decode), 0.321 (v4).

## 1. Is there a text of it already?

No. PARES 12751402 has four images, all opened: f. 1r the cipher (32 lines), f. 1v its last three lines with the
clear subscription "en burgos a v de junio de dxij" and the royal rubric, a blank page, and the address "A [mosen
Ger]onymo de Vich del su consejo y su embaxador en corte de Roma" with "Por el Rey" and the docket "1512 Junio 5
Burgos". No interlinear, margin or slip decipherment. The record's description lists none. The neighbouring
records in Estado 8715 that carry decipherments (N.46, N.52BIS) are of other letters; a PARES search for further
neighbours returned HTTP 429 on 22 Oct (rate limit, not retried). Terrateig, *Política en Italia del Rey Católico*
(1963) vol. II may print the clerk's decipherment; it is not online (needs-physical-access).

## 2. Read on the image

The 70 half-line strips (main checkout `targets/vich1511/half/h57_*.png`, cut from the PARES zoom-10 images) were
viewed at every line where the decode broke sense. Eleven label corrections (`n57_corrections.tsv`, applied by
`research/reading_audit/b16_vich_fix.py` → `n57_transcription_v3.txt`):

- L06: the first group is `oto` (qu), not `o` + `to`, and there is no `o` after `3t`: "segun **quan**
  encarecidamente" (the old decode had "gaugan").
- L04 `plart` → `plort`: "muy princip**al**". L26 `plort` → `plart`: "**mi**reys mucho".
- Six places where the d-sign carries a tilde-like superscript, transcribed `B` or `E`, read **a** (`bh`, a label
  already in the key from the siblings): "sobre c**a**da" (L03), "de **a**hi" (L10), "por vos **a**premiados", "**a**
  cada" (L13), "desauent**a**ia" (L18), "toca **a** hazer" (L28). The d with an 8 above (`B8` b) keeps b in "en**b**iado"
  (L05, L19). This split rests on the superscript's shape at the limit of the PARES resolution and is flagged for
  review in `key.md`.

Seen but not changed: L02 "se que&an" — the sign after `pef` is the `&` (y) shape, but "se [?quexan]" (`&2` x) is what
the sense needs; L22 `sar` (perhaps `sat` uno: "lo [?uno] esta [..] de lo otro"); L07 "retira**v**en" (V with three
or four bars; [?retirassen]); L26-27 `7o` gives "tal ye[ll]o" and L12 "fue e[ll]ado" where the sense is yerro / errado
(7o is ll at 90 other places, so not changed).

## 3. Key changes (whole corpus; `key.md` "b16 additions")

Adopted in `decode.py` after a KWIC over N.45, N.57, N.60 and the deciphered siblings (`b16_vich_kwic.py`): `goe`
aca (11 occurrences; here "vinieron **aca**"), `hoe` governar (3; here "[..] las **governar** los que estan
absentes"), `sid` son (12; here "por la liga **son** obligados"), `fet` fue (15; here "hasta el cabo **fue**
[?errado]"), and `gix`, `goi`, `Vs`, `gid`, `sas`, `ree`, `sue`, `men` from the other letters. `gz` and `ang` are
clause marks. All rest on sense across their occurrences except `gid` amor, which 8714 N.39's decipherment carries.
Proposed but not adopted: `pih` querer (here "[..] las governar": 2 of 3 fit), `sil` todos (here [?Todos]), `sig`,
`phi`, `sar`.

## 4. Building the reading

`n57_build.txt`: each line of the decode written out as words in the figures' spelling (code values joined with the
letters around them: "es crev ia de s" → escreuiades). `n57_reading.md` is generated from it by
`research/reading_audit/b16_vich_make.py` (render; the reading keeps the figures' spelling).

Word-by-word alignment (`research/reading_audit/b16_vich_align.py`, global edit-distance alignment of each build line
with its decode line): 433 unbracketed words, 431 carried at 0.6 or more of their letters; the two below ("lo" L22,
"de" in "d aqui" L25) are in the decode, checked by eye. Eight `[?word]`; 24 `[..]`; supplied words: `[y]` (L10),
`[s]` in su[s] (L04). Two of my own first-draft words were not carried and were rewritten: "con lo que" (L20; the
figures give "que esta lo que") and "teniendola" (L34; the figures give "tenia la").

## 5. Result

`_check_reading.py --file` on the body only (header cut): **0.600** (21 of 35 sentences clean; hole rate 0.117),
against 0.302/0.321 for the raw decodes. Path: first build 0.343; orthography modernised 0.543; with the b16 key
values (aca, governar, son, fue) 0.600. The sentences hold and translate (`n57_en.md`): a reader follows the whole
argument (the viceroy pushed into battle by Vich's letters and the papal threats, the proverb, the orders on the pay,
the Emperor's business and Ferrara). Graded B: it rests on the key alone, with 24 holes.

Sentence: "Y tened por cierto que las cosas de guerra es muy [?peligroso] [..] las governar los que estan ausentes
dellas, que siempre se ha de remitir a los que las tienen presentes." — "And take it for certain that in matters of
war it is very dangerous for those who are absent from them to govern them; they must always be left to those who
have them in front of them."

## Open, with blockers

- 22 unread groups or letter runs (`hno`, `rih`, `poh`, `fap`, `rar`, `mon`, `mug`, `sig` x2, `dup`, `pih`, `phi`
  x2, `sab`, `feg`, `for`, `pub`, `gud`, and the stray "de s" of L08, "g 8" of L20, "pax d" of L04) — no-key-material:
  none occurs in a deciphered sibling and none takes one value at all its occurrences.
- The tilde-d = a split, `&` vs `&2` in L02, `sar`/`sat` in L22 — illegible at the PARES resolution (zoom 10 is the
  maximum served).
- Terrateig 1963 — needs-physical-access.

- Revised 23 Oct 2026 (coordinator): the reading now keeps the figures' 1511 spelling (the modernised pass is withdrawn). Scores of the body: _check_reading 0.371 (13/35), explicit holes only (b17_score.py HOLES=1) 0.800 (28/35). Read sentence by sentence: coherent; kept read.
