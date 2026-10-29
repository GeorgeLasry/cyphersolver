"""Build candidates.json for the DECODE Venice/Milan sweep (Oct 2026)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
RV = "https://de-crypt.org/decrypt-web/RecordsView/%d"
GAL = {"label": "Gallica, BnF italien 1583 (ark from targets/it1583/bnf.htm, not re-checked)",
       "href": "https://gallica.bnf.fr/ark:/12148/btv1b10033686w"}
NOTE = ("Scored from the DECODE metadata, Mazzatinti's 1883 folio inventory of BnF ital. 1583 "
        "(targets/it1583/asl1883.txt) and the it1583 sibling-sweep notes during the Oct 2026 DECODE Venice/Milan sweep "
        "(research/venice_milan_decode/); not viewed here")
SF = ("Scored from DECODE metadata and a sample of 13 DECODE thumbnails plus one full PDF (R5430) viewed 28 Oct 2026 "
      "during the DECODE Venice/Milan sweep (research/venice_milan_decode/)")


def links(ids, extra=()):
    return [{"label": "DECODE R%d" % i, "href": RV % i} for i in ids] + list(extra)


C = []
C.append(dict(
    year=1446, date="1 Nov - 31 Dec 1446",
    title="Filippo Maria Visconti, Duke of Milan → Francesco Sforza, six cipher letters on parchment, Nov-Dec 1446",
    correspondents="Filippo Maria Visconti, Duke of Milan → Count Francesco Sforza (his son-in-law)",
    place="Milan; Cusago (31 Dec)", language="Italian", region="Italy", period="15th century",
    shelfmark="BnF italien 1583, ff. 110, 112, 130, 136, 154, 158",
    folio_note=("DECODE R7902 (f. 110, 2 pp.; Mazzatinti: Milan 1 Nov, DECODE 10 Nov), R7903 (f. 112, 7 Nov), "
                "R7904 (f. 130, c. 26 Nov), R7907 (f. 136, 29 Nov), R7914 (f. 154, 12 Dec, 2 pp.), R7915 (f. 158, "
                "Cusago 31 Dec); one page each, graphic signs + letters + numerals. Mazzatinti marks each 'In cifre: "
                "membr.' and lists f. 131 as 'Traduzione della lettera precedente' (a contemporary translation of f. 130). "
                "f. 145 (Duke, 1 Dec, in cifre) is not on DECODE."),
    cls="A",
    status=("DECODE Non-decrypted (all six; DECODE gives no sender or receiver, identified here from Mazzatinti). Not in "
            "the repo: targets/it1583 viewed R7900-R7915 on 23 Oct 2026 and found none in the f. 68/70 alphabet, but did "
            "not work them. f. 131 (not a DECODE record) is a contemporary translation of f. 130, and BnF ital. 1584 "
            "(1447) has more Duke's cipher letters each followed by a 'Traduzione' (ff. 5/6, 8/9): cribs for the "
            "Duke's cipher of these months."),
    why=("The last year of the last Visconti duke: his secret dealings with Sforza during the 1446 Venetian war, months "
         "before his death and Sforza's bid for Milan."),
    importance=5, solvability=4, difficulty=2, score_note=NOTE,
    verify=("Open Gallica ital. 1583 f. 131 and confirm it is the clear text of f. 130 (R7904); fetch R7902-R7915 "
            "images with the project cookie; check ital. 1584 ff. 5-9 on Gallica; check the DECODE Sforzesco key "
            "records (cart. 1597/1598) for a Duke-Count key."),
    links=links([7902, 7903, 7904, 7907, 7914, 7915], [GAL]), seen="catalogue", source="DECODE Venice/Milan sweep",
    prior_art=("open (checked 28 Oct 2026: web search 'Filippo Maria Visconti lettere cifrate 1446', Cipher Mysteries "
               "Milanese posts, repo it1583 notes; no edition of the cipher parts found; Cerioni 1970 edits keys, not letters)"),
    decode_ids=[7902, 7903, 7904, 7907, 7914, 7915]))

C.append(dict(
    year=1446, date="27-30 Nov 1446 (+ reply 3 Dec)",
    title="Nicodemo Tranchedini and Boccaccino Alamanni, Florence → Francesco Sforza, cipher letters, Nov 1446",
    correspondents="Nicodemo Tranchedini da Pontremoli (and Boccaccino Alamanni) → Francesco Sforza; Sforza → both (3 Dec)",
    place="Florence; Sforza's camp in the valle Fagnani near Pesaro", language="Italian", region="Italy",
    period="15th century", shelfmark="BnF italien 1583, ff. 134, 135, 139, 143, 147",
    folio_note=("DECODE R7905 (f. 134, Nicodemo, 27 Nov, 'partly encrypted'), R7906 (f. 135, Nicodemo, 28 Nov), R7908 "
                "(f. 139, Alamanni & Nicodemo, 29 Nov), R7909 (f. 143, undated, probably Nicodemo 30 Nov), R7910 (f. 147, "
                "Sforza to Alamanni & Nicodemo, 3 Dec); 1 page each. Mazzatinti marks ff. 133-139 'In cifre'; f. 133 "
                "(25 Nov) is not on DECODE."),
    cls="B",
    status=("DECODE Non-decrypted, no names on DECODE (identified here from Mazzatinti's inventory). Not in the repo. Key "
            "family: Lasry deciphered Tranchedini → Sforza 28 June 1452 (BnF ital. 2242; targets/tranchedini1452, "
            "55-symbol key); DECODE holds 208 Sforza keys from ASMi cart. 1591/1597/1598."),
    why=("Sforza's resident in Florence reporting during the 1446 war, by the man who later ran Milan's cipher office "
         "(the Tranchedino ledger)."),
    importance=4, solvability=3, difficulty=3, score_note=NOTE,
    verify=("Fetch R7905-R7910 images; try Lasry's 1452 Tranchedini key and the cart. 1597 keys headed for Nicodemo or "
            "Florence; f. 147 (Sforza's own letter) may be partly clear."),
    links=links([7905, 7906, 7908, 7909, 7910], [GAL]), seen="catalogue", source="DECODE Venice/Milan sweep",
    prior_art="open (checked 28 Oct 2026: repo tranchedini1452 and it1583 notes, Cipher Mysteries; no reading of the 1446 letters found)",
    decode_ids=[7905, 7906, 7908, 7909, 7910]))

C.append(dict(
    year=1446, date="7 Dec 1446",
    title="Sforza's envoys at Venice (Contucio; Stavoli, Giordani, Amidani) → Francesco Sforza, cipher letters, 7 Dec 1446",
    correspondents=("Contucio; Giovanni Stavoli, Matteo Giordani, Vincenzo Amidani, Agostino da Narni and Contucio → "
                    "Francesco Sforza"),
    place="Venice", language="Italian", region="Italy", period="15th century",
    shelfmark="BnF italien 1583, ff. 148, 151, 152",
    folio_note=("DECODE R7911 (f. 148, 2 pp., 'partly encrypted'; Mazzatinti: Contucio, Venice 7 Dec, 'In cifre'), "
                "R7912 (f. 151, 2 pp., the joint despatch of 7 Dec), R7913 (f. 152, 1 p., 7 Dec, continuation or enclosure)."),
    cls="B",
    status=("DECODE Non-decrypted, no names on DECODE. Not in the repo. Key lead: the Simonetta-Vincentius/Stavoli key "
            "is ASMi cart. 1597 no. 14 on DECODE, and R7900 (f. 89, Angelo Simonetta at Venice, 30 Sept 1446, 'Cum "
            "cifra Vincentii') has its contemporary clear text on R7901 (f. 90), per targets/it1583 notes. Mazzatinti "
            "does not mark f. 151 'in cifre', so check how much of R7912 is cipher."),
    why="Sforza's embassy in Venice in the winter of 1446, when Sforza was weighing a switch from Venice to the Duke of Milan.",
    importance=4, solvability=3, difficulty=3, score_note=NOTE,
    verify="Fetch R7911-R7913; test the cart. 1597 no. 14 key and the alphabet rebuilt from the R7900/R7901 pair.",
    links=links([7911, 7912, 7913, 7900, 7901], [GAL]), seen="catalogue", source="DECODE Venice/Milan sweep",
    prior_art="open (checked 28 Oct 2026: repo it1583 notes, web search; no reading found)",
    decode_ids=[7911, 7912, 7913]))

C.append(dict(
    year=1450, date="15th century (DECODE gives the placeholder 1450)",
    title="Sforza chancery letters wholly in cipher, ASMi Carteggio Sforzesco cart. 1597 (59 records)",
    correspondents="unknown (Sforza ambassadors and agents → the Duke of Milan, to be identified from addresses)",
    place="unknown", language="Italian", region="Italy", period="15th century",
    shelfmark=("Archivio di Stato di Milano, Carteggio Visconteo-Sforzesco, cart. 1597 (Chiavi e cifrari), nos. 80, 91, "
               "115-168, 172-174"),
    folio_note=("DECODE R5380, R5391, R5415-R5468, R5472-R5474; 1-4 pp. each, PDFs. R5430 viewed in full: a folded "
                "letter wholly in a graphic-sign cipher (c. 13 lines), no decipherment on the leaf. Thumbnails show "
                "cipher letters with seals and some clear leaves."),
    cls="A",
    status=("DECODE status N/A, all records unclassified, no metadata. Already noted in CATALOGUE.md as set-aside "
            "catalogue 292 ('may be key samples or exercises, check the images'): the images checked here show real "
            "enciphered letters, so this returns the pool with new evidence. DECODE also holds 115 key records from "
            "the same box (cart. 1597, record_type 2), e.g. no. 14 Simonetta-Vincentius/Stavoli."),
    why="A large body of unread 15th-century Milanese diplomatic ciphers filed with the keys that should read them.",
    importance=4, solvability=4, difficulty=3, score_note=SF,
    verify=("Sort the 59 records' thumbnails into cipher letters and clear leaves, read addresses and endorsements, and "
            "match each letter to the cart. 1597 key whose heading names that correspondent."),
    links=links([5430, 5380, 5436, 5465]), seen="image", source="DECODE Venice/Milan sweep",
    prior_art=("open (checked 28 Oct 2026: CATALOGUE.md cat. 292 note, it1583 notes; Cerioni 1970 edits the keys, no "
               "letter readings known)"),
    decode_ids=[5380, 5391] + list(range(5415, 5469)) + [5472, 5473, 5474]))

C.append(dict(
    year=1450, date="15th century (DECODE placeholder 1450)",
    title="Sforza chancery letters in cipher, ASMi Carteggio Sforzesco cart. 1598 and 1591 (110 records)",
    correspondents="unknown", place="unknown", language="Italian", region="Italy", period="15th century",
    shelfmark="Archivio di Stato di Milano, Carteggio Visconteo-Sforzesco, cart. 1598 nos. 2-113 and cart. 1591 nos. 63-64",
    folio_note=("DECODE R5476-R5587 (cart. 1598, 108 records) and R5297-R5298 (cart. 1591); 1-3 pp. each, PDFs. "
                "Thumbnails sampled (R5297, R5476, R5481, R5520, R5560, R5587): cipher letters mixed with clear texts, "
                "one apparently headed 'Da cifra' (a decipherment; reading of the thumbnail uncertain)."),
    cls="A",
    status=("DECODE status N/A, unclassified. Same set-aside catalogue 292 pool (CATALOGUE.md). DECODE holds 29 key "
            "records from cart. 1598 and 64 from cart. 1591; clear leaves in the same box are possible cribs."),
    why="Second half of the unread Sforza cipher pool; clear decipherments filed with it would make key recovery likely.",
    importance=4, solvability=4, difficulty=3, score_note=SF,
    verify="Sort the 110 records into cipher letters, clear decipherments and keys from thumbnails; pair each decipherment with its cipher letter.",
    links=links([5297, 5476, 5520, 5587]), seen="image", source="DECODE Venice/Milan sweep",
    prior_art="open (checked 28 Oct 2026: CATALOGUE.md cat. 292 note; no published readings found)",
    decode_ids=[5297, 5298] + list(range(5476, 5588))))

recs = json.load(open(os.path.join(HERE, 'inscope.json'), encoding='utf-8'))
for c in C:
    c['decode_ids'] = [i for i in c['decode_ids'] if str(i) in recs]
json.dump(C, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print([len(c['decode_ids']) for c in C])
