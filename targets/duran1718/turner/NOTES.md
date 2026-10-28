blocked
No standard edition or calendar of the legation's despatches was identified or opened by this worker (CS-A2-H, 3 Oct 2026); blocked on: ACA catalogue/PARES not opened (PARES dead from the cloud), so the holding record's availability flag is unquoted.

# Fernandez Duran to the marques de San Felipe, El Pardo, 30 November 1718

Built by HARVEST-SCOUT-3 (account 3, parent worker, 28 Sept 2026; brief
`.claude/briefs/runs/2026-09-28-parent-harvest-scout-3.md`, row 2 of `harvest/SCOUT-3.tsv`). Blocked at the key: the
ciphertext is transcribed and on disk, the nine keys of the same fonds catalogued on DECODE were all viewed and none
reaches the letter's value range. No decoding was attempted. No class (rule 10).

## The item

- Archivo de la Corona de Aragon, Diversos, Legacion en Genova y Turin, Cajon 1, leg. 22, doc. 67. DECODE record
  R10181 ("ACA_Diversos_Cajon_1_leg.22_doc.67.", Cipher, Non-decrypted, access mode Public, 4 images), catalogued
  with symbol set "Graphic signs"; the image shows a numerical cipher.
- Read on the image (this worker, grade M for the names, the hand is a clear secretary's hand): cover (P1) "... 30
  de Nov.e 1718 / Dn Mig.l F.z Duran / en Zifra", stamped Archivo de la Corona de Aragon, pencil "67"; text on
  the inner opening (P2 left leaf, 17 lines; P3 right leaf, 10 lines); closing in clear "Dios g.de a V.S. mu.os
  an.os como deseo. El Pardo 30 de Nov.e 1718", signature "D. Mig.l F.z Duran" (Miguel Fernandez Duran, Secretario
  del Despacho de Guerra 1714-1720); addressee at the foot of the left leaf "S.r Marq.s de S.n Ph.e" (Vicente
  Bacallar y Sanna, marques de San Felipe, envoy at Genoa). Inferred (I): a despatch from the war secretariat to
  the envoy at Genoa three months after Cape Passaro; content unknown.
- Images: not committed; `images/manifest.json` lists every DECODE file used with size and hash. The full-size
  files are served without login for this record's access mode (25 requests, 1.8 s apart, 28 Sept 2026).

## Ciphertext (harvest/)

- Two blind passes by Sonnet subagents, one leaf per call, on line crops cut by ink profile
  (`tools/iiif_lines.py` found 0 lines at its defaults and 9/15 wrong lines at `--distance 110 --prominence 2`
  on these crops, so the strips were cut by a row-profile threshold instead; the 17 + 13 strips are the same
  shape the tool produces): `passA_f2r.tsv`, `passB_f2r.tsv`, `passA_f2v.tsv`, `passB_f2v.tsv`.
- Reconciled value-blind (no key in hand, so every decision was made on the digit shapes alone) into
  `ciphertext.tsv`: **309 tokens, 148 distinct; 281 agreed by both passes (A), 22 settled from the image by this
  worker (R), 6 uncertain (M); 1 token keeps a `?`**. Values 2-877; 181 tokens above 300, 112 above 530.
- Scribal shapes that drove the disagreements: 7 is written as a ")" stroke (both passes read it as 2 or 9 in four
  places: 307 twice, 597 twice); 5 as an "S"; 4 as a triangle. f2r line 5 has "23.2." with a dot inside what is
  probably one group 232 (kept as two tokens 23, 2, grade M). A third blind pass by a different reader on the
  ")"-shaped tokens is the cheap next transcription step.
- Most frequent: 163 (15), 32 (11), 544 (9), 551 (8), 222 (8), 594, 216, 652 (7 each).

## The keys (harvest/keys_range.tsv)

Nine Key records of the same fonds, Cajon 19 leg. 30 (docs 1, 2, 3, 5, 6, 8, 15, 16, 19; R10189-R10197,
1711-1718), all viewed on the image this session. Their value ranges: 231, 282, 288, 243, about 440, about 530,
210, 209 (+ nulls 333-337), 182. The largest is doc 8 (R10194), "Copia de la cifra que el Marques de Monteleon
entrego al Marques de Villamayor de orden de Su Mag., dada por el Marques de Mejorada en carta de 30 de Noviembre
de 1711, para la correspondencia con S.M. por la via de Estado y de las dos Secretarias del Despacho Politico y de
Guerra" -- the right key family for a letter from the war secretariat, but its sheet ends at 530 ("Vuestro" 530,
blank ruled column after it, checked on the right edge of the image) while 112 of the letter's 309 tokens are
above 530. A key reads all of a letter's tokens; none of the nine reads more than 64% by range. So the key is not
among the catalogued ones. Leg. 30 has 19 documents and DECODE catalogues nine: docs 4, 7, 9-14, 17 and 18 are
the first place to look (PARES is dead from the cloud; the ACA reading room or a PARES description from the
owner's machine, LOCAL-QUEUE shape).

## Search log (28 Sept 2026, gate of row 2)

- DECODE: R10181 Non-decrypted, no document attached in the listing; decode-catalog.csv (aaymeloglu raw file, fetched
  28 Sept 2026) same status. Records R10170-R10198 were added to DECODE most recently (Sept 2026).
- Bourdeau (raw README.md, CATALOGUE.md, SOLVED_CATALOGUE.md fetched 28 Sept 2026): no hit for "Genova",
  "Legacion", "R10181", "Duran", "San Felipe" as a target.
- aaymeloglu CATALOGUE.md (raw, 28 Sept 2026): no row for R10181.
- Cryptiana mirror (`sources/cryptiana/web`, grep "Fern.ndez Dur.n", "Legacion en Genova", "Duran"): no hit.
- Cipherbrain site search ("Fernandez Duran", "Genua 1718 Chiffre", "Archivo de la Corona de Aragon"): 0 results.
- Cipher Mysteries site search: reachable with a browser user agent; "Escriva", "Bethune", "Throckmorton",
  "Geertruidenberg" all "Nothing Found" (this letter's names not searched there separately; nothing on the site
  indexes the ACA).
- Printed: San Felipe's own Comentarios de la guerra de Espana (1725) narrates the period but prints no despatch
  text; not checked for this letter.

## While waiting

The one action that depends on nobody: a third blind pass on the 24 tokens graded R or M (one Sonnet call on the
same crops), and a frequency table against the 1711 key's alphabet block (values 1-60) to test whether the letter's
low values (32, 31, 33, 39, 40, 42, 49, 51, 56, 62, 75, 81, 87, 89, 91, 92) fall on that key's homophones for
vowels -- a partial-family test that would say whether the missing key is an extension of the 1711 one.

## Failure log

- `tools/iiif_lines.py` on a pre-cropped local JPEG: autocorrelation pitch came out at 21-28 px against a real
  pitch of about 160 px, 0 lines at defaults; with `--distance 110 --prominence 2` it found 9 of 17 and 15 of 10
  lines. The fallback row-profile cut is in the session notes, not a tool; if this recurs, the tool needs a
  `--pitch` override.

## Web and blog check (CS-A2-H, 3 Oct 2026)

- Web searches (4, WebSearch standard): "Fernández Durán" "marqués de San Felipe" 1718 carta cifra Génova; "Legación en Génova y Turín" Archivo de la Corona de Aragón Diversos cifra 1718; Bacallar San Felipe Génova 1718 despacho Fernández Durán cifra descifrada 30 noviembre 1718 El Pardo; a fourth in the same family. Hits: nothing naming this letter. Related only: Quirantes' study of Fogliani's 1747 cifra (revistas.um.es 613681), different cipher and date.
- Blogs: Cipherbrain site search "Fernández Durán" 0 results (200); Cryptiana blog search "Duran 1718" "No posts matching" (200); Cipher Mysteries search URL answered 406 Mod_Security to curl, not retried (so this blog is unreachable by search here; one web search covers it only indirectly). Comment threads not read (no post hit).
- DECODE: record 10181 page fetched without login, Status: Non-decrypted, 1718; AssociatedRecordsList for 10181 fetched (no associated record seen in the page text).
- Solver repositories (shallow clones, grep only): dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers: only a catalogue row for R10181 itself (Non-decrypted) in aaymeloglu catalogue/decode-records.jsonl; no target, key or planning line for Duran / San Felipe / Legación en Génova.
- Google Books API (country=US, keyed): one query, 2 items, none relevant by title. Internet Archive advancedsearch: 2 queries, no relevant item inspected (count not read). Not a whole-volume sweep.
- Not done: ACA catalogue/PARES description (unreachable), HTRC test (no candidate calendar named), any printed edition.

## Premise check (CS-A2-H, 3 Oct 2026)

- (a) folder's own files: NOTES.md and README.md mention no decipherment, gloss or clear copy of this letter; not found. The earlier worker's cover/closing reading is the only clear text.
- (b) other solvers' working files: nothing on this item in either repository beyond the DECODE catalogue row; not found.
- (c) physical neighbours: the record has 4 DECODE images (cover, two text leaves and one more); the earlier worker viewed them; this worker did not re-view the images, so a pasted slip or facing-page copy is not independently excluded; unreachable/unchecked by this worker.
- (d) recipient/sender-side editions: San Felipe's Comentarios (1725) narrates the period, prints no despatch text per the earlier worker, unopened by this worker; no Spanish state-series edition identified; unreachable/unchecked.

Verdict: stays `blocked`. What would move it: the ACA reading-room or PARES description of leg. 22 doc. 67 and of leg. 30 docs 4, 7, 9-14, 17, 18 (owner's machine, LOCAL-QUEUE shape), and a full-text pass of the Comentarios. Nothing found to say the item is read. No class (rule 10).

## CS-BATCH4 pass (3 Oct 2026)

Re-checked for an opened edition: IA advancedsearch for San Felipe's Comentarios de la guerra de Espana returned no item (1 request), so no edition could be opened; ACA/PARES still unreachable from the cloud. Nothing new. Verdict unchanged: `blocked`; next step remains the owner-side ACA/PARES description of leg. 22 doc. 67 and leg. 30 docs 4, 7, 9-14, 17, 18 (LOCAL-QUEUE shape). The "While waiting" third-pass step above still stands.
