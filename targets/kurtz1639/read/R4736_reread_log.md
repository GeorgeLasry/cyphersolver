# R4736 re-read log (b06, 22 Oct 2026, Claude Opus 5.5)

Starting point: read/R4736.txt, unspaced key decode (1,403 tokens; P1 and P3, P2 an address leaf); state "decoded, not
read"; the weakest letter by eye (mixed German, Latin, Italian).

## 1. Is there a text already?

No gloss, slip or clear copy on the three images; no edition known. Read on the images.

## 2. Read on the image

All cipher lines of P1 and P3 (both halves) viewed on crops (scratchpad reread/b06/r4736_*.jpg). The transcription
holds; one label corrected (α -> #a-loop, "im sinn") and two clear lines re-read (salutation, "Glückstatt den 14.
April 1639") (read/R4736_corrections.tsv). The garble that remains is not misread figures but sign values.

## 3. Key observations (proposals; key.json not edited)

Read through this letter the sense needs, sign by sign: Δ = nu (dignum, nuzen, hoffnung), #dot = su (sub spe), 9 31 =
von (herr von Stralendorf, pas von Ihr Kay. Mtt.), #sect = z (Penz, zu obligiren), #hash = x (ex imperio, ex
factis), #s-long = ti (militis, optimo, etiam, satisfaction, negotium, interessati, stil, contenti), and the small
x-like sign = su (Suecos, transmissa sunt), vi (videt, villeicht, vil), ta (Glückstatt) besides i. The same values
recur in R3811 and R4645 (their logs). Together they would turn most of the remaining holes into words; they are not
applied because key.json is shared by all nine letters and the x and #sect splits need a sign-by-sign image pass.

## 4. Reading

read/R4736_reading.md, English read/R4736_en.md. Aligner: 5 flags, all words carried only under #s-long = ti (noted).
_check_reading.py on the body: 0.512 (41 sentences, 21 clean, hole rate 0.188). Below the bar: stays **decoded, not
read**.

## 5. What stays open and why

The Latin and Italian runs listed in the reading's Notes, which wait on the sign values above (blocker: a key
revision across all letters and a re-transcription that splits the x and #sect signs; labour, not the images); the
postscript and the gutter note in Kurz's cursive.

## Second pass (parent session, 22 Oct 2026)

- Key corrected for all letters (Δ = nu, #dot = su, #s-long = ti, 38 = d, m = a); the reading's [nu]/[su] brackets
  removed where the key now carries them (hofnung, dignum, nuzen, super, sub spe).
- Crops of P1 (lines 14-24) and P3 right (lines 44-49): "vel no[vu]m bellum", "penitus ener[v]atis omnia", "ich [?were]
  nie der enden gewesen", "einziges [?vom] konig erfo[l]genden gueten die[n]sts", "Dan ist [?darvon] wurden",
  "regi. Hof, sie sollen durch komben", "re[x]" (#hash = x), "[?vormauren]" (9 = vo).
- b06_align.py: 0 words not carried. b06_body_score.py: 0.512 -> 0.591 (26 of 44 sentences; hole rate 0.18). The
  sentences that fail are mostly Latin and Italian (the word list is German) and proper names.
- Open: "quid consilii [...] armorum zu [...]" (dotted signs before 85 and 15 on P1 l. 7), "E. Chf. Dhl. [...] pro
  semper", "uns [...] Pommeren" (3? u n s 6 18 78 #z-tail), "alli altri [?scoppa]", "lentra i gnadi", the postscript
  and margin note in Kurz's cursive (image blocker). No value in the key fits the remaining runs.

## 6. Second pass (22 Oct 2026, after the key revision)

The parent session applied the key of 22 Oct (38 = d, Δ = nu, #dot = su, #s-long = ti, m = a, 9v = vo) and edited the
reading from crops. This pass relabelled five figures 9 -> 9v where te makes no word and vo does (vormauren, darvon,
vom konig, herr von Stralendorf, den pas von Ihr Kay. Mtt.; read/R4736_corrections.tsv), re-ran decode.py R4736, and
wrote those words plain (reading and English). Aligner: 0 flags. Score 0.636 (44 sentences, 28 clean, hole rate
0.166): meets the bar, **read** (grade B). Open: the runs listed in the reading's Notes and the cursive postscript.
