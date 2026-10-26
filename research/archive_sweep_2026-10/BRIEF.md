# Archive sweep, Oct 2026: shared brief for each sweep agent

Goal: find historical ciphertexts (European classical ciphers, 1350-1950) that are **unsolved or possibly
unsolved** and that are not yet in this repository, so they can be added to `catalogue.json`. Each sweep covers
one archive or portal. Volume matters: list every plausible item, scored honestly, rather than a handful of
polished ones. But each row must be a real, identifiable item (shelfmark or stable URL), never invented.

## What counts

- A letter, despatch, register entry, or other document that contains enciphered text: a nomenclator, a
  substitution cipher, a code, or cipher passages in a clear letter.
- "Potentially unsolved" is enough: the catalogue says cipher or "en chiffre", and no decipherment is noted.
  Mark how certain this is in `status` and `prior_art`.
- Leave out: bare keys and cipher tables with no ciphertext (note them in the README as key leads, since they
  can read other letters); shorthand; items after 1950; Enigma; the famous ciphers (Voynich, Beale, Kryptos,
  Dorabella, Zodiac and so on); items whose catalogue description says the cipher was deciphered or that
  carry an attached decipherment, *unless* the decipherment is noted as partial.

## Dedup: run before writing a row

`research/archive_sweep_2026-10/known.py "<term>"` greps catalogue.json, SOLVED_CATALOGUE.md, README.md, CATALOGUE.md,
`targets/*/NOTES.md`, the Cryptoole snapshot and the DECODE list (10,106 records) for a shelfmark, name or
R-number. If an item is on DECODE (any status), give its R-number in `decode_ids` and say so in `status`. Keep it
only if DECODE marks it Non-decrypted, Partially decrypted, or N/A *and* it is not already in the repo.

Prior art. For the strongest candidates (importance 3 or more), do a quick web search for a published
decipherment: Tomokiyo's cryptiana (cryptiana.web.fc2.com), Lasry's papers, HistoCrypt proceedings, the
relevant printed calendar or edition. Record what was checked in `prior_art`, e.g. "open (checked 26 Oct 2026:
cryptiana, HistoCrypt)". "Cipher undeciphered" in an old calendar usually means the editor deciphered it himself.

## Output (write incrementally, after every few finds, so nothing is lost if you are cut off)

In your folder `research/<your_folder>/`:

1. `candidates.json`: a JSON list of objects with exactly these fields (no `id`; ids are assigned at merge):

```json
{
  "year": 1560,                      // integer, best single year
  "date": "12 Mar 1560",             // as precise as known
  "title": "Sender → recipient, short description",
  "correspondents": "Sender → recipient (\"unknown\" if not known)",
  "place": "place of writing or \"unknown\"",
  "language": "plaintext language or \"unknown\"",
  "region": "one of: England, France, Italy, Spain, Portugal, Low Countries, Central Europe, Germany, Scandinavia, Poland-Lithuania, Papacy, Americas, Other",
  "period": "one of: 15th century, 1497-1559, 1560-1589, 1589-1598, 1598-1610, 1611-1650, 1651-1700, 1701-1800, 1801-1900, 1901-1950, unknown",
  "shelfmark": "archive, fonds, item (as the archive cites it)",
  "folio_note": "folios / scan numbers / how much cipher, if known",
  "cls": "A | B | C",                // A siblings with decipherment in same volume; B partial key or known family in print; C no key, no sibling
  "status": "what the archive description says and what you checked; DECODE status if any",
  "why": "one sentence: what the cipher could add historically",
  "importance": 1-5, "solvability": 1-5, "difficulty": 1-5,
  "score_note": "Scored from the archive description during the Oct 2026 <archive> sweep (research/<folder>/); not viewed",
  "verify": "next step to confirm it is open and readable (view images at URL, check edition X)",
  "links": [{"label": "short label", "href": "https://stable URL to the item or its scans"}],
  "seen": "catalogue" (description only) or "image" (you looked at the scan),
  "source": "<archive name> sweep",
  "prior_art": "open (checked 26 Oct 2026: ...)" or what was found,
  "decode_ids": [1234]              // only if on DECODE
}
```

Scores: importance = historical weight (a ruler's or ambassador's despatch on a major affair 4-5; routine
merchant or family letter 1-2). Solvability = odds of a full reading from material online (images online + long
text + plausible language 4-5; no images 1). Difficulty = 1 trivial key alignment ... 5 statistics only on an
unknown system.

2. `README.md`: method (endpoints, search terms, counts of hits and of rows kept), the best leads ranked,
   key leads (bare keys found), dead ends, and what was not reached. Put scripts you write in this folder too.

Do not edit `catalogue.json`, `CATALOGUE.md`, the README or anything in `docs/`; the merge is done by the main
session. Do not commit. Do not download page images in bulk (a few to check a lead are fine; keep them
git-ignored, not in the repo). Respect each site's terms; if a portal blocks scripts, use the built-in browser
or note it and move on. Your final reply: number of candidates written, the top five, and what blocked you.
