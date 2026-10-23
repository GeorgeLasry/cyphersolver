# Re-reading log, PTR 53/69 copy X, recto ll. 12-13, 16-46 and verso (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b27)

## Starting point

Reading audit (22 Oct): copy X recto ll. 1-11 and 14-15 read; the rest is "decoded, not read": in `reading_X.md`
those lines are mostly `[..]` (letter-sign runs not read at PARES resolution) between code groups whose values are
sure (Galende's *Cifra general*).

## 1. Is there a text already? The key?

* No DECODE record (the letter is in AGS, on PARES only). No contemporary decipherment on any image of PTR 53/66-72
  (all opened 22 Sept); Bergenroth calendared the letter as unread (CSP Spain i 369) and mis-summarised copies X and Z
  as the 3 Oct letter (nos. 380-381). No edition, no Tomokiyo reading.
* The nearest text is the clear copy of Isabella's letter of 3 Oct 1503 (PTR 53/72, ff. 346-349), which summarises
  this one ("Por otras nuestras cartas de veinte de agosto ... dos mil peones ingleses escogidos"); it was already
  used as a crib for sense and vocabulary, and it is a summary, not a copy.
* The key is complete in print (Galende Díaz 1994, app. doc. 1; `targets/esp318/keys/cifra_general.txt`): nothing to
  look for in the AGS inventory. The open runs are unread signs, not unknown values.

## 2. Read on the image: failed today

PARES answered **HTTP 429 (Too Many Requests)** to every request on 23 Oct 2026, the catalogue page and the site root
alike (`research/reading_audit/b27_pares_fetch.py`, curl), so the images of PTR 53/69 could not be fetched again this
session. On 22 Sept every PARES route was tried (zoom 10/20/100, print view, quality flags): at most 997 x 1396 px, no
IIIF, no tiles; at that size a sign is 8-10 px high and the letter runs stay ambiguous between two or three sign
forms (NOTES, Escalation, retry). No other reproduction is online.

## 3. Partial reading

The unread lines converted to running text, code groups by value, nothing added:
`texts/PTR53-69_partial_reading.md`. Look-alike alternates: none adopted (no sign re-read).

## 4. Score

`b17_score.py`, LANG_=es, reading body: 0.128 (6/47); explicit holes the same, 0.128 (the holes are explicit `[…]`).
Before: the audit's judgement (mostly `[..]`). Kept **decoded, not read**. Blocker: illegible at the only available
resolution (needs-physical-access for a better reproduction: AGS Simancas photographs of PTR 53/69, which hold three
copies X, Y, Z of the letter to collate).

One sentence (verso, readable from the code groups): "el rey de Inglaterra nuestro hermano es obligado por virtud de
lo […] entre nos y el, de nos ayudar para defender nuestro […]" (the King of England our brother is bound by virtue of
[the treaties] between us and him to help us defend our [kingdoms]).
