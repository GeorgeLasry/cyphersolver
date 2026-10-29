# -*- coding: utf-8 -*-
"""Row builder for the second Internet Archive pass (series B). Writes candidates.json.
Every row comes from a printed calendar / edition read in the archive.org djvu OCR; none was viewed against an original."""
import json

SRC = "Internet Archive full-text sweep, pass 2b"
SCORE = ("Scored from the printed calendar/edition text during the Oct 2026 Internet Archive pass-2b sweep "
         "(research/ia_pass2_b/); not viewed against the original")
WEB = "web check not yet run beyond the printed edition"


def L(ident, q, label):
    return [{"label": label + " (full text, search)", "href": "https://archive.org/details/%s?q=%s" % (ident, q)},
            {"label": "Plain-text OCR", "href": "https://archive.org/download/%s/%s_djvu.txt" % (ident, ident)}]


rows = []


def add(**k):
    r = dict(year=None, date="", title="", correspondents="", place="unknown", language="unknown", region="England",
             period="unknown", shelfmark="", folio_note="", cls="C", status="", why="", importance=2, solvability=2,
             difficulty=3, score_note=SCORE, verify="", links=[], seen="catalogue", source=SRC, prior_art="")
    r.update(k)
    if not r["period"] or r["period"] == "unknown":
        y = r["year"]
        r["period"] = ("1497-1559" if y < 1560 else "1560-1589" if y < 1589 else "1589-1598" if y < 1598 else
                       "1598-1610" if y < 1611 else "1611-1650" if y < 1651 else "1651-1700" if y < 1701 else
                       "1701-1800" if y < 1801 else "1801-1900")
    rows.append(r)


CAL2 = "Calendar of the Clarendon State Papers preserved in the Bodleian Library, vol. II (1649-54), ed. W. D. Macray, Oxford 1869"
CAL3 = "Calendar of the Clarendon State Papers preserved in the Bodleian Library, vol. III (1655-57), ed. W. D. Macray, Oxford 1876"
PA_CL = "open (checked 28 Oct 2026: printed calendar only; Clarendon vol. II-III cipher notes say 'undeciphered'; Tomokiyo/cryptiana, Lasry and HistoCrypt not searched)"

# ---------------------------------------------------------------- Clarendon II and III
add(year=1651, date="13 Jul 1651", place="Antwerp", language="English",
    title="Hyde: instructions for his secretary Edgeman (mission to Scotland), plus two further copies by Edgeman mostly in the King's cipher and in Nicholas's cipher",
    correspondents="Sir Edward Hyde → William Edgeman (his secretary); the two cipher copies are Edgeman's",
    shelfmark="Bodleian Library, Clarendon State Papers (MS Clarendon; volume not given in the calendar); " + CAL2 + ", no. 540",
    folio_note="Calendar vol. II pp. 103-104. Plain draft plus 'two other copies by Edgeman, the greater part of the one being in the cipher used by the King, and the greater part of the other in the cipher used by Secretary Nicholas'",
    cls="A",
    status="Calendar entry 540. The plaintext is summarised in the calendar entry itself; the two cipher copies are not said to be deciphered. Same volume prints many letters deciphered by Nicholas, Hyde or Edgeman (royalist key rebuildable). Not looked up on DECODE (Bodleian, not on DECODE list).",
    why="Same text in two exile ciphers (Charles II's court after Worcester): a ready crib pair for the royalist ciphers of 1650-54.",
    importance=3, solvability=4, difficulty=2,
    verify="Open the Clarendon MS volume for July 1651 (Bodleian images/Digital Bodleian), find the two Edgeman copies; compare with deciphered Nicholas/Hyde letters from vol. II.",
    links=L("calendarofclaren02bodluoft", "Edgeman+cipher+used+by+the+King", "Clar. Cal. vol. II"),
    prior_art=PA_CL)

add(year=1654, date="16 Jan 1654", place="Paris", language="English",
    title="Hyde to Lord Rochester: copy by Edgeman, a few words in undeciphered cipher (Long's case, Sir H. Lee)",
    correspondents="Sir Edward Hyde → Earl of Rochester (Wilmot)",
    shelfmark="Bodleian Library, Clarendon State Papers; " + CAL2 + ", no. 1667",
    folio_note="Calendar vol. II p. 302; 'A few words in undeciphered cipher'",
    cls="A",
    status="Calendar note 'A few words in undeciphered cipher' (Copy by Edgeman, endorsed by Hyde). Short. Other Hyde-Rochester letters in the same volume are deciphered or printed in Clarendon State Papers iii.",
    why="Hyde's private view of Cromwell and the exiles' politics in Jan 1654; the cipher words are the sensitive ones.",
    importance=2, solvability=3, difficulty=2,
    verify="Check Clarendon MS for Jan 1654 and whether the cipher words appear in the Clarendon State Papers vol. iii (1786) transcripts.",
    links=L("calendarofclaren02bodluoft", "undeciphered+cipher+Edgernan", "Clar. Cal. vol. II"), prior_art=PA_CL)

add(year=1654, date="c. 10 Apr 1654", place="Paris", language="English",
    title="Hyde to Lord Rochester on the King's impending departure from Paris: part in undeciphered cipher",
    correspondents="Sir Edward Hyde → Earl of Rochester (Wilmot)",
    shelfmark="Bodleian Library, Clarendon State Papers; " + CAL2 + ", no. 1824",
    folio_note="Calendar vol. II p. 333; 'Part in undeciphered cipher'; date from the margin of the next entry (10 Apr), to confirm",
    cls="A",
    status="Calendar note 'Part in undeciphered cipher'. Copy by Hyde.",
    why="The King's plans to leave France for Germany (summer 1654), written in the royalist cipher.",
    importance=2, solvability=3, difficulty=2,
    verify="View Clarendon MS April 1654; confirm date and extent of the cipher part.",
    links=L("calendarofclaren02bodluoft", "King%27s+impending+departure+undeciphered", "Clar. Cal. vol. II"), prior_art=PA_CL)

add(year=1654, date="1 May 1654", place="Paris", language="English",
    title="Hyde to Lord Rochester (treaty of France with Cromwell; St Malo news): copy by Edgeman, a few lines in undeciphered cipher",
    correspondents="Sir Edward Hyde → Earl of Rochester (Wilmot)",
    shelfmark="Bodleian Library, Clarendon State Papers; " + CAL2 + ", no. 1867",
    folio_note="Calendar vol. II pp. 345-346; 'A few lines in undeciphered cipher'",
    cls="A", status="Calendar note 'A few lines in undeciphered cipher'. Copy by Edgeman.",
    why="Royalist intelligence on the Anglo-French treaty of 1654.", importance=2, solvability=3, difficulty=2,
    verify="View Clarendon MS May 1654.", links=L("calendarofclaren02bodluoft", "A+few+lines+in+undeciphered+cipher", "Clar. Cal. vol. II"),
    prior_art=PA_CL)

add(year=1654, date="c. 1 Dec 1654", place="Paris", language="English",
    title="Hyde to Ormonde (letters from Paris intercepted; steal the Duke of Gloucester away): partly in cipher, undeciphered by Ormonde",
    correspondents="Sir Edward Hyde → James Butler, Marquess of Ormonde (Cologne)",
    shelfmark="Bodleian Library, Clarendon State Papers; " + CAL2 + ", no. 2092",
    folio_note="Calendar vol. II p. 433; 'Partly in cipher, undeciphered by Ormonde. With small omissions, Cl. S. P. vol. iii. p. 259'. Date 1 Dec from the neighbouring entries, to confirm",
    cls="A",
    status="Calendar says the cipher was undeciphered by Ormonde (i.e. by the recipient); the printed Clarendon State Papers iii p. 259 omits parts. Only recipient failure noted, not a modern reading.",
    why="Plot to remove the Duke of Gloucester from his mother's pressure and the army plot in England, Dec 1654.",
    importance=3, solvability=3, difficulty=2,
    verify="View Clarendon MS Dec 1654 (and Carte MSS at Bodleian for Ormonde's copy); compare with Clarendon State Papers iii.",
    links=L("calendarofclaren02bodluoft", "undeciphcred+by+Ormonde", "Clar. Cal. vol. II"),
    prior_art=PA_CL)

add(year=1656, date="c. 1 Nov 1656", place="Bruges", language="English",
    title="Hyde to the Earl of Bristol (Irish regiments, Col. Grace): mention of 'Edgely's' proposed attempt in England in undeciphered cipher",
    correspondents="Sir Edward Hyde → George Digby, Earl of Bristol",
    shelfmark="Bodleian Library, Clarendon State Papers; " + CAL3 + ", no. 595",
    folio_note="Calendar vol. III pp. 194-195; '(in undeciphered cipher)'; date from the margin 'Bruges, Nov. 1', to confirm",
    cls="A", status="Calendar note: one mention in undeciphered cipher.",
    why="Royalist plan for a rising in 1656 (Edgely = a code name), at the time of the Spanish alliance.",
    importance=2, solvability=2, difficulty=3,
    verify="View Clarendon MS Nov 1656.", links=L("calendarofclaren03bodluoft", "proposed+attempt+in+England+undeciphered", "Clar. Cal. vol. III"),
    prior_art=PA_CL)

add(year=1657, date="6 May 1657 (O.S.)", place="England (agent's letter, received at Brussels)", language="English",
    title="Letter from Mr Ashton ('232'), a royalist agent in England: partly in undeciphered cipher (Wildman, J. Fisher; Parliament and the crown)",
    correspondents="Mr Ashton (agent no. 232) → [Hyde] (endorsed by Hyde)",
    shelfmark="Bodleian Library, Clarendon State Papers; " + CAL3 + ", no. 874",
    folio_note="Calendar vol. III pp. 289-290; 'partly in undeciphered cipher'",
    cls="A", status="Calendar note 'partly in undeciphered cipher'. Addressee not stated in the calendar entry (endorsed by Hyde).",
    why="English royalist intelligence in the week of the Humble Petition and Advice (offer of the crown to Cromwell).",
    importance=2, solvability=2, difficulty=3,
    verify="View Clarendon MS May 1657; check the list of royalist agent numbers in vol. III index.",
    links=L("calendarofclaren03bodluoft", "Ashton+partly+in+undeciphered+cipher", "Clar. Cal. vol. III"), prior_art=PA_CL)

# ---------------------------------------------------------------- Pepys manuscripts (HMC 1911)
PEPYS = "Report on the Pepys Manuscripts preserved at Magdalene College, Cambridge (HMC 1911)"
PEPYS_SM = "Pepys Library, Magdalene College, Cambridge (Evelyn gift, Leicester papers; HMC cites vol. %s p. %s); " + PEPYS


def pepys(date, y, sender, recip, place, ms, extra, note):
    return dict(year=y, date=date, place=place, language="English",
                title="%s to %s, %s: %s" % (sender, recip, place, note),
                correspondents="%s → %s" % (sender, recip),
                shelfmark=PEPYS_SM % ms, folio_note=extra, cls="B")


# Norreys->Leicester/Cecil letters in the Pepys MSS (6 Sep 1568, 26 Dec 1568, 15 Mar 1569, 28 Apr 1569) are already in catalogue.json id 872: dropped.

add(year=1561, date="6 Sep 1561", place="Brussels", language="English",
    title="George Gilpin (Elizabeth's agent) to Lord Robert Dudley: cipher passage undeciphered (Prince of Spain's illness, Lady Regent)",
    correspondents="George Gilpin → Lord Robert Dudley",
    shelfmark="Pepys Library, Magdalene College, Cambridge (Evelyn gift, Leicester papers); " + PEPYS,
    folio_note="HMC Pepys pp. 7-8; footnote 'Cipher undeciphered'",
    cls="B",
    status="HMC footnote 'Cipher undeciphered' (a few words). Gilpin's cipher letters to Cecil in CSP Foreign are deciphered by Cecil's secretaries, so the key is partly known.",
    why="Flemish news for Dudley in 1561, before the Dutch revolt.", importance=2, solvability=2, difficulty=2,
    verify="Locate the Pepys MS letter; compare with Gilpin's deciphered letters in SP 70/SP 81.",
    links=L("reportonpepys00greauoft", "Gilpin+Dudley+Brussels", "HMC Pepys"),
    prior_art="open (checked 28 Oct 2026: HMC Pepys text only)")

# Yard->Manchester 12 and 16 Oct 1699 (HMC Eighth Report) are targets/yard1699 (read 18 Sept 2026): dropped.

# ---------------------------------------------------------------- Downshire
add(year=1689, date="1 Jul 1689", place="Warsaw", language="French", region="Poland-Lithuania",
    title="De Veil to Louis XIV: full account of French attempts to win Poland, partly in cipher, undeciphered (copy)",
    correspondents="De Veil (French envoy in Poland) → Louis XIV",
    shelfmark="Trumbull MSS (Sir William Trumbull), Downshire MSS: Report on the Manuscripts of the Marquess of Downshire, vol. I part I (Papers of William Trumbull the Elder), HMC 1924, item XXVII, 23",
    folio_note="5 pp., French, copy; 'partly in cipher, undeciphered, copy'",
    cls="C",
    status="HMC Downshire vol. I part I calendar text: 'partly in cipher, undeciphered, copy'. The original is a French diplomatic cipher; the Trumbull copy came from the Constantinople embassy file.",
    why="French diplomacy in Poland on the eve of the War of the Grand Alliance and the Polish-Turkish war.",
    importance=2, solvability=2, difficulty=3,
    verify="Check the Trumbull Add. MS XXVII (Berkshire Record Office) and whether French archives hold the original despatch (AAE Pologne).",
    links=L("DownshireV1Pt1", "De+Veil+Louis+XIV+Warsaw", "HMC Downshire") if False else [
        {"label": "HMC Downshire vol. I pt I (archive.org item)", "href": "https://archive.org/details/ReportOnTheManuscriptsOfTheMarquessOfDownshireV1Pt1"},
        {"label": "Plain-text OCR", "href": "https://archive.org/download/ReportOnTheManuscriptsOfTheMarquessOfDownshireV1Pt1/Manuscripts_Marquess_of_Downshire_v1_pt1_djvu.txt"}],
    prior_art="open (checked 28 Oct 2026: HMC text only)")

# ---------------------------------------------------------------- Ormonde
add(year=1681, date="15 Oct 1681", place="Whitehall", language="English", region="England",
    title="Sir Leoline Jenkins to Ormond: Post Office passage in numerical cipher, only partly interpreted by the editor",
    correspondents="Sir Leoline Jenkins (Secretary of State) → James Butler, Duke of Ormond",
    shelfmark="Kilkenny Castle MSS / Ormonde papers (now NLI), Calendar of the Manuscripts of the Marquess of Ormonde, K.P., new series vol. VI (HMC 1911), pp. 192-193",
    folio_note="About 55 number groups (e.g. '553 . 184 . 254 . 278 ...') printed in the calendar; 'the words printed in italics are a partial interpretation of the following cipher'",
    cls="B",
    status="Calendar prints the figures and a partial interpretation. The Longford-Ormond cipher key (Mrs Lomas) is printed in the volume Introduction p. xix but the editor notes 'figures uninterpreted' elsewhere (p. 210: 1132).",
    why="Irish Post Office and revenue-farm affairs in Ormond's lord-lieutenancy; a printed ciphertext with a printed partial key.",
    importance=2, solvability=4, difficulty=1,
    verify="Read the calendar pages 192-193 and the key on p. xix; check whether the same cipher number set (Longford's) covers it.",
    links=L("cu31924091754089", "partial+interpretation+of+the+following+cipher", "HMC Ormonde n.s. VI"),
    prior_art="open (checked 28 Oct 2026: printed calendar only)")

# ---------------------------------------------------------------- CSP Ireland
add(year=1636, date="c. Sep 1636", place="Croydon", language="English", region="England",
    title="Archbishop Laud to the Lord Deputy (Wentworth): copy, Trinity College Dublin visitors' dispute, a passage in cipher follows",
    correspondents="William Laud, Archbishop of Canterbury → Thomas Wentworth, Lord Deputy of Ireland",
    shelfmark="TNA, State Papers Ireland, SP 63/255, ff. 141-143 (two copies); Calendar of the State Papers relating to Ireland, 1633-1647 (ed. Mahaffy 1901), p. 141 (Vol. CCLV, 1636)",
    folio_note="Calendar p. 141: 'A passage in cipher follows.' Pp. 2 3/4, two copies; the cipher passage is not printed",
    cls="C",
    status="Calendar omits the cipher passage ('A passage in cipher follows'); no decipher is mentioned.",
    why="Laud and Wentworth on Provost Bedell's/the Trinity College visitation and the Laudian reforms; a cipher passage in an archbishop's letter.",
    importance=3, solvability=2, difficulty=3,
    verify="View SP 63/255 f. 142-143; Wentworth's Strafford Letters (1739) print the letter and may give the passage; check the Sheffield Wentworth Woodhouse Muniments.",
    links=L("cu31924091770887", "A+passage+in+cipher+follows", "CSP Ireland 1633-47"),
    prior_art="open (checked 28 Oct 2026: calendar text; Strafford Letters not searched)")

add(year=1661, date="11 Jun 1661", place="Whitehall", language="English", region="England",
    title="Secretary Nicholas to the Earl of Orrery: Declaration of Settlement, partly in cipher",
    correspondents="Sir Edward Nicholas (Secretary of State) → Roger Boyle, Earl of Orrery (Lord Justice of Ireland)",
    shelfmark="TNA, State Papers Ireland, SP 63/308 (OCR '808'), p. 53 (entry book); Calendar of the State Papers relating to Ireland 1660-1662 (1905), p. 352",
    folio_note="Entry-book copy, 1/2 p., 'partly in cypher'",
    cls="C",
    status="Calendar says 'partly in cypher'; no decipher or key noted. Entry-book copies are short.",
    why="Council's hesitation over amending the Irish Declaration; a short cipher passage in the Restoration cipher between Whitehall and Dublin.",
    importance=1, solvability=2, difficulty=3,
    verify="View SP 63/308 f. 53; look for the Nicholas-Orrery cipher among the Orrery papers.",
    links=L("cu31924091769566", "partly+in+cypher+Orrery", "CSP Ireland 1660-62"),
    prior_art="open (checked 28 Oct 2026: calendar text only)")

add(year=1668, date="12 Dec 1668", place="Whitehall", language="English", region="England",
    title="Secretary Bennet (Lord Arlington) to the Lord Lieutenant: Irish bill; passage in cypher follows ('The King is informed that ...')",
    correspondents="Henry Bennet, Lord Arlington → James Butler, Duke of Ormond (Lord Lieutenant)",
    shelfmark="TNA, State Papers Ireland, SP 63/312 (OCR '812'), pp. 188-189; Calendar of the State Papers relating to Ireland 1666-1669 (ed. Mahaffy, 1908), p. 815",
    folio_note="Entry book, 1 1/4 pp.; '[a passage in cypher follows]'",
    cls="C",
    status="Calendar omits the cypher passage; no decipher mentioned. Ormond-Arlington cipher letters of 1680 are in the Ormonde calendar, so the key family is known.",
    why="The King's information against Ormond's Irish settlement policy in Dec 1668 (the cipher passage is what the King 'is informed').",
    importance=3, solvability=3, difficulty=2,
    verify="View SP 63/312 pp. 188-9; check the Carte MSS (Bodleian) for the deciphered letter from Arlington to Ormond.",
    links=L("calendarstatepa12offigoog", "passage+in+cypher+Rennet", "CSP Ireland 1666-69"),
    prior_art="open (checked 28 Oct 2026: calendar text only)")

add(year=1646, date="2 Jan 1646 (year to confirm)", place="Dublin", language="English", region="England",
    title="'John Poingdexter' (name as OCR) to [unnamed], Dublin: Ireland in a desperate condition; a passage in cipher follows",
    correspondents="John Poingdexter (OCR; sender's name to confirm) → [recipient not named in the calendar]",
    shelfmark="TNA, State Papers Ireland, SP 63/261 (Vol. CCLXI); Calendar of the State Papers relating to Ireland 1633-1647, entry 6146",
    folio_note="Calendar: 'The King's army [a passage follows in cipher]'",
    cls="C",
    status="Calendar omits the cipher passage; sender's name garbled in OCR and the recipient is blank in print, so check the printed page before the merge.",
    why="Dublin under Parliamentary naval blockade in winter 1645-46 with the Glamorgan treaty pending.",
    importance=2, solvability=2, difficulty=3,
    verify="Read calendar entry 6146 (Mahaffy 1901) to confirm sender and year; view SP 63/261.",
    links=L("calendarofstatep02grea", "passage+follows+in+cipher", "CSP Ireland 1633-47"),
    prior_art="open (checked 28 Oct 2026: calendar text only; heading to confirm)")

# ---------------------------------------------------------------- Home Office Papers
add(year=1760, date="14 Sep 1760", place="Hanover / London", language="French", region="Germany",
    title="Hanoverian minister to the Regency/Prince Ferdinand on a Duc de Broglie letter of 17 Aug 1760 sent to London for deciphering and not wholly made out",
    correspondents="Minister of Hanover → Regency; Prince Ferdinand of Brunswick (about a letter of the Duc de Broglie)",
    shelfmark="TNA, Home Office Papers (Domestic Entry Book / Calendar of Home Office Papers of the reign of George III 1760-65, ed. Redington 1878, no. 301)",
    folio_note="Calendar no. 301: translation of a letter; index adds 'Broglie, Duc de, letter from, not deciphered, 301'",
    cls="C",
    status="Calendar: the Broglie letter (French army cipher) was sent to London to be deciphered but the contents were not wholly made out. The ciphertext itself is not identified in the calendar (probably SP 84 Germany or the Cypher Collections).",
    why="Intercepted French army cipher of the Seven Years' War (Marshal Broglie, Aug 1760); the Hanoverian decipherer Boeltzing's work.",
    importance=2, solvability=1, difficulty=4,
    verify="Read the calendar entry; search SP 84 (Germany, Brunswick) and Hanover (Hauptstaatsarchiv) for the Broglie letter of 17 Aug 1760.",
    links=L("cu31924091775217", "Broglio+to+be+deciphered", "Cal. Home Office 1760-65"),
    prior_art="open (checked 28 Oct 2026: calendar text only)")

# ---------------------------------------------------------------- Montereul / Bellievre (SHS 1898-99)
SHS = "The Diplomatic Correspondence of Jean de Montereul and the Brothers de Bellievre, French Ambassadors in England and Scotland, 1645-1648, ed. J. G. Fotheringham (Scottish History Society, vol. II, 1899)"
add(year=1647, date="June 1647", place="Edinburgh", language="French", region="France",
    title="Montereul to Cardinal Mazarin: levies for Spain, effect of the army coup in England; eight lines undeciphered",
    correspondents="Jean de Montereul (French envoy in Scotland) → Cardinal Mazarin",
    shelfmark="Archives du Ministere des Affaires etrangeres, Paris, Correspondance politique Angleterre (as edited); " + SHS + ", letter CLV, pp. 165-166",
    folio_note="'Eight lines of the letter that follow remain undeciphered' (editor's footnote)",
    cls="C",
    status="Fotheringham printed the letter with eight lines left undeciphered. Montereul's letters to Brienne in the same series are near-copies and sometimes carry the plain text (editor p. 498).",
    why="French diplomacy between the Scots and the army in June 1647 (levies for Spain, the King's seizure by the army).",
    importance=3, solvability=3, difficulty=2,
    verify="Check the AAE original (Corr. pol. Angleterre vol. 56-57) via Gallica/the archive; compare the Brienne copies.",
    links=L("diplomaticcorres02mont", "Eight+lines+undeciphered", "Montereul vol. II"),
    prior_art="open (checked 28 Oct 2026: printed edition only)")

add(year=1647, date="late Jun / early Jul 1647 (date garbled in OCR)", place="London", language="French", region="France",
    title="Bellievre to Brienne (Lord Digby's agent, the King's approach to London): nine lines remain undeciphered",
    correspondents="Pomponne de Bellievre (French ambassador extraordinary) → Henri-Auguste de Lomenie, Comte de Brienne",
    shelfmark="Archives du Ministere des Affaires etrangeres, Paris, Correspondance politique Angleterre (as edited); " + SHS + ", letter CLVII, pp. 170-171",
    folio_note="'Nine lines remain here undeciphered' (editor's footnote, p. 170)",
    cls="C",
    status="Edited text leaves nine lines undeciphered. The date line is garbled in the OCR, so confirm in the printed volume.",
    why="French embassy in London during the Presbyterian-army crisis of June-July 1647.",
    importance=3, solvability=3, difficulty=2,
    verify="Read letter CLVII in the volume; compare AAE original.",
    links=L("diplomaticcorres02mont", "Nine+lines+remain+here+undeciphered", "Montereul vol. II"),
    prior_art="open (checked 28 Oct 2026: printed edition only)")

# ---------------------------------------------------------------- Americas
# Poinsett 1813, Anderson 1824 (Revenga) and Everett 1825 are already in catalogue.json (nara_state sweep): dropped.

add(year=1781, date="28 Jan 1781", place="Madrid", language="English", region="Americas",
    title="John Jay (Madrid) to Congress, 28 Jan 1781: letter 'largely in cipher and undeciphered', which led to Congress's action of 27 Apr 1781",
    correspondents="John Jay (US Minister to Spain) → [Congress; recipient not named in Burnett's note]",
    shelfmark="Papers of the Continental Congress (Jay letters; item number not given by Burnett); Letters of Members of the Continental Congress, ed. E. C. Burnett, vol. VI (1933), note 3 to no. 99 (S. Johnston to T. Burke, 8 May 1781); cf. Wharton, Revolutionary Diplomatic Correspondence IV, 381, 384",
    folio_note="Burnett: 'The letter from Jay (Jan. 28, 1781) which led directly to this action is largely in cipher and undeciphered.'",
    cls="C",
    status="Burnett (1933) says the cipher is undeciphered. Jay's other cipher letters were decoded in the Jay Papers and Johnston's edition, so a decode of this letter may already exist.",
    why="Jay's Spanish mission: the Spanish refusal of a loan and the Mississippi claim, in the American cipher of 1780-81.",
    importance=4, solvability=3, difficulty=3,
    verify="Search Johnston's Correspondence and Public Papers of John Jay vol. II and the Jay Papers (Columbia) for 28 Jan 1781; view Papers of the Continental Congress on Fold3/NARA.",
    links=L("lettersofmembers06burn", "largely+in+cipher+and+undeciphered", "Burnett vol. VI"),
    prior_art="open (checked 28 Oct 2026: Burnett note only; Jay Papers edition not yet searched)")

# ---------------------------------------------------------------- Mary Queen of Scots papers (Calendar of State Papers, Scotland, ed. Thorpe 1858, vol. I, Mary section)
THORPE = "Calendar of the State Papers relating to Scotland, 1509-1589, ed. M. J. Thorpe (1858), vol. I, Mary Queen of Scots section"
PA_M = "open as far as found (checked 28 Oct 2026: printed calendar; web search found no decipherment of this item; Fontenay's other despatches were deciphered by Pasquier for Nau and Sheila Richards published some in 1974, and the 1578-84 Mary-Castelnau letters were solved by Lasry et al. 2024, a separate cache; repo targets/sp53 covers SP 53/16 nos. 78-79)"
add(year=1585, date="1 Jul 1585", place="unknown", language="French", region="France",
    title="Fontenay to Nau (Mary Queen of Scots' secretary): cipher letter with an 'illegible interpretation'",
    correspondents="Fontenay (Mary's agent) → Claude Nau",
    shelfmark="TNA, State Papers Scotland, Mary Queen of Scots (SP 53/16, 'Vol. XVI July-December 1585'), no. 1; " + THORPE + ", p. 972",
    folio_note="Calendar: 'Fr. [In cipher, with an illegible interpretation.]'",
    cls="B",
    status="Calendar says the contemporary interpretation is illegible. Repo targets/sp53 notes the 'Mary-Fontenay cipher' (SP 53/22) as a neighbouring key; Fontenay's letter of Aug 1585 (no. 25) is deciphered in the same volume.",
    why="Mary Stuart's own cipher traffic with her secretary in July 1585, months before the Babington plot; a key-bearing sibling set exists.",
    importance=4, solvability=3, difficulty=2,
    verify="View SP 53/16 f. 1 on State Papers Online; compare the deciphered Fontenay letter of 1 Aug 1585 (calendar no. 25-26) and the SP 53/22 'Fontenay' cipher.",
    links=L("calendarstatepa00thorgoog", "Fontenay+illegible+interpretation", "Thorpe Scotland cal."), prior_art=PA_M)

add(year=1586, date="c. 30 Apr 1586 (margin dates garbled; to confirm)", place="Brussels / Flanders (Liggons' interview with Parma)", language="English",
    title="Mr Liggons to the Queen of Scots on his interview with the Prince of Parma and the unpaid Spanish money: a second copy 'undeciphered' beside the copy deciphered by Phelippes",
    correspondents="Mr Liggons (Ligons) → Mary Queen of Scots",
    shelfmark="TNA, State Papers Scotland, Mary Queen of Scots (SP 53/15), nos. 81-82; " + THORPE + ", p. 970",
    folio_note="No. 81 'In cipher, with interlinear explanation by Mr Phelippes'; no. 82 'Another copy of the same letter, undeciphered'",
    cls="A",
    status="Calendar no. 82 is a second cipher copy left undeciphered; no. 81 is the same letter deciphered by Phelippes interlinear (a plain crib).",
    why="A known-plaintext pair in Mary's 1586 cipher family; the Phelippes-deciphered copy gives the key for the rest of the volume.",
    importance=3, solvability=4, difficulty=1,
    verify="View SP 53/15 nos. 81-82; align the two copies (possibly a different cipher or a re-enciphering).",
    links=L("calendarstatepa00thorgoog", "Another+copy+of+the+same+letter+undeciphered", "Thorpe Scotland cal."), prior_art=PA_M)

add(year=1586, date="2-3 Sep 1586 (from the marginal dates; to confirm)", place="London", language="French", region="France",
    title="The French ambassador in England (Chateauneuf) to Courcelles in Scotland, two letters in cipher with no decipher listed (entries 72 and 73)",
    correspondents="Guillaume de L'Aubespine, baron de Chateauneuf (French ambassador in London) → Mons. Courcelles (French agent in Scotland)",
    shelfmark="TNA, State Papers Scotland, Mary Queen of Scots (SP 53, Aug-Sept 1586 volume; number not read), nos. 72-73; " + THORPE + ", pp. 1009-1010",
    folio_note="No. 72 '[In cipher.]', no. 73 'Another letter ... [Also in cipher.]'. The preceding entries (Giffard to Phelippes) show Phelippes' office was reading the French embassy cipher at the time",
    cls="B",
    status="Calendar lists both as 'In cipher' and none of the neighbouring entries is a decipher of them. Intercepted in the wake of the Babington arrests (Giffard/Phelippes). Possibly deciphered in the manuscripts without a calendar note.",
    why="French embassy cipher of 1586 at the moment of the Babington plot and Mary's trial; Courcelles was the French link to James VI.",
    importance=4, solvability=3, difficulty=3,
    verify="View SP 53/18 (or the Aug-Sept 1586 volume) on State Papers Online; check for Phelippes deciphers and the Chateauneuf cipher in SP 78/SP 106.",
    links=L("calendarstatepa00thorgoog", "French+Ambassador+Courcelles+cipher", "Thorpe Scotland cal."), prior_art=PA_M)

add(year=1608, date="7 Apr 1608 (as printed; context is the Earl's flight, so the year may be 1607, to confirm)", place="Howth, near Dublin", language="English", region="England",
    title="Sir Arthur Chichester (Lord Deputy) to the Earl of Salisbury: short numerical cipher passage printed in the calendar, 'to be expounded by the cipher your Lordship sent unto me'",
    correspondents="Sir Arthur Chichester → Robert Cecil, Earl of Salisbury",
    shelfmark="TNA, State Papers Ireland, SP 63/223, no. 69; Calendar of the State Papers relating to Ireland, James I, 1606-1608 (ed. Russell & Prendergast, 1874), entry 634, p. 464",
    folio_note="About 55 number groups interleaved with plain words ('the partie named ... to have had the Lord ... Chancellors mony ... his weife'); Pp. 5, holograph",
    cls="B",
    status="Calendar prints the numbers unread and says only that Salisbury's cipher is to be used. Salisbury-Chichester cipher letters elsewhere in the same volumes are deciphered or printed in clear.",
    why="Chichester's report on the Earl of Tyrone's flight and Sir Garret Moore; the cipher names who had the Lord Chancellor's money.",
    importance=3, solvability=4, difficulty=2,
    verify="Read calendar p. 464; view SP 63/223 f. 69; look for the Salisbury-Chichester cipher among the other numerical passages of 1607-08.",
    links=L("calendarofstatep02grea_0", "To+be+expounded+by+the+cipher", "CSP Ireland James I 1606-08"),
    prior_art="open (checked 28 Oct 2026: printed calendar only; cryptiana/HistoCrypt not searched)")

if __name__ == "__main__":
    json.dump(rows, open("candidates.json", "w", encoding="utf8"), ensure_ascii=False, indent=1)
    print(len(rows), "rows")
