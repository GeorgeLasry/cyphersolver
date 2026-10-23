# Re-reading log, R154 and R173 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b22)

## Starting point

Reading audit (22 Oct): both decoded, not read. Lasry's decode rows joined into running text gave 0.381 (61/160
sentences, 364D-1.txt) and 0.358 (19/53, 364D-20.txt) clean on `_check_reading.py`: runs of '00?', '70?', '80?' groups
DECODE could not read, open codes (<4545>, <4201>, <4434> ...), and several wrong values (4029 'quale', 78 'del').

## 1. Is there a text already?

Yes, on the DECODE images. Every file on R154 and R173 fetched with the project cookie
(`research/reading_audit/b17_fetch.py`, into the session scratchpad): the transcription, Lasry's key and corpus files
(already in `decode/keep/`) and the page images, 7 for R154 (only page 1 had been saved, in the main checkout's `img/`)
and 2 for R173. The record pages carry no comment block beyond "(Partly) deciphered within the letter".

The images show a **complete contemporary interlinear decipherment** over every cipher line of both despatches. NOTES
had called it "thin and unreliable ... a few words per page" because it was judged from DECODE's PLAINTEXT rows, which
the 2016 transcribers copied with most words as '?' ("Ee", "Narzio/Nunzio?"). On the images the hand is clear.

## 2. Transcription

`R154_decifrato.txt` (135 lines, ff. 12r-15r) and `R173_decifrato.txt` (34 lines, ff. 344r-344v), from 1800-px strips of
the 2833-px images (`research/reading_audit/b22_crop.py`), with zooms on doubtful words: f. 14r l. 2 'vivam.te' (DECODE
'ninam'), f. 15r l. 1 'essere persuasa' (over 4010 = essere), f. 344r l. 3 'cotesta' (unclear; 4545 + a), f. 344r l. 10
'e che però', f. 344r l. 26 'Io l'assicuro'. DECODE's PLAINTEXT rows skip one line on f. 12r and one on f. 13r; the image
line numbers are used.

## 3. Alignment with the figures

`research/reading_audit/b22_nunzio_align.py`: dynamic programming over Lasry's groups (as he segmented DECODE's figures)
and the decipherment's letters; output `R154_align.tsv`, `R173_align.tsv` (group by group) and `R154_words.tsv`,
`R173_words.tsv` (word by word, what carries it). Script helper `b22_nunzio_lines.py` prints the line scaffold
(DECODE PLAINTEXT, figures, Lasry's decode) used while transcribing.

| | letters | own value | code | look-alike | unread group | other value | no group |
|---|---|---|---|---|---|---|---|
| R154 | 4,030 | 2,998 | 430 | 93 (2.3%) | 255 | 163 | 91 |
| R173 | 1,172 | 862 | 143 | 19 (1.6%) | 79 | 46 | 23 |

Look-alike = a group that gives the decipherment's letters only when one figure is read as its look-alike (1/7, 0/6,
0/9, 3/8, 5/6 ...), or a four-figure code whose look-alike code begins with the same three letters (4570 -> 4576 dett-,
4470 -> 4479 VS Ill.ma). "Other value" is mostly code 4261 (Lasry N.S.), which the decipherer renders 'N.S.', 'il Papa'
or 'S. Stà' by context, and drift where DECODE mis-split the figures.

## 4. Key changes (key_b22.tsv)

Adopted (hold at every corpus place checked with `ctx.py` over seq.json, 364C + 364D): **78 = dal** (Lasry del; the
decipherer's dal/dall'/dalle/dalla at all 5 places in R154; 88 stays del), **4029 = però** (Lasry quale; all 37 places),
**4009 = essendo** (Lasry ere|esse; all 16), **4160 = esercit** (Lasry Capitol; 3 places, 'dell'esercito Turco'),
**4545 = cotest** (open; 2 places), **4434 = Em.za** (open; 13 places). 4545 and 4434 added to key_extra.txt.
For review (sense only): 4201 = Stà Sua (3 places, one loose). Kept: 4516 = 16 (the decipherer's 'd.o' there is
read as a slip for 4576). Tried and not adopted: 00 (46 places, DECODE '00?'; often 'di' in R154 and R173, but the
corpus contexts are too garbled to confirm), 4168 (2 places, no common value).

## 5. Transcription corrections (R154-R173_corrections.tsv)

R173 4594 -> 4597 (Prima); R154 4570 -> 4576 at two places; 4470 -> 4479 (split over a line end); one cipher line of
f. 13r missing from DECODE's transcription, figures read from the image; R173 false code 4839 = 58 3 90.

## Result

| doc | before (Lasry rows) | after (`b17_score.py` on the reading body) | explicit holes only | rests on |
|---|---|---|---|---|
| R154 | 0.381 (61/160) | 0.986 (68/69) | 1.0 | interlinear decipherment ff. 12r-15r + figures (0.85 of letters) |
| R173 | 0.358 (19/53) | 0.917 (22/24) | 1.0 | interlinear decipherment ff. 344r-v + figures (0.86 of letters) |

Both read, grade A. Open: nothing in the text; 'cotesta' (R173) marked [?] for the hand. 364D/23 (R176) is a second
copy of R173 (same date, same sentences).

Example (R154): 'Un tal pensiero ferisce il cuore di Nostro Signore, tanto più che il silenzio di Vostra Signoria
Illustrissima si stende ancora a tutte le altre cose più importanti del suo Ministero.' — Such a thought wounds Our
Lord's heart, all the more because your silence extends also to all the other more important matters of your ministry.
