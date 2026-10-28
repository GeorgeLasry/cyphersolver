# Prince Jabłonowski at Berlin → Stanisław August, 1791-1792 (Unsolved Catalogue no. 430)

Status: no write-up. Blocked on access: not digitised online (AGAD Zbiór Popielów 63 has no album on agadd2 and no letter list; szukajwarchiwach is behind a bot check).

Blocked on images. Nothing below rests on a sight of the letters.

## The document

- AGAD Warszawa, Zbiór Popielów (zesp. 12), sygn. 63; old sygn. N. 293, 370, 317. Inventory:
  https://www.agad.gov.pl/inwentarze/ZbPopiel12.xml
- Inventory title, in full: "Xżę Jabłonowski w Berlinie 1791 et 1792". Korespondencja polityczna prowadzona przez
  księcia Jabłonowskiego z Berlina z JKMcią Stanisławem Augustem częściowo szyfrowa (pismo cyfrowe) - pisane
  wyłącznie po francusku. Description: fascicle of loose papers, 123 pieces, k. 273, k. 152 missing. Language French.
  No decipherment and no microfilm number are noted.
- The writer is most likely Stanisław Jabłonowski (1762–1822), Polish envoy at Berlin 1789–1792 (Deutsche
  Biographie, "Jablonowski, von", https://www.deutsche-biographie.de/sfz36580.html). Not confirmed from the letters.

## Access (checked 28 Oct 2026)

- `https://www.agad.gov.pl/inwentarze/ZbPop63.xml` returns a 9-byte empty page: no letter-level list, unlike ZbPop
  4, 5, 17, 413-421, 428.
- The AGAD scan server album index `http://agadd2.home.net.pl/metrykalia/12/album/` lists only twelve Popiel units:
  4, 5, 17, 413, 414, 415, 416, 417, 419, 420, 421, 428 (6,869 images, modified 4 Apr 2025). `.../album/63/...`
  is 404.
- Not scanned there either: the Berlin siblings (Zabłocki cipher files ZbPop 13, 14, 20, 21, 423; Zabłocki with the
  King's replies 372, 373; Ignacy Potocki at Berlin in 392) and the cabinet keys (445/452 Kwilecki, Berlin 1772;
  451; 453-454).
- szukajwarchiwach.gov.pl: behind an Imperva checkbox check (research/polish_archives/README.md). Not tried again;
  solving bot checks is off-limits. A person can open it and look for fonds 1/12 sygn. 63.
- Not on DECODE; not in the repo before this folder.

## Prior art

None found. Web searches on 28 Oct 2026 (Jabłonowski + Berlin 1791/1792 + Stanisław August + szyfr; the IH PAN
"Korespondencja polityczna Stanisława Augusta" series) found the Vienna volumes only (Wiedeń t. 1 1788-1790, t. 2
1791-1792, ed. Danilczyk and Jusupović), no Berlin volume. A review in *Niepodległość i Pamięć* 14/1 (2007) of an
edition of diplomatic reports May 1791 – Aug 1792 from the Merseburg archive is probably the Prussian side
(Lucchesini); not checked. The 26 Oct sweep also ran known.py with no hit.

## Remaining gaps

- All 123 pieces: needs-physical-access. Nothing can be transcribed, counted or attacked until the scans are
  obtained (szukajwarchiwach by a person, or an AGAD reproduction order). The system is undetermined.

## Escalation

- Siblings: Zabłocki, the legation secretary at Berlin, wrote cipher at the same time (ZbPop 14, 1790-1792; 373 with
  the King's replies of 1791). The same cabinet cipher is likely. None is online.
- Clear pages: the file is "partly" in cipher and French; the clear passages may give a crib once imaged.
- Known keys: the Deboli codes rebuilt in `targets/deboli1791/align/` are Petersburg codes and Polish-language; worth
  a test against a Berlin page once one is seen, nothing more is expected. Cabinet keys ZbPop 445-454 are not online.
- Print: the Niepodległość i Pamięć 2007 review and the Merseburg edition may quote Jabłonowski; check.
- Next step: someone opens szukajwarchiwach (zespół 1/12, sygn. 63) in a normal browser and gets the scans, or
  orders them from AGAD. Then transcribe, count signs, try the Zabłocki siblings, and only then a ciphertext-only
  attack with a French 1700s model from `lang/`, with a control at the same length.
