# Marie de Médicis → Savary de Brèves, Rome, 10 Nov 1610 (BnF fr. 3789) — catalogue item 25

**Result, 20 Oct 2026: deciphered by Brice Dudout (with Claude and Codex) with the Henri IV–Brèves key, BnF fr. 3462
view 112; checked here sign by sign, read in part (95 of 98 glyphs supported, 3 signs in conflict with the key).**
See "Brice Dudout's reading" below.

**Earlier result, 21 Sept 2026: attempted, not read.** The passage is found and transcribed, its sibling (15 Sept 1610) too,
and the key it most probably uses is located. The only copy of that key available here is not good enough to apply.

## The letters

Gallica btv1b9059628m. The BnF notice's folios run two ahead of the stamped foliation in the scan: its "no. 12,
fol. 21 et 23" is **stamped f. 19r–v (canvases 36–37)**, and its "no. 11, fol. 19" (15 Sept 1610) is stamped f. 17
(canvases 32–34). Stamped f. 21 is a Savoy letter, which misled the first look.

- **10 Nov 1610** (signed Marie, countersigned Brulart): about 45 signs on f. 19r, lines 5–7, in mid-sentence:
  "Aussi vois-je bien [cipher] ne se[roit] pressé jusques à l'extremité du desarmement pour recevoir enfin la honte
  d'un refus absolu…". The context is Savoy's disarmament after Henri IV's death and Spain's refusal. The digits
  on f. 19v are show-through, not more cipher.
- **15 Sept 1610**: two passages, about 70 signs, f. 17r lines 22–24, on Savoy's son's journey to Spain.
- Transcription: `ciphertext.txt`. On DECODE they are R2076 and R2075 (Tomokiyo, "not deciphered").

The deciphered Villeroy letter in the same volume (stamped f. 26, Dec 1605) has an interlinear decipherment, but its
code is a different one: "content" = y b q 29̈ gives y=c, b=o, q=n, and those values turn Marie's text into nonsense.

## The key

DECODE **R2077** (Henri IV → Brèves, 5 Jan 1610, fr. 3541 f. 4–7) is marked Decrypted. Tomokiyo (louisxiii.htm)
says that letter was broken ciphertext-only by **Lasry, with Biermann and Tomokiyo, in 2021**. Camille Desenclos then
found the key at the BnF: R2077's note says **"The key is in BNF Français 3642"** (a mistyping of fr. 3462, confirmed by Tomokiyo in Oct 2026; see below). The record's only document is a
photo of that key (`DOC_2077_2022-Jan-30-16-52-01_93064.png`, 833 × 587 px, saved in `decode/`, git-ignored). The
R2077 note itself says R2075/R2076 "may be in the same cipher".

What the photo shows: an alphabet of 2–5 homophones per letter, many of them Latin letters used as signs (a b c d
under M, e f g h under N). A t/u/x/y/z box with qq, ǂǂ and ʓ for t. Plain numbers 4–99 for persons and a–b words: 4 le
pape, 14 le roy d'Espagne, 34 le duc de Savoye, 36 les princes de Savoye, 41 le duc de Parme, 62 card. Borghese,
c. 71–72 le Sr don Jouan / le Sr Conchine, 78 avoir, 79 avec, 86 armes, 88 bien, 96 Cardinal, 98 car. Letters with a
comma for c–e words: a, ce · y, et · x, en · 3, de?. Overbarred numbers 4̄–46̄ run from Flandres to milanois. The
photo stops there, so M–Z words are missing.

Marie's text uses the same kinds of sign (qq, ǂǂ, code letters with commas, plain and barred numbers). The 10 Nov
passage opens "72 4 79" = [Conchine?] le pape avec. But the alphabet as I read it from the 833-px photo gives
gibberish: `beam.py` runs a beam search over each sign's candidate letters, scored with the fr-1600-letters model, and
reaches −95 on 16 letters. One of three things is wrong: my assignment of photo columns to plaintext letters, the key
itself (a related table), or both.

## What would move it

1. **Lasry's R2077 decryption** (ciphertext plus plaintext) would calibrate every sign. He is the paper's
   co-author; ask him.
2. A full-resolution image of **BnF fr. 3642** (not on Gallica, SRU search 0 hits), including the M–Z code page.

## Brèves's reply (checked 21 Sept 2026)

Brèves's Rome letter-book, BnF **Cinq cents de Colbert 351** (Gallica btv1b10033961z, copies 1608–1611), pp. 724–730
(canvases 365–368): **"A la Reyne Regente, du 9 Decembre 1610"**, opening "J'ay receu les commandemens de V.M. du 10
Novembre". It answers the letter point by point **in paraphrase, never in her words**. It covers the pope's praise of
the regency over Cleves-Jülich, the Cologne conference breaking up, the Milan armament, and the hope that the king of
Spain would disarm at the pope's request. The pope approves the regency telling its ambassador in Spain that France is
bound to protect the Duke of Savoy if attacked, and Brèves warned the pope that Spain aimed to master Italy. Savoy is
the ciphered passage's subject, and this is its likely gist. But nothing in the reply fixes its words, so it gives no
crib strong enough to recover signs.
(The next letter, 14 Dec 1610, answers one of 23/24 Nov, p. 731 and canvas 370.)

**Closed as unreadable from available sources:** the key photo is partial and too coarse, the reply does not quote,
and the passage is too short (40 + 60 signs) for a ciphertext-only attack on a homophonic nomenclator. Only item 1 or
item 2 above would reopen it.

## Brice Dudout's reading (Oct 2026)

Brice Dudout (contributors.json `dudout`), working with Claude and Codex, deciphered both passages in mid-October 2026
and sent them by email (16 and 19 Oct 2026); dossier, CC BY 4.0:
https://bdudout.github.io/europe-chiffree/en/marie-de-medicis.html (repo github.com/bdudout/europe-chiffree). He agreed
on 15 Oct to cross-posting with attribution and to inclusion in the paper metadata. His readings (brackets his):

- 15 Sept: "ce sera trop manifester leurs malice et am[b?]ition que" … "acompagne[z?] d'imprudence et [de?] foi[b?]lesse"
- 10 Nov: "que le pape re[c?]ognoi[s?][s?]ant leurs arogance et [s?]entant sa timidite"

**The key's shelfmark.** Our notes above took R2077's "BNF Français 3642" as the key's location. Satoshi Tomokiyo
has confirmed to Brice that "3642" was a mistyped shelfmark for **BnF fr. 3462**, a volume of cipher keys; the key is
on **Gallica btv1b9058227h view 112** (https://gallica.bnf.fr/ark:/12148/btv1b9058227h/f112.item). The R2077 photo
is the same table. Tomokiyo also corroborated four barred numbers that are not on view 112: 72̄ que, 79̄ re, 86̄ se,
90̄ tion (Brice had first inferred them from context). He gives 41̄ as "leur" where Brice chose "leurs".

## Our check (20 Oct 2026)

Gallica's IIIF answered 403 (Cloudflare) on 20 Oct, so the check used the copies in Brice's repository: the key
(key-112.webp, 1800 × 1580 px, far better than the 833-px R2077 photo) and his line crops of f. 17r and f. 19r.
Every glyph was compared with the table cell it matches; the result, one line per glyph, is `alignment.tsv`
(98 glyphs: 59 on 15 Sept, 39 on 10 Nov). The reading with brackets is in `reading.txt`.

- **The key fits.** 86 of 98 glyphs sit in a cell of view 112 that gives Brice's value, and 3 more fit an entry whose
  word is not certain (41̄ ×2 = "Leurs", J, = "De(?)"): 89/98 = 90.8% from the page itself. The 6 barred-number
  occurrences that the page does not cover take Tomokiyo's values: **95/98 = 96.9%** of glyphs supported.
- **Three of Brice's brackets are settled by the key.** am[b]ition and foi[b]lesse: both signs are B1 (b with a flag).
  [s]entant: S1 (the looped crossed t).
- **Three signs conflict with the key as it stands on view 112.**
  - 10 Nov, re[c?]ognoissant: the sign is B1 (b), not one of the C homophones (u, hook, 5-shape, ʒ). The word needs c.
  - 10 Nov, the second s of recogno-i-s-[s]-ant: a loop with a diagonal stroke, closest to A4; no S cell has it.
  - 15 Sept, acompagne[z?]: a ß-like sign with a descender, either E3 (e) or Z2 (z). With E3 the word is
    **"acompagnee"**, agreeing with "ambition" ("ambition que j'estime … devoir estre acompagnée"), which is better
    grammar than Brice's "acompagnez". Undecided from the images.
  These are what Brice calls variants of a "very close" key: a slip by the encipherer or a regent's table that
  differs in a few cells. Only the regent's own key, or Lasry's R2077 decipherment for comparison, would tell.
- **41̄.** The entry on view 112 reads "Leurs" to me, with an uncertain ending; Tomokiyo gives "leur". Either way it is
  the same sign; "leur malice" would be the more usual grammar.
- **Corrections to our 21 Sept transcription.** 72 and 79 are overbarred (we missed the bars; the plain 72 is "le Sr
  Conchine", which misled the first attempt). "3ᵈ" on 10 Nov is two signs, 3 (a) and a raised crossed delta (r).
  "t u" on 15 Sept line 2 is one glyph, tu = U2, as Brice found. Several of our letters lumped different shapes:
  our "d" is P3, M4 or R3; our "z" is A1, P2 or T3; our "y" is A2 or I4; our "b" is M2 or S1.
- **Why the 21 Sept beam search failed:** the 833-px photo, the column assignment and those lumped shapes.

The reading is Brice's; this check confirms most of it from the key and adds the "acompagnee" alternative and the
b/c conflict. Outcome method: read after matching with key from external sources (Henri IV's key for an earlier
letter, filed in another volume, found to fit). Provenance: contributed.

## Remaining gaps
- 10 Nov, re[c?]ognoissant, one sign (B1 on view 112, c needed) - blocker: no-key-material; the regent's key or Lasry's R2077 decipherment would show whether c has this homophone
- 10 Nov, second s of recognoissant, one sign with no S cell on view 112 - blocker: no-key-material; same
- 15 Sept, acompagne[z?]/acompagnee, one sign (E3 or Z2) - blocker: illegible; the two cells differ by a stroke and the crop does not settle it
- barred 72, 79, 86, 90 (6 occurrences) - blocker: no-key-material; the N-Z page of the key is not in hand; values as corroborated by Tomokiyo

## Escalation
- [x] siblings: R2077 (Henri IV to Brèves, 5 Jan 1610) is the key's own letter; Lasry's decryption of it is not on DECODE or in hand (Brice asked; we do not have it)
- [x] clear-pages: f. 17v/19v hold show-through only; Brèves's reply of 9 Dec 1610 (Cinq cents de Colbert 351) paraphrases
- [x] known-keys: the Villeroy 1605 code (fr. 3789 f. 26) ruled out on 21 Sept; fr. 3462 view 112 fits
- [x] print: Tomokiyo louisxiii.htm and DECODE list both as not deciphered; no edition found
- [n/a] key-rebuild: the three conflicting signs occur once each; there is nothing to rebuild them from
- [x] retry: every glyph re-read against view 112 (alignment.tsv), 20 Oct 2026
