# Re-reading log, no. 97 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b29)

## Starting point

Reading audit (22 Oct): "decoded, not read", judged on the 22 Sept running text (`no97_reading2.md` §2), which has a
`[?]` in almost every line. Score of that text as a reading body (`b17_score.py`, LANG_=fr): **0.069 (2/29)**; explicit
holes 0.138. The 5 Oct pass (nulls λ γ U π m̄, 141 = qu'il, image corrections) had been graded in `no97_reread.txt` but
never rendered as running text.

## What was done

1. **Every file on the DECODE record.** R9449 (this letter) fetched with the project cookie: one image, a lower-resolution
   photograph of f. 109 (2023 x 2881) than the Gallica IIIF used since September; no attachment, no transcription, no
   comment. R9444 (no. 22, "Decrypted") re-fetched: two images of the plaintext decipherment of the January 1592
   Vaudémont letters; a different set of letters, no cipher on the sheet (as found in September).
2. **Is there a text of it already?** Tomokiyo's *Unsolved Historical Ciphers* page re-fetched 23 Oct: unchanged, still
   only the opening (*J'ay este infiniment mal satisfait du peu d'execution ...*), no key, no text. His *lorraine*,
   *nevers*, *league* and *henryiv* pages carry no key or decipherment of this letter.
3. **The key under another name.** The DECODE record list (`research/catalogue_harvest/decode/list.json`, 10,106 records)
   and the full metadata of the 2,444 ciphertext records (`views*.jsonl`) searched for Lorraine, Lorena, Lothringen,
   Vaudémont and Nancy: only R9449, R9444, R7952 (Bréval c. 1620) and a 1903 postcard. Key records of BnF holdings
   1580-1600 listed (103 BnF keys; fr. 3995 ff. 1-142, fr. 3022, fr. 3623): fr. 3623 no. 23 (R9453, the one not seen
   before) fetched and viewed: it is a Bienvenut-Nevers cipher of February 1590, not this one. Tomokiyo's fr. 3995 catalogue
   (`nevers.htm`) searched for letter-pair, reciprocal and Lorraine keys: none described. No key found.
4. **Running text from the 5 Oct graded re-read** (`no97_partial_reading.md`), with the clear opening line and the two
   clear lines inside the cipher. Word-by-word: every word is a graded word of `no97_reread.txt` (H/C plain, M as
   `[?word]`) or clear text from `clear_texts.md`; no word supplied.
5. **Key change, adopted: the standalone crossed t (T) is a null.** Eight standalone occurrences, all between complete
   words, and the sentence runs on without each: *[57] T et ceulx de la*, *il T fauldra*, *luy T dire*, *leur T ses
   promesses*, *[?…ien] T le fera*, *[…] T chemins*, *du dict T Chasteauvilain*, line-end after *[103]*. Same evidence as
   for λ γ U π m̄ (5 Oct). Inside words (*T-ien*, twice: L03, L17; L13 has m̄-*ien*) it is not a null and stays unread; *bien*
   fits L03 and *combien* L17 only if 146 = *com*, so nothing adopted there (sense-only, flagged).
   Not adopted (tested on the contexts, flagged): standalone G = *que* (fits *du peu d'execution G vous* and
   *mescontantement G vous*, fails *[123] G pioniers* and *[121] G r j*); j = null (fits *infiniment j mal*, untested
   elsewhere).
6. **Score** (reading body): **0.154 (4/26)**, explicit holes the same (0.154); before 0.069. One sign in five is open;
   the sentences do not hold. **Look-alike alternates: 0 letters** (no label changed this pass).

## Result

Stays **decoded, not read**.

## Open

- Special signs (ŧ inside words, ⊙ where not s, α, ꝗ, E, figure-4, Z, V, standalone G, j, D), figures 57, 98, 122, 123,
  13, 137, 88, 146, 121, 103, and the garbled runs of L11-L13 and L20: blocker **no-key-material** (no key on DECODE,
  in fr. 3995 or fr. 3623, or in print; no second ciphertext in this system in fr. 3621; each sign occurs 1-12 times
  with no single value fitting all its occurrences).
- A key or duplicate in the Archives départementales de Meurthe-et-Moselle (Lorraine ducal archive, series B) was not
  sought: blocker **needs-physical-access** (not consulted; no online item-level key found).
