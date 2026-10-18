# No. 18 (R4806): the project's key (24 Sept 2026) against George Lasry's (17 Oct 2026)

Two independent ciphertext-only solutions of one key. Ours: `transcripts/no18v.txt` (signs), `keys/no18_key.txt`
(solver output) and the final key at the end of `transcripts/no18_reading.txt`. His: the key figure in
`lasry_report.md` (signs cut from the manuscript, `docs/siena18_key.png`). The comparison below was made on 18 Oct
2026 by matching his cut signs by eye to our sign names (legend in `no18v.txt`); his figure has no sign names, so
the pairing of shapes is ours.

## Sign by sign

His key has 60 signs: 32 letter signs, 6 doubled-letter signs, 5 code capitals, 17 nulls and separators.
Our transcription has 30 sign names plus the dotted variants, which we treated as nulls.

| letter | his sign (occurrences) | our sign name | our value | agreement |
|---|---|---|---|---|
| a | 4 (90) | 4 | a | same |
| a | 7 (27) | 7 | a | same |
| b | long s with a dot (23) | S | b | same |
| c | 3-shape (45) | 3 | c | same |
| d | 9 (41) | 9 | d | same |
| e | + (177) | + | e | same |
| e | n, plain (4) | n (plain form) | e | same (we split it from the hooked n on the images) |
| e | dash (2) | - | e | same |
| f | 6 (14) | 6 | f | same |
| g | O, plain (12) | o (plain form) | g | same (split on the images) |
| h | 2 (2) | 2 | h | same |
| i | ⊣ (134) | T | i | same |
| i | open double loop (15) | OO (open) | i | same (split on the images) |
| i | d (4) | d | i | same |
| l | Γ (26) | F | l | same |
| m | ᴜ-shape (61) | U | m | same |
| m | small ш (7) | W | n / m | value same in the words we read with m; we did not separate the glyph from W |
| n | ш (112) | W | n | same |
| o | o with lead-in (42) | o ("-o" form) | o | same |
| o | 8 (26) | 8 | o | same |
| p | ⊢ (31) | L | p | same |
| q | hooked ∩ (20) | n (hooked form) | q | same |
| q | hooked 7-like form (6) | transcribed 7, corrected to n | q | value same (quot, querelis, quinque); we merged the glyph with n |
| r | ɔ (104) | D | r | same |
| r | 2-like form (1) | "2?" in armature | unread | ours open, his r |
| s | ɧ (96) | h | s | same |
| t | П (126) | N | t | same |
| u | γ (112) | Y | u | same |
| u | U with a dot (16) | U after q | u | value same; we kept it under U (m) and read u after q |
| u | a (3) | a | u | same |
| u | hooked a (1) | (not separated) | - | not in ours |
| x | H (7) | H | x (dotted H a null) | same |
| cc | low hook (2) | TRI | c | differs: his cc, our single c |
| ll | closed double loop (11) | OO (closed) | ll | same |
| pp | φ (2) | PHI | pp | same |
| rr | struck h (6) | HX | rr | same |
| ss | ꝗ-like (3) | Q | ss | same |
| tt | rounded ω (3) | ω (rounded W) | tt (doubtful) | same |

**Letter and doubled-letter signs: 38 in his key. Same value in ours: 35 of 38** (32 as signs we had named
separately, 3 as glyphs our transcription merged with a look-alike but read with his value from context). Differs:
1 (cc, which we read as c). Not in ours: 2 single-occurrence signs (his second r, which sits on the paper flaw of
*armature* that we left unread, and the hooked a).

Nulls: both keys treat dotted or barred signs as nulls (his 16 kinds, 47 occurrences, counted off his figure; ours "dotted signs are mostly
nulls"). The separator dot (his 181) is our point between words. Code capitals: both leave B., X., S. and M.X. in
clear and unresolved; his m. is our n.; his conjectures (B = Sanctissima Liga, M.X. = Maiestas) are new.

## Reading: where his text covers what ours left open

Grades (README Conventions): **H** read from a key, **C** from a known plaintext, **M** uncertain, **I** inferred
from context. His readings below are graded as they stand against our transcription and key; nothing was re-read on
the images for this comparison.

| place (ours) | ours (24 Sept) | his (17 Oct) | grade of his reading |
|---|---|---|---|
| P1 L1.1 | [.. telamonem?] unread | Telamonem | M (first word of the page, damaged) |
| P1 L1.2 | struck word "ionordi[..]nem" | in ordinem (not struck) | H; the key gives it, the stroke is the scribe's |
| P1 L1.2 | ponant?, pulueres? | ponant, pulveres | H (both read the + as p) |
| P1 L1.14 | [B.] [..] queue(x)? | [B]. que | H with a null; ours unread |
| P1 L1.24, L1.26 | [PX] unread | ✱ unread | both open |
| P3 L3.5 | PASSO? FEDUS | pax, fedus seu aliqua intelligentia | M; better sense than ours (pax beside fedus, intelligentia) |
| P3 L3.6 | c(e)um? | cum | H |
| P3 L3.10 | armature? | armature | H (his second r sign) |
| P4 L4.13 | defendam | defendat | H; ours a misread final sign |
| P4 L4.11 | cum [..] B. | cum s[anctissima]? [B]. | M (his own query) |
| P4 L4.19 | quoti solueret | quote solveret | H |
| P4 L4.20 | imponentur n. et Mx. | imponitur [m.] et [M.X.] | H for the cipher word; m./n. unresolved in both |
| P4 L4.27 | Senensibus [..] competit | Senensibus ius competit | H; ours unread |
| P4 L4.29, 4.30 | coram ÷; ÷ & B. | coram ÷; ÷ et [B]. | both open |
| P4 L4.2 | habeat? | habeat | H |

Clear-text differences (not cipher, so not counted): his *poterint* for our *potuimus*, *ad quas Sua Maiestas*
for *adque suam Maiestatem*, *competenti* for *capitanei(?)*, *veniret moderanda* for *venirent moderando*, *tamen
deo* for *hoc deo*, *cum quo* for *omni quo*. His readings make the Latin grammatical where ours did not.

## Dating and order

Ours: 1510s-1520s, not fixed (Ziegler, a King and an Emperor as two parties, Ponte a Valiano). His: Pisa, November
1496, fixed by Maximilian I's stay at Pisa, Ziegler's secretaryship from 1494, the Holy League of 1495 (the Pope's
half quota) and the Sienese attacks on the Florentine bastion at Ponte a Valiano in 1496, with Regesta Imperii XIV,
Pecci and Sanudo cited. His dating replaces ours. His page order is P4, P3, P1 (P4 carries "Primo loco petita");
ours ran P1, P3, P4. His order is the order of the negotiation.

## Counts

His: 1,469 cipher signs, 181 separator dots, 144 clear stretches. Ours: 1,459 tokens (reading file count), 1,456
(prep script). His full decryption leaves six single signs unread (÷ four times, ✱ twice) and one query
(s[anctissima]?).
