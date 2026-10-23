# Scipion de Fiesque, Vienna, to Catherine de' Medici and Charles IX, Oct 1567 – Nov 1569 (BnF fr. 15919)

Status: in progress (22 Oct 2026). Contributed reading (issue #52, Harumi-Matsuba), checked here; all 23 letters re-read into sentences 22 Oct, read in part.
View 23 left, the second cipher page of the 15 Nov 1567 letter, is not transcribed, and the doubtful stretches and
code words are workable, not blocked (see Remaining gaps).

22 Oct 2026, re-read (REREAD_BRIEF, batch b02, Claude Opus 5.5): **all 23 letters now read as French sentences and
are translated** (`read/<doc>_reading.md`, `_en.md`, `_reread_log.md`; 4 grade A, 19 B). Four follow contemporary
decipherments found in the volume: view 23 right (15 Nov 1567, now read to the end, covering the untranscribed cipher of
view 23 left) and the left margins of views 65 right (4 Jun 1568, not recorded before), 103 right (21 Aug 1568) and
125 right (6 Nov 1568); view 37 right's margin deciphers its two cipher lines. The other 19 are built word by word from
the key decode, reading through the known sign confusions, with image checks on views 6, 37, 109 and 159. Found: the
"Oct 1567?" letter is dated 11 Oct 1567 on its docket and begins with an untranscribed cipher page on view 6 right; the
4 Sep 1568 letter docketed "au Roy" addresses "Madame" in its cipher. Sign values suggested by the readings (not
entered in key.tsv): a lone ϖ is the code for l'Empereur (margins of views 65 and 103) or le Roy; 16 fits "vostre" in
the 1569 letters to the King; H# = ss in ambassadeur/commissaires/asseurer; =ii stands for a person (King of Spain;
once the Landgrave). fraction_read about 0.97 (estimated: view 6 right unread). Holes remain (Remaining gaps).

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): **read**: f. 79r and f. 94r
only, in the contributed `READING.en.md` (continuous French with scattered holes; the first pages of the 17 Jul and
14 Aug 1568 letters). **Decoded, not read**: the other 21 letters and the rest of those two. The 44 `decoded_*.txt` are
unspaced mechanical output (0-17% of sentences clean, `docs/_check_reading.py`); the line readings of ff. 39r-v, 100r and
158r have "…" holes in most lines. 99.7% (signs with a value) is withdrawn as a reading figure; about 5.6% of the signs
read (estimated, 1,669 of 29,707).

**Outcome: read with known key, read in part; contributed.** Satoshi Tomokiyo's reconstructed key for this volume
(Cryptiana, "French Ciphers for German (and Eastern) Affairs", frencheastern.htm) applied by Harumi-Matsuba to an
AI-made transcription of all 44 cipher pages (822 lines, 29,707 signs). All of their transcription, decoding and
checking was done by AI models (Anthropic Claude for the first transcription and decipherment; OpenAI Codex and
Claude Sonnet for the second transcription and image checks). **No human checked the transcription.** Their "full
reading" means 85.0–93.6% value agreement between two AI transcriptions plus a shuffled-key control, not this
project's read bar (README Conventions: 95% of tokens read as sense, measured). Here: 29,627 of 29,707 signs
(99.7%) take a value; 81.0% of the decoded letters fall in French words (lexical screen, `measure.py`); one letter
calibrated against the contemporary decipherment on view 23 right: 83.8% of its letters agree (`calib.py`).

## The documents

- BnF Français 15919 (formerly Harlay 238 (8)), 174 folios: letters of Scipion de Fiesque (Scipione Fiesco), French
  envoy at the court of Emperor Maximilian II, to Charles IX and the Queen Mother, October 1567 – November 1569,
  during the negotiation of the King's marriage with Elisabeth of Austria. Gallica ark:/12148/btv1b90573568 (183
  views, each a double-page opening of microfilm MF 15717). Catalogue: https://archivesetmanuscrits.bnf.fr/ark:/12148/cc46124x
- 23 letters with cipher, 44 pages; per page view numbers, figures and summaries in `contributed/docs/PAGES.en.md`;
  grouped by letter in `profile.json` documents. Letters to the King: 15 Feb 1568, 4 Sep 1568 (ff. 100–101), 10 Sep
  1569, 20 Oct 1569, 29 Oct 1569 (f. 158); the rest to the Queen Mother. One from Speyer (2 Dec 1568).
- Clear text surrounds the cipher: openings ("Madame, j'ay receu vostre lettre…") and closings are in clear.
- No DECODE record for this volume (contributor searched DECODE fields for 15919, Fiesque, Fiesco, Harlay).

## The key

Tomokiyo's reconstructed table (one table for the whole volume; one key, so one entry). The contributor gave its
signs names (`contributed/data/key.tsv`, 95 entries: 72 `table`, 23 `inferred`): two to five homophones per letter,
doubled-letter signs (ee, ff, ll, mm, nn, rr, ss, ii), 12 word codes (=22 que, =23 qu'il/quel, =10 et, =18 vous,
=inf le Roy, Φ Saxe …) and 20 named null groups. Values inferred from context: 16 = ce, ꝭs = t, ρ = e, ꝑꝑ = ff.

## What Harumi-Matsuba did (issue #52, 20 Oct 2026)

Repository https://github.com/Harumi-Matsuba/fiesque1567-public (CC BY 4.0 data, MIT code), copied at commit
659e2e1 into `contributed/` (see `contributed/ATTRIBUTION.md`). First transcription by Claude from line crops of the
full-size BnF IIIF images; three Codex runs and Sonnet image checks used to correct it (only where both readers
agreed); independent Codex second transcriptions afterwards: 85.0–93.6% value agreement per page (lowest run);
control 0/1000 shuffled keys per page; positive control on an enciphered La Ferrière letter. Line-by-line
conjectural readings of five letters in `contributed/docs/READING.en.md` (most lines marked "inf."); mechanical
decodes of all 44 pages in `contributed/data/decoded_*.txt`. They did not calibrate on view 23 right ("AI reading of
the cursive is unreliable", their OPEN §7: 51–55% when read by Sonnet/Codex).

## What was checked here (21 Oct 2026, Claude Opus 5.5)

1. **Re-measure** (`measure.py` → `measure.txt`). The contributed key re-applied to every transcription by our own
   decoder. 29,707 signs, 29,627 with a value (99.7%). Shared model `fr-1530-despatches` (order 5, no spaces): true key
   −2.37 to −3.42 per character; best of 200 shuffled keys per page −4.38 to −5.31; 0 of 8,800 shuffled keys reach the
   true key. Clean French scores −1.64 on the same model, so the decodes are far from noise but well short of clean
   text. Lexical screen (DP segmentation into words of a lexicon from fr-henri4 + fr-1520s-diplomatic): 81.0% of
   decoded letters covered, against 27.6% for shuffled keys and 90.3% for clean French; per page 68% (view 8 left) to
   90% (view 155 right).
2. **Calibration** (`calib_v023r.txt`, `calib.py` → `calib.txt`). View 23 right ("deschiffré de la precedente", f. 19r)
   is the contemporary decipherment of the 15 Nov 1567 letter. Read here by eye from a 2,600-px IIIF crop as far as
   the end of view 22 right's cipher ("une diette"), 1,193 letters. The contributed decode of view 22 right matches
   1,000 of them (83.8%; 86.6% of the decode's letters); 98 of 182 words of three or more letters come out intact. The
   sense agrees throughout (Lignerolles's departure, levies in Germany for the Huguenots, the Emperor's mandates,
   Chantonnay, the diet). Two content differences: where the decipherment has "au pays du duc de Wirtemberg et du
   conte palatin", the decode has "du duc de SAXE et du[n]…" (the Φ code read as Saxe; palatin missing); and "lo
   sarteiment" for "le partement" (the s/p y-shape). My reading of the cursive is itself unchecked by a human.
3. **Spot check on the images** (views 22, 23, 99 from openapi.bnf.fr IIIF at 3,200 px). View 22 right line c01: 40
   signs on the image, 40 in the transcription, each consistent with the contributed sign names (e.g. Φ, ⊣, the
   lr ligature as b, △ as tri); line c03: 26 of 26 signs at its start consistent, one place near its end (between
   fu and ptil) not confirmed at this resolution. No clear disagreement found in about 80 signs.
4. **Found: view 23 left is not transcribed.** The 15 Nov 1567 letter continues in cipher on view 23 left (f. 18v,
   about 17 lines, perhaps 600 signs); the decipherment on view 23 right continues past "une diette" ("de son pays
   d'Austriche … Fiesque") with its text. The contributed page list has no v023l. Other untranscribed pages may
   exist (the contributor scanned the 183 views at reduced size).

## Prior work

- Tomokiyo published the key and wrote that it "will allow reading undeciphered portions"; no reading of the
  passages in Cryptiana.
- The contributor's adversarial prior-work check (`contributed/docs/PRIOR_CHECK.en.md`, 20 Oct 2026): this ledger,
  NoAutopilot/cipher-lab, pangoleen/cipher-readings, Cryptiana, DECODE, OpenAlex, Persée, BnF SRU, GitHub, La Ferrière's
  *Lettres de Catherine de Médicis* iii (prints Catherine's replies, not Fiesque's cipher): nothing found. Not
  checked: Patrouch, *Queen's Apprentice* (2010), BnF fr. 17020 ff. 227–228.
- The volume itself holds the contemporary decipherment of the 15 Nov 1567 letter (view 23 right), and the margins of
  views 103 right and 125 right may hold more (contributor's OPEN §7; not read here).

## Files

- `contributed/` — the contributor's key, transcriptions, decodes, figures and documents, unchanged (CC BY 4.0 / MIT).
- `measure.py`, `measure.txt` — project re-measure (LM, shuffled keys, lexical coverage).
- `calib_v023r.txt`, `calib.py`, `calib.txt` — calibration against the contemporary decipherment.
- `profile.json`. Images are not kept; crops for the site are `docs/fiesque1567_*.jpg`.

## Remaining gaps
- View 6 right, the first cipher page of the 11 Oct 1567 letter (about 22 lines, about 800 signs) - blocker: not-attempted; not in the contributed transcription, image good
- View 23 left cipher (15 Nov 1567) - blocker: not-attempted; read through the contemporary decipherment on view 23 right; one cramped decipherment line ("gens de Flandres ... Chantonnay") would be closed by transcribing and decoding the cipher
- Phrase-level holes in f. 79v and f. 80 (17 Jul 1568), f. 100r c17-c27 (4 Sep 1568), v150l c17-c23 (10 Sep 1569), v038l c03-c04 and c17-c18, f. 39r c22-c29, single words elsewhere (read/<doc>_reread_log.md) - blocker: not-attempted; AI-only transcription, workable by sign-level crops and re-decoding
- Lone signs standing as codes, values not settled: ϖ (l'Empereur or le Roy), =ii, Dz, mm, pp, the arrow, "lele"; 16 = ce or vostre - blocker: open-codes; not in Tomokiyo's table, read from context; key.tsv unchanged

## Escalation
- [x] siblings: all 183 views were looked through by the contributor; here views 22, 23 and 99 opened, and view 23 left found untranscribed
- [x] clear-pages: view 23 right is the contemporary decipherment of views 22 right and 23 left (read in full 22 Oct); the margins of views 65, 103 and 125 right decipher those letters, view 37 right's its two lines (read 22 Oct); no other cipher view has a margin decipherment (contact sheet of all 34)
- [x] known-keys: Tomokiyo's reconstructed table for this volume is the key; no other key of Fiesque's embassy is known
- [x] print: La Ferrière, Lettres de Catherine de Médicis iii (Catherine's replies only), Cryptiana, DECODE and the contributor's prior-work list; nothing printed of Fiesque's cipher
- [x] key-rebuild: contributor inferred 23 values from context; the calibration shows one code (Φ) mis-valued in one place
- [x] retry: the whole volume decoded again here with the contributed key and scored (measure.py); 22 Oct every letter built into sentences from the decode, with image checks on views 6, 37, 109, 159; sign-level re-transcription of the remaining holes still to do
