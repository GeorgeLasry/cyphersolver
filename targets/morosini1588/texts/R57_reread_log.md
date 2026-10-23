# Re-reading log, R57 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R57_decryption.txt` (character model on DECODE's D1721 under Meister
no. 40): two French papers in Italian translation recognisable, but most lines garbled ("la cita dise tra se burg ho
aempre sia cr fermi li scudi", "et trouai souiene sto sono [FRANZESI]"). Clean-sentence share 0.415.

## 1. Is there a text already?

- DECODE images: 3 cipher pages (524r–525r); no "cleartext" image attached. No glosses.
- The two pieces are translations of French originals (a letter signed Regnault to M. de la Guiche, 10 June 1589, and
  the Moulins oath of 16 June 1589). The French originals were not searched for (not in Tempesti; a printed copy of
  the Moulins oath may exist in Bourbonnais local histories — not checked: possible outside source).

## 2. Word decode and hand re-parse

From `R57_worddecode.txt`; corrections in `R57_corrections.tsv` (49 rows). Main causes:
- **Plain-figure numbers** between null 8s, which the decoder read as letters: 1500 (raitri), 6000 (raitri), 1589
  (twice), probably 16 (June) and "x"/11 (the day); the same device as R28's "8 2 0 0 8" = 200.
- French names the vocabulary lacks: Monbeliard, Langres, Strasburg (decoder "dise tra se burg"), Sanci (Sancy),
  Semur, Digion, Authun, Dezize (Decize), Regnault, Cheseron (Chazeron, governor of the Bourbonnais), Borbones[e],
  escheuini, manenti, lanzquinech, raitri.
- Decoder's wrong splits: "io ho truouato", "corre grande fortuna", "i diti suizeri uengono a Langres", "io credo che
  e' si pasarano", "re legitimo et sourano", "rinuntiato", "sanno segnare".

## 3. Image checks (crops, scratchpad only)

- 524r ll. 18–20: "sola" (4 9 1 5 0 2, DECODE 4 9 2 5 0 2); "6 0 0 0" before raitri clear; the Strasbourg sum
  "2 5 0 0 0 3 5 8 3 0 0 … milia scudi" as transcribed (not resolved into a number).

## Result

Before 0.415 → after 0.574 clean-sentence share (the checker counts the French names and the clerk's spellings as
holes). By hand: 7 unread stretches ([…]) and 9 partly carried words in about 600 words. The oath (524v l. 6 – 525r)
reads throughout; the letter has an unread stretch in its second sentence (524r ll. 9–11, the army's march) and the
Strasbourg sum. Grade B.

## Still open, and why

- 524r ll. 9–11 (the army near Montbéliard/Langres), l. 15, l. 18 (the sum), ll. 21–23 (Semur, the county): no word
  parse; part of the line 2 paper is damaged (DECODE comment). A French original of the Regnault letter would settle
  them (outside material, not located).
- The two dates (dì [?x], [?16] giugno): plain figures vs letters ambiguous.
- Heading (524r l. 1) and the closing line (525r l. 13, corrupt in the transcription).

## 23 Oct 2026, r2d (Claude Opus 5.5)

Regraded on the v2 measure (research/reading_audit/r2d_score.py, body only, every conjecture and unread stretch a hole): see the profile reading_review for the scores; now read. DECODE attachments re-opened (no decipherment). Image checks this pass (crops in the session scratchpad, r2d/morosini/crops): 524r ll. 14-15 ("con [...] dodici pezi"): as transcribed; left open.
