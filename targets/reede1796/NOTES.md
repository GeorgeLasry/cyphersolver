# Van Reede's code passages to the Hereditary Prince, 1796-1807 (KHA A35-1232, A32-549)

Status: attempted, open (26 Oct 2026): the 1796 "Chiffre Litteral" is a book code and the book is unknown; the 1797-1801 list cannot be rebuilt from the few glosses

Koninklijk Huisarchief, The Hague: A35-1232 (A.W. van Reede to the future Willem I, 1788-1814) and A32-549 (Van Reede
to Princess Wilhelmina, 1796-1814). Found in the KHA sweep (research/nationaal_archief, leads K8/K9; pairing files
`research/nationaal_archief/k89/pairs_A35-1232.tsv`, `pairs_A32-549.tsv`).

## The passages

Transcribed at full size (`BRIEF.md`; `runs_a.txt` for A35-1232 1796, `runs_b.txt` for the later pages; images in
`full/`, git-ignored). Unread, with no decipherment:

| Page | Date | Groups | Note |
|---|---|---|---|
| 143592 | Jan-Feb 1796 | 78 in 14 runs | black overt letter over brown invisible ink |
| 143603 | Feb 1796 | 50 | rows of figures over an invisible-ink letter |
| 144339 | P.S., Jan 1796 | 54 + signs | the "petit chiffre"; warns not to confuse "valeurs reelles" and "indicateurs" |
| 144352 | Blankenburg 5 July 1796 | 19 | |
| 144361 | "Precis" of the letter of 29 July 1796 | 127 in 3 blocks | sent in cipher because too long (144358) |
| 144448-49 | c. Dec 1801 | 73 | between lines of invisible ink on Haugwitz, the indemnity, Tuscany |
| 144507 | c. 1806-07 | 35 | over invisible ink |
| 171667 | 1797-98 | about 98 | dot-separated, some fractions and plus signs |
| 171744 | Berlin 5 Dec 1800/1801 | 46 | framed by "Votre chiffre primitif" |

Controls (glossed): 144358 (15 Aug 1796: 91 = Ivoy, 72 = du Duc, 13 = Athlone, 73 = Portland, 2 = de Luc), 144386
(the Prince's draft, 27 Sept 1796, meanings in parentheses: "la mission du Sr. Hammont ... ne pas ignorer", "la
Russie se declare et que"), 171692 and 171693 (1798, 6/52 = Haugwitz, "de Reede" over 53 53).

## Keys tested (26 Oct)

`test_keys.py` (log `test_keys.log`) decodes every run with (R) target reede1789's table, Van Reede's 1789-92 code to
Wilhelmina, and (E) target wilhelmina1795's 1795-96 Euler word list, and scores both on the 15 glossed control runs:
R puts 3 of 13 decoded pieces in their own gloss against 2 of 13 in another run's; E 3 of 32 against 0. Neither is
the code. The control values confirm it: in 1796 91 = Ivoy, 72 = Duc, 13 = Athlone (Euler 13 = difficile, reede1789
13 nothing); in 1798 6/52 = Haugwitz (Euler 52 = une, 169 = haugwitz). The 1801 groups run to 1951. These letters use
at least two other codes (1796 small numbers; 1797-1801 a larger list with prefixes and superscripts).

## The Prince's drafts and Van Reede's "Explication" (26 Oct)

The six draft pages were opened at full size (`full/`):
- 144342 "Chiffre a Mr de Reede, Berlin 11 Juin 1796", 144346, 144354 (Berlin 2 July 1796), 144356, 144375: the
  Prince's clear drafts of his own cipher letters to Van Reede (Russia, Kalitscheff, Elgin, the neutrality of North
  Germany, Haugwitz's proposals). No numbers: they are the plaintexts of letters whose enciphered versions went to
  Van Reede and are not in this file.
- 144359 is Van Reede's letter of 15 Aug 1796 (the cipher of 144358), with on its right page an **"Explication des
  chiffres employes dans la lettre; chaque trait indique que la phrase est finie, & qu'il faut passer au chiffre
  suivant"**: Ivoy - le Duc - envoye a Ivoy un memoire pour etablir & justifier les principes d'une nouvelle
  coalition basant sur la reconnoissance de Louis XVIII comme seul moyen d'inspirer de la confiance a la Prusse et de
  l'etablir generalement / Athlone - Duc de Portland - de Luc - Portland - le Duc - Ivoy - (3) qu'il n'y avoit rien a
  faire des que l'Angleterre n'adoptoit pas en plein la marche proposee ... In the letter: "Je me sers, Monseigneur,
  du Chiffre Litteral usite pour ma correspondance particuliere avec Elle", and dotted groups "39.97.16" and
  "29.17.19.37" in the text.

What it shows: run (1) of 144358, seven groups ("12 15' 72' 45' 92 171 319"), stands for a sentence of some 200
letters, so the groups are not letters or single words; with dotted three- and four-part groups and the name
"Chiffre Litteral", the 1796 system reads as a book code keyed to a printed text shared by Van Reede and the
Prince (page.line.word or similar). The text is not named. Single numbers (91 Ivoy, 72 Duc, 13 Athlone, 73 Portland,
2 de Luc) are a short name list beside it.

Retry: the 1796 passages cannot be decoded without the book; the Explication gives plaintext for the 15 Aug letter
only, too little to identify a book by itself (a book search would need candidate texts of 1790s London-Berlin
correspondence).

## The Explication, second half (26 Oct, escalation)

Run (4), "39.97.16", is explained as "de son voyage de Pyrmont"; run (5), "29.17.19.37", as "le Roi doit
s'applaudir de sa position, etre dispose a persister dans les principes actuels, & que d'apres cela le Duc croit
qu'il n'y a rien a faire, & est-il de tres mauvaise humeur". Four groups for some thirty words: each number points to
a whole phrase. The "Chiffre Litteral" is therefore a list of prepared phrases (or a text whose lines are those
phrases) made for this correspondence, not a dictionary or almanac; testing printed books cannot recover it.

## Remaining gaps

- The nine passages above (about 580 groups) - blocker: no-key-material; the 1796 "Chiffre Litteral" is a book code (seven groups for a 200-letter sentence, dotted page.line groups) and the book is unknown; the 1797-1801 pages use a larger list with prefixes and superscripts, glossed values too few; neither known table fits

## Escalation

- [x] siblings: all of A35-1232 and A32-549 paired (k89 pairing files); glossed controls transcribed
- [x] clear-pages: all six drafts opened: clear drafts of the Prince's outgoing cipher letters (no numbers), and Van Reede's Explication for 15 Aug 1796 (144359), which shows a book code
- [x] known-keys: reede1789 table and the Euler list tested on the controls; neither fits
- [x] print: Colenbrander GS II (1795-98) and III (1798-1801) full text searched: no letter of Van Reede to the Erfprins printed (the hits are Pieter Vreede)
- [x] key-rebuild: not possible without the book; the Explication's sentences give no word-level alignment
- [x] retry: 1796 passages re-examined against the Explication; not decodable without the book

## Log

- 26 Oct 2026: drafts opened; Explication found (144359); 1796 system identified as a book code.
- 26 Oct 2026: target opened; nine unread passages and four glossed controls transcribed; both known keys tested, no fit.
