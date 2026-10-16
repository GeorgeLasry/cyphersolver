# Seven lines of unknown signs in the margin of a printed Latin book (user-supplied image)

Status: in progress. Provenance unknown; script identified only provisionally; nothing read.

## Target

- One photograph supplied by the user on 16 Oct 2026 (`margin.png`, 1259 × 540 px), no shelfmark, book, library
  or date given. It shows seven lines of handwritten signs in black ink written over a leaf of a printed Latin book
  (the type shows through: "...que hic manifestum ...", "... crescit ...").
- Not found in this repository, in `catalogue.json`, or by web search (Schmeh's Encrypted Book List, Cipher
  Mysteries); see Prior work.

## What the image shows

- About 170 signs in seven lines, written left to right: the lines are aligned on the left margin and the last
  line stops at about two thirds of the width (then a gap and one isolated sign inside a loop at the right).
- Signs are blocky pen forms: an arch family (∩ with a stub on top, with a short or long middle leg, plain, with a
  flat top), a reversed-E family (Ǝ, often with a long middle bar or a dash), a fork family (Y/Ψ on a stem, with or
  without a crossbar), ꭗ, a cross on a long stem (ϯ), a Γ on a stem, ʎ, a plain stroke ı, ɛ, 6, s, ξ, ≻.
- Barred signs: a sign set between two or more horizontal bars ("≡" with a squiggle), nine times, and a "~m~"
  form, four times, mostly in lines 3, 5 and 7.
- Punctuation-like marks: four dots ∷ (three times), two dots after ı and ʎ, single dots after Λ.
- Five or six loops ("lassos") enclose one or two signs and trail a long stroke down and to the left, crossing the
  line below. A few small signs are written between lines 1–2 and 2–3 (under the F-like sign; over a Ǝ).

## Script hypotheses tested

Reference charts rendered here from the Noto fonts (Google Fonts) and compared sign by sign.

| hypothesis | for | against |
|---|---|---|
| **Ethiopic (Ge'ez fidel) in an unpractised hand** | arch family = ሰ, ሐ, በ; ተ = ϯ; ገ = Γ on a stem; ለ = Λ; አ = ꭗ; ነ = ı; ቀ = fork with crossbar; ∷ = ። and the two dots = ፡; barred signs = Ethiopic numerals (figure between over- and under-bars) | the commonest sign (Ǝ with a long middle bar, 25 of 174) has no clear fidel counterpart; word dividers are not regular |
| Samaritan / Paleo-Hebrew used as a cipher alphabet for a western language | Ǝ = he, ≡ = samekh, × and + = taw/aleph, Y = waw, ʎ = lamed | the arch family has no counterpart; written left to right |
| Glagolitic (round and angular), Tibetan, Old Italic, Old Hungarian, Georgian, Armenian, Phoenician | individual look-alikes | no consistent match |
| Upside-down Latin letters | ʎ, ᴧ, ᑎ, Ǝ look like rotated y, v, u, E | the rotated image (`rot` test) does not read; line layout implies the image is the right way up |

A renaissance reader practising Ethiopic (from Potken's 1513 Psalter, Teseo Ambrogio 1539, Mariano Vittorio
1548/52) in the margin of a Latin book is the most economical explanation, but this is not established. If it is
Ethiopic, the text may not be a cipher at all, only a note in Ge'ez.

## Transcription

`transcription.txt`: one line per manuscript line, one code per sign, provisional classes (E = Ǝ, A = ꭗ, Y = Y/Ч on
a stem, U = fork with a crossbar, H = arch with stub and short middle leg, M = arch with long middle leg, S = arch
with stub, N = plain arch, D = flat-topped arch, V = Λ, L = ʎ, I = ı, G = Γ on a stem, T = cross on a stem,
T2 = cross with hooks, C = ɛ, O = 6, Z = ξ, X = s, F = F-like, P = ≻, B = [ with a dash, R = ꝛ, Q = barred sign,
W = ~m~, ∷ = four dots; rare forms have their own codes). Loop-enclosed signs are transcribed in place; the small
interlinear signs are left out. Measured: 174 tokens, 40 codes (`_check_profile.py --measure`). Several classes
are uncertain splits or merges (the arch family above all); the transcription has not been checked by a second
reader.

## Attempts

1. Simple substitution into Latin (Caesar, Cicero, Sallust from the CLTK Latin Library on GitHub, 0.66 M letters;
   quadgram scoring, 12 annealing restarts, one-to-one key on the 22 commonest classes, homophones for the rest;
   `work/anneal_latin.py`). The real text scores −12.86 per quadgram; three shuffled controls −12.46, −12.62,
   −12.50. **No signal**: Latin under a simple substitution of this transcription is not supported. An
   unconstrained homophonic run collapses to "ssiss…" for both the real and the shuffled text.
2. Other languages not yet tested: the repo's `lang/` corpora are not cached in this container and Gutenberg is
   blocked; only GitHub raw is reachable.

## Remaining gaps

- Provenance (book, library, shelfmark, date): needs the user or the owner of the image.
- Script identification: needs a Ge'ez reader, or a sharper image, to settle the Ethiopic hypothesis and the value
  of the Ǝ sign.
- Reading: none yet.

## Escalation

- Ask the user where the image comes from (a library record would give the book, its owners and the date).
- Test the Ethiopic hypothesis on a Ge'ez corpus (TraCES, Univ. Hamburg, doi:10.25592/uhhfdm.707) by syllable
  frequency and by searching for common Ge'ez words (ወ-, ዘ, እግዚአብሔር, ሰላም ለኪ); test Italian, French, German and
  Spanish under a substitution once corpora are available.

## Prior work

No earlier reading or publication of this image found (web search, 16 Oct 2026). Contamination: none known.
