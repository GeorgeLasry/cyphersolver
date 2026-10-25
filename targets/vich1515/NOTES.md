# Ferdinand the Catholic → Jerónimo de Vich (Rome), Pedrezuela, 26 October 1515 (AHN Estado 8715 N.73)

Split on 14 Oct 2026 from `targets/vich1511/` under the one-key rule (George Lasry, 14 Oct 2026). The letters of
1511-12 to Vich (N.45, N.57, N.60) are in another cipher, the 1511-12 nomenclator, and stay in `targets/vich1511/`
(vich1511.html): a different cipher, with its own page. This entry is N.73 alone.

**Outcome (25 Oct 2026): key recovered from ciphertext-only, text not read.** Michael Brackx (@brackxm, issue #94)
recovered the sign alphabet ciphertext-only and read 40 code-group types by context (0.636). He then found the letter
quoted from its minute in Terrateig 1963 and used the quotation as a crib for ll. 9-31: the decode now measures
**0.824** of words read as sense (0.949 on ll. 9-31), but look-alike readings are 3.09% of letters, five letters over
the 3% limit, so it stays *decoded, not read*. Key partial: 77 group tokens unread, 25 tentative.

**Prior text in print (the contamination question).** The letter's clear minute, AGS Estado leg. 847 fol. 125, was
printed in full by Doussinague, *La política internacional de Fernando el Católico* (1944) p. 520, and quoted at length
by Terrateig (1963) vol. I pp. 631-634. It was found **during the attempt, after the ciphertext-only break** of the
alphabet and the first 40 groups, and **used** as a crib for the group values on ll. 9-31. No key was ever published,
but the text is not a first reading: `first_break` false, `prior_solution` in print.

PARES: AHN Estado 8715 N.73, id 12751418 (4 images). Images are not committed; they are in the main checkout under
`targets/vich1511/img/n73_*.jpg` and the line strips under `targets/vich1511/lines/` (re-fetch with
`python ../vich1511/pares.py img 12751418 n73`).

## The letter and its cipher

`n73_transcription.txt` (124 lines, 3,177 tokens, 197 distinct) and `n73_freq.txt`. Mostly three-letter code
groups (`sin` 151, `sud` 97, `no` 93, `zre` 89, `xed` 68) with a smaller set of signs (`X` 171, `TH` 170, `PHI` 163,
`RH` 151). Its clear text: docket "a 26 de octubre 1515", opening "videlicet iterum", ending "en Pedrezuela a xxvj
de otubre de dxv". No deciphered sibling: N.74 of 1519 is Charles I's and a third system.

**The system (Brackx).** Homophonic letter signs, 37 types including 8 letter-pair signs (`PHI` = s, `RH` = e, `TH`
= o, `O` and `Z` = a, `RS` = u, `KH` and `BO` = i ...), mixed with three-letter code groups that stand for whole
words (`zre` = que, `sud` = de, `yob` = por, `yem` = papa, `teb` = Italia, `xif` = liga) **and for syllables and
single letters inside spelled words** (`tok` = ha, `gso` = l, `no` = t, `xed` = la). That last feature is why the
September attempt failed: it annealed the groups as letters or as whole-word units, never as both.

## How the key was recovered (Brackx, with Claude Code / Claude Opus 5.5)

Details in `brackx2026/notes_solve.md`.

1. **Joint annealer** (`brackx2026/script_wsa4.c`, from his esp318no93 work): a value for every sign (a letter or one
   of the 40 commonest letter pairs) and every code group (a word, syllable or letter from a fixed list, or unknown),
   scored by a Spanish character 5-gram (*Celestina*, *Quijote*) plus an encipherment-cost term n log(n/N) per sign
   and group that keeps the search from collapsing onto a few letters. 16 processes × 3 restarts per run.
2. **Fixing step by step:** values fixed only when the best runs agreed and decoded contexts confirmed them; best
   score -3.73 per token with nothing fixed (shuffled tokens -4.56), -3.37 with every sign fixed.
3. **Groups by context**, three passes (CSP Spain II used for context only: no. 240 of Nov 1515 refers to "the 26th
   of the previous month"): firm 40 types / 1,005 tokens (76%), tentative 29 / 177 (13%), unread 90 / 144 (11%).
4. **`sin` is two groups:** *ſin* (two minims) = *es*, *ſim* (three) = *en*, side by side on p. 3 l. 10; the 151
   tokens split by the 5-gram in context, 6 close calls read on 2× crops. **`X`** given *r*, *s* or *z* by the model.

## Controls

- **Matched control** (`brackx2026/script_control_matched.py`): *Lazarillo de Tormes* (held out of the model)
  enciphered the same way at the same size (3,282 tokens, 38 sign types, 158 group types). The same first step gets
  **every sign token right** and 35-44% of group tokens: the alphabet comes out reliably, the groups only in part.
- **Statistical validation here** (`docs/_validate.py`, `validation.tsv`: tokens as transcribed, firm values only,
  es-golden-age): reading -2.068 per letter, random keys -4.040 (z 8.8), a key annealed onto shuffled text -2.760
  (z 42.5), annealer power -2.036; polyphony 4.5% (the `sin`/`X` splits). **Verdict: pass.**

## The Terrateig crib (Brackx, issue #94 comment of 23 Oct 2026, 21:49)

Terrateig quotes the letter in 15 passages. Each was aligned with the token stream (gapped, anchored on the firm
values) against 12 *Don Quijote* passages of the same length. The long quotation, 1,069 letters, aligns with ll. 9-31
at 0.29 cost per letter (best control 0.98); two short phrases also fit (*salido del cuydado*, l. 7; *no son para
haver plazer*, l. 6). The other 13 align no better than random and were not used. 714 of the quotation's letters fall
on values already firm and agree except at eight places, each checked on the image. It settled 27 groups (`be`
*suycos*, `poz` *capitan general*, `zuy` *rey de francia*, `dik` *voluntad* ...), confirmed 11 tentative values,
corrected `seg` and `soo`, and decided 38 `sin`/`sim`/`X` tokens; four transcription slips corrected on the image.
Four context rounds followed; the last changed nothing. The 1963 text is not reproduced; `work_crib_tokens.tsv` gives
letters and page references.

## Measured (25 Oct 2026)

`research/reading_audit/v10_relabel.share` on `brackx2026/n73_reading.md`, every tentative value counted as a hole:

| | before the crib | after |
|---|---|---|
| read share, ll. 1-124 | 0.636 (839 words, 480 holes) | **0.824** (1,099 words, 235 holes) |
| read share, ll. 9-31 | | 0.949 |
| look-alike readings | 3.9% | 3.09% (165 of 5,337 letters) |
| group tokens firm / tentative / unread | 76% / 13% / 11% | 93% / 1% / 6% |
| `_validate.py` | pass (-2.068 vs shuffled refit -2.760) | pass (-2.025 vs -2.524) |

Grade: *decoded, not read* (look-alikes over 3%, and 0.824 under 95%). Coherent sentences run over 59 of the 124 lines.

What it says, as far as it reads: Ferdinand cannot help being *muy malcontento* that through the *soberuia y locura
de suycos*, who would not wait for his army, and the slowness of *mi uisorrey y capitan general*, *todas las cosas de
Italia* are in danger; worse, *la flaqueza del papa*, set on *concertarse con franceses* against the league's
capitulation that no confederate may make peace or truce without the others. Vich is to strengthen him *de mi parte*.

## Files

- `n73_transcription.txt`, `n73_freq.txt`: the September 2026 transcription (pass 1 labels).
- `brackx2026/` (issue #94 gist, 23 Oct 2026): `n73_reading.md` (all 124 lines, writer's spelling, holes sized:
  `[?3 groups]`, `[?sign]`, `[x]` supplied, `{?word}` tentative), `n73_en.md` (English with the same marks),
  `n73_decryption.md`, `n73_tokens.tsv` (one row per token, 3,163: label, split label, value, status, reading
  word), `n73_sin_x_tokens.tsv` (every `sin`/`sim`/`X` with basis and model margin), `n73_codebook.md`,
  `n73_legend.md`, `key_signs.*`, `key_groups.*`, `notes_solve.md`, the `script_*` solver and control scripts and
  the `work_*` files. The scripts were written to run side by side without the `script_` prefix; not run here.
- `validation.tsv`: the pairs for `docs/_validate.py`.
- `solve73.py`, `solve73g.py`: the failed September annealers.

## What was tried before (18 Sept 2026)

Annealing against the repo's Spanish 5-gram model (`solve73.py`, `solve73g.py`) with the lowercase groups split into
letters, as whole units, and as context breaks around symbol runs: -2.7 to -3.5 per character with seeds disagreeing.
The 1511-12 nomenclator, the N.74 system and the N.79 "Clave de cifra" table were compared: none fits.

## Remaining gaps
- 77 unread code-group tokens (60 types, most once, probably names) and 13 unvalued signs - blocker: no-key-material; four context rounds after the crib, the last changed nothing; the minute (AGS Estado leg. 847 fol. 125, not digitised) or Doussinague 1944 p. 520 (not online) would give a crib for the rest
- look-alike readings 3.09% of letters, five over the 3% limit (`sin`/`sim` minims, `X` = r/s/z outside ll. 9-31) - blocker: needs-physical-access; PARES serves 1,147 px, a high-resolution copy from the AHN would settle them
- lines outside the quoted stretch - blocker: needs-physical-access; the minute or Doussinague 1944

## Escalation
- [x] siblings: the Vich ciphered letters on PARES (8714 N.12, N.26, N.39; 8715 N.41-N.79) sorted; none of the deciphered ones is in this key; N.72 (16 Oct 1515) is a clear letter on another matter
- [x] clear-pages: the four images carry only the docket, the clear opening and the dateline
- [x] known-keys: the 1511-12 nomenclator, the N.74 (1519) system and the N.79 table compared; none fits
- [x] print: Terrateig 1963 vol. I pp. 631-634 quotes the letter (used as the crib for ll. 9-31); its source, the minute AGS Estado leg. 847 fol. 125, is printed in full in Doussinague 1944 p. 520, not found online (archive.org, HathiTrust, Google Books); CSP Spain II no. 240 refers to it (Brackx)
- [x] key-rebuild: sign alphabet recovered ciphertext-only by joint annealing, groups read by context in three passes (Brackx); validated here (pass)
- [x] retry: four rounds after the crib re-read every unread group; a solver ranking of the remaining repeated groups gave flat margins; the last round changed nothing

## Log

- 18 Sept 2026: transcribed; letter-level annealing failed.
- 14 Oct 2026: split from vich1511.
- 23 Oct 2026: Brackx's key, reading, English, token table and scripts (issue #94 and gist) taken in; measured 0.636,
  decoded, not read; `_validate.py` pass.
- 25 Oct 2026: Brackx's update of 23 Oct (21:49), which crossed our take-in: the Terrateig crib and four rounds.
  Gist re-copied; 0.824, still decoded, not read; `_validate.py` pass; prior print recorded (Doussinague 1944).
