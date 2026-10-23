# Nicholas Throckmorton to Elizabeth I, Paris, 10 July 1559, in his Cipher 1: BL Add MS 4136 f. 32 (DECODE R2988)

Status: in progress. not read (reading audit, 22 Oct 2026: decoded, not read). Was: read in part (21 Sept 2026): the 10 July 1559 letter ~85-90% with Tomokiyo's Cipher 1 key and seven corrections. Write-up docs/throck1559.html.

**23 Oct 2026, re-read (REREAD_BRIEF batch b36, Claude Opus 5.5): still decoded, not read, but the letter now builds into sentences.** Tomokiyo's key image lists code signs the September passes never used (*as* G/б, *have* б̄, *had* r̄, *whom* ṭ, *upon* ḟ, *so* g̲, *this* б̲, *your Majesty* ξ, which is also the old "null" ζ). Lines 5-15 re-transcribed sign by sign at measured line centres (`texts/R2988_signs.tsv`, decoder `research/reading_audit/b36_throck.py`): "...as I wish your Majesty to have knowledge of, considering the present [?time], have I iudged it best to dispatche this gentelman ... to whom it may [?please] your Majesty to giue credit. He [?hath] since [?his] coming on [?this] side done your Majesty diuerse and sundry wais so [?good] and [?painfull] seruice, as he [?hath] deserud to be well considered and rewarded ..." Partial reading `texts/R2988_reading.md` (English `_en.md`, log `_reread_log.md`): b17 0.35 plain, 0.60 explicit holes. Kept decoded, not read because 30 of 496 letters (6%) rest on look-alike choices (ρ t/d, 7 r/g, μ h/b, x i/y, ⊥/┘ o/a) and no text of the letter exists to confirm them. Neighbours R2986, R2987 (9 July) and R2990 (13 July) are sibling letters in the same cipher, not copies; Forbes I prints the 13 July letters (pp. 157-160): the next step.

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): **decoded, not read**.
The opening sentence (lines 1-5, the despatches by Gray and Carew) reads; from line 6 the running reading has `[...]`
holes every few words, so the letter cannot be built into sentences. Class now not read, method not solved; the
85-90% below is the share of signs given a value, withdrawn as a reading figure.

Split on 14 Oct 2026 from `wod1568` under the one-key rule (George Lasry, 14 Oct 2026): one entry per key. The old entry
(catalogue 97) joined three systems on the leaves Add MS 4136 ff. 32–33. This folder keeps **Throckmorton's own letter
in his Cipher 1**. The marginal word-sign code on the same leaf is a different cipher, with its own page
([`targets/throck1559margin/`](../throck1559margin/), docs/throck1559margin.html), and so is John Wood's 1568 line on
f. 33 ([`targets/wod1568/`](../wod1568/), docs/wod1568.html). The images (`img/`, git-ignored) stay in the main
checkout `targets/wod1568/img/` (`IMG_R2988_I20714_P.jpg`, Tomokiyo's key attachment `DOC_2988_*.png`).

R2988 = f. 32 (old 9), Throckmorton's holograph letter to the Queen, Paris, 10 July 1559, signed, 16 lines of cipher.
The Throckmorton cipher text on the leaves is identified by Tomokiyo as his Cipher 1 (key image attached to the DECODE
record; see also `../throckmorton/`), but the text of this letter is unpublished (not in Forbes or CSP Foreign;
Tomokiyo only says the key deciphers it).

## Session 1 (2026-09-21)

- A first pass is in `main_decrypt.txt`, lines 1-5 only, low-medium confidence: "...[it may] please <Queen's
  majesty> to <be> advertised that whereas I sent ... of the eight of <this> <moneth> at five of the clock in
  the afternoon ... of the same date written at midnight touching <French King>'s state ... I judge <Queen's
  majesty> [will] be desirous to be further informed thereof ... convenient to put in writing the [whole?]
  discourse of ...". Lines 6-15 were sign transcriptions only, line 16 not transcribed.
- The starred insertion in the main text is on line 13, after "z ⊥ k v 5 1 H x 3". The left-margin `*` note
  keys to it; the note itself is written in the margin word code (throck1559margin).

**Main letter (Cipher 1), read.** Re-cut at the measured line centres (y = 812, 910, …, 2220), the whole block
decrypts with Tomokiyo's key after these corrections: x and υ = i; y = f/h; z = m; ρ = d/t; ∫t = w; Q = *be*;
ξ = *your Majesty*; a dot over a sign marks a code word. Lines 1-4 are secure (see `main_decrypt.txt`, pass 2).
Lines 5-15 decode to continuous English with the same key: "…convenient to put in writing the whole discourse
of … the present … state … the French King … service well considered … graciously … perceive … experience …
shall be able to declare more plainly and particularly when it shall please the same to command … preserve
your Majesty's health … wealth … at Paris the tenth of July". This is an unpublished letter (not in Forbes;
CSP Foreign vol. 1 pp. 362-369 has only the 8 July despatches).

**10 July letter, pass 3 (`main_decrypt.txt`).** Lines 1-4 are secure; lines 5-15 read at ~85% (≈470 of 550
signs). Content: Throckmorton sends a gentleman (the bearer) to report the French King's state by word of
mouth. He asks the Queen to give him credit, praises his "diverse and sundry" service since coming over and
asks that it be rewarded, then signs off "…to preserve your Majesty in health, wealth and all felicity. At Paris
the tenth of Julii". Key additions: flat-topped 6 = w; ζ = null inside words; q̇ = your Majesty; K = all(?).
Twelve code signs are still open (1k̲ ρ̲ g̲ δ̄ δ̲ ō ⊓̄ q̄ r̄ π̄ ƒ̇ ʋ̲).

The letter mentions Throckmorton's two despatches of the 8th (by Gray, and at midnight by Carew): CSP For. i nos.
947 and 950. The bearer is not named in the decrypted part.

## Files

`main_decrypt.txt` (sign transcription and passes 1-3) · `rec2988.htm` (DECODE record page, shared with
throck1559margin) · `../../decode_updates/decryptions/R2988.txt` (public reading).

## Log

- 2026-09-21: three passes over the letter (subagent, re-cut crops, full re-transcription).
- 2026-10-14: split from `wod1568`; `main_decrypt.txt` and `rec2988.htm` moved here.

## Remaining gaps

- 10 July letter, 30 of 496 letters of lines 5-15 rest on look-alike choices (6%, above 3%) - blocker: not-attempted; test on the sibling letters R2986/R2987 (9 July) and R2990 (13 July) against Forbes I pp. 157-160 whether ρ serves for both d and t (a key homophone, not a look-alike) and confirm q̄ hath, ō good, ġ letters
- 10 July letter, code signs 1̲ k̲ (l. 6), ť (l. 5), r̲ (l. 8), v̲ (l. 14), ℓ̄ (l. 15) and the groups `i б υ` (l. 4), `L T 8` (l. 2) - blocker: no-key-material; not in Tomokiyo's key list (r̲ is *then* there and does not fit), one context each
- 10 July letter, the starred note keyed to line 13 - blocker: no-key-material; it is in the margin word code (throck1559margin, a different system, no key)
- closed 23 Oct 2026 (b36): lines 6-15 decoded, not read (holes every few words) - re-transcribed and decoded with the key's code list, now a partial reading in sentences; the "illegible" spans were crop overlaps, re-cut at measured line centres; five of the twelve old open codes are in the key (б̄ have, r̄ had, g̲ so, ξ your Majesty, ḟ upon), q̄ and ō read from sense

## Escalation

- [x] siblings: Add MS 4136 key leaves ff. 173-185 (R9258-R9262) and the twenty targets/throckmorton/ records checked; the twelve code signs are not on any of them
- [x] clear-pages: no decipherment on the leaf; Forbes has no copy of this letter
- [x] known-keys: Tomokiyo's Cipher 1 (fits, seven corrections); Ciphers 2-3, Smith 1563 and Cecil-Norris give nothing for the code signs
- [x] print: Forbes I, CSP Foreign I (BHO) checked: only the 8 July despatches
- [x] key-rebuild: Cipher 1 corrected (seven values) and extended in pass 3 (6 = w, ζ = null, q̇ = your Majesty, K = all?)
- [x] retry: three passes over the 10 July letter (subagent, re-cut crops, full re-transcription); fourth pass 23 Oct 2026 (b36) with the key's code list, partial reading in sentences
