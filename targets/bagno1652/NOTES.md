# Guidi di Bagno to the Secretariat of State, Paris, 5 January 1652

**Status:** key recovered from ciphertext-only by George Lasry; all four cipher pages deciphered with the scattered gaps and tentative code values listed below. Key state: partial.

## Contribution, 20 October 2026
Solved by George Lasry. Transcription was made with CTTS (CrypTool Transcriber and Solver), using its machine-learning model and manual correction. Ciphertext-only cryptanalysis was performed with GPT-6 Astra and Anthropic Claude Opus 5.5 under Lasry's direction.

The submission covers all four cipher pages, ff. 6r–7v, in reading order P3, P4, P5, P1. The record also includes a clear opening leaf, f. 5r; it is not included in the four-page cipher reading.

This letter was not part of George Lasry, Beáta Megyesi and Nils Kopal, "Deciphering papal ciphers from the 16th to the 18th Century", Cryptologia 45(6), 479–540 (2021; published online 2020), DOI 10.1080/01611194.2020.1755915 (scope confirmed by George Lasry).

## Historical context and contents
Written from Paris on 5 January 1652, during the Fronde, the despatch concerns opposition to Cardinal Mazarin's return to France. Guidi di Bagno reports the Parlement's death sentence and 150,000-livre bounty, threats against Mazarin, and an appeal for papal intervention. The central dispute is whether a secular court can punish a cardinal or whether that authority belongs to the pope.

The nuncio rejects the Parlement's jurisdiction over a cardinal. A speaker tentatively identified as the Duke of Orléans threatens that Mazarin will be killed in his cardinal's robes unless the pope summons or deprives him. The letter also reports the Queen's broken promise that Mazarin would not return.

The record identifies the recipient as the Secretariat of State. The working edition calls him Cardinal Chigi; Fabio Chigi was not created cardinal until 19 February 1652. We therefore retain the record's office attribution in the public title, without silently treating the working header as proof of a personal addressee.

## Files and reading order
- `key.txt`: current CTTS key; `?` remains tentative.
- `transcription/all.txt`: exact CTTS grouped ciphertext, export order P1/P3/P4/P5.
- `decryption/all.txt`: exact CTTS automatic key application; not the edited prose.
- `edited/all.txt`: full existing edited Italian rows, reordered P3/P4/P5/P1.
- `edited/edits.txt`: original CTTS aggregate.
- `reading_edition.txt`, `translation_en.txt`: complete contributed editions, including all four cipher pages and uncertainty conventions.
- `snapshots/key.png`, `snapshots/decryption key.png`: refreshed CTTS snapshots, copied without recompression.
- `token_audit.tsv`, `counts.json`, `source_hashes.json`: reproducible counts and source integrity.

## Measured coverage
1,796 cipher elements; 94 distinct labels (93 digit codes plus the unresolved x3); 3,404 represented digits. Cleartext placeholders are excluded.
1,759/1,796 (97.94%) occurrences have unqualified key values; 35 have tentative values and 2 are unresolved. This is key-application coverage, not a claim of that percentage of correct Italian. The edited reading still has local gaps and uncertain word divisions.

## Recovery
The attack recovered the grouping of a continuous digit stream into single-digit letters, two-digit letters and syllables, and four-digit word/name codes. Repeated Italian words and crib testing constrained the values; the roughly alphabetical nomenclator helped extend them. The manuscript was revisited to correct touching-digit ligatures, duplicated boxes, and the marked 04 = qu versus plain 04 = che. Values were checked across the four cipher pages. No matching historical key or decipherment was used. Clear words interspersed in the letter supply context, not a parallel decipherment of the cipher passages.

The rejected Francia 346 key, noisy OCR, and proposed generic null-5 rule did not supply the solution. No general null-5 rule was accepted. The double-digit ligatures require image checks; they cannot be inferred solely to force fluent language.

## Remaining gaps
- 2698 in the Sedan date — blocker: no-key-material. One occurrence after venti; the day must remain twenty-[…], not a guessed precise date.
- x3 at f. 6v line 21 — blocker: illegible. Ink blot obscures the grouping.
- f. 6r lines 19–20 and f. 7v closing fragment — blocker: illegible. The edited reading retains explicit gaps; assigned letters alone do not recover the lost wording.
- Tentative nomenclator and Queen passage — blocker: no-key-material. 35 occurrences of 27 tentative labels; names and the conditional sentence remain marked with question marks.

## Escalation
- [x] siblings: previous repository investigation checked the exact shelfmark and neighbouring DECODE records; no matching sibling found.
- [x] clear-pages: previous investigation inspected all five record images; no parallel decipherment.
- [x] known-keys: Francia 346 excluded; the solution reconstructs this letter's own key.
- [x] print: prior repository search found no edition of this despatch; author confirms exclusion from the papal-cipher article.
- [x] key-rebuild: CTTS ML-assisted transcription, Italian cribs, repeated groups, alphabetical code structure and source checks.
- [x] retry: repeated application across all four cipher pages; the residual date, blot and tentative names stay explicit.

## Previous repository investigation, 22 September 2026
The following records the earlier unsuccessful attempt, not the current outcome.

## The suggested Francia 346 key

George Lasry's reconstructed key for AAV Francia 346, used successfully on the Barberini–Ceva correspondence of 1632, was the first test. It is a two-digit homophonic/syllabic nomenclator in which `6` is a separator and never belongs to a code group. R5622 repeatedly has `66` and `666`; treating every 6 as the Francia 346 separator leaves dead one-digit and malformed groups. A checked line decoded with that table gives invalid groups and no Italian.

This is a structural exclusion, not merely a bad language-model score: the observed digit stream cannot have been written under that separator rule.

## Searches and sibling check

- DECODE has no second record for `Francia_104`, no attached documents, and no image transcription.
- Adjacent records are unrelated: R5617–R5621 are Francia 32 items; R5623 is Francia 173 (Ranuzzi, 1684–85); R5625 onward is Francia 346. None is a clear copy or same-key sibling.
- Searches for the exact shelfmark, correspondent, date and route found no printed edition of this despatch. The published study of Guidi di Bagno during the Fronde covers 1647–50, not this 1652 letter. Neveu's *Acta Nuntiaturae Gallicae* 10 concerns Ranuzzi in 1684–85, the separate R5623 record.
- No online register of *decifrati* or matching nunciature key for Paris in 1652 was located.

## Transcription attempts

Whole-line OCR and character segmentation were tried on the four cipher pages. The handwriting, touching figures, variable spacing and bleed-through produced enough substitutions and missed digits that the output cannot support cryptanalysis or publication. A glyph-clustering pass found thousands of candidates but did not yield a dependable digit sequence. These experiments are evidence about the work still needed, not a transcription.


## Sources
- [DECODE R5622](https://de-crypt.org/decrypt-web/RecordsView/5622), AAV Segreteria di Stato, Francia 104, ff. 5r–7v; cipher on ff. 6r–7v.
- [Julien Régibeau, study of Guidi di Bagno and Mazarin during the Fronde](https://orbi.uliege.be/handle/2268/210527), background only, not this letter's plaintext.
- [Lasry, Megyesi and Kopal, papal-cipher article](https://doi.org/10.1080/01611194.2020.1755915), not the source of this solution.
- [Treccani, Alessandro VII](https://www.treccani.it/enciclopedia/alessandro-vii_%28Enciclopedia-dei-Papi%29/), Chigi's promotion on 19 February 1652.
