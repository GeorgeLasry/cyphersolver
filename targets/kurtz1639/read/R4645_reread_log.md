# R4645 re-read log (b06, 22 Oct 2026, Claude Opus 5.5)

Starting point: read/R4645.txt, unspaced key decode of the Hamburg letter (P9, P1, P2, P6; 1,236 tokens) plus clear
enclosures (Banér copies P3, P4, P5, P7, P8, read earlier in read/R4645_clear.md); state "decoded, not read".

## 1. Is there a text already?

No gloss, decipherment or clear copy of the cipher on any of the nine images; no edition known (the Kurz letters are
unpublished apart from Mírka's 2012 summary of R3811). The letter is read on the images.

## 2. Read on the image

All cipher lines of P9, P1, P2 and P6 viewed on crops (scratchpad reread/b06/r4645_p*.jpg). The transcription is
good; one label corrected (P2 l. 8 #sect -> φ, "iezundt") and one clear line on P6 re-read
(read/R4645_corrections.tsv). The letter's order is P9 (salutation), P1, P2, [missing leaf], P6 (end, date,
signature, postscript); b06_align.py was given that order.

## 3. Key observations (proposals; key.json not edited)

- **Δ = nu** (key: e): de-nu-ncire, Nuncio, nun x2 here; warnung, hoffnung, continuieren, eigennutz, nur in the other
  letters (kwic over all letters). Printed [nu].
- **#dot = su** (key: null): sufficient x3, subsidia, consummirter, summum periculum, succurs, Suecos, suspiciones,
  verfassung, desuper across the letters.
- #sect stands where the sense needs z three times here ("kurz", "zeig", "zugleich"); printed [?].

## 4. Reading

read/R4645_reading.md, English read/R4645_en.md. Aligner: 0 words not carried. _check_reading.py on the body
(b06_body_score.py): 0.625 (32 sentences, 20 clean, hole rate 0.169). The sentences hold in German and Latin and
translate. Meets the bar: **read** (grade B).

## 5. What stays open

- A leaf between P2 ("quae ergo") and P6 ("Ohsenstern nit abermal ...") is not among the DECODE images. Blocker:
  physical access / not imaged.
- P6 closing lines and the four-line postscript in Kurz's cursive (image blocker, recorded 21 Sept).
- P9 ll. 17-18 Latin run "saepius di zi pen wi o a ut en cau ten quuam"; P2 l. 8 group "?(8742)"; "re ra" before
  noluit; "persua o" (persuasio?). Single occurrences, no other text to test them.

## 6. Second pass (22 Oct 2026, after the key revision)

Key of 22 Oct (Δ = nu, #dot = su, #s-long = ti, 9v = vo) applied by the parent session; Nuncio, nun, denuncire now
carried by the key. No 9 in this letter reads vo (no relabel). "[?war]" written plain (#sect a r: w-a-r carried; the
4? between is an unread stroke); a colon after "futurum" (Penz's report). Re-scored: 0.625 (32 sentences, 20 clean,
hole rate 0.163); aligner 0 flags. Stays **read** (grade B).
