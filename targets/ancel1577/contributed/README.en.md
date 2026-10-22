# Ancel's cipher letters in BnF Colbert 398 (Oct–Dec 1577): reading of the passages left undeciphered

[日本語の README](README.md)

BnF, Cinq Cents de Colbert 398 holds letters of Jean de Vulcob (1575–76) and Guillaume Ancel (1576–78, 1584), French residents at the Imperial court. Most cipher passages carry a contemporary decipherment in the left margin. This repository reads the passages that have none (p.525–526, p.539, p.561–563, p.565) with Satoshi Tomokiyo's reconstructed key "Vulcob and Ancel's Cipher (1575-1584)".

- **Status: full reading.** The cipher of p.525–526, 539 and 561–565 (123 lines, 4,357 symbols, not counting the cipher fragment at the end of p.524) is read through and most of it reads as words ([docs/READING.en.md](docs/READING.en.md)). On these seven pages: control 0/1,000; lowest independent agreement 88.8% (95.2% over the seven pages); calibration 85.9%; 97.4% of symbols have a value. Most code words (plain-letter groups inside the cipher) are unexplained, and some look-alike symbol pairs are decided by context ([docs/OPEN.en.md](docs/OPEN.en.md)). The single line on p.570 turned out to have a contemporary decipherment in the last margin line of p.569 ("… quil ny reussiroit(?) peu ou point de proffit"), so it was not undeciphered; the key output ("…[ss]iroit peu ou point de profit") agrees with it.
- **Relation to prior work:** the key is Tomokiyo's reconstruction; he writes that it "will allow reading undeciphered letters" ([Cryptiana, French Ciphers for German (and Eastern) Affairs](https://cryptiana.web.fc2.com/code/frencheastern.htm)) but publishes no readings. George Lasry compared a key in this volume when he deciphered the 1573 letter to Vulcob (BnF fr.3318; [Cryptiana GL.htm](https://cryptiana.web.fc2.com/code/GL.htm)). Damien Fontvieille's 2024 paper treats Vulcob's ciphered correspondence of the 1570s on the basis of the contemporary interlinear decipherments and does not overlap with Ancel's 1577 passages read here (according to the conference report). A reader who took no part in the decipherment searched with the aim of showing these passages had already been read; as of 20 Oct 2026 no decipherment of them was found in the places searched ([docs/PRIOR_CHECK.en.md](docs/PRIOR_CHECK.en.md)). Some places could not be checked, so we do not claim to be first.
- **No human has checked the transcription.** Transcription, cross-checking and reading are by AI (Claude and OpenAI Codex) and have not been checked by a person against the manuscript. Agreement between AI systems is not a substitute for a human check.
- **Numbers** (sources in [docs/METHOD.en.md](docs/METHOD.en.md)):
  - Independent second transcription: after the transcription was fixed, OpenAI Codex read the line images three times in new contexts, without seeing it (given only the images and the list of symbol names). Agreement by value on the seven read pages: 95.8%, 96.1%, 95.2%; lowest page 88.8% (p.565) to 97.7%. By symbol name, lowest page 87.0%.
  - Control: 1,000 keys with shuffled letter values; none scores as well as the real key on any of the seven read pages.
  - Calibration: two pages with a contemporary decipherment in the margin (p.258, p.285; chosen before any result was seen) were processed with the same procedure without the margin being seen; letter agreement with the margins 85.9% (546 letters; long gaps such as code-word positions not scored). The reference margin is the word-level majority of five independent readings (Codex 3 runs, Claude Sonnet 2 readers; none saw the cipher or the decode). Against a single image-adjudicated margin reading the figure was 81.8% (560 letters): the reference itself varies.
  - 97.4% of symbols have a value, 0.4% are unreadable, 2.2% are plain-letter groups.
- **AI use:** prior-work search, key table, transcription, decoding, scripts and documents by Anthropic's Claude (Claude Opus 5.5 and Claude Sonnet 5.5). Cross-check and independent transcriptions by OpenAI Codex (codex-cli 0.163.0-alpha.10.2, default model). Choice of target, direction of the work and the decision to publish by a human.

## Content (summary; includes inference)
- **22 October 1577 (p.523–526):** Archduke Matthias's departure for the Low Countries. Malstet, envoy of the States, had asked the Emperor for Matthias "not as governor but as lord". The cipher gives Ancel's view that the Emperor (code word *saturnus*) will deny any part in it, and why: the young archduke could not take a step out of his room without his brother's leave, could not have left the castle that is shut at night, and had no one to rely on.
- **2 November 1577 (p.539):** the Emperor does all he can to persuade the Spaniards that the departure happened without his knowledge.
- **14 December 1577 (p.561–563):** the Marquis of Varambon, sent by Don John of Austria to obtain leave to levy troops in Germany, has waited more than three weeks for an answer; the Spanish envoy Borgia says that if the Emperor supports his brother he must do it in earnest, as the Catholic King will do everything to keep his right; the Emperor gives the Spaniards fair words but secretly does things against them; the Estates of the Empire will hardly grant extraordinary aid.
- **21 December 1577 (p.565):** Varambon is back from Archduke Charles's court and has obtained nothing; the Emperor waits for the answer of the King of Spain (code word *Juno*, checked against the contemporary decipherment on p.440) to what he wrote after Matthias's departure.

## What this work adds
1. Identification of the passages without a contemporary decipherment (all pages listed by Tomokiyo were viewed; docs/METHOD.en.md).
2. A line-by-line transcription of those passages in symbol names (`data/transcription/`).
3. Additions and checks to the key: uu, ff, nn; the flat L-like sign = g; a lone c = null; etc. (docs/OPEN.en.md section 1).
4. The reading, controls, calibration (p.258, p.285) and an independent second transcription by another AI.

## Layout
| path | content |
|---|---|
| docs/READING*.md | key output and reading per line |
| docs/METHOD*.md | method, numbers, AI use, limits |
| docs/OPEN*.md | open points (symbols, code words, unread passages) |
| docs/PRIOR_CHECK*.md | prior-work check |
| data/key.tsv | key table (Tomokiyo's table in symbol names) |
| data/transcription/ | final transcription (`<page>.txt`), first pass (`<page>_first.txt`), after the first adjudication (`intermediate/`) |
| data/decoded/ | key output |
| second/ | Codex transcriptions (pass1, pass2, pass3a–c = cross-checks used for correction; pass4a–c = independent) and the prompts |
| xcheck/ | image adjudication records (two rounds), comparison with the independent pass, control table |
| calib/ | calibration (p.258 and p.285 transcriptions, margin readings, key output) |
| src/ | key and control (vk.py), comparison (xcompare.py, namecompare.py, vote.py, mvote.py), code words (codewords.py), line re-cutting (recut.py), calibration (calib.py), line cutting (lines.py, tiles.py) |
| tests/ | `python3 -m unittest discover -s tests` |

No images are included. Sources are cited by shelfmark and Gallica view number in SOURCES.md.

## Change log
- 2026-10-20: first version.
- 2026-10-20: the calibration reference (margin reading) replaced by the majority of five independent readings (method fixed before the result was seen): calibration 81.8% → 85.9%. Decode and scoring unchanged. Status changed to full reading.
- 2026-10-20: the single line on p.570 found to have a contemporary decipherment in the last margin line of p.569 and removed from the undeciphered passages (the key output agrees with it). Code-word meanings checked against the margins of the two calibration pages (saturnus = l'empereur etc., OPEN section 3).
- 2026-10-20: code word Juno checked against the contemporary decipherment on p.440 (three independent readings of the margin agree on "le Roy d'Espaig[ne] … avoit … voulu"; OPEN section 3).
- 2026-10-20: code word my (qu'il) checked against the margin of p.321; totum (l'Empire?) and others added to OPEN.
