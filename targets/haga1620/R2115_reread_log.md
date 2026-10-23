# Re-reading log, R2115 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b28)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R2115_reading.md` was a partial reading: clear text given as `[...]`
where not transcribed, the P2 and P4 cipher spans strings of `{?...}`, and the page order wrong.

## 1. Is there a text already? No

- DECODE R2113, R2114, R2115, R2118 re-fetched with the project cookie (`research/reading_audit/b28_fetch.py`, DOC_
  attachments only, scratchpad `reread/haga/`): no DOC_ attachment, no comment block, no plaintext on any of them; R2115
  holds only its four images (I15012-I15015, already in the main checkout `targets/haga1620/decode/`).
- No contemporary decipherment: the cipher spans carry no interlinear gloss, and R2114 (11 May 1620, "Decrypted" on
  DECODE) is a different letter with no plaintext file.
- Print: a web search for an edition of Haga's 1620 despatches found none (Wikipedia, NNBW, CSP Venice index entries
  only). Not in Heeringa's Levant trade sources as far as known (that series prints trade letters).
- The key itself is DECODE R2118, filed in the same NA inventory number; nothing else needed.

## 2. Read on the image

All four pages read line by line from native-resolution crops (`b28_strips.py`: rotated -90, half-width strips of
three lines at 0.85; `b28_crop.py` for single words at 1.0-1.6). Clear Dutch transcribed in full (the earlier file had
it in summary). Cipher read sign by sign with the R2118 alphabet:

| page | cipher spans | what changed against the old reading |
|---|---|---|
| P3 | 8 | "m?i?tt?i?nge? d?ian? tii?t?" = **winninge van tijt** (the doubled sign is the crossed t-shape, i.e. n, not the long t); "[62] a?n?mme? n?ieus?" = **om [62] alomme odieus te maecken** |
| P4 | 6 | "die, onder? conservatie" = **die inde conservatie vande**; "scheen te willen overgeven?" = **scheen te willen favoriseren**; "tot overdrag? Bohemia? van [62] ende [46] ge?ei?s? heb ick vo?rderen?" = **tot faveur regis Bohemiae van [62] ende [46] gedisponeert heb, in vougen dat** |
| P2 | 25 | **Ungarie soude aennemen**, **op mijn versocht**, **arbeiden**, **coempt [58] alleen toe**, **wert de besendinge vanden siaus ende [15] aen [43] te doen van tijt tot tijt gediffereert**, "vergee?fs?" = **verhoepe**, **nablijven**, "geconformeert" = **geinformeert**, "vanden paus?" = **vanden siaus** |
| P1 | 4 | "om het s?ee?l? ... bussen? aen te verderven" = **om het spel in ... met sodanigen bulleman te verderven** |

`R2115_cipher_spans.tsv` lists the 43 spans (599 letters) with the look-alike resolutions and the old readings. No
key value changed: m = the 4-shaped sign (NOTES, 21 Sept) holds in **vermanen, teenemael, maecken, alomme, gemackt,
coempt, geinformeert** (every occurrence). The hand's sign pairs that look alike — l (2 with a loop) / s (the key's z,
written 2-like), n (crossed t) / t (long ʃ), i (key ɐ, written like æ) / p (a C with a hook) — were resolved per word;
13 letters rest on such a look-alike alternate (winninge nn, ende n, aennemen nn, op p, siaus s, last l, alomme l,
bulleman ll, om o, vougen u).

**Page order corrected**: P3 (opening of 24 April), P4 top (its end, dated "xxiiij Aprilis 1620"), P4 bottom (opening
of the May letter), P2 (P4 ends "den Vizir, Mufti," and P2 begins "Choggia, ende Janitsaraga"), P1 (P2 ends "daer mede
voor-" and P1 begins "heeft"). NOTES had P3, P2, P4, P1. The May letter's date on P1 reads "den [?vij] Meij 1620";
DECODE gives 4 May.

## 3. Word-by-word alignment

`research/reading_audit/b28_haga_align.py`: every span's words are found in the reading body, in order (43/43). Every
other word is clear text transcribed from the image. Words not fully carried are `[?word]` (19: the date "xvj", the
envoys' title "Commissen" twice, "tselvige", "gejouisseert", "haere", the audience date, "hier", "seeckere", "best",
"geweest", "goet", "eenige jaren", "Hier mede", "Oppersten", "heeren", "erwelen", "verlies", "eijnde", "Met", "te
geleijden", "selvige", "vij"); `[…]` once; no supplied word. Codes: [3], [7], [19], [43], [58], [62] given as the
key's words; [15] (key: "Bassa van Babilonia", does not fit) and [46] (a heading fragment on the key) left as numbers.

## 4. Score and judgement

`research/reading_audit/b17_score.py`, LANG_=nl, reading body: **0.023 (2/86)** on the checker's modern Gutenberg Dutch
word list, which does not know 1620 spelling (uersocht, geinformeert, tijt, sijn all count as unknown); explicit holes
only (HOLES=1): **0.942 (81/86)**. Before: the audit's partial file (decoded, not read). Reader's judgement: every
sentence builds as Dutch, the cipher clauses included (the argument for gaining time and electing a Hungarian king,
the warning against Imperial rumours, the honour of the resolution to the States, the delayed chiaus, the "bulleman").
Set **read, grade B** (scattered `[?]` words in the clear and two unidentified codes).

## Open

- [15], [46]: the key's values do not fit or are illegible on the photograph — blocker: no-key-material.
- [?…] (the audience date, P3) and the [?] clear words above — blocker: illegible (photograph resolution, tight hand).
