# Key notes, 1643 letters (scans m0064-m0086)

## The key does not change in 1643

The draft key in `key.py` (rebuilt from the 1642 cipher/clear pairs of letters 8 and 13)
reads the October 1643 letters unchanged. Verified word by word on m0068 (9 Oct 1643):

| cipher | plain | where |
|---|---|---|
| `fc` | de | m0068 l.3 |
| `goto` | para | m0068 l.3 (confirms the given example) |
| `eorncppo` | Castella | m0068 l.3 |
| `aivntxeuev` | instruções | m0068 l.3, l.23 |
| `E(t)oico` | França | m0068 l.3 |
| `gol dctop` | paz geral | m0068 l.4 |
| `sxe` | que | m0068 l.4, l.23, l.24 (confirms the given example `sxc`) |
| `ve tcecgctoz` | se receberam | m0068 l.4 |
| `euz` | com | m0068 l.4 |
| `eixaue` | envie | m0068 l.23 |
| `dur` | aos | m0068 l.23 |
| `zaiavntuv` | ministros | m0068 l.23 |
| `ieppo` | nella | m0068 l.24 |
| `zoifu` | mando | m0068 l.24 |
| `ovravnat` | assistir | m0068 l.24 |
| `evne` | este | m0068 l.24 |
| `iedueaie` | negócio | m0068 l.24 |
| `zxi(v)nct` | Munster (Münster) | m0066 l.12 |
| `fu ai(E)oinc` | do Infante | m0066 l.13 |

No new letter values and no changed values were observed. Nothing in these letters
requires a 1643 key: every word that could be transcribed decoded under the 1642 key.

## No additions to the alphabet

I found no cipher letter outside the alphabet already in `key.py`. No new homophone was
needed: `v` and `r` both for plain s, and `x` for u and v, behave as in 1642.

## Code words / symbols

* `⊕` — Castela / ElRei de Castela. Used in 1643 inside otherwise clear text, not only
  inside cipher runs: m0066 l.1 "e por ⊕ q importava ao bom gov.o de meus R.nos",
  m0085 l.3 "dos bons ef.os da intelig.a con ⊕ ...". Confirms the meaning given.
* No instance of the short code `ft` (ElRei Christianíssimo) was met in the runs read;
  in these letters "ElRei Chr.mo" is written out in clear (m0068 enclosure, m0085).

## Transcription traps confirmed (and one new one)

* **c / e** — constant. `fc` (de) is repeatedly indistinguishable from `fe`; whole words
  fail to decode until the reader allows every `e` to be `c` and vice versa. Decode both
  ways before declaring a word unread.
* **t / z** — `zaiavntuv` (ministros) first read as `raiavntuer`; `dctop` (geral) first
  read as `dcbop`.
* **r / v** — the same stroke; since cipher r and v are both plain s this is usually
  harmless, but it hides `t` as well (`tcecgctoz` = receberam read as `tvecgctoz`).
* **o / u (new)** — in this hand a closed `o` and `u` are often the same loop, and since
  cipher o = plain a and cipher u = plain o, a single misread flips "todos" to "tados".
  `nufuv` (todos) was first read `nofuv`; `our` (aos) first read `dur`.
* **d / o (new)** — the scribe's `d` has a very small bowl; `our` (aos) read as `dur`.
* **Blots are not signs.** On m0068 l.3 what looks like a crossed symbol before `toico`
  is an ink blot over the capital E; the word is `E(t)oico` = França.

## Resolution limit

These are 1060 x 1390 px scans of a crowded cursive. Even at 8-10x upscaling, individual
letters inside the longer cipher words cannot be separated reliably; that, and not the
key, is what left words unread here (letter 56's three cipher words in particular). Any
further reading of these runs needs higher-resolution images from DigitArq.
