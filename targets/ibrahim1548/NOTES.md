# Sigismund August, Frater Georg and Queen Isabella to Ibrahim Pasha, 1548 (catalogue 885)

Status: in progress. Images fetched, Latin exemplars of two letters transcribed, cipher not yet transcribed or decoded.

HHStA Wien, StAbt Türkei I 7-4-4 (AIS 7040827, f. 28-30, 5 images), 7-4-5 (AIS 7040824, f. 31-34, 6 images), 7-4-9
(AIS 7040845, f. 51-59, 11 images). Copies of letters to Ibrahim Pasha ("Hebrai Bassa") that Malvezzi sent to
Ferdinand I in the summer of 1548. Each cipher copy is filed with a clear Latin exemplar, so the plaintext is in hand.

## Access (corrects the first report)

AIS marks the records "Kein Zugang (Reservatbestand)", but the digital copy downloads to any client that keeps the
session cookie from `detail.aspx`: `fetch_images.py` (one request at a time; `width=2400` returns the full scan; the
JPEG is labelled text/html). `bildansicht.aspx` looks empty without that session. All 22 images fetched 30 Oct 2026
(not committed). PR #196 reported these as unreachable; they are not.

## What is on the images

- **7-4-4** (Sigismund August to Ibrahim Pasha, Cracow, 1 June 1548): image 1 (f. 28) and image 3 (f. 29, headed A,
  "Dupl. 1548") are cipher, image 2 is a scribbled-out verso, image 4 (f. 30) is the **Latin exemplar**
  (`texts/exemplar_7-4-4_A.txt`), image 5 a docket verso.
- **7-4-5** (Frater Georg to Ibrahim Pasha, Vinea, 2 July 1548): images 1-3 are cipher copies (B and C among them),
  image 5 carries two **Latin exemplars**, C ("Aliud exemplum", `texts/exemplar_7-4-5_C.txt`) and B (not yet
  transcribed), image 6 their continuation.
- **7-4-9** (Malvezzi to Ferdinand I, covering letter with enclosed cipher copies): images 1-5 and 10-11 landscape,
  6-9 portrait; not looked at beyond a contact sheet.

## The system (first look)

The signs on 7-4-4 f. 29 are the signs of the Ferdinand-Malvezzi key of 1548 (`../malvezzi1548/KEY_BRIEF.md`, DECODE
R367/R386): the first line begins with the Latin-letter words *Idcirco*, *b.*, *d.*, which are three of that key's
nulls, and the graphic signs (hash, pi, crossed circles, breve and bar forms) are the same. Same key family, to be
tested. The Latin exemplar of 7-4-4 is about 560 letters; the cipher on f. 29 is 13 lines of about 45 signs, the same
order of magnitude, so f. 29 may encipher exactly this text (with nulls). Not yet tested.

## Remaining gaps

- transcription of the cipher on f. 28 and f. 29 (7-4-4), f. 31-33 (7-4-5) and the enclosures of 7-4-9 - blocker: open-codes; nothing is blocked from outside, the work has not been done

## Escalation

- [x] siblings: malvezzi1548 (R366, R367, R386) is the same key family; its brief is the starting key
- [ ] clear-pages: the Latin exemplars on f. 30 and f. 34 are the plaintext; 7-4-9 not yet read
- [ ] known-keys: apply R367 unchanged to a transcribed line, then extend by alignment on the exemplar
- [ ] print: Austro-Turcica 1541-1552 (pp. 276-278) not seen
- [ ] key-rebuild
- [ ] retry

## Next steps

1. Transcribe the cipher of 7-4-4 f. 29 sign by sign from the 2400-px image (13 lines), using the R367 labels.
2. Decode with the R367 alphabet and align the result on `texts/exemplar_7-4-4_A.txt`; the exemplar settles doubtful signs.
3. Repeat for f. 28, then 7-4-5 (B and C against the two exemplars), then the 7-4-9 enclosures.
4. Credit Harrison Bornstein (PR #196) for the lead to the Malvezzi key.
