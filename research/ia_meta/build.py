"""Builds candidates.json from the curated rows below (IA calendar/edition notes 'cipher, undeciphered')."""
import json

IA = 'https://archive.org/details/'
SRC = 'Internet Archive metadata sweep'
NOTE = 'Scored from a printed calendar/edition note on archive.org during the Oct 2026 Internet Archive metadata sweep (research/ia_meta/); original manuscript not viewed'
CAVEAT = ('The calendar note means the manuscript carries no contemporary decipherment; the editor may have read '
          'some of it, so the printed abstract can already contain the sense. ')


def row(year, date, title, corr, place, lang, region, period, shelf, folio, cls, status, why, imp, sol, dif, verify,
        links, prior='open (checked 28 Oct 2026: known.py, DECODE list; calendar note only, no web search)', seen='catalogue',
        decode=None):
    r = dict(year=year, date=date, title=title, correspondents=corr, place=place, language=lang, region=region,
             period=period, shelfmark=shelf, folio_note=folio, cls=cls, status=status, why=why, importance=imp,
             solvability=sol, difficulty=dif, score_note=NOTE, verify=verify,
             links=[{'label': a, 'href': b} for a, b in links], seen=seen, source=SRC, prior_art=prior)
    if decode:
        r['decode_ids'] = decode
    return r


def lp(vol_label, ident):
    return (f'Archive.org scan: {vol_label}', IA + ident)


R = []

R.append(row(1449, 'c. 1449 (f. 80r)', 'Stephanus Bilicich, cryptogram in a Sebenico miscellany bound with Guillaume de Lanicia, Via salutis',
 'Stephanus Bilicich (copyist, abbey of St Nicholas, Sebenico) -> unknown', 'Sebenico (Sibenik)', 'unknown', 'Other', '15th century',
 'Penn Libraries (Kislak), Ms. Codex 88, f. 80r (within miscellany ff. 79v-94v)', 'One cryptogram on f. 80r',
 'C', 'Penn catalogue description (OPenn) says the miscellany "includes a cryptogram (f. 80r)"; no decipherment mentioned. Not on DECODE (no hit in known.py for "Codex 88" or Bilicich).',
 'A 15th-century (1449) Dalmatian-Venetian cryptogram in a copyist\'s notebook, in the pre-1497 range the repository is looking for.',
 3, 3, 3, 'Open the OPenn images of Ms. Codex 88 (openn.library.upenn.edu) and read f. 80r: a few lines of signs or letters; check the Penn catalogue and Schmeh/Tomokiyo lists of 15th-century ciphers.',
 [('Archive.org item (OPenn upload)', IA + 'mscodex88'), ('Penn Libraries catalogue (Franklin), see description on item', IA + 'mscodex88')],
 prior='open (checked 28 Oct 2026: known.py only; no web search yet)'))

stile = ('BL Cotton MS Vespasian C i (John Stile series, 1509-13), LP Henry VIII vol. 1 nos. around 3593, 3607, 3614',)
R.append(row(1512, '16, 22 and c. 29 Dec 1512', 'John Stile -> Henry VIII, three despatches from Logrono "entirely in cipher, undeciphered"',
 'John Stile (English envoy to Ferdinand of Aragon) -> Henry VIII', 'Logrono', 'English', 'Spain', '1497-1559',
 stile[0], 'Three letters, each marked "Hol., entirely in cipher, undeciphered" with Stile\'s monogram/mark',
 'B', CAVEAT + 'The same LP volume prints many other Stile letters headed "(In cipher)" with abstracts, so a key family is known.',
 'Henry VIII\'s agent at the court of Aragon in the winter after the Holy League; a large, early English cipher series with siblings.',
 3, 3, 3, 'In LP vol. 1 compare nos. around 3593, 3607 (marked duplicate) and 3614; check whether Stile\'s ciphered abstracts were read from a Vespasian C i decipher; find BL images of Cotton Vespasian C i.',
 [lp('LP Henry VIII vol. 1', 'letterspapersfor01greauoft'), lp('LP Henry VIII vol. 1 (other scan)', 'letterspapersfor11lond')]))

for d, pl, x in [('2 Apr 1518', 'Arranda', 'LP II no. 4056 (the entry before no. 4057)'), ('30 Jun 1518', 'Saragossa', 'LP II, entry before no. 4278'), ('16 Aug 1518', 'Saragossa', 'LP II, entry before no. 4385')]:
    R.append(row(1518, d, f'Thomas Spinelly -> Henry VIII, {pl}, despatch "mostly cipher, undeciphered"',
     'Thomas Spinelly (English ambassador to Charles of Spain) -> Henry VIII', pl, 'English', 'Spain', '1497-1559',
     'Probably BL Cotton MS Vespasian C i (LP cites "Vesp. C. i" for this series; verify) - ' + x, 'About 6-9 pp., mostly cipher',
     'B', CAVEAT + 'Sibling Spinelly cipher letters are catalogued here (Galba B V ff. 40-41, DECODE R8416, read; catalogue 305 for LP ii 1553).',
     'Spinelly reporting the Aragonese Cortes and Charles V\'s first Spanish year; Spinelly\'s key is already published by Tomokiyo.',
     3, 4, 2, 'View the Cotton images; read with the Spinelly key used for catalogue 305 / R8416.',
     [lp('LP Henry VIII vol. 2 pt 2', 'letterspaperspt202greauoft'), lp('LP vol. 2 pt 2 (Google scan)', 'lettersandpaper12offigoog')]))

R.append(row(1517, '8 Nov 1517', 'Letter from Rome to Wolsey (about Peter Vannes, the collectorship and the Tournay bull), part cipher',
 'Unknown (English agent at Rome) -> Wolsey', 'Rome', 'Latin', 'Italy', '1497-1559',
 'LP Henry VIII vol. 2 pt 2, entry for 8 Nov 1517 (LP no. 3781 or 3782 area); source not shown in my extract', '10 pp., Latin, part cipher',
 'C', CAVEAT, 'Wolsey\'s Rome correspondent on the Tournay bulls and the Vannes collectorship.', 2, 2, 3,
 'Read the LP entry header and source note on archive.org; find the Cotton/State Papers shelfmark.', [lp('LP Henry VIII vol. 2 pt 2', 'letterspaperspt202greauoft')]))

R.append(row(1524, '30 Oct and 13 Nov 1524', 'Valladolid despatches to Wolsey, part and one sentence in cipher, undeciphered',
 'English ambassador(s) in Spain (Lee / Sampson, verify) -> Wolsey', 'Valladolid', 'English', 'Spain', '1497-1559',
 'LP Henry VIII vol. 4 pt 1, entries before nos. 781 (31 Oct 1524) and 828 (13 Nov 1524)', '17 pp. part cipher (30 Oct); one sentence in cipher (13 Nov)',
 'C', CAVEAT, 'Embassy of 1524 on the Emperor\'s intentions and the French indemnity.', 2, 2, 3,
 'Identify sender and BL/TNA source from LP.', [lp('LP Henry VIII vol. 4 pt 1', 'letterspaperspt104greauoft')]))

ghin = [
 ('13-17 Nov 1525', 'Rome despatches, 13/14 and 17 Nov 1525 (two copies of the first; 17 Nov signed Hier. Eps. Wigorn.)', 'Hol., cipher undeciphered; duplicates'),
 ('25 Nov - 12 Dec 1525', 'Rome despatches, 25 Nov and 12 Dec 1525 (Lat., "chiefly cipher" / "mostly cipher")', 'Two letters'),
 ('4-25 Jan 1526', 'Rome despatches, 4, 12, 17 and 25 Jan 1526 (Lat., cipher undeciphered; 12 and 25 Jan mutilated)', 'Four letters'),
 ('4 Mar - 5 Jun 1526', 'Rome despatches, 4 Mar, 5-6 May, 1 and 5 Jun 1526 (cipher undeciphered, mutilated)', 'About six letters, incl. joint Ghinucci/Casale of 6 May'),
 ('17 Aug - 5 Sep 1526', 'Rome despatches, 17 Aug, 21 Aug and 5 Sept 1526 (cipher undeciphered, mutilated)', 'Three letters'),
]
for d, t, f in ghin:
    yr = int(d[-4:]) if d[-4:].isdigit() else 1526
    R.append(row(yr, d, 'Ghinucci (Bishop of Worcester) and colleagues -> Wolsey, ' + t,
     'Girolamo Ghinucci (with Casale), English agents at Rome -> Wolsey', 'Rome', 'Latin', 'Papacy', '1497-1559',
     'BL Cotton MS Vitellius B VII/VIII (LP cites "Vit. B. vii/viii" folios; verify exact ff.)', f,
     'A', CAVEAT + 'Same Worcester cipher as the 1527 Valladolid despatches that this project already deciphered (targets/ghinucci1527/, key rebuilt from Cotton Vespasian C IV); DECODE has no Vitellius records.',
     'Wolsey\'s Rome correspondence during the League of Cognac negotiations; the Worcester key is already in hand.', 3, 4, 2,
     'View Cotton Vitellius B VII/VIII (fire-damaged); apply the targets/ghinucci1527 key; many Latin clear passages give cribs.',
     [lp('LP Henry VIII vol. 4 pt 1', 'letterspaperspt104greauoft'), lp('LP Henry VIII vol. 4 pt 2', 'letterspaperspt204greauoft')]))

R.append(row(1527, '5 Jun and 27 Oct 1527', 'Lee (and Ghinucci) -> Wolsey, Valladolid 5 Jun and Burgos 27 Oct 1527: cipher passages undeciphered',
 'Edward Lee (with Ghinucci) -> Wolsey', 'Valladolid / Burgos', 'English', 'Spain', '1497-1559',
 'LP Henry VIII vol. 4 pt 2 (entries before 3153 and 3524); BL Cotton / SP 1 (verify)', 'Some passages (5 Jun); two passages (27 Oct)',
 'A', CAVEAT + 'The Lee-Worcester cipher is rebuilt here (ghinucci1527, lee1526 notes).', 'Lee\'s Spanish embassy during the sack of Rome.', 2, 4, 2,
 'Locate in Cotton/SP 1 and apply the existing key.', [lp('LP Henry VIII vol. 4 pt 2', 'letterspaperspt204greauoft'), lp('same volume, other scan', '11001939bsb')]))

R.append(row(1530, '6 Jan and 2 Feb 1530 (Venice)', 'Two Venice letters to a cardinal (Wolsey?/Worcester?), cipher undeciphered, mutilated; duplicates',
 'unknown (English agent at Venice, c. Casale) -> unknown', 'Venice', 'Latin', 'Italy', '1497-1559',
 'LP Henry VIII vol. 4 pt 3 (entries before 6141 and 6192), source Vit. B. xi (verify)', 'Letter plus duplicate; second letter on 2 Feb',
 'C', CAVEAT, 'The 1529-30 Divorce correspondence from Venice.', 3, 2, 3, 'Read the LP entry headers for sender and recipient.',
 [lp('LP Henry VIII vol. 4 pt 3', 'lettterspapersfo0004jsbr_w1f6')]))

R.append(row(1536, '10 Mar 1536', 'Lyons despatch on French war preparations, three passages in cipher undeciphered',
 'unknown English agent -> unknown (Spanish text)', 'Lyons', 'Spanish', 'France', '1497-1559',
 'LP Henry VIII vol. 10 (Add. MS 28,588 f. 226 per the LP note)', 'Four pp., three cipher passages',
 'C', CAVEAT + 'The misdated document was first inserted in vol. IV of LP.', 'Habsburg-side intelligence on Francis I\'s plans in 1536.', 2, 2, 3,
 'Check BL Add MS 28588 f. 226.', [lp('LP Henry VIII vol. 10', 'letterspapersfor10greauoft')]))

R.append(row(1539, 'c. 24 Dec 1539', 'French despatch to the Constable (Montmorency), postscript in cipher undeciphered (Marillac letter-book)',
 'Charles de Marillac (probable) -> Anne de Montmorency', 'London', 'French', 'France', '1497-1559',
 'LP Henry VIII vol. 14 pt 2 (BnF Marillac letter-book copy; original not stated)', 'Postscript only',
 'C', CAVEAT + 'Date inferred from the neighbouring entry; check.', 'Marillac\'s early embassy; short.', 2, 2, 3,
 'Read the LP entry.', [lp('LP Henry VIII vol. 14 pt 2', 'letterspaperspt214greauoft')]))

# CSP
R.append(row(1550, 'c. 1549-50 (no. 97)', 'Letter of the English ambassador, five pages, "first and larger part in cipher, undeciphered"',
 'unknown -> unknown (Edward VI)', 'unknown', 'English', 'Other', '1497-1559',
 'CSP Foreign, Edward VI (Turnbull 1861), no. 97 (the entry before no. 98, Bishop of Westminster -> Petre, on the Interim)', '5 pp.',
 'C', 'Calendar note only; no key. ' + CAVEAT, 'Edward VI-era diplomatic cipher, rare.', 2, 2, 4,
 'Open the calendar entry and find the SP 68 shelfmark.', [('CSP Foreign Edward VI', IA + 'calendarofstatep0000vari_q2n4'), ('same, other scan', IA + 'calendarstatepa00turngoog')]))

R.append(row(1551, 'c. 1551, date torn off (no. 271) and 27 Apr (no. 328), 1552 (no. 588)', 'Morysine and Pickering ciphers, Edward VI: "partly / five lines / principally in cipher, undeciphered"',
 'Sir Richard Morysine (Augsburg) -> Cecil; Pickering (France) probable', 'Augsburg / Paris', 'English', 'Central Europe', '1497-1559',
 'CSP Foreign Edward VI nos. 271, 328, 588 (SP 68 / SP 69; verify)', 'Three items: 2 pp., 2 pp. with 5 cipher lines, 2 pp. principally cipher',
 'C', 'Calendar note only. ' + CAVEAT, 'Edward VI embassies: Morysine at the Imperial court during the Interim.', 2, 2, 4,
 'Check Tomokiyo for a Morysine cipher; find SP 68 images.', [('CSP Foreign Edward VI', IA + 'calendarofstatep0000vari_q2n4')]))

R.append(row(1562, '6 Dec 1562', 'Letter to Queen Elizabeth from the Prince of Conde\'s camp before Paris, 3 pp., in cipher undeciphered',
 'unknown (writing to Elizabeth from Conde\'s camp) -> Elizabeth I', "Prince of Conde's camp before Paris", 'unknown', 'France', '1560-1589',
 'CSP Foreign, Elizabeth 1562 (Stevenson), no. 1195 (the entry before no. 1196, Smith to the Queen); SP 70', '3 pp., entirely cipher (about counter-mines)',
 'C', 'Calendar note only; related Throckmorton ciphers R9260-R9262 exist (Add MS 4136) and do not obviously apply.',
 'Huguenot-English co-operation at the siege of Paris, a month before Le Havre fell.', 3, 2, 4,
 'Open the calendar entry and TNA SP 70 catalogue; try the Throckmorton ciphers.', [('CSP Foreign Elizabeth 1562', IA + 'calendarstatepa03britgoog')]))

R.append(row(1570, 'c. 1570 (nos. 811-812, April)', 'Cipher in the "cipher of John Marsh": one letter partly, then a four-page copy "entirely in cipher, not deciphered"',
 'unknown -> unknown (Cecil?)', 'unknown', 'unknown', 'England', '1560-1589',
 'CSP Foreign, Elizabeth 1569-71 (Stevenson), nos. 811-812 and a one-page entirely cipher letter before the piracy proclamation; SP', '3.5 pp. + 4 pp.',
 'B', 'Calendar note only; "John Marsh" cipher is mentioned in the entry; Tomokiyo may have it.', 'Spanish pressure on Scottish affairs, 1570.', 2, 2, 4,
 'Read the calendar entries, find the key under Marsh.', [('CSP Foreign Elizabeth 1569-71', IA + 'calendarofstatep00grea_0')]))

R.append(row(1572, '1572-73', 'Norton / Lee / Hunsdon intercepts, Dom. Eliz. Addenda: italicised passages "in cipher undeciphered"',
 'Francis Norton, John Lee, Lord Hunsdon, others -> Leicester, Burghley', 'Antwerp / London', 'English', 'England', '1560-1589',
 'CSP Domestic, Addenda Elizabeth 1566-79 nos. 19, 28, 31 and others; keys in "Collection of ciphers of Queen Elizabeth, Vol. I, Nos. 63, 64"', 'Six or more letters',
 'A', 'Calendar note plus a key reference. ' + CAVEAT, 'Burghley\'s spies among the Northern Rising exiles.', 2, 3, 3,
 'Find the key at SP 12 / SP 106 (Elizabeth cipher collections).', [('CSP Domestic Addenda', IA + 'statepapersmary07greauoft')]))

R.append(row(1594, 'Jan-Jun 1594', 'Phelippes-drafted Catholic intercepts: Allen letter (28 Jan), "J. to A." (14 Mar), Wicham/Sterrell to Derick (1 Jun)',
 'unknown English Catholic correspondents -> Antwerp / Spain', 'unknown', 'English', 'Low Countries', '1589-1598',
 'CSP Domestic Elizabeth 1591-94 (Green), nos. around 69 (Roger Manners), 76 (Aubrey) and Dom. Eliz. 1581-90 no. 75 (Winwood to Cecil)', 'Each 2-3 pp. in cipher; asterisks mark "undecipherable" parts',
 'B', 'Calendar note only; Phelippes drafted decipher copies, but passages "proved undecipherable". ' + CAVEAT, 'Intercepted Catholic correspondence after the Armada, Cardinal Allen\'s circle.', 3, 3, 3,
 'Locate the Phelippes drafts in SP 12 and SP 106.', [('CSP Domestic Elizabeth 1591-94', IA + 'calendarofstatep03greauoft'), ('CSP Domestic Eliz. 1591-94, other scan', IA + 'cu31924091775274'), ('CSP Domestic Eliz. (Wicham/Sterrell)', IA + 'bub_gb_ELGK9pFXS50C')]))

R.append(row(1605, '2 Nov 1605', '"E. F. Mak" to Richard Bankes, anonymous letter "fownd in the streete" on the Gunpowder Plot, partly in cipher, undeciphered',
 'E. F. Mak -> Richard Bankes', 'unknown', 'English', 'England', '1598-1610',
 'TNA SP 14/216 (Gunpowder Plot Book, verify) - CSP Domestic James I Nov 1605, no. 4 (copy no. 5)', 'Short; part cipher',
 'C', 'Calendar note only; a web search (28 Oct 2026) found the entry but no decipherment.',
 'A cipher letter of the Gunpowder Plot week, probably from a conspirator sympathiser.', 4, 2, 3,
 'Order the SP 14 image; check Gunpowder Plot Book 3 and Nicholls\' work.', [('CSP Domestic James I', IA + 'calendarofstatep0000mary_h2k1'), ('Calendar entry on British History Online', 'https://prod.british-history.ac.uk/node/8417')],
 prior='open (checked 28 Oct 2026: calendar entry via web search; no decipherment found)'))

R.append(row(1644, '15 Dec 1644 / 18 Jan - 6 Mar 1645', 'Charles I to Ormond, original "in cypher, not decyphered", carried by Col. John Barry',
 'Charles I -> Marquess of Ormond', 'Oxford', 'English', 'England', '1611-1650',
 'Bodleian, Clarendon State Papers, calendar no. 1815', 'One letter (duplicate of 15 Dec and 18 Jan)',
 'B', 'Calendar note only; the Ormond-Hyde ciphers are partly known. Sibling no. 2424 is "decyphered on following paper".', 'Charles I\'s Irish treaty correspondence.', 4, 3, 3,
 'Find the Clarendon MS volume and the King-Ormond cipher in the Egerton/Carte papers.', [('Calendar of the Clarendon State Papers vol. 1', IA + 'calendarofclaren01bodluoft')]))

R.append(row(1646, '29 Apr 1646', 'Sir Edward Hyde (Jersey) -> Secretary Nicholas, "nearly all in cypher, not deciphered"',
 'Edward Hyde -> Edward Nicholas', 'Jersey', 'English', 'England', '1611-1650',
 'Bodleian, Clarendon State Papers, calendar no. 2505', 'One letter, nearly all cipher',
 'B', 'Calendar note: "possibly Glamorgan" commission discussed. Hyde-Nicholas cipher may be recoverable from siblings.', 'Hyde on the Glamorgan commission and the royalist collapse.', 4, 3, 3,
 'Check the Clarendon calendar vol. 1 and the Hyde-Nicholas cipher in the Bodleian MS.', [('Calendar of the Clarendon State Papers vol. 1', IA + 'calendarofclaren01bodluoft')]))

R.append(row(1659, 'May-Jul 1659', 'Royalist intercepts: De Vaux -> Du Chastel (12/22 May), Slingsby to La Haye (18 Jul) and Marces copies, partly cipher not deciphered',
 'M. de Vaux -> Marquis du Chastel; Slingsby -> Hyde', 'London / Paris', 'French', 'England', '1651-1700',
 'Bodleian Clarendon MS 63 ff. 33-4; cal. SP Dom 1658-9 p. 346; Cypher Collections vol. VI no. 35g (key from interlined decyphers)', 'Several short letters',
 'A', 'CSP Domestic notes say "a key to the cypher has been formed from decyphers interlined"; remaining figures not read.',
 'Intercepted correspondence on Richard Cromwell\'s fall.', 3, 4, 2, 'Fetch the Cypher Collections key; read the leftover groups.',
 [('CSP Domestic 1659-60 (French correspondence)', IA + 'cu31924091770473'), ('same volume, other scan', IA + 'cu31924091770465'), ('Clarendon calendar vol. 4', IA + 'calendarofclaren04bodluoft')]))

R.append(row(1655, 'Feb-Sep 1655/6', 'Royalist agents\' letters in CSP Domestic Commonwealth: "italics in cypher undecyphered" (Lamplugh, Francis/Pile, others)',
 'T. Lamplugh, Dick Pile, other royalist agents -> Williamson, Whitley et al.', 'Paris / London', 'English', 'England', '1651-1700',
 'TNA SP 18 (Commonwealth Domestic), CSP vols. covering 1655-56', 'About eight letters of 1-3 pp.',
 'C', 'Calendar note only.', 'Thurloe-era interceptions of Charles II\'s network.', 2, 2, 3, 'Find the SP 18 volumes and the Thurloe/Williamson cipher collections.',
 [('CSP Domestic Commonwealth 1655', IA + 'cu31924091770424'), ('CSP Domestic Commonwealth 1655-56', IA + 'cu31924091770440'), ('CSP Domestic 1655-56 (Williamson)', IA + 'calendarstatepa01offigoog')]))

R.append(row(1664, '13 Jun 1664', 'Sir Richard Fanshaw: "six pages of cipher, undeciphered" (duplicate of a letter) in the Heathcote papers',
 'Sir Richard Fanshaw -> unknown (Lisbon/Madrid embassy)', 'unknown', 'English', 'Spain', '1651-1700',
 'HMC, Manuscripts of J. M. Heathcote, Conington Castle (1899), 1664 June 13; private papers, current location unknown', 'Six pages',
 'C', 'HMC note only. A web search (28 Oct 2026) found the HMC volume but no decipherment.', 'Restoration ambassador to Portugal/Spain on Tangier and the Alliance.', 3, 2, 3,
 'Find the Heathcote papers in a county record office.', [('HMC Heathcote', IA + 'manuscriptsjmhe00heatgoog')],
 prior='open (checked 28 Oct 2026: web search, HMC volume only)'))

R.append(row(1568, '1568-69', 'Norreys (Paris) -> Leicester and others: "partly in cipher undeciphered", Pepys MSS Magdalene',
 'Sir Henry Norreys -> Earl of Leicester / Cecil', 'Paris / Verdun', 'English', 'France', '1560-1589',
 'Magdalene College Cambridge, Pepys MSS, Leicester volume (II. 67, II. 573-579)', 'Several letters; one is 3.5 pp.',
 'A', 'HMC note: "a key has been constructed by inspection of deciphered letters of Chaloner" for the Chaloner letters; Norreys\' Cecil-Norris table is Tomokiyo\'s and is applied in targets/norreys1567; the Pepys copies are new.',
 'Norreys at Paris during the Wars of Religion.', 2, 4, 2, 'Compare with norreys1567; find Pepys MSS images.', [('HMC Pepys MSS', IA + 'reportonpepys00greauoft'), ('same, other scan', IA + 'reportonpepysman00grea')]))

R.append(row(1573, '17 May 1573', 'Arrow letter shot into Edinburgh Castle, cipher not yet deciphered (reported by Sir Valentine Browne)',
 'unknown (Huntly\'s party) -> Earl of Huntly', 'Edinburgh Castle', 'unknown', 'England', '1560-1589',
 'CSP Foreign Elizabeth 1572-74 no. 966; original probably SP 52', 'Cipher text itself not printed',
 'C', 'Calendar note only.', 'Siege of Edinburgh Castle.', 2, 1, 4, 'Search SP 52 for the arrow letter.', [('CSP Foreign Elizabeth', IA + 'calendarofstatep10grea')]))

R.append(row(1659, '17 Feb 1659/60', 'Mordaunt -> Nicholas, address in cipher not deciphered; Vol. 5 Hague 1661-62 phrases',
 'Mordaunt -> Edward Nicholas', 'unknown', 'English', 'England', '1651-1700',
 'Bodleian, Clarendon MSS (vol. 69; vol. 107 ff. 171-4)', 'Short',
 'B', 'Calendar note only; very short cipher parts.', 'The week of the Restoration preparations.', 2, 2, 3, 'Minor.',
 [('Clarendon calendar vol. 4', IA + 'calendarofclaren04bodluoft'), ('Clarendon calendar vol. 5', IA + 'calendarofclaren05bodl')]))

json.dump(R, open('candidates.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R))
