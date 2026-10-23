# Re-reading log, R9416 f. 263 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch r2h)

## Starting point

The f. 263 entry counted only recto lines 11-16 (`reading_p3_11-16.txt`, 30 Sept); the rest was the annealer's working
decrypt (`decrypt_f263.txt`) and the escalation step "retry" (re-key the rest by hand) was open. The request for this
batch was to decode f. 263 with the f. 262 key rebuilt from that leaf's contemporary decipherment.

## What was done

1. **DECODE record.** R9416 carries four images and no attachment or comment (b32 fetch, 22-23 Oct). P3/P4 are
   3468 x 4624 px, the full DECODE resolution (byte-identical to `targets/kaa4591/img/` in the main checkout). Copied to
   the scratchpad, turned 180 deg, cut into one crop per cipher line (three overlapping thirds, recto skew
   compensated), and zoomed crops where a sign or the gloss was doubtful.
2. **The f. 262 key does not apply.** Set side by side, the two leaves use different sign sets (f. 262: figure-eight g,
   ♀ and 9 for e, triangle d, 6-shapes for r/m; f. 263: open square n, two-barred daggers, `io`, triangle f). The NOTES
   already said "two sign sets of their own"; checked on the images, confirmed. f. 263 was decoded with its own hand key
   (`f263_key.md`, the 30 Sept key extended).
3. **Interlinear decipherment on f. 263 too.** A faint contemporary gloss stands over recto lines 1-12 (not just the
   first two) and over the last lines of the verso ("tu mich", "gehorsamer un(der)"). Transcribed as far as legible:
   `f263_gloss.txt`. It names three codes: "fg" over the hourglass X (= E. F. G.), "Khö" over the barred T (a king),
   "Ferd" over g. Recto 13-39 and verso 1-40 have no gloss.
4. **Reading, line by line** (`f263_reading.md`), every line checked on its crop against the decode of the v2 labels
   (`research/reading_audit/r2h_dec263.py`). New from the figures:
   - K serves both k and b: "bracht" r18, "bei" r23 and **"Bresburg" r22, r24, v36** (the old "kreekurg/Krakau" was a
     misreading of this look-alike: the agreed diet was at Pressburg).
   - θ (v2 `e`) = d/t ("der" v02, "getan" v09); Y = ll ("wollen", "aller"); final hook 7 = s ("solchs", gloss).
   - "mit vij scheffe" r17 (the Turkish embassy came with seven ships; Bavarian "Scheff"), "copei" r19, "verwilligten
     tag" r22, "schon bei im selber ... entschlussen" r26-27, "Emrich Besche" r28/r32 (written with the two-bar s, not
     "beeche"), "widisch lannt, welches doch nit sein ist" r31, "schanckung" r33, "grosmutig" r36.
   - Verso: Gritti dispatched with the Turkish embassy sent ahead "auf der post"; the writer, always called to the
     King's negotiations, asked in the presence of [Ω] that both dukes be included in the treaty; an article reserving
     the King's allies was put in [Ω]'s instruction; the commissioners recalled from Pressburg; **"datm ofen den 12
     marcij"** (Datum Ofen = Buda, "12 marcij" in clear): the report was written at Buda, 12 March (1533 or 1534).
5. **Retry of the unread groups** with the extended key: r08-r09 (gloss half legible; "erbern", "wisen", "[…]hen"
   stay doubtful), the dotted-circle clusters on r12/r21/r34 (passed over by the gloss; perhaps nulls or an
   abbreviation; unread), the codes +L (6 times, always beside Ferd.: probably the Emperor) and Ω (7 times, a lord with
   an instruction), v10-v11 "nit zu […]nem nachtail", v27-v28 and v38-v40 (letters run together, values not settled).
   These stay holes.
6. **Word-by-word alignment** of the reading with the decode (`research/reading_audit/r2h_lookalike263.py`): every
   word differing from the decode is either a value of a multi-valued code chosen by the word, or bracketed.
7. **Score** (`v2_score.py`, de, body only): **plain 0.465 (33/71), explicit holes 0.775 (55/71)**, hole rate 0.099,
   670 words. Before: no reading outside r11-r16 (the 30 Sept excerpt).
8. **Look-alike letters.** 2,738 letters; 117 (4.2%) rest on the second value of a multi-valued sign chosen by the word:
   z e/s 43 and dagger o/s 8, b d/l 35, p b/w 21, K k/b 3, o/e 6 (counted against the v2 labels). Of these 9 stand in
   gloss-covered lines; **108 (3.9%) are not confirmed by any contemporary text.** Spot checks on the image do not
   separate the e and s daggers consistently (the s of "ist"/"des" on r19 has the two-bar form of the e of "nemen" r02;
   the s of "kaiser" r16 a curled one-bar form), and b is one shape for d and l ("den" r01, "latein" r18).

## Result

Not read: above the 3% look-alike limit with no contemporary text over r13-v40, so f. 263 stays **decoded, not read**,
with this partial reading kept (0.775 explicit-hole share; the sentences hold from r10 to v26 and v29-v37). The reading
and the dating (Buda, 12 March) are new.

## Open

- r13-v40 letters chosen by sense on the d/l, e/s, b/w, k/b signs (3.9%) - blocker: no-key-material (no contemporary
  decipherment or print over these lines).
- Codes +L and Ω, the dotted-circle cluster - blocker: no-key-material.
- r08-r09, v27-v28, v38-v40 groups - blocker: no-key-material (gloss illegible or absent; values tried).
