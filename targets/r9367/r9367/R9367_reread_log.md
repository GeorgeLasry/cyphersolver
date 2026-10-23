# Re-reading log, R9367 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b32)

## Starting point

Reading audit (22 Oct): "decoded, not read". `reading.txt` gave the clear German roughly and the cipher runs as
letter strings with `_`, `?` and `[#]` mid-word; only a few phrases assembled. No reading file; clean-sentence share
before: no reading (0.00).

## What was done

1. **The DECODE record.** R9367 fetched logged in (research/reading_audit/b28_fetch.py): two images, no attachment,
   no transcription, no comment ("Partly encrypted cipher"). P2, never looked at before, is the back of the leaf:
   blank except two pen crosses with small rings at the ends (like the cross in the left margin of P1); no address,
   so it does not name the father. Neighbours: R9366 (ff. 167-168) is a key ("D. Multmeri" / Aurelio Augurelio),
   R9368 (ff. 170-171) a letter in another cipher addressed to Aurelio Augurelio; neither is a decipherment of f. 169.
   No print or scholar's text is known (kaa4591 notes: web search found no edition of the KAA 4591 ciphers).
2. **Image.** P1 (4624 x 3468) is the page turned 90 deg; rotated (lines horizontal) and cut into full-resolution
   tiles (research/reading_audit/b32_band.py and inline crops; scratchpad only, the image is not public domain).
   Every cipher run and the clear German re-read line by line.
3. **Transcription.** `transcription_v2.txt` (cipher runs only), changes in `R9367_corrections.tsv`. The main
   corrections: the barred-cross pair ‡‡ (X) and the 'cc' pair (K) told apart; the boxed-H (H) told apart from the
   boxed dot; a 7-/ʑ-shaped sign (new label S) where the old file had z/4; the circle with a bar (O) apart from the
   circle with a dot (new label d, once); the second m-sign in L16; π (Z) at the start of L32.
4. **Key.** Register block 2_4 values kept (A 9 not used; B v, C Δ, D +, E 6, H 4, I w, K ‡ (not seen), L 8, M ¥ =
   our V, N 3, S y, T ♉ = our e, Z π, ch ε-like = our E); with these the clear-shaped words come out. Values adopted
   because they hold at every occurrence (evidence = the words they give):
   - v = b and w (one sign, as in the register's B): aber, hab, bei, geben, schreiber, firgeben / swer, firwar,
     worden, wol, wais. Not a look-alike: one shape, two sounds, the Bavarian b/w spelling.
   - X (‡‡) = u/v: guet, verkhuntschaft, und, hindurch, vergunt, euch, uerauf (7 words).
   - K ('cc') = z: zeit, ziechen, Schmalcz, selczam, herczen (5). **Sense-only** (not in the register): flag for review.
   - O (Φ) = b: bin, bringen, botschaft, bring (4). **Sense-only**: flag for review.
   - S = sch: verkhuntschaft, botschaft, Schmalcz (3). Probably the register's "sch" sign (a hooked C); **sense-only**
     as read here: flag for review.
   - U = ll: alles (1; register "ll" has its own sign, drawn differently). **Sense-only, once**: flag for review.
   - H (boxed H) = k: verkhuntschaft, kan, Tircken, khan (4). Kept from 21 Sept (the letter's own value).
   - q = a, A (Λ) = r, e = t, C = s, u = o, J = f/v, E = ch: kept from 21 Sept, every occurrence checked.
   - Nulls ♀ (Q), ≈ (W), ⊡ (D): kept; in every run they fall inside or between words without a letter needed.
   - Not identified: # (triple-barred cross, 13x: most occurrences stand where the sentence needs nothing, e.g.
     "nit [#] fir guet ansechen", "es [#] sein euch wol 10", "hercze[#]n", but that is sense, not proof, so it stays
     [#]); P (Π, 4x: "gegen s [Π] verkhuntschaft", "[Π] erfodert mich", "wie er [Π] die botschaft bring", "bei [Π]":
     a word or name sign, probably a person); R (once); d (once); the g-sign in L17.
5. **Word-by-word alignment.** `research/reading_audit/b32_r9367_dec.py` decodes transcription_v2.txt; each cipher
   word of the reading was checked against it. Differences are the b/w reading of v (printed as the sense needs, see
   above), and the words given as holes. Corrections made at this step: "alles [g] verlaugnet" (the g-sign is
   there), "[?uerauf]" (figures u-e-r-a-u-f; the first sign is re-inked, "herauf" not proved), "vernufft" as written.
6. **Look-alike alternates.** Letters resting on the other member of a look-alike pair rather than the shape read:
   ‡‡/cc at L17 "selczam" (the pair is faint) and L37 (re-inked X): about 2 letters of some 470 cipher letters
   (under 1%).
7. **Score** (research/reading_audit/b17_score.py, LANG_=de, reading body, with [#], [Π], [R], [g] counted as holes):
   **0.256 (10/39)** plain (the word list is modern German and cannot know 1535 Bavarian spelling: khumen, gescheft,
   zethuen, firgeben ...); explicit holes only (HOLES=1) **0.641 (25/39)**. Reader's judgement: the letter reads through.
   The cipher passages that hold: the son was questioned about strange arts and denied everything, claimed to be a
   poor writer sent to learn because he is young; has not yet learnt anything thorough until he reaches the place;
   will bring his body through; someone asked how "he" brings [Π] the message; many Turks moving up; postscript:
   Friedrich Schmalcz begrudges the father nothing good; "he can and may". Passages that hold only in part: L09-L10,
   L14, L16 (who summoned him), L31, L34.

## Result

Read (grade B): 0.641 on explicit holes, sentences hold except in five cipher passages; the codes [#] (13x) and [Π]
(4x) and five sense-only values are flagged for review.

## Open

- [#], [Π], [R], d, the g-sign - blocker: no-key-material (not in register block 2_4; contexts do not fix them).
- L01-L02 (the place where the letter was written, 'ckiuibt[#]te / sbarde[#]inl') - blocker: no-key-material (a
  name, unread with these values).
- The right-margin pairs beside L30-L33 ("7 ʒ", "ʒ ǂ°", "ↄ q+"), probably a reader's sign equations - not-attempted.
