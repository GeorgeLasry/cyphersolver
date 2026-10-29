# Maffeo da Treviglio to Tamas Bakocz, Buda 30 Nov 1490 (MNL OL DL 46150), catalogue 1235

Status: in progress. Attempted, open: no transcription could be made (image access blocked), so no key was tested.

## The document
Hungarian National Archives (MNL OL), Diplomatikai Level­tar, DL 46150 (Q 10, Veghely collection), 30 Nov 1490, Latin
original with seal on the back, "Mapheus Trituliensis" to Tamas (Bakocz), bishop of Gyor; regest: 4 paper pages in secret
writing, probably Maffeo da Treviglio, Milanese envoy. Record: archives.hungaricana.hu/en/charters/228061/. No
publication or decipherment found (verification of 28 Oct 2026, research/verify_2026-10/e_swiss_austrian.json).
It is the Hungarian-side original of the Maffeo cipher family of targets/buda1489 (Milan copies, 1489-90), so Somogyi's
key and the original key R5411 (`../buda1489/key_R5411.md`) are the first things to test.

## What was done (28 Oct 2026)
1. Read buda1489 NOTES, key_R5411.md and the 1235 verification record. DECODE R5411 (the key) is already transcribed
   there; no DECODE record exists for DL 46150 itself.
2. Hungaricana viewer (`/en/charters/view/228061/`): five images: ceteri (colour target, 1), orig_1 (p. 1, 3668x3739
   px), orig_2 (spread of pp. 2-3), orig_3 (p. 4), sigil (seal). `/charters/view/228061/` on www.hungaricana.hu is 404.
3. **Blocker.** The viewer (OpenLayers `arc.imageview.DocView`) asks `static-cdn.hungaricana.hu/tile/imagesize/...` by
   XHR; in the built-in browser the CDN sends no Access-Control-Allow-Origin, the request is blocked, the main pane stays
   blank (console: CORS error, "Invalid JSON string"). The tile URLs are in addition encrypted client-side
   (`tile/image/<path>/<enciphered "n|zoom|x|y">`); I did not reproduce that, since it is the site's access control.
   No captcha or proof-of-work was met or bypassed.
4. The only reachable image is `/tile/thumb/...` at 829x512 for the pp. 2-3 spread (about 26 lines per page, dense
   cipher, no clear text visible). A sign is a few pixels wide there; nothing can be transcribed from it.

## What would unblock it
- The tile images fetched from a normal desktop browser, where the viewer renders (the CDN may allow its own origin
  or the user's browser), saved as image files for the three originals; or an image request to MNL OL.
- Then, per the plan: per-line crops, sign-by-sign transcription with `../buda1489/AGENT_BRIEF2.md` values, decode with
  R5411 (`../buda1489/decode.py`), score with `lang/` (`lm.best_language`, Italian/Latin models), extend by constrained
  annealing where the key only partly fits. Note the language question: the letter is described as Latin; the
  buda1489 key reads Italian, so a Latin plaintext in the same cipher would be a new finding (Maffeo wrote to a Hungarian
  bishop).

## Measured
Nothing: no ciphertext file exists (`transcription/README.md`).

## Remaining gaps
- all four cipher pages of DL 46150 - blocker: illegible (no usable images; viewer blocked by CORS, thumbnails only)

## Escalation
- [x] siblings: buda1489 (Milan copies of the same cipher) and its key R5411 identified; not yet testable
- [x] clear-pages: none known for this letter; none visible on the thumbnail
- [x] known-keys: R5411 and Somogyi's key are the candidates; not applied (no transcription)
- [x] print: no publication found (28 Oct 2026 verification)
- [ ] key-rebuild: needs a transcription first - blocker: not-attempted
- [ ] retry: with images from a working browser or an MNL OL request - blocker: not-attempted
