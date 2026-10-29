# Verification brief (28 Oct 2026)

The Oct 2026 archive sweeps added catalogue entries scored from catalogue descriptions only. Your job is to verify the
ones assigned to you: is the cipher really there, is it really unread, and can the images be reached?

Read access: `C:\Users\dbour\cyph-merge\catalogue.json` (the file has `{"entries": [...]}`; each entry has `id`, `title`,
`shelfmark`, `links`, `status`, `prior_art`, `verify`, `source`, scores). Your group's ids are in
`C:\Users\dbour\cyph-merge\research\verify_2026-10\groups.json` under your group key. The sweep README for each entry's
`source` is in `research/<sweep folder>/README.md` (same worktree) and has context and known pitfalls.

## For each id

1. **Prior art.** Web-search for a published decipherment or reading: Tomokiyo's cryptiana (cryptiana.web.fc2.com),
   Lasry's papers, HistoCrypt proceedings (ecp.ep.liu.se), Cryptologia, Schmeh's blog, printed editions and calendars
   that print the document deciphered, the archive's own catalogue notes ('deciphered', 'mise en clair',
   'décryptage', 'Auflösung', 'decifrado'). Also DECODE (decode.cs.uni-kassel.de or the repo dumps):
   `python -X utf8 C:\Users\dbour\cypher\research\archive_sweep_2026-10\known.py "<term>"` greps the repo ledgers and the
   DECODE list. "Cipher undeciphered" in an old calendar usually means the editor deciphered it himself, so check.
2. **The item.** Open the `links` / archive record or scans if reachable (WebFetch, or the built-in browser
   `mcp__Claude_Browser__*`; do not bypass Cloudflare/captcha/proof-of-work; do not disable TLS checks; the browser pane
   is shared with other agents, so open your own tab). Confirm the cipher is present, roughly how long, what kind
   (numeric, symbols, nomenclator, partial), whether a decipherment/key sits in the same file, and whether images are
   viewable online. If you can view a page, `seen` becomes "image".
3. **Verdict**, one of: `open` (cipher present, no decipherment found), `partly_read`, `solved_published` (a published
   decipherment exists: give the citation), `not_cipher`, `duplicate` (already in the repo or another catalogue row:
   give the id/target), `unreachable` (could not verify; say what blocked it).

## Output

Write `C:\Users\dbour\cyph-merge\research\verify_2026-10\<group key>.json`: a JSON list, one object per id:

```json
{"id": 1234, "verdict": "open", "prior_art": "open (checked 28 Oct 2026: cryptiana, HistoCrypt 2019-25, Birch 1742; ...)",
 "evidence": ["https://..."], "status_update": "one or two sentences to append to the entry's status: what you found",
 "seen": "image|catalogue", "importance": 3, "solvability": 3, "difficulty": 3, "ciphertext_size": "e.g. 4 pages, ~600 groups, or unknown",
 "next_step": "what to do to read it", "scans_online": true}
```

Scores change only if you learned something (keep the old ones otherwise). Write the file incrementally after every few
ids so nothing is lost. Be strict: only say `open` if you searched. Quote nothing long from sources; cite them.
Do NOT edit catalogue.json or any other repo file, and do NOT commit or push; the parent merges. python -X utf8.
Final report: counts by verdict, the 3-5 best confirmed-open leads, and anything blocked.
