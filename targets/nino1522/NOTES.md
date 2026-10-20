# Rodrigo Niño (Naples) to Charles V, 19 March 1522 — BNE MSS/20213/27 (DECODE R1182)

Status: write-up prepared — George Lasry recovered the key with CTTS cryptanalysis; eight cipher lines deciphered, with one sign identity still ambiguous. Contribution prepared 20 October 2026.

## George Lasry contribution, 20 October 2026

**Solved by George Lasry.** Transcribed with CTTS (CrypTool Transcriber and Solver); an initial key was recovered with CTTS built-in cryptanalysis. The key and translation were refined by GPT 6.1 Sol and Anthropic Opus 5.5. Lasry supplied the workflow attribution. This is an outside contribution, not a claim that Bourdeau's September solver succeeded.

The current eight lines contain **260 cipher elements in 49 observed classes**: 257 non-null occurrences and three null occurrences (`mer` twice and `por` once). The key has 44 letter-sign classes (one still has an unresolved p/y identity), two word-part classes (LL and ND), one honorific code (V.M.), and two null groups. The largest settled homophone sets have **four signs per vowel** (a and i), **three per consonant** (g, p and r). `decode.py` recomputes the inventory; labels are CTTS identifiers, not historical numerical codes.

**255 of the 257 non-null occurrences have an unambiguous assigned value (99.2% assignment coverage).** The same unresolved class (39) occurs twice. Coverage is not a measured transcription or translation accuracy. LL and ND are contextual one-occurrence readings; see key.tsv. The clear prose outside the eight-line block is historical context, not claimed as newly transcribed or deciphered here.

Files: `transcription.txt` (eight labelled lines), `key.json`, `key.txt` (CTTS), `key.tsv` (status), `decryption_tokens.txt` (token-aligned), `decryption_literal.txt` (no word division or repairs), `decryption_edited.txt` (spacing, accents, u/v normalized), and `translation_en.txt` (the whole cipher block, with the uncertainty retained). `ctts/` contains positions, palette, transcription, edited records and newly drawn icons. Source page images are not redistributed: the DECODE metadata explicitly requires archive permission. The website shows the reconstructed key and sign inventory, with a link to R1182; no manuscript photograph is published in this PR.

### Corrections and tests

- Seven duplicate detections of single physical signs were merged. The old 336-character eye transcription incorrectly split modifiers and is superseded, not pooled with this one.
- Separated the two-tick loop (52=u) from plain loop (37=b); source contexts give `sufrir` and `abrá`.
- Separated `ofo` (53=i) from `oto` (9=d), giving `Dios` rather than `Ddos`.
- Merged former class 33 with 13=a, supported in `paga` and `guarda`; did not adopt the suggested 33=i.
- (20)=V.M. is supported by three contexts: `suplico a V.M. mande`, `crea V.M.`, `servicio de V.M.`.
- Retained the nasal-marked d as (35)=nd in `pan de`; the plain d in line 5 belongs to (8). Retained the distinct double-barred sign (50)=ll in `ellos`, with its one-occurrence limitation.
- Removed the unsupported initial `Mas` and closing `nuestro señor` expansions. The literal groups there are `mer` and `mer por`, agreeing with the null-group description cited in the earlier research.
- (39) would need p in `pan`, y at the start of line 7 (`y este`). No visual split or general polyphony is proved. The machine key retains `p/y?`; literal output prints `?`; the edited text and translation mark the proposed connective uncertain. No silent contextual p/y substitution is counted as a settled value.
- `bivir`, `ynconviniente` and `abrá` preserve historical spelling. Plain u is normalized to v in the edited `bivir`, `ynconviniente` and `servicio`; the literal output retains u.

### Prior research and independence

The following September record is retained as the prior attempt. Its claim of a simple alphabet and exact identity with Kolosova's system has not been confirmed against her actual key: the new working inventory is homophonic. Tomokiyo's description of a related 1522 Niño cipher and Kolosova's earlier reconstruction must be acknowledged, but no exact-letter or first-publication claim is made. The CTTS initial alphabet key and the October reading existed before this submission pass consulted that prior-research note. The published description helped correct the null interpretation; it did not supply the alphabet mappings or the paragraph plaintext.

## Remaining gaps
- (39), two occurrences — blocker: illegible; one class may conflate a subtle modified sign; context suggests p and y, but the source image does not establish the split.
- LL (50) and ND (35) are each contextually reconstructed from one occurrence, not checked against a surviving original key.

## Escalation
- [n/a] siblings: this submission concerns the one eight-line block supplied by Lasry; no other ciphertext in a different record is claimed deciphered.
- [x] clear-pages: the opening is clear outside this block; no literal decipherment is visible beside it.
- [x] known-keys: the earlier Lope Hurtado comparison failed; no external alphabet key was applied.
- [x] print: Kolosova and Tomokiyo's prior related-system reconstruction is acknowledged below; exact letter coverage remains unconfirmed.
- [x] key-rebuild: CTTS recovery followed by source-based sign splitting, duplicate removal and contextual testing.
- [x] retry: every one of the 260 elements is included in token-aligned output; (39) is left ambiguous in both occurrences.

## Earlier research record (September 2026)
The sections below preserve the earlier observations and unsuccessful attempt, rather than attributing that attempt to Lasry.

## The document

- Biblioteca Nacional de España, MSS/20213/27 (Gayangos collection; stamp "PASCUAL de GAYANGOS" on f. 1).
  DECODE R1182, 3 images (authenticated; not public domain, so the images stay git-ignored):
  `IMG_R1182_I5903_P1.png` (f. 1r), `IMG_R1182_I5904_P2.png` (opening f. 1v–2r), `I5905_P3` (did not download).
- Headed "S.a C.a C.a M.t", dated at the top and at the foot "Napoles 19 de março 1522"; signed by Rodrigo Niño.
- **The letter is almost all clear Spanish.** It covers the death of the viceroy (Ramón de Cardona, d. 10 March
  1522), the Council's steps to govern the kingdom, pleas for a successor, Don Juan Manuel, the duke of Sessa's arrival,
  Marco Antonio Colonna, the French in Lombardy, and financial business (the *pagamentos fiscales*, Salmona, the sale
  of offices). **One paragraph is ciphered**: 8 lines on f. 1v (lower half of the left page), opening with
  `[mer]` and closing `[mer por]`. It comes after the paragraph about the duke of Sessa and Juan Manuel and before one
  on the tension in Naples between the popolo and the nobles, so it probably concerns the viceroyalty or Juan Manuel.
- DECODE describes it as "homophonic; graphic signs, numerical", date "1522", sender Rodrigo Niño, Naples. That is right.

## Prior art (checked first)

- **Tomokiyo, cryptiana `spanish2C_now.htm` (copy at `targets/vasto1527/prior/`), "Ko.15 Rodrigo Niño (1522)"**: Olga Kolosova
  reconstructed Niño's cipher "from three letters in Spanish from 1522. This is a simple substitution cipher. The
  specimen includes three symbols for words/phrases (e.g. 'g e' = gente de armas) ... three- or two-letter
  combinations such as 'por', 'pu', 'mor', 'mer', looking like codes, are used as nulls (p. 458-459)."
  **This block opens with `mer` and closes with `mer por`**, which fits her description exactly. So this is the same
  system, and very probably one of her three letters (her corpus is Salazar y Castro at the RAH plus BNE letters).
- Kolosova, O. (2017), *El lenguaje secreto de la diplomacia de Carlos V (1521-1527)*, doctoral thesis, Universitat de
  València (RODERIC hdl 10550/66216). **The RODERIC PDF (148 pp., `lit/`, git-ignored) is a short version with no Niño
  chapter**; Tomokiyo cites 854 pp. The 2024 book (Ediciones Universidad de Salamanca, doi 10.14201/0MX001, 20 €, not
  open access) has a "Cifrarios" section at pp. 171–224, which should contain the Niño alphabet.
- So a reading probably exists in Kolosova's thesis edition. I have not seen it, and I cannot confirm this letter is
  among her three.

## Attempt (21 Sept 2026)

- `cipher_p2.txt`: an eye transcription of the 8 lines, one ASCII letter per sign, spaces kept. 128 words, 336 signs;
  `#` (a double-barred cross) follows many other signs and is 19% of all signs. Recurring words: `oto` ×7, `xzH` ×7
  (probably *que*), the single-sign words `T` ×5 and `w` ×4 (probably *y* and *a*).
- `anneal.py` + `nulltest.py` + `mergetest.py`: simulated annealing with `lang` es-golden-age 5-grams, at most two
  signs per letter, and with variants: `#` dropped as a null, `o` dropped, both dropped, `#` merged into the sign
  before it. **Best −2.9 to −3.5 per character; real Spanish scores about −1.1.** Nothing readable.
  (The first run, with no cap on signs per letter, collapsed to all-'i'. The cap is needed.)
- Why it fails: the signs are small cursive shapes at DECODE's resolution (about 12 px high). Several pairs
  (`g`/`9`, `l`/`L`, `4`/`+`, the barred signs) cannot be separated reliably, and the null groups (Kolosova's
  `mer/mor/pu/por`, plus possibly `ao`, `eo`, `oe`, `mo`) cannot be pinned down without the key. 336 signs with
  unresolved nulls and a doubtful transcription is below what a blind attack needs.

## What would move it

1. Kolosova 2024, "Cifrarios" (pp. 171–224) or the full 2017 thesis: the Ko.15 alphabet would read the block at once.
2. A better image: BNE Biblioteca Digital Hispánica may hold MSS/20213 at full resolution (the DECODE note points there).
3. Niño's other ciphered 1522 letters (RAH Salazar or BNE MSS/20213): more text for a proper attack.
