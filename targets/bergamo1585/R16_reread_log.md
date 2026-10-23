# Re-reading log, R16 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b24)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R16_decryption.txt` (decode_with_key.py, Lasry's F18 alphabet +
Meister's names realigned from OCR) was a run-on block with an open `<nn>` group or slip in nearly every clause and two
"open codes" (18, 48).

## 1. Is there a text already? No decipherment; but the key's missing half was on the record

DECODE R15 and R16 fetched with the cookie (`research/reading_audit/b24_fetch.py`, scratchpad). R16's attachments:
D1610 and D1792 (TimB's transcription, twice), D3104 (the R15 decryption misfiled), D3105 (Lasry's key), **D3195 = a PDF
of Meister p. 324-325**, and D984-D987 (the clear covering letter, Paris 7 March 1586, "con cifra duplicata", which
reports on the clergy and the bull but does not repeat the cipher). D3195 prints the **whole Ragazzoni nomenclator**,
of which `meister324_nomenclator.txt` (from OCR) had only part: the plain names and words (78 Italia ... 10 Germania,
60 Monsignor di, 70 Ambasciatore di, 80 Nuntio di, 90 Principe di), x4+ (Cardinale ... 84+ denari, 94+ Galere), a
stroked x4 (14 Sua Santita, 24 Sua Maesta ...), hooked x6 (16 Avignone, 26 che/chi, 36 per ... 86 come), x8+ (quanti
... essere), struck x0 (10 essendo, 20 non, 30 lettere, 40 corriero, 50 risposta, 60 risolutione, 70 lega, 80 mente,
90 pace), dotted x4 (14 Religione Cattolica, 24 Catolici, 34 Heretici, 44 Guerra, 54 Lega, 64 Suspensione); "et" is
29, "con" a dotted 0. Written out in `key_ragazzoni_meister_full.txt`.

## 2. Decoder and image checks

`decode_with_key.py` took every lone 8 as the null, so the 8 of 84+ (denari), 86ꜧ (come), 80- (mente) vanished and
the following mark was left stranded ("<4+>", "<6¸>", "<0->"); "3^. 4" (dotted 34, Heretici) was split as 3 + "48
Duca di Parma". `research/reading_audit/b24_bg_decode.py` decodes by beam search over the tokens with the
it-cinquecento letter model: a lone 8 is a null only when it does not start a code; marked tokens join the digit
before them; names cost a fixed penalty. DECODE writes the stroked 4 as "2+" (22+ = 24 stroked, Sua Maesta; 12+ = Sua
Santita).

Every remaining break was looked at on line crops of IMG_R16_I95/I96 (`b24_bg_line.py`; line centres by ink
projection): 16 labels corrected (`R16_corrections.tsv`, `R16_transcription_corrected.txt`, `b24_bg_fix.py`), among
them l.4 "1?" = 7 (fermo), l.6 31 = 37 (vendere), l.8 01 = 07 (rispondere), l.17 a crossed 4 (apreso), l.34 "uers·48" =
uerso and "ogni", l.42 a plain 0 (resistere), l.44 a dotted 0 (congreg.), l.46 molto, l.54 tenta. Five are look-alikes:
the writer's 5 closes like an 8 (l.47 "l'aleenatione", l.50 "fata") and his 7 takes a hook DECODE reads as 6¸ (l.43
"ocorendo", l.55 "vedo"); l.40 "si e" (43, or 45). The heading reads 7 (not 3) March 1586, the date of the covering
letter. Output `R16_decode_b24.txt` (score -3373, 5 tokens dropped, every line printed under its number).

Key changes, each holding at every occurrence: 29 = et (Meister; Lasry's D3105 had "che": "Metz et una buona soma",
"di quanti, et l'ha fato vedere", "in cio, et mi oferisco"). Not changed: 18 = Duca di Ferrara, after 70 "Ambasciatore
di" (the Ferrarese ambassador; fits); 48 does not occur once the labels are corrected.

## 3. Reading and word check

`R16_reading.md` (words divided, v for the key's u|v, the clerk's spelling kept), English `R16_en.md`.
`b24_bg_check.py`: 428 words, all in the decode stream but one ("Ferrara": its group 18 is on the image, l.4, and was
dropped by the beam). No supplied words. Look-alike count: 5 letters (si [?e], [?ocorendo], [?l'aleenatione], [?fata],
[?vedo]).

## Result

| record | before (audit) | after: clean-sentence share of the body (b17_score.py, LANG_=it) | explicit holes | rests on |
|---|---|---|---|---|
| R16 | 0.00, decoded, not read | 0.757 (28/37) | 1.00 | figures under the full Meister/Ragazzoni key, 16 labels corrected |

Open: "[?futurum]" (futu + a dotted 3 and 9, not in the key) and the last eleven digits of f. 206v (no word): no key
material.
