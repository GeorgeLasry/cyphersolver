# Ferdinand the Catholic → Jerónimo de Vich (Rome), Pedrezuela, 26 October 1515 (AHN Estado 8715 N.73)

Split on 14 Oct 2026 from `targets/vich1511/` under the one-key rule (George Lasry, 14 Oct 2026). The letters of
1511-12 to Vich (N.45, N.57, N.60) are in another cipher, the 1511-12 nomenclator, and stay in `targets/vich1511/`
(vich1511.html): a different cipher, with its own page. This entry is N.73 alone.

**Outcome (23 Oct 2026): key recovered from ciphertext-only, text not read.** Michael Brackx (@brackxm, issue #94)
recovered the sign alphabet ciphertext-only and read 40 code-group types by context; the decode measures 0.636 of
words read as sense, so it is *decoded, not read*. The key is partial: 144 group tokens unread, 192 tentative.

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

## Measured (23 Oct 2026)

`research/reading_audit/v10_relabel.share` on `brackx2026/n73_reading.md`, every tentative value counted as a hole:
839 words, 480 holes and doubtful words, **read_share 0.636** (Brackx's own figure; `_check_reading.py` 0.158 clean
sentences). Look-alike readings are 3.9% of letters. Grade: *decoded, not read*. The issue's first post said "largely
read"; Brackx withdrew that in his reply.

What it says, as far as it reads: Ferdinand cannot help being *muy malcontento* that through pride and delay *las
cosas de Italia* are in danger, and worse at *la flaquesa del papa*, who seems set on terms that break what the
league capitulated; *yo no creo ni creere* it, and Vich is to *esforçarle de mi parte* and not let him lose heart.

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
- 144 unread code-group tokens (90 types, most once or twice, many probably names) and 13 unvalued signs - blocker: no-key-material; read by context as far as the contexts go (three passes); a crib is needed (Vich's answer, a Rome decipherment, or Terrateig 1963 vol. II, not online)
- 192 tentative group tokens (29 types: `bay` = uisorrey, `suh` = emperador, `rie` = confederado ...) - blocker: no-key-material; each needs a second context or a crib
- `sin`/`sim` (151 tokens) and `X` = r/s/z (171 tokens), split by the model in context, 6 tokens image-checked - blocker: needs-physical-access; PARES serves the record at 1,137-1,147 px, a high-resolution copy from the AHN would settle the minims and sibilants

## Escalation
- [x] siblings: the Vich ciphered letters on PARES (8714 N.12, N.26, N.39; 8715 N.41-N.79) sorted; none of the deciphered ones is in this key; N.72 (16 Oct 1515) is a clear letter on another matter
- [x] clear-pages: the four images carry only the docket, the clear opening and the dateline
- [x] known-keys: the 1511-12 nomenclator, the N.74 (1519) system and the N.79 table compared; none fits
- [x] print: CSP Spain II (Bergenroth) has no entry for 26 Oct 1515, only no. 240 referring to it; Terrateig 1963 vol. I is on the Internet Archive (politicaenitalia0001terr, lending only), vol. II not found online; Zurita and Sarrablo Aguareles not found in searchable text (Brackx)
- [x] key-rebuild: sign alphabet recovered ciphertext-only by joint annealing, groups read by context in three passes (Brackx); validated here (pass)
- [x] retry: the third pass re-read every unread group with wide context and a 1515 name list; it added three tentative values and changed no firm one

## Log

- 18 Sept 2026: transcribed; letter-level annealing failed.
- 14 Oct 2026: split from vich1511.
- 23 Oct 2026: Brackx's key, reading, English, token table and scripts (issue #94 and gist) taken in; measured 0.636,
  decoded, not read; `_validate.py` pass.
