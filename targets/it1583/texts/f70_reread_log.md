# Re-reading log, f. 70 (DECODE R7899 image P1) (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b29)

Files are in `texts/` and not beside the decryption in `lasry2026/`, because `lasry2026/verify.py` checks that folder's
file inventory against its manifest (any added file fails it).

## Starting point

Reading audit (22 Oct): "decoded, not read": lines 6-8 read, lines 1-5 have one to three ? holes in each clause, the
signature is unread. Clean-sentence share before (Lasry's `companion/edited.txt` lines as sentences): not measured;
the audit's judgement was that sentences do not build in lines 1-5.

## What was done

1. **Every file on the DECODE record.** R7899 (BnF_1583_075, "Non-decrypted", no transcription, no DOC_ attachment)
   fetched with the project cookie (`research/reading_audit/b28_fetch.py`): image P1 (the opening ff. 70v/71, with the
   f. 70 slip pasted at the top right; 3702 x 2590, the same near-binarized photograph Lasry transcribed) and image P2
   (an address leaf: *Ill.mo domino domino meo singularissimo Francisco [Sfortie] Vicecomiti Marchioni et Cremone
   domino atque S. R. Ecclesie Capitaneo generali*). P2 is not the decipherment and carries no name of the sender;
   it is not f. 70's address (the slip has none).
2. **Is there a text of it?** No contemporary decipherment on the record or on the leaf; Mazzatinti 1883 prints the
   heading only; no edition known (September search, NOTES).
3. **Key material: siblings and the archive.** All sixteen other 1446 records of ital. 1583 on DECODE (R7900-R7915,
   ff. 89-158) fetched and viewed (24 images): letters of Angelus, Nicodemo Tranchedini, Johannes de Stavolis and others.
   **None uses the f. 68/f. 70 sign alphabet** (their signs: the Tranchedini family with *per/par* syllable signs and
   ⊩/÷/ꝏ, and on R7900 a third alphabet). Found on the way: **R7900 (f. 89, 30 Sept 1446, Angelus, headed *Cu[m] cifra
   Vincentii*) and R7901 (f. 90, pencilled *Explication du chiffre*) are the same despatch in cipher and in clear** -- a
   contemporary decipherment of the "Vincentius" cipher, which is the cipher of the ASMi Sforzesco cart. 1597 no. 14 key
   ("Angelus cum cifra Vincentij"). Its alphabet is not f. 70's, so it does not read f. 70; it is a lead for the other
   ital. 1583 targets (noted in NOTES; DECODE queue not edited in this batch, per the brief). The September sweep of the
   208 Sforza key records (cart. 1591/1597/1598) had already found no key with this alphabet.
4. **Re-read on the image.** Every sign of lines 1-8 compared with Lasry's overlay and the P1 crop (2x): Lasry's sign
   labels confirmed at every open place; no label changed (no corrections tsv needed). The clear word in line 2 reads
   *[fo]rnendo* or similar (binarized strokes, the initial letters broken); the clear syllables before *te cose* in line 6
   remain uncertain (*[?ques]te*).
5. **Key changes.** **#30 = null, adopted**: 8 occurrences, all at word or phrase boundaries, none inside a word, and no
   letter value makes a word at any of them (f. 70 l. 1 end *cremona #30*, l. 4 end *tute le #30 / sue*, l. 6 *sara stata
   #30 advisata*, l. 8 *e #30 s m n*; f. 68 l. 2 *#25 (6) #36 #30 zorzo*, l. 9 *#25 #30 ad la parte*, l. 11 *_ #30 per
   svspecto*, l. 11 end). Not adopted (flagged for review): #25 as null (9 of 10 occurrences at boundaries; f. 68 l. 10
   *n #25 intita* undecided); (25) = *Duca*, (19) = *ordine*, (26) = *gente*: sense-only, one or two occurrences each.
6. **Partial reading** (`f70_partial_reading.md`) and English (`f70_en.md`); word-by-word alignment with the decode:
   every word is carried by the figures except the clear words (*[?fornendo]*, *[?ques]te*); u/v rendered by position;
   no word supplied. **Look-alike alternates: 0 letters** (no sign label was changed or chosen between look-alikes).
7. **Score** (`b17_score.py`, LANG_=it, reading body): **0.50 (5/10)**; explicit holes (HOLES=1) **0.70 (7/10)**. Before:
   Lasry's `companion/edited.txt` lines 1-7 as one text, 0.40 (4/10), explicit holes 0.70.
   Reader's judgement: sentence 1 (the Duke [?] moving against Cremona, Venice expected to declare itself) and sentence 3
   (the closing and date) hold; sentence 2, the news itself (who has gathered, what order is given, to whom), does not:
   three open sign classes and the unclear *gli do venire unire piu*. Kept **decoded, not read**.

## Open

- (25), (19), (26), #25, (4), (6), (22) without values: blocker **no-key-material** (no key, no decipherment, no sibling
  in this alphabet among R7899-R7915 or the 208 Sforza key records).
- The signature: blocker **no-key-material** (same classes).
- The clear words in lines 2 and 6: blocker **illegible** (binarized photograph; a colour BnF scan would decide them).
