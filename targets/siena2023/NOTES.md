# Siena 20 and 23 — DECODE R4808 and R4811

Status: **read; key recovered from ciphertext-only** by George Lasry with CTTS and Claude, 15-17 Oct 2026 (his
consolidated report of 17 Oct 2026: "both sheets read in full (c. 4,260 symbols, one key with nomenclator)"). Seven
name signs and the subscription of no. 20 stay open. Updated 18 Oct 2026 from "read in part" to the report's statement;
the PR #41 material below (17-18 Oct, "transcribed with CTTS, then solved by GPT-6 Astra") is kept as filed.

## George Lasry's report (17 Oct 2026)

`lasry_report.md` holds the report's whole section on nos. 20 and 23 (pp. 4-9: status, references, ciphertext, key,
sample decryption, contents, dating, open points, sources, the full decryption and translation) and its contents
line, verbatim; `key_lasry.jpg` is the report's key figure (signs cut from the manuscript, with occurrence counts).
What it says that differs from or adds to PR #41:

- **Credit and method.** "15-17 October 2026, by George Lasry with CTTS and Claude: no. 23 transcribed by the author in
  CTTS, no. 20 by a detector trained on no. 20 with Lasry's ResNet model and corrected by the author in CTTS; key
  recovered by Claude via crib testing and dragging, refined by the author with CTTS." PR #41 said "transcribed with
  CTTS, then solved by GPT-6 Astra". The profile, the page and the ledgers now follow the report.
- **Extent.** "Solved: both sheets read in full". PR #41 had "read in part" (98.94% key coverage, seven name codes
  and editorial gaps). The report's own open points are the same kind: the name signs [Name3], [Name4], [Name5] and
  "?" (PR #41's `e` = [Name6?]), the place [Eucebio?], the stretch "dessut" and the subscription of no. 20;
  [Paolo Orsini?], [Sforza?] and [Tartaglia?] remain hypotheses. Under the read bar this is "read" with scattered
  name codes open.
- **Key.** 60 distinct signs (PR #41: 59 observed classes): four signs for a and i, three for e, o, u, two each for g,
  l, s, one for every other consonant; single signs for ci, et, ff, qu, re, rr, ss (PR #41: CI, ET, FF, RE, RR, SS, no `qu`
  class); eleven nulls; a nomenclator of seven name signs.
- **Dates and people, now stated.** No. 20: Perugia, 30 March 1413, a captain in the king's pay, "most probably Muzio
  Attendolo Sforza", to King Ladislaus. No. 23: King Ladislaus's chancery, two memoranda, to Iacobo Spinello (to the
  Marche) and Francesco Gattola of Naples (to Tartaglia), mid-April 1413. PR #41 proposed the same year as a hypothesis.
- **Reading differences.** The report renders PR #41's `[Name6?]` as "?"; otherwise the two editions agree in the
  passages compared (both "ante terre pedum oscula"; the siena1421 survey of 24 Sept had misread "post"). George's
  readings are not re-edited here.
- Sibling: no. 12 (R4790, Naples, 10 March 1413, to Sforza) is the same spring and circle but a different key (report
  heading B); its own entry is [`targets/siena12/`](../siena12/NOTES.md).

## Questions for George

1. PR #41 (17-18 Oct) credits "transcribed with CTTS, then solved by GPT-6 Astra"; your report of 17 Oct credits
   Claude ("key recovered by Claude via crib testing and dragging") and a ResNet detector for no. 20. Did both models
   work on it (Astra first, Claude later, or the reverse)? Which Claude model? The profile now lists Claude as the
   solver and keeps Astra as "named in PR #41 only".
2. The report says "read in full"; PR #41 called the same edition partial. We now record it as read (key recovered,
   seven name signs open). Agreed?
3. The report counts 60 signs, PR #41's snapshot 59 classes (plus an unused `n`). Is the 60th the `qu` sign?

## Editions and summary

| Document | Readable Italian | English | Date and proposed correspondents |
|---|---|---|---|
| No. 23 / R4811 / Letter 1 | [Reading](R4811_reading.txt) | [Translation](R4811_translation.txt) | Two royal memoranda, probably Ladislaus’s orders; Iacobo Spinelo and Francisco Gactule named. Before the 4 May deadline; spring 1413 proposed. |
| No. 20 / R4808 / Letter 2 | [Reading](R4808_reading.txt) | [Translation](R4808_translation.txt) | Perugia, 30 March, year absent; Muzio Attendolo Sforza to Ladislaus proposed. |

[Summary and historical background](SUMMARY.html) · [Visual key](visual_key.html) · [Working key](key.txt) · [Five-line mechanical excerpt](excerpt.txt).

The readings follow the current `edited/4808_edits.txt` and `edited/4811_edits.txt`, copied as `R4808_edited_lines.txt` and `R4811_edited_lines.txt`. Only physical line-break hyphens are joined and paragraphs added; all current words, uncertainty brackets and CLEAR1–CLEAR4 passages are retained. These are edited readable texts, not a newly generated complete mechanical decoding. English translations have been revised to follow these readings. Source inputs and publication inputs have SHA-256 manifests. No source-project file was changed in preparing this contribution.

The latest reading has **docento cavali (two hundred horses)**, **Ecclesia**, **però che**, and the unresolved **[Eucebio?]**. `fat = [Paolo Orsini?]` and `o+ = [Sforza?]` remain hypotheses. `e` appears eight times and is retained as `[Name6?]`, a person-reference or possibly pronoun, not silently deleted. `# = [Tartaglia?]` is tentative despite the certain alphabetic heading *ad Tartaliam*. In the English version the unresolved `dessut` clause is explicitly marked; its syntax is not claimed resolved. The phrase *rompere a la scorta* permits more than one interpretation.

## Cryptanalysis

The key was recovered from ciphertext patterns and original cleartext framing; no interlinear/marginal decipherment or matching archive key was used. Later historical sources propose identities and a date; they did not supply the alphabet or a plaintext copy. Original clear-script passages are transcribed as CLEAR1–CLEAR4 and must not be confused with a decipherment of the encrypted lines.

The system is **graphical homophonic substitution with letter groups, one common-word sign, a small nomenclator of names/references, and provisional nulls**. The current transcription has **4,254 ciphertext elements in two documents**: R4808 1,045 in 16 rows, R4811 3,209 in 54 rows. Eleven of 4,265 selections are punctuation or clear-script blocks and are excluded. There are **59 observed classes**: 34 single-letter signs, six multi-letter signs (CI, ET, FF, RE, RR, SS), seven unresolved/proposed name-reference signs, eleven provisional null classes (188 occurrences), and one erased class (two occurrences). An unused `n = ?` mapping is retained in the working key, but not counted as an observed class.

The alphabet has 19 values, with up to four homophones for A/I, three for E/O and U/V, and two for other consonants. The seven reference signs have 41 occurrences: `#` 9, `fat` 8, `o+` 7, `ovo` 7, `Fom` 1, `ta` 1, `e` 8. Three have tentative historical names; four remain placeholders. Thus all seven remain unresolved at the identity level. Assignment coverage excludes hypotheses, erasures and provisional nulls: **4,023 / 4,066 = 98.94%**. This is not a percentage of coherent prose or a claim of full decipherment.

## Mechanical verification — exactly five lines

Only **R4811 CTTS physical lines 6–10** are mechanically decoded. The 322 selected signs produce 328 literal letters after omission of provisional nulls. V represents u/v. There are no letter substitutions, inserted letters, spelling corrections or filled gaps. Physical boundaries split *personalmente* at the start and *Tronto* at the end. The joined output is an exact substring of the normalized current readable edition.

`build.py` regenerates counts, token counting files, the visual key, the five-line excerpt, its token alignment, and the reveal data. `validation.tsv` contains this excerpt only. Any language-model test applies only to these deliberately selected five lines, not both full editions or all key assignments.

## Historical research

<p><strong>Two documents, one cipher; proposed spring 1413 setting.</strong> Siena Concistoro 2308, fasc. 2, no. 20 (DECODE R4808) is a captain’s complaint addressed to a king from Perugia on 30 March, without a written year. No. 23 (R4811) contains two royal memoranda for Iacobo Spinelo and Francisco Gactule. Its 4 May date is an arrival deadline, not an issue date. The best current historical hypothesis is Ladislaus of Naples’s campaign of spring 1413, with the memoranda probably written before 4 May. The year and correspondents remain inferred.</p>
<p><strong>Contents.</strong> The letter’s writer says an enemy has taken fully 200 horses and threatens retaliation despite the risk of royal punishment, while promising not to harm the Church’s lands, people or livestock. The first memorandum coordinates the guarding of passes near Ascoli, the Tronto, Arquata and Montemonaco to contain a hostile captain in the Marche, with intelligence gathering and limited, secret cooperation with the Malatesta. It also orders the recovery of castles using 140 lances. The second arranges a royal muster at “Maccione de le Rose”, a payment of 1,000 ducats, and a promise under seal.</p>
<p><strong>Why 1413.</strong> The Fermo chronicle describes an unusually close parallel in April 1413: forces at Forca di Presta and Sforza’s troops around Caldarola and Sarnano were placed to prevent Paolo Orsini from leaving the Marche at the King of Naples’s request. Orsini’s departure and pursuit are recorded on 10 May. This supports the campaign setting and <code>fat = [Paolo Orsini?]</code>, but supplies no verbatim decipherment. [<a href="https://archive.org/stream/bub_gb_i1rhdgfMJrYC/bub_gb_i1rhdgfMJrYC_djvu.txt">Cronache della città di Fermo, printed pp. 39–40</a>]</p>
<p><strong>Probable participants.</strong> Minuti recounts Sforza’s grievance against Orsini, his service to Ladislaus, and his return to Perugia in February 1413 before pursuing Orsini in the Marche. This makes Muzio Attendolo Sforza a plausible writer of no. 20, although its subscription remains unread. Rodolfo is probably Rodolfo III da Varano; “messer Ludovico” probably Ludovico Migliorati. These contextual proposals do not replace the names actually recovered. [<a href="https://archive.org/stream/MiscellaneaDiStoriaItaliana7/Miscellanea_di_Storia_Italiana_7_djvu.txt">Minuti, Vita di Muzzo Attendolo Sforza, pp. 163–169</a>]</p>
<p><strong>Key comparison and dating safeguard.</strong> Meister’s printed Viviani nomenclator, dated 25 July 1412, has a circle-and-cross Sforza sign comparable to <code>o+</code>. This supports <code>[Sforza?]</code>; the Lucca alphabets differ, so they are not the recovered key. Meister’s 1421 date belongs explicitly to Siena piece no. 1, not nos. 20 or 23. The local “Siena1421” name therefore cannot date this pair. [<a href="https://nbn-resolving.org/urn:nbn:de:hbz:6:1-143638">Meister, Die Anfänge der modernen diplomatischen Geheimschrift (1902), pp. 51, 55–57</a>]</p>
<p><strong>Place and remaining limits.</strong> “Maccione de le Rose” probably denotes the Mazzone delle Rose muster ground. Later royal records independently attest a camp there, including near Ponte Annecchino in 1450; they support the place identification, not the date of these letters. [<a href="https://www.accademiapontaniana.it/wp-content/uploads/2018/03/REGISTRO-9.3.2018.pdf#page=278">I registri privilegiorum di Alfonso il Magnanimo, register 2905, nos. 11–16; register 2914, no. 27</a>]</p>
<p>The supplied research report surveys 44 key records, 43 with images, and reports no matching key; R4783 could not be inspected. It also reports no external copy of these plaintexts. These are bounded search results. The heading certainly names Tartaglia, but <code># = [Tartaglia?]</code> remains tentative: <code>#</code> and the repeated <code>e = [Name6?]</code> may name different people. Name3–Name6, the place [Eucebio?], one difficult clause and the subscription remain unresolved. No priority or “oldest deciphered cipher” claim is made.</p>

## Remaining gaps

- `#`, `fat`, `o+`, `ovo`, `Fom`, `ta`, `e` and historical identities/year — blocker: open-codes. Three name hypotheses remain tentative; Name3–Name6 have no secure identification, and `e` could be a pronoun. The proposed writer and 1413 date are historical inferences.
- Erased selections, `dessut`, `[essereme?]`, `[Eucebio?]`, `[prout?]`, the closing abbreviation and subscription — blocker: illegible. The current readable editions retain unresolved text and editorial restorations; five-line agreement does not settle these passages.
- Nulls, compound segmentation and editorial emendations — blocker: open-codes. Occurrence-level manuscript checks remain necessary; a nearly complete alphabetic assignment is not a completely verified reading.

## Escalation

This publishes the contributor’s current edited result; it does not declare further research exhausted.

- [x] siblings: the supplied report describes review of the 25 photographed fascicle pieces and finds no further document in this cipher. Nos. 6/24 are a different system.
- [x] clear-pages: original clear passages are retained as CLEAR1–CLEAR4. No interlinear or marginal decipherment was used.
- [x] known-keys: the supplied report surveys 44 records, 43 with images; R4783 remains unavailable. No matching key reported. Meister’s Lucca comparison was independently checked here and is a different key.
- [x] print: independently checked the Fermo and Minuti parallels, Meister’s inventory and 1412 nomenclator, and later Mazzone camp attestations. No exact external plaintext established.
- [x] key-rebuild: imported the current reviewed key and edited files; refreshed all glyph samples and counted the new classes. Source mappings were not altered for publication.
- [x] retry: reapplied the current key to exactly five physical lines and verified literal agreement with the current edition. The remaining editorial gaps are disclosed above.

## Earlier project attempt (siena1421 survey, 24 Sept 2026)

Before this contribution, nos. 20 and 23 were part of the bundle entry `targets/siena1421/` (catalogue 336), listed
as unread and "probably one system". That survey's transcriptions and solver inputs were moved here on 18 Oct 2026
under the one-key rule, unchanged, to `project_attempt/`:

- `no20.txt` / `no20.tok` (no. 20, R4808, agent C: 1,230 tokens, 51 sign names) and `no23a.txt`, `no23b.txt` /
  `no23.tok` (no. 23, R4811, two transcribers: 54 lines, 3,702 tokens); the other `.tok` files are solver variants
  (f-groups merged, superscripts as nulls, both letters pooled).
- What was tried: homophonic annealing (`homsolve.py`, `homsolve2.py`), null-aware (`homsolve3.py`) and bigram
  (`sylsolve.py`) solvers, Italian, Latin, Catalan and Spanish models, order 3-5; filed keys R4760, R4768 and R4778
  compared with no. 20. None converged (about -2.9/token against -1.74 on a synthetic control of the same size); the
  survey concluded the system was not plain letter substitution as transcribed. The solvers are in `research/siena2308/` (moved from `targets/siena1421/` on 18 Oct 2026).
- Nothing of that failed attempt is claimed in the reading above, which is George Lasry's, made from his own CTTS
  transcription.

## Sources and credit

George Lasry supplied the images, CTTS material and successive Italian readings, directed the work, and confirms: **transcribed with CTTS, then solved by GPT-6 Astra**. Codex prepared this contribution, revised the English translations to match the latest Italian edition, checked the five-line excerpt and selected historical sources, and regenerated the visual key.

- [DECODE R4808](https://de-crypt.org/decrypt-web/RecordsView/4808) and [R4811](https://de-crypt.org/decrypt-web/RecordsView/4811): Archivio di Stato di Siena, Concistoro 2308 fasc. 2 nos. 20 and 23.
- User-supplied research report: *Siena Concistoro 2308 keys and sources.md*, 17 October 2026 source snapshot. Its broad survey is attributed, not represented as independently repeated in full. Primary sources are linked in the historical section.
- [Earlier collection survey, now the collection index](../../research/siena2308/README.md), for the preceding attempts and other cipher systems.

DECODE updates are queued as **Partially**, not sent. No inferred year or sender is entered as established metadata. No oldest/first decipherment claim is made.
(18 Oct 2026: the queue now proposes **Decrypted** for both records, following the report's "read in full", with
the report cited; still not sent, and the year and writer are still not entered as DECODE fields.)
