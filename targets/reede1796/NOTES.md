# Van Reede's code passages to the Hereditary Prince, 1796-1807 (KHA A35-1232, A32-549)

Status: in progress

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

## Remaining gaps

- The nine passages above (about 580 groups) - blocker: no-key-material; neither the 1789-92 table nor the 1795-96 Euler list fits the glossed controls, and the glossed values (about 15) are too few to rebuild the 1796 or 1797-1801 codes

## Escalation

- [x] siblings: all of A35-1232 and A32-549 paired (k89 pairing files); glossed controls transcribed
- [x] clear-pages: the Prince's draft replies 144386 checked; the other drafts (144342, 144346, 144354, 144356, 144359, 144375) not yet opened at full size
- [x] known-keys: reede1789 table and the Euler list tested on the controls; neither fits
- [x] print: Colenbrander GS II (1795-98) and III (1798-1801) full text searched: no letter of Van Reede to the Erfprins printed (the hits are Pieter Vreede)
- [ ] key-rebuild: not done; too few glosses
- [ ] retry: not done

## Log

- 26 Oct 2026: target opened; nine unread passages and four glossed controls transcribed; both known keys tested, no fit.
