# R3811 re-read log (b06, 22 Oct 2026, Claude Opus 5.5)

Starting point: read/R3811.txt, unspaced key decode (38 = d applied by the parent session the same day); state
"decoded, not read".

## 1. Is there a text already?

- Contemporary interlinear decipherment on I23099 (p. 1, every cipher line) and on the first eleven lines of I23100
  left. Re-read on 2x crops of the DECODE images and transcribed: read/R3811_interlinear.md. The first transcription
  (19 Sept) had attached the glosses one or two figures off; re-attached. The glosses agree with the key decode
  throughout and settle eight labels (corrections.tsv).
- Mírka 2012 (Západočeské archivy 2012, 44-72; Crypto-World 11-12/2012) rebuilt the key from the same glosses and
  summarised this letter in Czech; no plaintext printed. Used as a content check only (lit/ not consulted again; the
  summary in NOTES.md agrees: Polish king, supply, Saxe-Lauenburg and Denmark, Arnim's defence).
- I23102/I23103 carry a separate clear "Extract Schreibens aus Hamburg vom 18 January 1639", not this letter.
- I23104 right: the closing lines of this letter (clear) and a postscript in Kurz's cursive (not transcribed).

## 2. Read on the image

Every cipher line of I23099, I23100, I23101 and I23104 checked on crops (scratchpad reread/b06/r3811_*.jpg). 21 label
or clear-text corrections (read/R3811_corrections.tsv); decode.py R3811 re-run after each batch. The margin addition
on I23101 moved to its #ins mark so the decode runs in reading order.

## 3. Key observations (proposals, key.json not edited)

- **#s-long = ti**, not t, in this letter (15 occurrences: quartir, recrutiren, competiren, committirt, legation,
  dehortiren, ratione, protection, instruction, resolution, optima, amnistia, petiit, stil, Holsatiae); the
  interlinear glosses it ti three times. The other forks read #s-long as t in R3812/R3813/R3815 ("dienst"), so either
  two signs are merged under #s-long or the sign is ti and t-readings elsewhere are slips; needs a sign-by-sign check.
- **#dot = su** four times (suspiciones, verfassung, regia Suecis, desuper); the key treats #dot as a null.
- **x = to** three times (protectorium, Stockholmb, Electore); elsewhere x = i (bei, Kai.).
- **9 31 = von** three times (herzog von Holstein, von hinnen, Augustus von Sachsen with 93 #z): a vo sign merged with 9.
- **1 = su** once (subsidia, glossed); **#hook = vi** once (virium, glossed).
- #s-cross = ta (calamitates, ita).

## 4. Reading

read/R3811_reading.md, English read/R3811_en.md. Aligner (b06_align.py): 4 flags, all explained in the Notes (stil and
Holsatiae carried only under #s-long = ti; subsidia by the gloss; "so" a two-letter alignment artefact).
_check_reading.py on the body (b06_body_score.py): 0.449 first draft, 0.512 after filling clear-text gaps and printing
the ti words (80 sentences, 41 clean, hole rate 0.175). Below the 0.60 bar: stays **decoded, not read**.

## 5. What stays open and why

- About 20 gaps in the clear Kurrent text that the first transcription left as "..." and this pass could not read
  with confidence at DECODE resolution ("doppelter [...] ist der [...]", "wenig [...] könig erlebte", "[...] solle
  [...] ad constantiam Regis", "Mit allem ware [...] herrn"...). Blocker: labour plus a reader of 17th-century Kurrent;
  the images are legible enough for a palaeographer.
- Cipher holes: "939 44 40 38 99 19 28 6 74 95 969" before "-reich" (Haus [Öster]reich?), "zum fall 9 α tradiment",
  "59 31 9 w" after "weil und", "40 45 #dot 26" (putat?), "Δ 28 #sect" (wolle), "9 π" before Reichsboden. Blocker: the
  sign values (proposals above) need checking across all letters before they can be applied.
- Many unclean sentences fail on period spellings, names and Latin the checker's word list does not know (Volckh,
  Crais, widerstant, Fridlant, plenipotenz, defenditur) rather than on holes.
- Postscript on I23104 right in Kurz's cursive: not transcribed.

## 6. Second pass (22 Oct 2026, after the key revision)

Key of 22 Oct (38 = d, Δ = nu, #dot = su, #s-long = ti, 9v = vo) applied by the parent session, which also re-read
much clear text (logged in the corrections file). This pass: six figures relabelled 9 -> 9v (von, bevorab, Augustus
von Sachsen, von hinnen, protectorium von Kai. Mai., herzog von Holstein; one had been transcribed ψ but is a plain 9
on the image), 87 -> 81 ("dolere se"), and seven clear lines re-read on the images ("stehet zu erwartten", "als wan
er vom", "Mit allem ware seines herren", "machts dergleichen sich einzubilden", "Wir habe ihm mehr ... zum fenster
hinein gesehen", "für am besten in", "Wohl angelegt"). English updated. Score 0.658 (79 sentences, 52 clean, hole
rate 0.14); aligner 7 flags, all explained in the Notes (gloss-carried ex, virium, ist, subsidia; protectorium x2 and
Stockholmb need x = to). Meets the bar: **read** (grade B, rests on the interlinear for p. 1 and the key decode).

Still open: "Doppelter [...] ist der[...]", "[...] ob darunter", the word after "bey vergangenem", "Darumb solle
[...]", "bey [...] Kays. Mtt." (Kurrent this pass could not read with confidence), "zum fall [9 α] tradiment" and
"[...] werde" before "machts", "[?Stecknitz] [?stelle]", "verfassung [?ettlis]", the postscript in Kurz's cursive.

## r2c (23 Oct 2026, Claude Opus 5.5)

Key k = to and m = va after the check against Mírka's key on DECODE R3813/R3814 (KEY.md). Three x labels are the looped k-form (to) on the images: I23101 r. l.8 and l.22 (protectorium, twice) and I23104 l. l.6 (Stockholmb); relabelled k (R3811_corrections.tsv); the three words unbracketed in the reading. Readings of R3812, R3815 and R4736 brought in line with k = to (contento, a proposito, acceptos, puncto, bis dato, protectorium, fundamento, sadisfatto, armatos).
