# Re-reading log, R2988 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b36)

## Starting point

Reading audit (22 Oct): "decoded, not read". Lines 1-4 read as a sentence; lines 5-15 were a running decode with `[...]`
every few words (`../main_decrypt.txt` pass 3, `decode_updates/decryptions/R2988.txt`); twelve code signs open. No
reading file: before = 0.00 on the reading body (the running text has holes in every sentence after line 5).

## 1. Is there a text already?

- `research/reading_audit/b36_fetch.py` fetched DECODE R2988 logged in: one image (`IMG_R2988_I20714_P.jpg`, 3269 x 4205)
  and Tomokiyo's Cipher 1 key image (`DOC_2988_*.png`, 589 x 379); no transcription, plaintext or comment block. The
  image has no interlinear or marginal decipherment of the letter (the margin note and the lines under the signature
  are the separate word code, throck1559margin).
- The holding volume and print were checked in September (NOTES Escalation): Add MS 4136 key leaves ff. 173-185, Forbes,
  CSP Foreign i (only the 8 July despatches). Forbes I (main checkout `targets/throckmorton/sources/forbes1.txt`)
  re-checked for 10 July 1559: only the Queen's letter to Throckmorton of that day (p. 156). Neighbouring DECODE
  records fetched and opened: R2986 (f. 30, Throckmorton to Cecil, Paris, 9 July 1559), R2987 (f. 31, to the Lords of
  the Council, 9 July 1559), R2990 (ff. 34-35, to Cecil, 13 July 1559), each in the same Cipher 1 with Tomokiyo's key
  attached, none with a decipherment of f. 32; R2989 is the 1568 Wood line. No text of this letter exists.

## 2. On the image

- **The key image was read in full for the first time.** Besides the alphabet it lists code signs that the September
  passes had not used: *are* F, *as* G, *all* K, *at* O, *be* Q, *before* S, *could* W; dotted *in*, *long*, *one*,
  *moneth*, *others*, *peace*, *upon* ḟ, *whom* ṭ, *war*, *hundred*; barred *both* ꝗ̄, *do*, *did*, *ever*, *for*,
  *great*, *have* б̄, *had* r̄, *here* f̄, *his* v̄, *hence*, *is*; underlined *sea*, *ships*, *so* g̲, *this* б̲, *these*,
  *their*, *those*, *then* r̲, *time* e̲; names (Queen Dolphin A, ambassador E, French King B., King Dolphin, Cardinal of
  Lorrain, Constable, Duke of Guise, France, England, Scotland, *Queen's majesty* ξ, Pope б, Earl of Arran).
- Line centres measured by projection (y = 813 ... 2221; 15 lines, the "line 16" of September does not exist); every
  line of 5-15 cropped in thirds at 2-3x and re-transcribed sign by sign: `R2988_signs.tsv` (look-alike choices marked
  `label:value`, codes in braces). Decoder: `research/reading_audit/b36_throck.py`.
- Results: ζ and ξ are both *your Majesty* (the old "null ζ" falls in "done your Majesty diverse", "beseching your
  Majesty"); G/б before a clause is the code *as* ("as I wish", "as he hath deserved", "as he may perceive", "as I
  shal be able"); б̄ *have* ("to have knowledge", "have I iudged", "I have had"); r̄ *had*; ṭ *whom*; ḟ *upon*; g̲ *so*;
  the "3" before "to have knowledge" is ξ; line 9 ends *so good and painfull*, not "[g̲ ō] and l-a-i-n-f-u-l-l".
- Values adopted from sense (logged, flagged in the reading): q̄ *hath* at all three occurrences (Tomokiyo *both* fits
  none); ō *good* at all four; ġ *letters* at both; π̄ *God*, ῡ *his*, ϱ̲ *time*, V *I* (one context each).

## 3. Alignment and look-alikes

Word-by-word alignment of `R2988_reading.md` with the decoder output: every unbracketed word is spelled by the figures
or is a key code; sense-only codes and words with an unmatched sign are `[?word]`; no supplied words. **Look-alike
letters: 30 of 496 letters of lines 5-15 (0.060)** rest on the other member of a look-alike pair (ρ/℘ t/d nine times,
x/X i/y three, 7/¬ r/g two, μ/M h/b two, ⊥/┘ o/a three, and single ones), above the brief's ~3%. No contemporary or
printed text exists to confirm them.

## 4. Score

| | before | after |
|---|---|---|
| reading body, b17 plain (LANG_=en) | no reading (0.00) | 0.35 (7/20) |
| reading body, b17 HOLES=1 (English 1559) | - | 0.60 (12/20) |

Reader's judgement: the letter now builds into sentences (the bearer's errand, the request for credit, the praise of
his service, the close), with holes in the clause after "thereof" and in the codes listed below.

## Result

Kept **decoded, not read** (look-alike share 6%, above 3%, with no confirming text; explicit-hole share at the 0.60 bar).
The partial reading replaces the running decode.

## Open

- Codes 1̲ k̲ (the subject of "the hoole discours of"), ť, r̲ (the key's *then* does not fit), v̲, ℓ̄, `i б υ` (end of l.
  4) and `L T 8` (l. 2): no-key-material (not in Tomokiyo's key list, one context each).
- The 30 look-alike letters: no text of this letter can confirm them. Not yet tried (blocker not-attempted): the
  sibling letters in the same cipher, R2986/R2987 (9 July) and R2990 (13 July), against Forbes I's prints of the
  13 July letters (pp. 157-160), would show whether the writer's ρ serves for both d and t (then a homophone of the
  key, not a look-alike choice, which would bring the share under 3%) and would test q̄ *hath*, ō *good*, ġ
  *letters*.
