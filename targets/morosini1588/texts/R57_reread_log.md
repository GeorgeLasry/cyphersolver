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

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

The rest of R57 (after r2d's 524r ll. 14-15): each hole located (`research/reading_audit/r2p_holes.py`), its line
looked at on the image (scratchpad `reread/r2p/crops`; the pages are clean), cancellation strokes looked for (none),
the figures parsed (`r2p_parseall.py`).
Filled:
- 524v l. 7 "d'hogi 16 giugno": "26 7 26 14 91 40 17 | 8 1 6 | 40 17 37 ...": the day in plain figures after a null 8.
- 524v l. 14 "nel Borbonese": "42 91 00 42 91 01 35 45 35 8", every letter carried.
- 525r l. 3 "ubidire": "3 42 17 26 17 00 5", as the figures spell it (was "[?obedire]").
Left, with blockers ("[?6000] raitri", 524r l. 19: "6 0 0 0" stands clear on the image but with no null 8 to mark it as
a number, so it stays partly carried; the same Borbones[e] on 525r l. 12 has an extra figure, "45 1 35"):
- 524r l. 1 "Ill ma […] tradutione dela": "5 9 8". Blocker: too-short.
- 524r l. 2 "Guicha Mio [s] ignore quando": "(none)". Blocker: nothing written there; no-key-material.
- 524r l. 2 "un huomo [?espreso] per inuiarui": "5 4 6 3 5 4 5 9" (best parse "steso"). Blocker: no-key-material.
- 524r l. 9 "di suizeri [?…] a quatro": "8". Blocker: no-key-material.
- 524r l. 9 "da Monbeliard [?…] hora che": "8 2 5". Blocker: no-key-material.
- 524r l. 10 "hora che […] lasciati […]": "1 7 1 9 5 0 7" (best parse "ioep"). Blocker: no-key-material.
- 524r l. 10 "[…] lasciati […] sarano a": "6 9". Blocker: too-short.
- 524r l. 10 "a Langres […] di questo": "8 2 5 0 1 7 1 1 5 8" (best parse "lit"). Blocker: no-key-material.
- 524r l. 18 "di Strasburg h[a] sola presta[to]": "1 4 8". Blocker: too-short.
- 524r l. 18 "h[a] sola presta[to] […] milia": "3 3 3 5 4 7 2 1 2 2 5 0 0 0 3 5 8 3 0 0" (best parse "uuestaalrer"). Blocker: no-key-material.
- 524r l. 19 "ha pagato [?6000] raitri et": "6 0 0 0" (best parse "kr"). Blocker: no-key-material.
- 524r l. 21 "sig Cesare [?a] Semur et": "8 2 3 2 1 2" (best parse "fra"). Blocker: no-key-material.
- 524r l. 22 "et nela [?…] [col] quale": "7 1 7 4 0 1 0 1 7 8 2 5 0" (best parse "iignial"). Blocker: no-key-material.
- 524r l. 23 "contea perché […] si fa": "4 1 5 3 5 0 7 7 1 7 1 7 1" (best parse "seepiii"). Blocker: no-key-material.
- 524r l. 24 "dela lega [che] corre grande": "(none)". Blocker: nothing written there; no-key-material.
- 524v l. 2 "pasarano a [?le] porte di": "0 5". Blocker: no-key-material.
- 524v l. 4 "Questo dì [?x] di giugno": "1 1 8". Blocker: no-key-material.
- 524v l. 5-6 "seruitore Regnault […] tradutione del": "8 4 9 7 7 0 | 0 0 1 1 9 5 7 2 2 111^. 8" (best parse "oipnnconeicr[il"). Blocker: no-key-material.
- 524v l. 10-11 "et luogotenente [?generale] per S": "4 0 3 5 0 1 3 5 0 0 4 | 5 0 5" (best parse "genersene"). Blocker: no-key-material.
- 524v l. 13 "uila et [fa] uborghi di": "8 3 9". Blocker: too-short.
- 524v l. 19 "tà nel [?gouernamento] del deto": "4 0 9 1 3 7 3 5 0 0 1 0 2 1 2 0 3 5 0 3 5 1 9" (best parse "gouernarmenecon"). Blocker: no-key-material.
- 525r l. 1 "humilisimi seruitori [et] di esa": "(none)". Blocker: nothing written there; no-key-material.
- 525r l. 12 "signoria di Borbones[e] nel fine": "4 2 9 1 0 0 4 2 9 1 0 1 3 5 4 5 1 3 5 8" (best parse "borboneste"). Blocker: no-key-material.
- 525r l. 13 "dele presenti […]": "8 4 9 2 7 5 9 1 1 2 2 166^." (best parse "olteoraa[questo]"). Blocker: no-key-material.
Result: 3 holes filled; R57 is now checked on the image throughout; 24 left, each with its blocker.
