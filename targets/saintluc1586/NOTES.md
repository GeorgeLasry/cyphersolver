# Saint-Luc(?) to the King or Villeroy, 30 January 1586 (BnF fr. 15572 f. 43)

Outcome (22 Oct 2026): **key recovered from ciphertext-only by George Lasry** (CTTS, 2022; completed with Claude Opus
5.5, 2026; PR 76). Every sign carries a value; four words are doubtful and two sign values tentative.
Write-up: docs/saintluc1586.html.

## The document

BnF Français 15572 (despatches to Henri III and Villeroy, January–July 1586), f. 43: two pages wholly in cipher
except the clear date line *Du xxxe Janvier 1586*. Unsigned and unaddressed. Tomokiyo (cryptiana, *French Ciphers
during the Reigns of Charles IX and Henry III*) attributes it from the hand to François d'Espinay de Saint-Luc,
governor of Brouage (same hand as his clear letter at f. 35, same day as his letter at f. 42). Photographs f43a, f43b,
f43c in George's CTTS project (`lasry2022/ctts/`).

Not part of `matignon1586` (Mayenne–Forget's Cipher-1) or `matignon1586c3` (Matignon's Cipher-3): their notes record
that f. 43 is in neither cipher. Saint-Luc's other ciphered letters in the volume (ff. 245, 260) use another table
(Tomokiyo, "StLuc's Cipher"); not worked here. f. 260r-v with the f. 245r-v cribs is now its own target, `saintluc1586b` (Michael Brackx, issue #90).

## The key (George Lasry)

`lasry2022/ctts/key.txt`, image `lasry2022/cryptiana/images/saintluc1586_key.png`. Homophonic: 20 letters plus x, 51
symbols, two or three per letter (i five, s four). 20 signs for 17 words and syllables (que, qui, est, de, et, dict,
tout, faire, je, vous, lui, bien, plus, peut, pas, mal, ons). One sign doubles the letter before it, one marks an
abbreviation, 10 are nulls. CTTS labels each invented symbol with a two-digit number.

## How it was obtained

George transcribed the three images in CTTS and recovered the homophones with its built-in cryptanalysis (2022); the
key image is on Tomokiyo's page of his solutions (GL.htm, "An Unsigned Letter in BnF fr.15572 (1586)"), with no
plaintext. In 2026 the thirteen unassigned signs were resolved from context with Claude Opus 5.5 and the French
edited and translated (`lasry2022/CONTRIBUTION.md`; reading in `reading.txt`).

Checked here (22 Oct 2026):
- `decode.py` re-applies the key to the transcription: 1,315 signs = 1,168 letters + 77 word signs + 44 doubling and
  abbreviation signs + 26 nulls, none unassigned. Same as George's counts.
- `docs/_validate.py` (model `fr-1600-letters`, word signs as their words, doubling and abbreviation signs left out):
  reading -2.091 per letter; random keys -4.722 (z 9.9); key fitted to shuffled text -3.014 (z 25.7); annealer on the
  real text -2.203. Verdict: pass.
- The f43a overlay (`lasry2022/cryptiana/images/saintluc1586_f43a_decryption.jpg`) compared by eye with the decode of
  its first four lines: same values on the same signs.

## Prior solution

Lasry's own 2022 key image on GL.htm; no plaintext published. Tomokiyo's henryiii.htm lists f. 43 as undeciphered
apart from its date line. No printed decipherment found (web search, 22 Oct 2026).

## Remaining gaps
- four doubtful words (f43a ll. 7, 15; f43b ll. 5-6) and the tentative values 36 = et, 84 = lui - blocker: too-short; single occurrences, no clear copy of the letter known
- recipient and the people behind the cover names (the concierge, the gardener, the stonecutters, the governor, the planter) - blocker: no-key-material; the letter names them only by cover name

## Escalation
- [x] siblings: Saint-Luc's other ciphered letters (ff. 245, 260) are another table (Tomokiyo); the Matignon and Mayenne ciphers of the volume are other keys (matignon1586, matignon1586c3, mayenne1586c2)
- [x] clear-pages: only the date line is clear; no decipherment on the leaf
- [x] known-keys: f. 43 fits none of the volume's other known keys
- [x] print: GL.htm (key only), henryiii.htm; no printed decipherment found
- [x] key-rebuild: every sign assigned; the two tentative values have one or two occurrences
- [n/a] retry: no extended key; nothing left to rerun

## Files
- `lasry2022/` — George Lasry's contribution (PR 76): CONTRIBUTION.md, CTTS project, Cryptiana-style entry and images.
- `decode.py`, `validation.tsv`, `reading.txt`, `profile.json`.
