# DECODE R1871 — Sebastiano Foscarini, Paris, 11 September 1680 (ASVe Busta 30, catalogue 264)

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026). This entry used to hold two unrelated
despatches; R1873 (Alvise Mocenigo, Rome, 25 April 1558) is a different cipher, read from Paolo Bonavoglia's
published decipherment, and now has its own entry ([`targets/r1873/`](../r1873/NOTES.md), page `r1873.html`).
This entry keeps R1871 only.

**Outcome: read from existing decipherment** (27 Oct 2026). Paolo Bonavoglia's decipherment of this despatch is back
online (`crittologia.eu/storia/SebFoscarini_Parigi16800911.html`, pointer from Brice Dudout's email of 27 Oct 2026) and
is saved in `r1871_bonavoglia.txt`. Nothing was deciphered here; the ciphertext-only attempt of 22 Sept 2026 (below)
failed. Earlier verdict (22 Sept): not solved, because his page was offline.

Catalogue 264 ("... (England?) to unknown recipient, 2 ciphertexts, 1555–1558") merged the two records. Neither is
from England. The "England?" region and the 1555 date come from DECODE's R1871 metadata, which seems to have been
copied from its neighbour R1872 (Giovanni Michiel, Brussels, 19 Mar 1555, also in Bonavoglia's list).

## The despatch

- Images `IMG_R1871_I8939`–`I8940` (2 PNG). f. 4 (not 1555): one page of continuous digit cipher under
  "Ser.mo Principe", marked "#117 P.S. Sola", signed "Sebastian Foscarini Amb.r", dated "Parigi li … 1680"; the
  dorse is addressed to the Doge with the docket "11 Sett. 1680 … n.o 117".
- Bonavoglia's list includes "1680-09-11: Dispaccio di ambasciatore Sebastiano Foscarini", the same despatch.
  He says the Foscarini cipher was used at both Paris and Madrid and was "troppo regolare e ordinato".
- His decipherment could not be retrieved: the interactive page returns HTTP 500 (22 Sep 2026), the Wayback snapshots
  show only the default (Mocenigo) despatch, and his dedicated page `storia/SebFoscarini_Parigi16800911.html`
  (indexed by search engines: "busta 171A, Senato, Dispacci Francia, entirely in cipher except salutation and
  signature") is 404 on www and connection-refused on web.crittologia.eu; not in the Wayback Machine or archive.today.

### Attempt here (22 Sep 2026): not read

- Transcribed the whole cipher page (23 lines, 1,839 digits; `tx.txt`, `r1871_digits.txt`) from deskewed line strips
  (`rot.png`, `lines/`), two agents, first pass (3/5 and 2/0 are the likely confusions; L22 middle weakest).
- System: **3-digit groups**. The rare digits 0, 7, 8, 9 occur only in the third place: within each line their
  positions are constant mod 3 over long stretches, and the phase jumps are transcription slips. `seg3.py` segments
  to 612 groups (593 of 3 digits; `groups.txt`, `runs.txt`): 211 distinct, first digit 1–5 (6 rare), second 1–6,
  third 0–9 → a table of about 300 codes (110–569). Top groups 156 ×22, 517 ×20, 256 ×19, 152 ×16, 459 ×15.
- Not an alphabetical (ordered) table: Sukhotin's vowel test puts vowel-like and consonant-like codes side by side
  (151/156 vowel-like, 152–154 consonant-like).
- Rejected splits: 2-digit pairs (gap parity random); self-delimiting [1-4]*[5-0] and [1-5]*[6-0] tokens (annealing
  gives no Italian).
- Solvers, all with a clean Italian 4-gram (`q4.npy`, `buildq4.py`: the shared it-cinquecento/it-modern models score
  "iiii…" above real text because the nunziature OCR has i-runs for m/n/u):
  monotone syllabary annealer (`msolve.py`, 12 seeds; recovers a synthetic ordered control only in part) → same
  non-Italian text every seed; free letter-per-code annealer (`anneal3.py`) → −2.15/char, not Italian; free
  letter/syllable annealer (`usolve.py`, 8 seeds) → fluent-looking but seed-dependent gibberish (overfit), or
  degenerate "mentemente…" at high bonus.
- Why it fails: 211 free code values against 612 groups is beyond the unicity distance of an Italian LM for a
  homophonic + syllabic table. It needs the key (ASVe *Cifre, chiavi e scontri*, not on DECODE: the only Venetian key
  records there, R1788–R1790, are 16th-century Pasini tables), more ciphertext in the same key (Foscarini's other Paris
  and Madrid despatches, 1680–84, ASVe Senato Dispacci Francia 171A and Spagna), or Bonavoglia's decipherment.

## The reading (Bonavoglia, retrieved 27 Oct 2026)

- Bonavoglia: original in ASVe Senato, Dispacci Francia, **filza 171A**, wholly in cipher except "Ser.mo Principe" and
  the signature; the doge's chancery decipherment is in **filza 166**. R1871 (Busta 30 f. 4) carries the same despatch
  (no. 117, "P.S. Sola", 11 Sept 1680).
- Content: a postscript written after the despatch was signed. Rumoured Spanish reinforcements in the Milanese; Louis XIV
  said to mean to raise the Pinerolo garrison to 6,000 men of the old regiments and spread 16,000 men over Dauphiné and
  Provence; the Duke of Mantua's illness, abbé Morel, a Spanish plan to push 5-6,000 men into Casale; munitions sent to
  Pinerolo by way of Savoy. Bonavoglia judges it a false alarm.
- 262 words (measured). His open items: "[Francesi?]269?", "114?", the closing "202.106.100".
- Not checked here: his ciphertext viewer (`venezia_nomenclatore.html?dispaccio=SFoscaParigi`) still returns HTTP 500,
  so his decipherment was not aligned group by group with `groups.txt`.
- Brice Dudout (27 Oct 2026) rebuilt the table, which Bonavoglia does not publish: **a syllabary in blocks of five
  consecutive codes, with the blocks out of order**. It matches Bonavoglia's text at 94.9% on held-out lines. This is
  why `msolve.py` (one monotone syllabary) could not converge. He suggests checking our transcription at L18-19 and
  L22 (L22 was already marked weakest).

## Remaining gaps

- None in the text: Bonavoglia's decipherment covers the despatch, apart from his own open items (three number groups).
- Not done here: the key (table) is not rebuilt, and his text is not aligned with our transcription. Next, if it is
  worth doing: ask Dudout for his block table and check `groups.txt` against it (L18-19, L22).

## Escalation

- [x] siblings: DECODE has no other Foscarini 1680s despatch (Busta 30 records R1869–R1875 checked); other
  despatches in the same key are in ASVe busta 171A, not digitised. R1873 (now `targets/r1873/`) is another cipher.
- [x] clear-pages: none on the record (clear salutation and signature only).
- [x] known-keys: DECODE's Venetian key records (R1788–R1790, 16th-century Pasini tables) do not match.
- [x] print: none found; Bonavoglia's page is the reading, online again and retrieved 27 Oct 2026. The viewer
  `venezia_nomenclatore.html?dispaccio=SFoscaParigi` still returns HTTP 500.
- [x] key-rebuild: done (above): monotone, free letter and letter/syllable annealers, no Italian.
- [n/a] retry: needs more ciphertext in the same key or the key itself before a rerun is worth it.

## Assumptions for George's review

- Outcome "read from existing decipherment" from 27 Oct 2026: Bonavoglia's text was retrieved and is the reading.
  It was listed before our attempt (contamination: found before attempt, but offline, so unused until 27 Oct).
  The project's failed ciphertext-only attempt stays in the steps.

## Steps

1. Fetched R1871/R1872/R1873 record pages and all 12 images with the shared DECODE cookie.
2. Viewed all pages: identified sender, place and date from the clear text, signature and dockets.
3. (R1873 only, now in `targets/r1873/`: CSP Venice vi grep.)
4. Followed Tomokiyo's note on R1872 to Bonavoglia's page; its archived copy holds only the R1873 decipherment
   and the list naming the Foscarini 11 Sep 1680 despatch.
5. Transcription, segmentation and the solver runs above (22 Sep 2026).
6. 14 Oct 2026: R1873 split off into its own entry (`targets/r1873/`).
7. 27 Oct 2026: Brice Dudout's email: Bonavoglia's page back online, filza 166 chancery decipherment, his own block
   table (94.9% on held-out lines). Retrieved Bonavoglia's decipherment (`r1871_bonavoglia.txt`); outcome changed to
   read from existing decipherment.
