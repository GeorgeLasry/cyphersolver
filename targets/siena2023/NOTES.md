# Siena 20 & 23: DECODE R4808 and R4811

Status: read in part — contributed key recovery and readable editions by George Lasry, 17 October 2026.

These two documents use one graphical cipher. They belong to **Archivio di Stato di Siena, Concistoro 2308, fasc. 2, “Lettere in cifra”, nos. 20 and 23**. This contribution supplies Lasry’s Italian readings and English translations, the current working key and an illustrated key. It does not claim a complete decipherment or establish a year or all the personal names.

## Documents and supplied editions

| Document | Supplied edition | English translation | Internal dating and parties |
|---|---|---|---|
| No. 23, R4811 (the contributor’s **Letter 1**) | [R4811_reading.txt](R4811_reading.txt) | [R4811_translation.txt](R4811_translation.txt) | Two memoranda for Iacobo Spinelo and Francisco Gactule, giving a king’s orders; the second requires arrival by 4 May. No year or issue date established. |
| No. 20, R4808 (the contributor’s **Letter 2**) | [R4808_reading.txt](R4808_reading.txt) | [R4808_translation.txt](R4808_translation.txt) | An unidentified writer at Perugia addresses a king; the closing gives the penultimate day of March, i.e. 30 March, without a year. |

The Italian text is the contributor’s supplied edition, unchanged apart from removal of the exterior “Letter 1/2” labels. The English translations are also supplied by the contributor; headings and paragraph separation are presentation only. Square brackets, question marks, angle brackets, lacunae and unidentified names are retained. Editorial restoration is not represented as additional key recovery. In particular, the English wording sometimes interprets difficult Italian passages more freely; it is not independent evidence for their reading.

Only one short mechanical check is included: [excerpt.txt](excerpt.txt), three display lines corresponding to no. 23, CTTS L49 item 39 through L51 item 24. The 108 sign selections yield 109 letters and match the supplied edition after word spacing, punctuation, accents and u/v normalization. There are **no substituted letters or filled gaps in this excerpt**. The excerpt was selected for agreement and is not a random sample or a validation of the complete editions. No full mechanical decipherment is included.

## Cryptanalysis

**Transcribed with CTTS, then solved by GPT-6 Astra**, as confirmed by George Lasry. Recovery used ciphertext patterns and original cleartext framing, without a historical decipherment or matching archive key, and is classified as **ciphertext-only**. The supplied readable editions are outputs of the work, not externally discovered plaintext used to recover the key; no first-publication claim is made.

The system is a **homophonic substitution with word and letter-group signs, name codes, and provisional nulls**. The current CTTS snapshot contains **4,247 cipher elements in two documents**: R4808 has 1,045 elements in 16 transcription rows, R4811 has 3,202 in 54 rows. The 4,258 total selections include 11 punctuation or cleartext-region selections excluded from the cipher count. These are snapshot counts; previous geometry revisions had more overlapping selections.

The 64 cipher-sign classes comprise **39 letter assignments** (19 plaintext letters; maximum five homophones for a vowel, three for a consonant), **four word/letter-group assignments** (`ci`, `et`, `re`, `rr`), **ten provisional null classes** (173 occurrences), **nine bracketed assignments** (36 occurrences, including four apparent personal-name codes), and **two unmapped classes** (`s2`, four occurrences; `m2`, one). Thus there are eleven uncertain or unidentified classes, in addition to the unresolved h/s classification and provisional nulls. This is not a complete historical inventory of the nomenclator.

Excluding nulls, 4,033 of 4,074 occurrences have unbracketed assignments (98.99%). This measures assignment coverage only: mixed glyph classes and editorial restoration prevent equating it with meaningful or correct plaintext coverage. The coherence percentage remains unmeasured, and both editions remain partial.

## Key and evidence

- [visual_key.png](visual_key.png) and [visual_key.html](visual_key.html): regenerated from the current `key.txt`, transcription counts and actual CTTS glyph samples. The older local chart had stale counts and `y1 = h`; this chart follows the current `y1 = s` and explicitly flags the remaining h/s problem.
- [key.txt](key.txt): the supplied 16 October working key, preserved verbatim. Its `# - [tartaglia?]` line is a genuine name-code assignment and must not be discarded as a comment.
- `R4808_transcription.txt`, `R4811_transcription.txt`: sign labels only, not plaintext. `glyphs.json` connects each sign label to its source glyph and checksum. Full manuscript photographs remain outside Git.
- `counts.json`: measured inventory; `input_checksums.json`: checksums of the submitted inputs. `R*_cipher_tokens.txt` prefixes labels with `g:` so the repository’s counter does not omit the `#` sign as a comment.
- `build.py`: reproduces the counts, visual key and short check only. It asserts that the three-line excerpt matches the supplied Italian reading. `validation.tsv` contains only this excerpt.

The local 16 October work records CTTS transcription cleanup, duplicate and compound-sign review, comparison with earlier local seed assignments, and contextual reconstruction across the 54 lines of R4811, followed by application and further sign review on R4808. George Lasry confirms the workflow: CTTS was used to transcribe the cipher, then GPT-6 Astra solved it. The local review ledgers document the analysis and sign checks; exact initial run settings and a complete chronology are not reconstructed.

The earlier repository survey in [siena1421/NOTES.md](../siena1421/NOTES.md) documents unsuccessful attempts on this pair. It is prior project history, not a prior complete plaintext. The separately deciphered nos. 6 and 24 belong to a different cipher, with their own [siena1431 page](https://dbourdeau.github.io/cyphersolver/siena1431.html).

## Historical context — checked 17 October 2026

**Proposed window: circa 1409–1414; narrower working hypothesis: 1412–1414.** Neither is a recovered documentary date. The two texts need not belong to the same year.

**Internal evidence.** The second memorandum’s alphabetic heading spells *ad Tartaliam*. Its body then addresses `lo [#]`, a captain with his own company, infantry, baggage and seal, to whom 1,000 ducats are to be paid. This strongly supports `# = Tartaglia`; it is more than a guess based on the military setting. The supplied edition and key retain their uncertainty marks. Identifying that Tartaglia with a particular historical man is a separate step.

**Likely setting, not an established date.** Angelo da Lavello, known as Tartaglia, is a strong candidate. Treccani dates his death to 1421, while the detailed Condottieri di ventura chronology places his service with Ladislaus and his activity around Perugia and the Marche in the relevant period. If the identification is right, the underlying instructions predate his death; that does not independently date this physical copy, nor prove that both documents were written in the same year. Sources disagree on the month of his execution (Treccani: December; Condottieri: October), so no month is used as a dating anchor. [Treccani](https://www.treccani.it/enciclopedia/angelo-tartaglia/); [Condottieri di ventura](https://condottieridiventura.it/tartaglia/).

**Ladislaus is plausible.** The scholarly biography of Ladislaus records his acceptance of Perugia’s lordship on 19 June 1408, its confirmation in the 1412 peace, and his death on 6 August 1414. The Rodolfo III da Varano biography documents Rodolfo’s alliance with Ladislaus in 1405–1414, including a pact in December 1408. Together these support a Ladislaus-era interpretation, with circa 1412–1414 a working hypothesis, not a recovered date; the broader years around 1409–1414 cannot yet be excluded. No conclusion follows merely from the local folder name “Siena1421.” [Ladislaus, DBI](https://www.treccani.it/enciclopedia/ladislao-d-angio-durazzo-re-di-sicilia_(Dizionario-Biografico)/); [Rodolfo III, DBI](https://www.treccani.it/enciclopedia/bio-varano-rodolfo-iii-da_(Dizionario-Biografico)/).

**Other identifications need restraint.** “Messer Ludovico” may be Ludovico Migliorati of Fermo, but the chronology records conflict with Carlo Malatesta in 1412–1413 and a truce mediated by Rodolfo and Berardo da Varano. Mentioning Ludovico and the Malatesta together therefore does not establish that they were allies or fix the year. Francesco Gattola is a possible lead for Francisco Gactule: the DBI gives the variants Gattula and de Gactulis and connects the family with the royal court, but it does not identify this envoy or memorandum. Iacobo Spinelo and Names 1–3 remain unassigned. [Migliorati chronology](https://condottieridiventura.it/ludovico-migliorati/); [Francesco Gattola, DBI](https://www.treccani.it/enciclopedia/francesco-gattola_(Dizionario-Biografico)/).

**Limits of this check.** Focused searches for “Maccione de le Rose,” “Maccione delle Rose” and “Macchione delle Rose,” with Ladislaus and the named envoys, did not establish the camp’s location or locate these complete texts in a printed edition. This was a limited check, not an exhaustive search. The 4 May reference is an arrival deadline, not the date of the memorandum; 30 March is the letter’s day and month, not a year. The archive’s dating and provenance still need independent confirmation. No external historical passage was used to change the submitted decipherments.

## Remaining gaps

- Personal-name codes `fat`, `o+`, `ovo`, and historical identities/year — blocker: open-codes; the three code names have no securely established identities, and a shared key does not supply the date.
- `b1`, `3bar`, `Fom`, `y3`, `ta`, `s2`, `m2` and h/s fork variants — blocker: open-codes; uncertain or mixed glyph classes remain, particularly in R4808.
- The lacunae, subscription and doubtful words retained in both supplied editions — blocker: open-codes; contextual readings are preserved as editorial proposals rather than asserted key values.
- Null classes and compound/component segmentation — blocker: open-codes; the current working transcription still needs occurrence-level checking before a complete-reading claim.

## Escalation

This is publication of the contributor’s existing partial result, at his request, not a declaration that further cryptanalysis is exhausted.

- [x] siblings: the submitted pair shares the working key; the earlier collection survey and the distinct nos. 6/24 system were checked. No newly found sibling supplied the missing text.
- [x] clear-pages: both submitted page images were inspected; R4808 has original clear salutation/closing, R4811 has isolated clear-script passages. No interlinear or marginal decipherment is used.
- [n/a] known-keys: no new archive-key campaign undertaken for this submission; the earlier collection survey is cited for its tests, not claimed as a fresh exhaustive check.
- [x] print: limited named-person/place and exact-phrase searches described above; no complete printed plaintext established.
- [x] key-rebuild: the contributor’s 16 October reconstruction and sign-review records were consulted; current key and visual counts cross-checked. No unlogged new recovery is claimed.
- [x] retry: the selected 108-sign excerpt reapplied exactly and matched against the supplied edition; the rest remains the supplied partial edition, without a new full mechanical decode.

## Sources and credit

- George Lasry, supplied readings, translations, CTTS transcriptions and working key; submission requested 17 October 2026. Transcribed with CTTS, then solved by GPT-6 Astra, as confirmed by Lasry. Codex prepared the contribution, checked its inventory and excerpt, and added the explicitly qualified historical context.
- [DECODE R4808](https://de-crypt.org/decrypt-web/RecordsView/4808), ASSi Concistoro 2308 fasc. 2 no. 20; image `IMG_R4808_I27971_P.jpg`.
- [DECODE R4811](https://de-crypt.org/decrypt-web/RecordsView/4811), same collection no. 23; image `IMG_R4811_I27977_P.jpg`.
- [Earlier collection survey](../siena1421/NOTES.md), dated 24 September 2026 and subsequent updates. Historical sources are linked beside the claims above.

DECODE changes are queued locally as **Partially**, not sent by this PR. No exact year, sender identity or replacement text is asserted. The supplied readings take precedence over automated cleaning; their uncertainty conventions are preserved in the queued copies too.
