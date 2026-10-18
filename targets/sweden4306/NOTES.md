# Sweden DECODE R4306

Status: read in part — contributed solution, 17 October 2026.

**Belongs to: Riksarkivet key-box and Oxenstierna ciphers.** See the [earlier group survey](../riksarkivet1628/NOTES.md) and its [public page](https://dbourdeau.github.io/cyphersolver/riksarkivet1628.html). R4306 has its own entry because it uses a different key from the other systems in that group.

**Transcribed with CTTS, then solved with Opus 5.5**, as expressly confirmed by George Lasry. Lasry directed the work and supplied the Dutch reading, English translation, contextual notes and working material. Codex prepared this contribution and independently checked the transcription counts, source glyphs and five mechanical lines. The original local research files were not changed.

## Document and scope

Riksarkivet, Stockholm, **Chifferklaver låda II:133**, [DECODE R4306](https://de-crypt.org/decrypt-web/RecordsView/4306). The public metadata checked on 17 October 2026 lists a numerical cipher, status Non-decrypted, three pages and a broad date range 1600–1699; the sender, recipient and languages are blank. Its general collection note lists Oxenstierna correspondence, but does not attribute this particular letter.

This contribution covers **one cipher page**, supplied as `1.png` (the earlier survey labels this view IMG_R4306_I25832_P_hi.jpeg). The earlier survey reports a wrapper numbered II:104 and an Amsterdam address; those other views have not been independently inspected for this submission. The live image manager requires login. Do not treat three record pages as three newly deciphered ciphertext pages.

The cipher page has a pencilled **1632?** at upper left. This annotation is visible but is not an established date of composition. The letter mentions earlier letters of 23 February and 13 March, without a year in the deciphered body. The contributor’s suggested late-March/April setting, diplomatic congress and recipient in Swedish service remain hypotheses. Custody in a Swedish archive alone does not identify the recipient, and the February/March references do not prove composition in those months of the same year.

## Cryptanalysis

No interlinear, marginal, top- or bottom-of-page decipherment appears on the supplied cipher page. The contributed key was recovered from ciphertext, using CTTS transcription and Opus 5.5 analysis, not a historical decipherment or a matched archive key; this is a **ciphertext-only recovery**. The supplied readable text is the result, not an external plaintext source used to obtain the key.

The system is **monoalphabetic substitution with nulls and a small unresolved nomenclator**. There are **461 cipher elements in one document**, 40 distinct cipher types, across 35 CTTS rows. The 463 selections include two date-numeral units (`285`, `d13`) excluded from the cipher count. The 461 comprise **422 alphabetic occurrences, 34 nulls, and five occurrences of four unidentified codes**: 105 once, 106 once, 113 once and 114 twice.

The working alphabet assigns consecutive values **30–52 to 23 letters**, with no letter homophones (one number per vowel/consonant). Only 21 alphabet values occur: 45=q and 51=x are predictions from the ordered sequence, not observed recoveries. The preserved source key’s “24-letter alphabet” header is a counting error; there is no listed j, v or z value. Fifteen null classes occur; the key additionally lists 13 as a null, but it is absent from the current transcription. The four nomenclator values remain unidentified, with personal names, powers or courts suggested by their syntax; no complete nomenclator inventory is claimed.

The labels `285` and `d13` are CTTS identifiers for the date numerals interpreted as 23 (written 2o3) and 13 with a superscript mark. These two are not additional deciphered name codes. Assigned-letter coverage is 422/427 non-null cipher occurrences (98.83%); this is not a measurement of semantic accuracy. Edited words, transcription uncertainty and open codes keep the contribution partial.

## Readings and five-line mechanical check

- [reading.txt](reading.txt): the contributor’s **edited, normalized Dutch** text, preserved verbatim.
- [translation.txt](translation.txt): the contributor’s English translation, preserved verbatim.
- [contributor_context.txt](contributor_context.txt): the supplied translation notes and interpretation; formatting only has been simplified.
- [key.txt](key.txt), [transcription.txt](transcription.txt): current CTTS inputs copied byte for byte, with checksums in `input_checksums.json`.
- [visual_key.png](visual_key.png), [visual_key.html](visual_key.html): current numerical alphabet, actual manuscript glyph samples, nulls, open codes and separate date numerals.
- [mechanical_excerpt.txt](mechanical_excerpt.txt), [mechanical_excerpt.json](mechanical_excerpt.json): **exactly the first five manuscript/CTTS lines**, 73 selections yielding 62 letters. Nulls are omitted; no word division, u/v normalization, spelling correction or gap filling is performed.

The literal excerpt reads:

```text
alleswtdenuw
enuerstaenicsal
mondelingekll
menantwoorden
alsodesaecken
```

The uncertain `ekll` / `men` crossing lines 3–4 is retained literally; the supplied edition has `[gekl…men?]`. Likewise line 5 is `alsodesaecken`, not a mechanical confirmation of every restored letter in “Als o[o]c des saecken”. Elsewhere the source key explicitly notes unresolved written readings such as 39 in line 10 and 38 in line 32. The full edition must not be mistaken for exact key output.

`build.py` reproduces the inventory, chart and those five lines only. `validation.tsv` contains only that excerpt. At 62 letters it is below the repository validator’s 80-letter threshold; no full-text statistical validation or accuracy claim is substituted for this limitation.

## Historical research and prior work

The earlier 21 September `riksarkivet1628` survey records unsuccessful attacks on R4306 in several languages and unsuccessful tests of R4296/R4310. Its 1632/Amsterdam description is cited as earlier research, not silently promoted to a proven attribution. The old survey and profile remain as dated project history; the public page receives a dated link to this contribution.

The current key is a new contributed solution by Opus 5.5, as confirmed by Lasry. An earlier local backup is labelled CTTS cryptanalysis and contains incompatible preliminary letter assignments; it is not the successful key or a historical plaintext source. No exact prompt history, solver settings or chronology beyond the supplied records is claimed.

A limited exact-phrase web search for the opening did not locate a complete earlier edition. This is not an exhaustive prior-publication search. The identities of codes 105/106/113/114, writer, recipient and location remain open. The supplied “U.L.”, “gade gegeven” and diplomatic-setting notes are preserved as contributor commentary, rather than independently verified identifications.

## The project's earlier attempt (folded in 18 Oct 2026)

Before this contribution, the project had its own entry for the same record, `riksarkivet4306` (split on 14 Oct 2026
from `riksarkivet1628` under the one-key rule; work done 21 Sept 2026 in the riksarkivet1628 session; the old profile lists claude-opus-5 and claude-opus-5-5 over two sessions).
It ended attempted, open, with no value recovered. Under "one key, one entry" this entry is now the only one for R4306;
the old entry's transcriptions are kept in [`project_attempt/`](project_attempt/), and its page
`docs/riksarkivet4306.html` is a stub pointing here.

- `project_attempt/r4306_transcription.txt` (agent, 21 Sept 2026): 463 numbers in the 21 Sept count; re-measured
  14 Oct 2026 as 492 tokens, 51 distinct, IoC 0.073.
- `project_attempt/r4306_v2.txt` (21 Sept 2026): re-transcribed keeping the scribe's variant forms (34/74, 40/4o/9o,
  30/3o/70/7o: 55 tokens); 465 tokens, 62 distinct. Whether the variants were distinct signs was left open.

What was tried, all without result:

1. (21 Sept 2026) Statistics: monoalphabetic by IoC (0.078 in the 21 Sept count); "34 42" x31.
2. (21 Sept 2026) Simple-substitution and homophonic annealing (`targets/riksarkivet1628/solve_num.py`, `qg.py`) over
   quadgram models in nl, de, la, fr, sv, en, it, es, pt, da, also with low/high numbers as word breaks: no language
   converged (best about −4.3/char against about −2.5 for real text). A search bug (free changes propagating by swaps)
   and a backoff-model artefact were fixed first. Dutch, the language of the contributed reading, was among the ten.
3. (21 Sept 2026) The same on `r4306_v2.txt`: no fit.
4. (21 Sept 2026) Box keys R4310 (Siebenbürgen "Schauis") and R4296 (1632, 30 ends every word) tested: no fit; the
   other 68 of the 70 fetched Chifferklaver key records (R4259–R4329) were not tried.
5. (14 Oct 2026) Split from riksarkivet1628; both transcriptions re-measured. No new attack.

The earlier entry recorded the page as addressed to a "Mr ?ilick" at Amsterdam, with three DECODE images
(`IMG_R4306_I25832_P.pdf`–`I25834`) and the wrapper II:104; these come from views of the record other than the one
contributed page; the address (Amsterdam) and wrapper were verified on 18 Oct 2026 (see Findings of 18 October 2026). Why the September annealing failed where the
contributed key works (nulls, the four codes, the digit-variant reading, or the search itself) has not been examined.

## Findings of 18 October 2026 (proposals for George Lasry's review)

Done by Claude after publication, on the DECODE images fetched with the project cookie (the 21 Sept download plus
R4319–R4321, fetched now). George's key, reading and translation are unchanged; everything below is a finding or a
proposal for him to accept or reject.

- **The other two views of R4306.** Image I25833 is the address leaf: *Aen Mr. ?ilick* (Wilick?) *… Amsterdam*. That
  confirms the earlier survey's Amsterdam; the first letter of the surname is unclear. Image I25834 is the archive
  wrapper, *II:104*, "1600– Chifferbref till … i Amsterdam".
- **A cipher note on the address leaf, not counted before.** Three lines in the right margin, in the same numerals,
  part of line 1 torn away: `40:34:46. , [torn] 37:40:33:34:42` / `113:42:30:34:40:33.30:11:42:` /
  `39:42: 101. 42:30:27:11:41:39`. With the letter's key: *ler., … hlden / [113] naeldan / kn [101] na..mk*. That is not
  Dutch. Caesar offsets of the alphabet and the R4287 sequential key fail too. It adds a fifth code value, **101**,
  and a second occurrence of **113**.
- **The pencil list on the wrapper is not R4306's nomenclator.** A faint list on I25834 (*Nz …, Oz …, Tz Rex Polon.,
  Vz Victoria …*) is the last leaf of R4305 (the Brandenstein 1630 key, II:132, filed next to it), seen through or
  offset onto this sheet.
- **Box keys, all of them.** The archivists' wrappers of the Chifferklaver keys give each key's *a* values
  ("a = 7, 35, 51", "a = 20", …). None of the 43 labelled wrappers says a = 30. The unlabelled and wrapperless keys
  (R4272, R4275–R4277, R4280, R4281, R4287–R4299, R4301–R4302, R4305, R4308, R4309, R4314, R4322, R4324, R4328) and
  the three never-fetched records R4319–R4321 were opened page by page. None has an alphabet a=30 … y=52. R4287
  ("diverse chiffernycklar från 1600-talet av okänd proveniens") is a similar sequential type with another
  alphabet (a = 2/28/10, c = 31, the tens skipped).
- **The template, as a proposal.** R4319 (Jacob du Moulin, 1650) is built exactly like R4306 at another offset: a
  sequential alphabet a=20 … z=43, then a book of nomenclator words in alphabetical sections numbered from 101
  (101 Archangel, 102 Arensborg … 111 Agent, 112 Ambassadeur, 113 Amsterdam; B from 120, C from 133). If R4306's key
  followed the same layout, its 101–114 would be words beginning with A (or B). Proposal only: five occurrences of
  four values cannot test it.
- **Doubtful words on the image.** The scribe writes 0 as a tailed *o*, so 30/38 and 40/43 are ambiguous: line 4
  ends `33:34:40·3ø:42·16:2ø:36:34:39:40:40:`, line 33 ends `41:30:46:3ø:52` (Mar…y). No better reading can be
  forced from the one image.

## Remaining gaps
- Codes 105, 106, 113 and 114 (and 101 in the address-leaf note) — blocker: no-key-material; no key with this alphabet among the 61 Chifferklaver låda II key records on DECODE (checked 18 Oct 2026), no gloss on any of R4306's three views, and five occurrences of four values are too few to rebuild the nomenclator. The R4319 template points to A/B-initial words (proposal).
- Doubtful words and literal-versus-edited discrepancies — blocker: illegible; the scribe's tailed 0 makes 30/38 and 40/43 ambiguous on the only image, the rest are the scribe's slips, and no contemporary decipherment exists. George's restorations stand.
- Cipher note on the address leaf (I25833, three lines, about 22 numbers, partly torn) — blocker: too-short; does not read under the letter key, offsets or R4287, and is too short and damaged to fit a variant.
- Year and sender — blocker: needs-physical-access; the letter names neither, and the wrapper date (1600–) and pencilled 1632? are archivists' estimates. Recipient read as Mr ?ilick (Wilick?), Amsterdam; only Riksarkivet provenance records could date it.

## Escalation
The supplied solution was published at the contributor's request on 17 Oct; the steps below were worked on 18 Oct 2026.
- [x] siblings: R4306's own two other views opened (address leaf with cipher note, wrapper); neighbouring records R4305 (key, source of the wrapper's ghost list) and R4307 checked; the group survey's unrelated systems (Bremen, Rusdorff, E 708) reviewed.
- [x] clear-pages: no historical decipherment on any of the three views; the address-leaf note is cipher, not a gloss.
- [x] known-keys: every Chifferklaver låda II key record on DECODE checked for an a=30 alphabet (wrapper labels plus page-by-page for unlabelled keys; R4319–R4321 fetched); none matches. R4296/R4310 failures credited to the earlier survey.
- [x] print: limited exact-opening and record searches found no complete printed plaintext; no priority claim.
- [x] key-rebuild: alphabet verified; nomenclator bracketing tried against the R4319 template (A/B-initial words from 101), not testable on five occurrences; no values invented.
- [x] retry: doubtful spots re-read on the page image (digit-form ambiguity), the address-leaf note decoded with the key and variants; nothing further reads.

## Sources and credit
- George Lasry, supplied CTTS material, edited Dutch reading, English translation and contextual notes, 17 October 2026. **Transcribed with CTTS, then solved with Opus 5.5.**
- [DECODE R4306](https://de-crypt.org/decrypt-web/RecordsView/4306), Riksarkivet, Chifferklaver låda II:133; public metadata checked 17 October 2026.
- [Earlier group survey](../riksarkivet1628/NOTES.md), 21 September 2026, retained as dated prior work.

DECODE changes are queued locally as **Partially**, with Dutch plaintext and the recovered system described, but are not sent by this PR. No exact date or correspondent correction is proposed.
