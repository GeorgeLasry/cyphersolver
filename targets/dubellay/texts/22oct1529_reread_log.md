# Re-reading log, dubellay 22 Oct 1529 opening (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b26)

## Starting point

Reading audit (22 Oct): "decoded, not read", excerpt only. The repository held Le Grand's clear part (from
"Escripvant ceste lectre") and the first lines of Scheurer's print seen in Google Books snippets; the leaf fr. 3005
f. 165 had not been seen (Gallica 403 to scripts on 9 Oct). No DECODE record of this letter (NOTES, DECODE queue:
"new record suggested").

## What was done

1. **Existing text?** DECODE: no record, so no attachments to open. Print: Le Grand 1688 calls the opening "en
   chiffre non dechiffré"; Brewer and Tomokiyo call it undeciphered; Scheurer t. I (1969) pp. 111-112 prints it, but
   only snippets are reachable (Google Books eNw8AAAAIAAJ, snippet view; copyrighted, cited not copied). No
   contemporary decipherment on the leaf: ff. 165r-166v viewed in full (canvases 259-262), no interlinear and no
   decipherment slip; the neighbours (canvases 255-258, 263-266: a clear document ending f. 161, blank ff. 162-164 and 167, the
   Marquis of Saluzzo's letter f. 168) hold no decipherment; f. 166v is the address leaf ("A Monseigneur, monsr le grand maistre et mareschal de France").
   **Key in the holding archive:** BnF NAF 4206 no. 5 (Friedmann's key, DECODE R9467) has no image on DECODE
   (NOTES section 6); NAF 4206 is not digitised on Gallica (no ark found); not reachable.
2. **Leaf found.** fr. 3005 is Gallica ark btv1b90599952 (link on Tomokiyo's francis.htm, section fr. 3005). The
   manifest has no folio labels; folio numbers read on the corners: canvas 258 = f. 164, **259 = f. 165r, 260 =
   f. 165v, 261 = f. 166r**. Fetched at full resolution (4308 x 6112) from openapi.bnf.fr; scratchpad only.
   The letter is the signed original ("Jo. du Bellay e. de Bayonne"), not a copy: 34 cipher lines on f. 165r, 35 on
   f. 165v, 5 on f. 166r, with clear islands, then Le Grand's clear text.
3. **Read on the image.** Lines cut into native-resolution strips (research/reading_audit/b26_strips.py) and read sign
   by sign with key_p21.tsv and Tomokiyo's table; value transcription `22oct1529_transcription.txt`, sign values
   beyond the key with their evidence in `22oct1529_corrections.tsv`. The opening agrees with Scheurer's snippets
   word for word ("la ou je vouldroye, si ne me sçauroye je guarder d'accorder ... sa requeste qu'il me faict f[aire]
   par ung sien serviteur italien qui luy est demouré seul feal"; "bien aseurez d'avoir maint tour de corde"), which
   checks the key and the transcription on the first five lines and on line 16.
4. **Key values.** Adopted where they hold in every occurrence: ᴗ = a, ᴖ = s, ƕ = f, tall ϙ = m (short ϙ = h), ⊼/Ā =
   l, ẋ = e. Confirmed key values: R = faict, V = bien, 4 = madame (2 of 3 places). Flagged, sense only, not adopted:
   ꝑ (five places, "le Roy" = Henry VIII), ℋ (two places, the King of France: "il supplye ℋ et madame"), —ʊ = n. Not
   adopted (conflicting): ꝗ (t or s), # (null or ç). Unidentified: ꝏ.
5. **Corroboration from the 17 Oct letter** (Le Grand III p. 371, `ref/legrand3_p330_400.txt`): "qu'il plaise au Roy &
   à Madame de l'ayder" matches the cipher's "si le roy et madame ne l'aydent"; Le Grand's clear part of this letter
   ("Outre les pilleries dont on le charge") matches the cipher's "les pilleries qu'il a faictes".
6. **Alignment.** The reading was checked against the transcription line by line; words neither carried by figures nor
   by a clear word are bracketed ([aire] in "f[aire]", [t] in "remons[t]rer", [et], [a]); doubtful values are
   [?word]; stretches with no sense are […].
7. **Look-alike alternates.** 10 letters of the reading rest on a look-alike alternate: m in "main" (△ for ◇), s in
   "son" (ᴗ for ʊ), y in "[?luy]" (barred ϖ), p and l in "[?perpetuele]" (△, ẋ), e in "vieillesse" and "laquelle" (♀
   for ✝), m in "jamais" (◇+ for ◇), s in "est" (small ▵), e in "toute" (♀ for ✝).
8. **Score** (b17_score.py, fr, reading body): 0.513 (20/39); explicit holes (HOLES=1) 0.692 (27/39). With the two
   sense-only word signs written as codes instead of [?Roy] the figure is 0.59 (23/39). Before: excerpt only (0.00).
   Reader's judgement: the first three paragraphs hold (the request; the seal taken, the inventory, the choice of
   the King or Parliament, the charges: the Ferrara league, the bond, the war against the Emperor; "they mean to make
   him lose his head"); the fourth and fifth paragraphs do not (several stretches of signs read letter by letter give
   no words: "qui luy ont […] si tranportes ont mais […]", "ne […] osera", "regrossant ... regnent").

## Result

Not read by the bar: score 0.51 (0.69 explicit holes) and the last two paragraphs do not build sentences. Kept
*decoded, not read*, with this partial reading. The first half (about 300 words) reads as sentences.

## Open, with blockers

- Unread stretches of f. 165v ll. 21-35 and f. 166r ll. 1-5, and the word signs ꝑ, ℋ, ꝏ, the second 4 and #:
  blocker **needs-physical-access**: Scheurer t. I (1969) prints the whole opening; only snippets are reachable
  (snippet view, in copyright); a copy of the volume would settle the open signs and the doubtful words.
- Friedmann's key (NAF 4206 no. 5, DECODE R9467): **needs-physical-access** (no image on DECODE, not on Gallica).
