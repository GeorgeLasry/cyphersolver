# Re-reading log, no. 4 (DECODE R4793) (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b25)

## Starting point

Reading audit (22 Oct): "decoded, not read": the first runs complete their clear sentences, the second paragraph
(ll. 17-24: Antonio d'Arezzo, the Pope, the clergy, the Turk) is runs, code words and '?' between doubtful clear
words. No reading body existed (`no04_reading.txt` is a run list + running text with '?').

## What was done

1. **DECODE record** R4793 fetched again with the cookie (research/reading_audit/b25_fetch.py): two images (P1
   address, P2 letter), no DOC_ attachment, no comment block; record metadata wrong (name Concistoro_2308_47, dates
   1500-1599; already noted for the queue). Neighbouring records R4790-R4814 are the other fasc. 2 pieces, each in
   its own key (research/siena2308/README.md); none is a clear copy of no. 4.
2. **Key in the archive**: the six 1450s keys of fasc. 1 were tested on 24 Sept (none fits); the alphabet fragment on
   the letter itself is the key. Nothing new.
3. **Print**: Senatore 2009 cites the letter; no edition of its text found (web search 23 Oct 2026).
4. **Re-read on the image**, ll. 17-24, per-line crops at 1.9-3x (scratchpad only). Gains:
   - gloss over *pedesi* (l. 18) reads **"Iacopino"** (24 Sept: "sa? più"): pedesi = Iacopo Piccinino;
   - gloss over *cras* (l. 17) reads **"a pace"**, and over the l. 18 *cras* "pace": cras = pace (24 Sept: parte);
   - gloss over `q_foot <toffe>` (l. 19) confirmed **"al papa"**;
   - l. 17 the run before *Calor* is `4 longs` = EL ("el duca"), not `A longs`;
   - l. 19/20: "che non aveva anche permesso ne al papa ne a cardinali se ne pigliasse": `a 4 3 <vapor>` = NE A
     <cardinali> by the fragment values a = n, 4 = e, 3 = a.
   Key changes (code words only; each rests on a gloss, both occurrences of cras agree): cras = pace, pedesi =
   Iacopino. Logged in keys/no04_key.txt.
5. **Clear hand of ll. 20-23** re-read at 2.2x: "uno giorno in altro modo miss. p. ve. ad quas instituit", "est. i.
   nt. volent^a instructi? ricoprimento e poi per bisognando contra lo Turcho tantudi?", "vernit. di sho?", "...to
   aussurumi? e chosi adisse tutto": the rapid cursive and its abbreviations do not resolve into words beyond those
   given in the reading; no further gain.
6. **Reading** written as `no04_reading.md` (whole letter, holes marked; one supplied word "[el] papa"), English
   `no04_en.md`. Alignment: every cipher-run word is carried by the fragment values or a gloss; clear words marked
   [?] where the hand is doubtful. Look-alike alternates: none chosen in the runs read (the 19 unread signs are left
   unread); 0 letters rest on a look-alike alternate.
7. **Score** (research/reading_audit/b17_score.py, LANG_=it, reading body = whole letter): **0.594 (19/32)**;
   explicit holes (HOLES=1) **0.719 (23/32)**. Before: no reading body (0.00; the audit's verdict "decoded, not
   read"). The `es` list gives 0.0 (wrong language). 

## Result

Stays **decoded, not read**. The first, third and closing paragraphs hold with scattered holes, but the second
paragraph (ll. 17-24) still does not build sentences after its first one ("Antonio d'Arezzo qua era detto el duca
essere bene disposto et a Lucca et a pace"): the doubtful clear hand of ll. 20-23 and the unread signs leave its
sentences half holes. The score sits at the bar but the reader's test fails for that paragraph.

## Open

- ll. 18-23, the rapid clear hand around the runs (abbreviations "miss. p. ve.", "ad quas instituit", "volent^a",
  "tantudi", "vernit", "aussurumi"): blocker illegible (re-read at 2-3x; the DECODE image, 2248 px wide, is the only one).
- the 19 rare cipher signs (`4 x T_long` l. 18, `+ + R · delta B` l. 24, ...) and toffe/vapor beyond their glosses:
  blocker too-short.
