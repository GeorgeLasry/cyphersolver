# Re-reading log, R1040 second part (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b19)

## Starting point

Reading audit (22 Oct): "decoded, not read": `R1040_second_key_machine_decipherment.txt` had a bracketed code in most
lines (about 700 of 5,956 groups without a value) and the last stretch was "fragments of Dutch, French and unread
codes".

## 1. Is there a text already?

- DECODE R1040's only attachment is DOC_R1040_D2396, the transcription already in `R1040_transcription.txt`. The 23
  images (main checkout `R1040_p*.png`) were opened on a contact sheet: no interlinear or marginal decipherment, no
  slip; clear text only in the docket (image 5453), a few clear lines on 5456-5457 (first part) and the close on 5475.
- NA 1.01.02 inv. 7408 and 1.02.13 inv. 158 have no scans online (checked by the parent session). No edition known.

## 2. The segment's extent: image 5474 is not in the 1765 key

The transcription's marks differ by page: 5453-5458 use single strokes, double strokes, underline and double
underline (DECODE's ^', ^'', ^_, ^__); 5460-5473 use the 1765 key's caret, circle, barred circle, two strokes and
underline (^^, ^o, ^+, ^'', ^_) and never ^' or ^__. Image 5474 again has ^' (56) and ^__ (89) and no caret or circle;
the 1765 key covers 69.5% of it, like 5453-5458 (59-70%), against 87-92% on 5460-5473; and the decode turns to nonsense
right after "het antwoort dat daar op geven is", the last words of 5473. So 5474 (331 groups) belongs to the first,
missing code. `decode_1765.py` now stops the 1765 segment at 5473: 5,625 groups (5459 from group 180, 5460-5473).

## 3. Context pass (values adopted, `R1040_B19` in `decode_1765.py`)

Each value was checked on every occurrence in this segment and in R1036 (`research/reading_audit/b19_kwic.py`). The R1038
scan cells for these codes are illegible on the photographs (DECODE has <IL>; the p4 column around 78 was looked at and
its numbers cannot be read), so the evidence is the contexts:

| code | value | evidence |
|---|---|---|
| 34^_ | in | 94x: (in)dicien, in het zekere, waar in, in den jaare, in Europa, (in)vlood, main-t-in-eeren |
| 21^^ | of | 32x: een plan of project, meer of minder, vyf of zes, of ook, of op eenige andere wyze, Rumantz-of |
| 78 | eenen | 25x after w: het hof van W-eenen; once after "h" (token 2369; h/w transcription slip suspected, not checked) |
| 15^_ | het hof van | 22x before W[eenen] or Vrankryk: dat/met/by/van het hof van Weenen |
| 81^_ | honderd | 12x: zeventien honderd vyf en tachtig; negen honderd man per regiment |
| 213^o | twee | 12x: Hertog van Twee-bruggen (Zweibrücken), Paltz Tweebruggen, voor twee jaar, twee vyfde, twee Esquadres |
| 922 | Hertog | 21x: den heer Hertog van Tweebruggen, by/met den Hertog, Hertog-lyke hof, aarts-Hertog Fransek |
| 343^_ | me | bequaa-me, gehey-me, la Me-diteranee; R1036 me-est overeenkomstig, mari-ti-me acte, zogenaamde me-n[ins] |
| 341^_ | mari | de marine (3x); R1036 maritime acte |
| 495^_ | mede | daarmede, waarmede, mede-deelen (3x), rapport mede voorgesteld |
| 800^_ | omstandigheden | veele andere omstandigheden, tyds omstandigheden (2x), embarrassante omstandigheden |
| 108^_ | il | voorgedeta-il-leerde (2x), Maxim-il-iaan (3x), versp-il-lingen, br-il-lanten |
| 152^" | at | leg-at-ionsraad, at-tribueeren, ge-at-tribueerd, iter-at-if |
| 339^_ | man | Ru-man-zow (3x incl. R1036), man-queeren, negen honderd man, geld-man-gel |
| 261^_ | im | Max-im-iliaan, an-im-ositeit, geh-e-im, gean-im-eerd, im-portant, gl-im-pige |
| 617^" | courier | de voorgemelde courier van Weenen, een courier van hier over Berlyn (5x; R1036 2x; scan "Cou...") |
| 3^_ | hoe | in hoe verre (3x), hoe zeer |
| 154^o | stel | werk-stel-lig maaken (3x), tegenover-stel-lingen |
| 141^_ | heden | zwaarig-heden, bedenkelyk-heden, doorlugtig-heden, [705^_]ig-heden |
| 178 | eerst | het eerst-e moment; R1038 scan reading "eerst" (high) |
| 38^_ | onderrigt | in het zekere onderrigt (1x), zal direct onderrigt wezen (2x) |
| 28^_ | ig | zwaar-ig-heid (5x), doorlugt-ig-heid (5x), werkstell-ig, afkeer-ig, toelaat-ig-heid, magt-ig; one unexplained (token 1355 "tot [ig]tydige") |
| 161 | t | DECODE "ta": Duy-t-sche (4x), beken-t, zoek-t, tex-t, t-riple, main-t-ineeren, aar-t-s, gedeel-t |
| 801^" | deel | DECODE "dut": oor-deel, ge-deel-te, voor-deel, mede-deel-en (10x; R1036 oordeelde) |
| 777^_ | niet | DECODE "nict?": 15x |
| 227^" | atie | DECODE "atic?": associ-atie, proclam-atie, situ-atie, oper-atie (18x; R1036 educatie) |
| 689 | formeeren | DECODE "formeean?": een haak/alliantie/associatie formeeren (4x) |
| 316^" | belang | DECODE "become?": zyne andere belang(en), hun belang, de belang en vue (4x; R1036 hun belang) |

Tried and not adopted (a value fails at least one occurrence): 120 (de/die/deze), 969^" (reeds?), 940 (houden: fits
"neutraal te houden", "binnen behoorlyke paalen te houden", "zig verzekerd houden" but not "veele [940] zig
persuaderen"), 851 (gehad: fails "plaats hebben [851] gebragt"), 690^_, 226 (plaats/koste), 7^_ ("de Heer van
[7^_]enfels" = Hofenfels, but "raad van [7^_]st" and "van [7^_] beide koning" do not fit "Ho"), 79^o (toe[stem]mingen,
letters do not join), 761^^, 40^_, 265^_, 5^^ ("ng", 5x, no single value), 831^_ ("meet": melden in "te meet en",
moet elsewhere). The French passages' unknown groups (931^^, 916^", 234^^ ...) were not attempted beyond the decode.

R1036 tokens whose value changed with these additions: 47, 1553 (617^" courier), 108 (178 eerst), 190 (161 t), 431
(227^" atie), 445 (339^_ man), 595 (341^_ mari), 597, 1259, 1705 (343^_ me), 1258 (316^" belang), 1270 (801^" deel).

## 4. Reading

`R1040_part2_reading.md` (with `R1040_part2_en.md`, decode `R1040_part2_decode.txt`): 5,386 of 5,625 groups have a
value. Word check (`b19_wordcheck.py` with `R1038_key_misreadings.tsv`): every unbracketed word is carried. The text: the
suspected Austro-French alliance and the attention of the Prussian and English envoys; Kaunitz's plan; the Bavarian
exchange and the Duke of Zweibrücken's refusal, the role of the late Hofenfels; France's position on the German
League; the Black Sea fleet scattered by the September storm; the state of the Russian army and navy; two squadrons
fitted out at Kronstadt; the Turkish war; a French report; Sweden and Denmark. The passage tokens 1384-1651 is written
twice (1652-1875).

Clean-sentence share of the reading body:

| measure | share |
|---|---|
| `docs/_check_reading.py` (modern Dutch word list) | 0.038 |
| `b17_score.py` LANG_=nl | 0.019 (6/311) |
| `b17_score.py` HOLES=1 (explicit holes only) | 0.666 (207/311) |

The checker's Dutch list fails 18th-century spelling and the code's own forms (zyn, Vrankryk, tegenvoordig, allientie),
as for battier1686 and dedem1788; the decision rests on the reading and the explicit holes. The Dutch paragraphs build
sentences (long and with holes, but the sense carries); the French quotations (tokens 2268-2350, 4460-4580,
5300-5575, about 8% of the groups) read only in part.

## Open

- About 240 groups without a value, mostly rare codes seen once or twice (too-short to fix from context) and the R1038
  cells that are illegible on the photographs (illegible).
- The French passages: the 1765 key's French entries are thin and many groups there have no value (no-key-material).
- Image 5474 and the first 1,928 groups: the missing first code (needs-physical-access: NA 1.02.13 inv. 158 not online).
