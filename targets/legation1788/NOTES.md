# legation1788 — residual groups in Jefferson's legation codes Nos. 10, 13 and 16 (Short 1792, Carmichael 1788, T. Pinckney 1793)

Catalogue no. 484 (Founders Online sweep, `research/founders_emlo/`). Worked 26-27 Oct 2026 from the solve-page brief.
Sibling target: `jefferson1787` (Code No. 11, catalogue 483).

## What it is

Three letters to Thomas Jefferson as Secretary of State (or minister in Paris), each partly in a numerical code, each
printed in *The Papers of Thomas Jefferson* with a few groups left unread or read by conjecture:

| Letter | Code | Original | What was open |
|---|---|---|---|
| William Short → TJ, The Hague, 26 Jul 1792 ("Private") | No. 10 | LoC Jefferson Papers ser. 1, mtj1 016_0998-1009 (RC, TJ interlinear); extract re-enciphered in Short → TJ 27 Jul 1792, 016_1010-1012 | 401, 1083, 401 (note 21); 359, 199, 34, 724 (note 23) |
| William Carmichael → TJ, Madrid, 14 Apr 1788 | No. 13 (the code David Franks left with him, Nov 1786) | LoC mtj1 009_0223-0230 | five groups read by conjecture: [Maryland] x2, [Massachusetts], [majority], [you?] |
| Thomas Pinckney → TJ, London, 28 Aug 1793 | No. 16 | NARA RG 59, Despatches from US Ministers to Great Britain, M30 roll 2 frame 0140 | three sentences "deciphered in part"; "Undeciphered code 497"; [time?], [secret?], [Dunda]s |

The codes are two-part numerical codes of about 1,700-1,850 groups (words, syllables, letters), groups separated by
dots, numbers in no alphabetical order (checked for No. 10 on 016_1007-1008: 7 s, 12 pleny, 68 president, 153 al, 218 my,
224 the, 294 I, 426 to ... no run is ordered), so a group cannot be bracketed between its neighbours.

## Sources and files

- `transcription/short_17920726.tsv`: the open groups of Short's letter and their neighbours, both copies.
- `transcription/short_17920726_full.tsv`: every code group of the 26 Jul letter with TJ's interlinear (subagent).
- `transcription/code10_hunt.tsv`, `code10_checked.md`: the search of the other Code No. 10 letters for the six groups.
- `transcription/carmichael_17880414.tsv`: Carmichael's five code items.
- `transcription/pinckney_m30.tsv`, `pinckney_m30_frames.md`: every code group on M30 roll 2 frames 0101-0330 (15 coded
  frames, ~2,660 rows), with the interlinear decodings of 20 Jun, 25 Sep, 27 Nov, 17 Dec 1793, 28 Jan and Feb 1794 and
  the "Explication of the Cyphers" (0179) aligned to 25 Nov 1793.
- `reading_pinckney_17930828.tsv`: the 28 Aug 1793 passage group by group, graded against the attested values.
- `key.tsv` (`make_key.py`): values decoded at the time, per code. `make_profile.py` → `profile.json`, `ct/`, `texts/`.
- `dl_m30.py`: downloads M30 roll 2 frames from the NARA catalog media server (images git-ignored).

## Findings

### Pinckney, 28 Aug 1793 (Code No. 16)

The coded passage is on M30 roll 2 frame 0140 (right page; TJ's pencil "copy so far only" above it), 58 groups in five
lines; the leading digits of lines 2-5 are lost in the binding gutter. Values from Pinckney's decoded letters on the
same roll confirm the editors' frame word by word: 753 = i (reg-i-ments), 1490 1517 = to be, 709 = with, 323+ =
general-s, 856 = and, 800 = s, 513 525 = under him, 1228 ... 1181 = des-tina-tion, 885 = is, 323 675 175 = general-ly
thought, 1226 = for. Of 58 groups, 30 carry a value attested in another letter (H), 23 rest on the editors' reading
and fit (E), 4 are the editors' bracketed conjectures (C: 234 [time], 501 [secret], ?55 668 [Dunda-]), and 1 is open.

- **The open group is 447, not 497.** The image shows two matching open 4s (same form as the 4 of 1465 on the page).
  447 occurs nowhere else in the 15 coded Pinckney frames. Context: "447 regiments are to embark in a short [time] on a
  [secret] expedition"; a number or "several" is expected, but the code's number words seen elsewhere are 1244 = 6,
  531 = 8, 383 or 6?4 = nine, 1491 = six (approximate); none is 447.
- 234 [time?] and 501 [secret?] also occur only here. They stay conjectures.
- The 15 Aug 1793 letter (frames 0135-0136, ~1,020 groups, no interlinear) has an en clair State Department copy
  (Bankson's Tr, printed in PTJ 26), so it is not open; it does not contain 447, 234 or 501.

### Short, 26 Jul 1792 (Code No. 10)

- The passage: "if I had not counted enough on the justice of government to have **401** sure. There **1083** have
  **401** no of it if my conduct was satisfactory" and "say that the salary should not **359 199 34 724** allowing the
  president to fix each at what rate he pleases".
- Short's private letter of 27 Jul 1792 repeats the whole paragraph in cypher with the same groups and no decoding
  (and a struck 1312 687 after 757: he first wrote "salaries", then 757.427 "salary"). It confirms the digits only.
- "Been" is 1700 in this code (TJ's interlinear, this letter and three others), so 401 = been would need a homophone.
  401 carries a caret below it in both copies; the same caret marks 985 (= less), so the mark is not specific to 401.
- None of the six groups occurs in any other Code No. 10 letter checked (Founders notes of all 39 documents; page
  images of Short 26 Sep 1790, 27 Oct 1790, 11 and 13 Nov 1793, TJ to Carmichael & Short 31 May 1793, ~1,100 groups).
- Readings by context only, kept as conjectures: 401 [been?], 1083 [would?] ("to have [been] sure. There [would] have
  [been] no[ne?] of it"), 359 199 34 724 [four groups, e.g. "exceed a fixed sum"; not filled].

### Carmichael, 14 Apr 1788 (Code No. 13)

- Five items: 108 ("Had I been in 108 I should ... have been of the sentiment of Paca"), 108 again (blotted: "108 has not
  acceded to the Constitution"), 223 ("223 has"), 273 ("the 273 seem pleased with it"), 597 ("what says 597").
- Code No. 13 is not Code No. 11 read through a faulty copy: in the rebuilt Code No. 11 table (`jefferson1787/key.tsv`,
  `reading.tsv`) 597 = freedom and 223 = trouble. Founders "Code No. 13" returns this letter only, so there is no
  sibling text.
- The context fixes 108 = Maryland (Carmichael's state; Paca was Maryland's leading Antifederalist; Maryland ratified
  on 28 Apr 1788) and 223 = Massachusetts (ratified 6 Feb 1788) with high confidence, 273 = majority as likely.
  597 [you?]: "what says Virginia" fits the sentence as well as "you" (Virginia had not ratified; TJ was a Virginian);
  both are context guesses and 597 stays open.

## Reading

`make_reading.py` → `reading.tsv` (one row per counted code group; Short's one struck group excluded). Grades: T = TJ's
interlinear over the group; H = value attested by a decoding in another letter of the same code; E = the PTJ editors'
reading, not attested elsewhere; C = conjecture (editors' brackets or context only); O = open.

| Letter | Groups | T | H | E | C | O |
|---|---|---|---|---|---|---|
| Short 26 Jul 1792 | 674 | 511 | — | 156 | 0 | 7 (401 x2, 1083, 359, 199, 34, 724) |
| Pinckney 28 Aug 1793 | 58 | — | 30 | 23 | 4 | 1 (447) |
| Carmichael 14 Apr 1788 | 5 | — | — | — | 4 | 1 (597) |
| **All** | **737** | 511 | 30 | 179 | 8 | 9 |

728 of 737 groups (98.8%) carry a reading; 720 (97.7%) without the conjectures. Every letter is covered; what stays
open is nine single-occurrence groups in three letters, each without a decoded occurrence anywhere in its code.
Short's full code: 7 coded frames (016_0999, 1001, 1005-1009), 32 groups with a doubtful digit (read through TJ's
interlinear and the editors).

## Outcome

Method: existing decipherment (TJ's interlinear decoding of Short's letter, the PTJ editors' printed decodings of all
three, conjectures in brackets); the work was transcription, checking every group against the attested values of the
same code, and searching every sibling letter for the open groups. Extent: complete by the read bar (97.7% without
conjectures, measured; only scattered single-occurrence groups open, each externally blocked). Key: partial (none of
the three codes has a key; `key.tsv` collects 171 Code No. 10 values from TJ's interlinear and 262 Code No. 16 values from
Taylor's decodings and the Explication). Profile class: already solved (as erving1807); grades in profile.json: H = T+H
(541), M = E (179), I = C (8). Prior solution: the editors'
readings (PTJ 13, 1956; 24, 1990; 26, 1995), found before the work and used. What this adds: 447 for the editors' 497
(Pinckney); the confirmation of 30 of the 58 Pinckney groups from Taylor's decodings; the proof that the open Short
groups and Carmichael's code occur nowhere else (Code No. 13 ≠ Code No. 11; "been" = 1700); a full transcription of
Short's 674 groups and of Pinckney's 15 coded frames on M30 roll 2.

## Remaining gaps

- Pinckney 28 Aug 1793, group 447 (first word of the passage, before "regiments") - blocker: too-short; single occurrence in all 15 coded Pinckney frames on M30 roll 2, no decoding; Pinckney's own copy (PrC, Pinckney Family Papers, South Carolina Historical Society) not online
- Pinckney 28 Aug 1793, groups 234 [time?] and 501 [secret?], ?55 668 [Dunda-] - blocker: too-short; single occurrences, kept as the editors' conjectures; the first digits of ?55 are in the gutter (illegible)
- Short 26 Jul 1792, groups 401 (x2), 1083, 359, 199, 34, 724 - blocker: too-short; they occur only in this passage and its re-encipherment of 27 Jul; no decoding in any Code No. 10 letter checked; 401 is not the attested "been" (1700)
- Carmichael 14 Apr 1788, group 597 (and the context-only values of 108, 223, 273) - blocker: no-key-material; Code No. 13 survives in this letter only, no key and no other text

## Escalation

- [x] siblings: Short's re-enciphered extract of 27 Jul 1792 (016_1010-1012); 39 Code No. 10 documents (Founders notes) and six of them on the images; all 15 coded Pinckney frames of M30 roll 2 (1793-1795) transcribed, seven with decodings; Founders "Code No. 13" = this letter only
- [x] clear-pages: TJ's "copy so far only" Tr omits the coded section; the 15 Aug 1793 clear Tr and the 25 Nov 1793 "Explication of the Cyphers" (frame 0179) used as cribs for Code No. 16 values; no clear copy of 28 Aug exists in RG 59
- [x] known-keys: Code No. 11 table (jefferson1787) tried on Carmichael's Code No. 13: does not fit (597 freedom, 223 trouble)
- [x] print: Founders Online (PTJ 13, 24, 26), Founders search for each number, web search for the size of Grey's force (Aug 1793): no number found
- [x] key-rebuild: Code No. 16 values collected from seven decoded Pinckney letters and applied (31 of 58 groups of 28 Aug attested); Code No. 10 checked for alphabetical bracketing (none: two-part code)
- [x] retry: 447/497 re-read at 2x on frame 0140; Carmichael's blotted 108 re-read at 2x; every open group searched in all transcribed frames
