# R7476 reread log (23 Oct 2026, batch r2b)

## Why

The pass-3 reading (9 Oct 2026) of `R7476_reading.txt` was in modernised Polish ("mogą", "ponieważ", "jest",
"Lepiej", "i"), which the reading rules forbid: modern spelling goes only in the English file. It also marked doubtful
words "(?)", which the explicit-hole score did not count as holes (0.651 on 23 Oct).

## What was done

1. `research/reading_audit/r2b_chom_stream.py` parses `R7476.txt` into per-line streams (codes with gloss G and key
   value K, clear words). `research/reading_audit/r2b_chom_restore.py` takes the gloss value of each code (the key
   value where the gloss is unreadable; the pass 5-7 corrections as overrides), folds diacritics and y/j/i, aligns the
   stream letter by letter with the pass-3 reading and re-spells each word from the letters its figures carry. Letters
   of the modern word that no figure carries came out in [brackets]. Draft:
   `C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\r2b\chom_draft.txt`.
2. Every line was then checked by hand against `R7476.txt` (C/G/K) and the pass notes. Clear words are now as
   transcribed ("y", "poniewasz", "lepiey", "nisz", "niey", "zwyczayna", "trochy", "niechcą", "Correspondent",
   "wszytkich", "interessom"); code words as glossed ("ongi", "kihai", "bawio", "chco", "kazdo", "zadno", "mno",
   "z tod", "puki", "bespiecznie", "Polskię", "powracic", "iest", "zemby ostrzo", "Ozowa", "wiazd", "priwatnim",
   "wexlowe", "odpowiedzielem", "poydzie", "posc", "Dewłet Gireia", "Czerkiesimi").
3. Readings changed where the figures give a better word than pass 3 had: p.31 L5 "ongi" (179 170 85 o-n-gi; pass 3
   "onegdy"); p.32 L1 "na swoie panstwo" (294 wo + 105 ie; pass 3 "swe"); p.32 L20-21 "ktoro on" (179 is the o of
   "on"); p.33 L23 "odpowiedzielem" (140 le); p.32 L27 "wozy" is the word code 314 (pass 3 "wozów").
4. Doubtful words are now `[?word]` (pass 3 "(?)"): the reading of each rests on a gloss unreadable at 3-3.5x, a value
   outside the code's alphabetical band, or a gloss whose letters give no certain word (mogą 2x, się 3x, Zatrzymanie,
   żeby, intentare, gdybyć, poznać, czym, komisarzów, prędszego, mając, Stambuł, cię, informacyą, posyła, swoich,
   sollicitacyą, lwowych, ferman, obiecował, dać, asekuracyą, odezwano, jest, zwłoka, tysiąc, i, okręty, fregat,
   audiencyą, Koronnemu, rzeczy, nieszczęści, jego, apostata). Letters the writer did not encipher are bracketed
   (przyi[ą]ł, bedz[i]e, prze[y]scie, trakta[t], m[u] for the slip 156 mo, wiadom[o]sc, s[y]na, dan[o] m[i],
   niewolniko[w], z[p]łondrowała for 151 m, u[po]minaiąc for 104 ia, Iedykuł[y], prowiant[u], taler[ow], zta[d], t[u],
   P[an]u, s[a]mego, P[a]n, pan[a], Wezy[r], krol[e]wskich, Ob[a]czymy, rzec[z]y, t[eg]o, miar[ą], zadane[y], wi[e]m).
   Word codes take the case the sentence needs without brackets (Portae, Stambule, Tatarow).
5. Surplus figures left out of the reading: p.31 L7 61 (e/le after "bedzie", read as a partial [?ze]); p.31 L17 the
   second 170 n of "y n i n"; p.31 L21 284 u (struck by the glosser); p.31 L22 326 z and 85 go (doubled in
   "szwedzkiego"); p.31 L31 270 t after "maiac"; p.32 L6 245 s of "zes" kept as written; p.34 L8 60 e after "nazad";
   p.34 L10 the second 272 ta.

## Score

`python research/reading_audit/v2_score.py targets/chomentowski1713/R7476_reading.txt pl`:

| | plain | explicit holes | hole rate |
|---|---|---|---|
| 23 Oct, pass-3 modern spelling, "(?)" not counted | 0.143 | 0.651 (41/63) | 0.104 |
| 23 Oct, writer's spelling, doubtful and supplied marked | 0.079 | 0.524 (33/63) | 0.143 |

The plain score is meaningless here (modern Polish word list against 1714 spelling). On the explicit-hole measure the
reading falls below the 0.60 bar once its doubtful words count as holes: 30 of 63 sentence windows carry two or more
holes, mostly on p.31 L19-L34 and p.32 L9-L36, the stretches the 9 Oct passes already worked at 2.5-3.5x.

## Decision

Kept as a partial reading; the document is set to `decoded, not read`. Not workable within this pass: the residue is
the one passes 4-7 already took to the image digit by digit and gloss by gloss (34 + crops, `sien/R7476_pass5.txt`),
and the DECODE images are not on disk in either checkout (they were cropped in the sieniawski1708 session and not
kept). Gap blocker: illegible - the [?word]s sit under glosses that were unreadable at 3-3.5x on the DECODE
JPEGs (82, 249, 315 and the unbanded codes) or give letters that form no certain word; only a better image of the faint
brown glosses (a new photograph or the original in Kraków) could settle them.

## Not done here

`R7484_reading.txt` and `R7485_reading.txt` are also headed "modernised Polish" and need the same restoration.
