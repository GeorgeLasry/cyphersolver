# R3815 re-read log (batch b06, 22 Oct 2026, Claude Opus 5.5)

## Is there a text already?

No. No DECODE transcription or key; no interlinear or margin decipherment on the images (P1 right, P2 left checked on
crops); Mírka 2012 read only R3811. read/SUMMARY_R3815.md is our own September summary (guide only).

## Page order

The images are spreads: the letter runs P1 right, P3 left, P3 right, P2 left, P2 right (date and close). P3 ends "und
ob" and P2 left goes on "... nicht ... manglen lassen". The reading follows the letter; the aligner was run per
paragraph (b06_align.py --para) because the decode stream follows the image order.

## Transcription (read/R3815_corrections.tsv, 9 rows; tr/IMG_R3815_*.txt edited in place)

- `p` after 27 relabelled #f-cross (ta): Maiestat, tausent, statum, Craistag (4).
- `6` before 25/11 = φ (zu beantworten, zu lassen) (2).
- Clear text corrected on the images: "replicirt" (not resolviret), "nach Lüneburg hab ich noch khein antwort bekommen,
  und ist auch" (not "nach Wien bringen habe ... es auch").

## Key observations (proposals; key.json not changed)

- `p` = vi in [?salvum] (α 33 p 11 π) and [?resolviren] (resol p ren), as in R4625 and R3814.
- `9` = vo in "einem [?von] acht bis in neun tausent", as in R4625.
- `m` after 29 = a ("quam fundamenti").

## Reading

read/R3815_reading.md, read/R3815_en.md. b06_align.py --para: 0 words not carried. b06_score.py (body only):
clean share 0.62 (28 of 45 sentences), hole rate 0.15. Before: the deciphered runs were unspaced (audit: decoded,
not read). Much of the clean share is the clear German that frames the cipher; the deciphered sentences carry the
argument (the army left to perish waiting for the Circle; 8-9,000 men against a starved enemy; Denmark perplexed and
temporising to avoid the conjunction) with about fifteen holes.

## Stays open

"uberfturohrenereltbehette" (P1), "mitzulolechungdesgraventenhalefelds" (P3), "sowsseu", "mittu", "nqum fundamenti",
"lo in" after perplez, "trintgen", "puschwritficirtt", "wafenallon?nrung", "amre hint", "velgtkinlest" (P2). The
figures are legible; blocker is labour (a further image pass on P3 and P2) and the key questions above.

Result: meets the step-4 bar narrowly (0.62); the sentences cohere apart from the runs listed.

## Second pass (parent session, 22 Oct 2026)

- Key corrected for all nine letters after kwic checks across the whole corpus (the parent session, from the
  sub-sessions' proposals): 38 = d (feindt, und, landt; was g), Δ = nu (warnung, hoffnung, nun; was e), #dot = su
  (sufficient, subsidia, verfassung; was null), #s-long = ti (militaria, resolution, obligation; was t), m = a (after
  29: quartier, quam, quando; was null). In this letter's hand #s-long, #dot, p and λ also stand as flourishes before
  c/h/g/t; read as nulls where they do (sach, furst, absonderlich, erfolgenden).
- Every cipher line of P1-P3 checked on full-resolution crops (scratchpad r3815_*.jpg). Seven label fixes and twelve
  clear-text fixes (rows 11-28 of R3815_corrections.tsv): λ (not #l-loop) in "uber frohrener Elbe"; φ 16 19 (not 61 61 19)
  in "zuziechung"; φ in Hazfelds, Herzog and "zu recognosciren"; ψ (not the 4-hook) in "die zeit erleidet"; #f-cross in
  "standt"; clear "dess Salvij alhier", "auch dem Craisstag bey wohnen", "weil sich der", "So hat auch", and the close
  on P2 right.
- Reading rewritten; paragraphs split at the page joins for the per-paragraph aligner. b06_align.py --para: 0 words not
  carried. b06_body_score.py: clean share 0.62 -> 0.667 (32 of 48 sentences), hole rate 0.13.
- Still unread (no value fits, one occurrence each; figures legible): see the reading's Notes. Not an outside blocker:
  these need a sign value nothing else in the corpus gives; another reader may see them.

Result: read (grade B): the sentences cohere and translate; clean share 0.667.
- 9v = vo (polyphonic 9, same shape) added to key.json by the parent session; three R3815 tokens relabelled (von nothen, Graven von Hazfelds, einem von acht); score 0.667 after (hole rate 0.128).
- pv = vi (crossed long-s) added to key.json; two R3815 tokens relabelled (resolviren, irresolvirt).

## r2c (23 Oct 2026, Claude Opus 5.5)

Key k = to (quam fundamento) and m = va (29 + m = qua) after the check against Mírka's key on DECODE R3813/R3814 (KEY.md). The Salvium `p` (I27184 P2 l. l.5) is the curled p-form, relabelled pv: "salvium". b06_align.py --para 0 flags.
