"""Write candidates.json for the NAA RecordSearch sweep (28 Oct 2026). Rows are hand-picked from review.tsv."""
import json
D = 'https://recordsearch.naa.gov.au/SearchNRetrieve/Interface/DetailsReports/ItemDetail.aspx?Barcode='
V = 'https://recordsearch.naa.gov.au/SearchNRetrieve/Interface/ViewImage.aspx?B='
NOTE = 'Scored from the archive description during the Oct 2026 NAA RecordSearch sweep (research/oceania_naa/); not viewed'
NOTE_IMG = 'Scored during the Oct 2026 NAA RecordSearch sweep (research/oceania_naa/) after viewing a few pages'
PA = 'open (checked 28 Oct 2026: repo known.py, web search)'


def row(year, date, title, corr, place, lang, region, period, shelf, fol, cls, status, why, imp, sol, dif, verify, bcs,
        seen='catalogue', prior=PA, dig=False):
    links = []
    for b in bcs:
        links.append({'label': f'NAA item {b} (RecordSearch; open a search session first)', 'href': D + b})
        if dig:
            links.append({'label': f'NAA digital copy {b}', 'href': V + b})
    return dict(year=year, date=date, title=title, correspondents=corr, place=place, language=lang, region=region,
                period=period, shelfmark=shelf, folio_note=fol, cls=cls, status=status, why=why, importance=imp,
                solvability=sol, difficulty=dif, score_note=NOTE_IMG if seen == 'image' else NOTE, verify=verify,
                links=links, seen=seen, source='National Archives of Australia RecordSearch sweep', prior_art=prior)


C = [
    row(1918, '11 Jan 1918', 'Fanning Island radio: unknown wireless groups intercepted, attributed to a Japanese warship',
        'unknown sender (Admiralty guessed a Japanese man-of-war) -> intercepted by the Fanning Island W/T station',
        'Pacific (Fanning Island)', 'unknown', 'Other', '1901-1950',
        'NAA: MP1049/1, 1914/0467 (Navy Office, Wireless telegraphy intercepted messages 1914-1918 War), item 405327',
        'Telegram copy at digital page 8: about 14 two-letter groups (YO UT UP ...); Admiralty letter of 22 Jan 1918 at p. 5; file 1914-19, digitised',
        'C',
        'Digitised file, opened 28 Oct 2026: the Navy Office telegram copies the groups with a note on one doubtful letter; '
        'the Admiralty only says the message was "probably made by a Japanese man-of-war". No reading on file in the pages seen. '
        'The rest of the file (other intercepts, "unknown wireless signals" 1918) was not read through.',
        'An unexplained naval W/T intercept in the Pacific in 1918; the rest of the file may hold more unread German or Japanese traffic.',
        2, 1, 5, 'Page through all of MP1049/1 1914/0467 (digitised) and list every intercept with no plain text beside it',
        ['405327'], seen='image', dig=True),
    row(1902, '1902-1903', 'Telegram in cypher from London to the Governor-General of Australia, left untranslated',
        'London (Colonial Office / Secretary of State) -> Governor-General of Australia', 'London', 'English (code words)',
        'Other', '1901-1950', "NAA: A6662, 50 (Governor General's Office correspondence), item 935087",
        'One telegram; the catalogue quotes its opening: "Nowise anerrone heartily bank you kinetic and Commonwealth of Australia aureka kind kock leoast George"',
        'B',
        'Catalogue title says "Telegram in cypher from London untranslated". Code words mixed with clear; Colonial Office cypher and code '
        'books of the period are held by NAA (A12000, A11804 1912/23 Cypher R 1903 ed., B197, A9553 Decypher CO1 1922). Not digitised.',
        "A government code telegram the Governor-General's office never translated; a test of whether the CO code books held in Canberra read it.",
        2, 2, 3, 'Request a digital copy of A6662/50; try the Colonial Office code books (A12000, A11804 1912/23 Cypher R)', ['935087']),
    row(1940, '1939-1941', 'Japanese Consul-General in Australia: messages in code (seized consulate papers)',
        'Japanese Consulate-General, Sydney <-> Tokyo / Japanese firms (unknown)', 'Sydney', 'Japanese', 'Other', '1901-1950',
        'NAA: C443, J427 (Correspondence of the Japanese Consul General in Australia), item 313533',
        '3 cm of papers, box 9; not digitised', 'C',
        'Catalogue: "Japanese messages in code [Collection maintained by the Japanese Consul General in Australia]". Series C443 is the '
        "consulate's own papers, seized in Dec 1941. Whether the file holds code text without plain text, or code-word lists, is unknown. "
        'Japanese diplomatic codes of 1939-41 were broken by D Special Section and FRUMEL (Ball and Tamura 2013), but these consular '
        'copies may be commercial code telegrams.',
        "Code messages of the Japanese consulate in Sydney on the eve of the Pacific war, possibly the consul's own code-word telegrams.",
        3, 2, 4, 'Request digitisation of C443/J427; compare with Ball & Tamura, Breaking Japanese Diplomatic Codes (2013)', ['313533'],
        prior='open (checked 28 Oct 2026: web search; D Special Section broke Japanese diplomatic codes 1941-45, nothing on these consular copies)'),
    row(1946, '1946', 'Japanese messages in code, Investigation Branch file (3 pages)', 'unknown (Japanese) -> unknown', 'Sydney',
        'Japanese', 'Other', '1901-1950', 'NAA: C439, 5 (Investigation Branch), item 1789203', '3 pages; not digitised', 'C',
        'Catalogue title only: "Japanese messages in code [Investigation Branch correspondence][3 pages]". No decipherment noted.',
        'Short post-war Japanese code messages that reached the Commonwealth Investigation Branch.', 2, 2, 4,
        'Request a digital copy of C439/5', ['1789203']),
    row(1943, '1943-1944', 'Intercepted telegrams between the French Committee (Algiers) and the French Delegation in Australia',
        'French Committee of National Liberation <-> French Delegation in Australia', 'Algiers / Canberra', 'French', 'Other', '1901-1950',
        'NAA: A989, E1943/350/9/7 PART 1 (item 184174) and A989, 1944/350/9/7 (item 184175)', 'Two files, extent unknown; not digitised', 'C',
        'Titles: "France: Intercepted telegrams between French Committee and Delegation in Australia" (1943) and "... to and from French '
        'Delegation in Australia" (1944). Related files A989 1944/350/19/8 "French Representative in Australia. Cyphers and Codes" and '
        'MP1049/5 1835/2/736 "Fighting French - use of code & cypher" show the delegation used its own cipher. Whether the intercepts are '
        'ciphertext only or carry Allied decrypts is not stated.',
        'Free French diplomatic cipher traffic from Australia, otherwise unpublished; Australia never officially admitted intercepting diplomatic traffic.',
        3, 2, 4, 'Request digital copies of both A989 files; check whether decrypts are filed with the intercepts', ['184174', '184175'],
        prior='open (checked 28 Oct 2026: web search, nothing on Australian intercepts of Free French traffic)'),
    row(1918, 'Jun-Aug 1918', 'Radiotelegraphic messages to and from Japanese residents in the Pacific, intercepted by the Navy',
        'Japanese residents in the Pacific islands <-> unknown', 'Pacific islands', 'Japanese (romanised?)', 'Other', '1901-1950',
        'NAA: CP506/1, 1 (item 8352370); also CP506/1, BUNDLE 1 (item 260520)', 'Extent unknown; not digitised', 'C',
        'Title: "Copies of Radiotelegraphic messages to and from Japanese residents in the Pacific intercepted by the Navy Department June 1918". '
        'Language or code not stated.',
        'Australian wartime surveillance of Japanese residents in the former German Pacific; code content possible.', 2, 2, 3,
        'Request a copy of CP506/1, 1 and check for code groups', ['8352370', '260520']),
    row(1916, '1914-1916', 'Intercepted Dutch wireless messages (Netherlands Indies), Navy Office file',
        'Dutch stations (Netherlands Indies) -> unknown', 'Netherlands East Indies', 'Dutch', 'Other', '1901-1950',
        'NAA: MP1049/1, 1916/0235 (Examination of wireless telegraphy intercepted messages, war period 1914-1918), item 400554',
        'Digitised; pages 3 and 8 are minutes about "copies of intercepted Dutch messages" (Apr-May 1916)', 'C',
        'Viewed two pages 28 Oct 2026: the Navy found it was "getting very little from these messages" and cancelled the instruction to '
        'forward them. Whether the copies are in code, and whether any are on file, not checked.',
        'Neutral Dutch wireless traffic watched by Australia in WWI; low weight unless coded.', 1, 2, 3,
        'Page through the digitised file for message copies', ['400554'], seen='image', dig=True),
    row(1916, 'circa 1914-1918', "German soldier's notebook, partly written in code (captured WWI document)",
        'unknown German soldier (own notes)', 'unknown (front)', 'German', 'Germany', '1901-1950',
        'Australian War Memorial: AWM46, 96 (Captured German documents, 1914-18 War), NAA item 5194688',
        'Notebook with notes on training; part in code; access "Not yet examined"; not digitised', 'C',
        'Catalogue: "German soldier\'s notebook - contains notes on training experiences - partly written in code - (German language)". No reading noted.',
        "A private soldier's coded notebook passages; likely a simple personal cipher.", 1, 2, 2,
        'Ask the AWM for a copy of AWM46/96', ['5194688']),
    row(1918, '1918', 'Robert Fleming, Melbourne: secret communications in code (censor case)', 'Robert Fleming -> unknown', 'Melbourne',
        'English', 'Other', '1901-1950', 'NAA: B741, V/95 (Military Intelligence, 3rd Military District), item 395925', 'Not digitised', 'C',
        'Catalogue title: "Fleming Robert - Secret Communications in code". Outcome unknown.',
        'Wartime suspect correspondence in a private code.', 1, 2, 3, 'Request a copy of B741 V/95', ['395925']),
    row(1943, '1943', 'Defence censorship: Mr Stiver, use of a secret code', 'Stiver -> unknown', 'Australia', 'English', 'Other', '1901-1950',
        'NAA: A989, 1943/235/1/2/19 (External Affairs), item 183724', 'Not digitised', 'C',
        'Catalogue title only. Whether the code text is on file is unknown.', 'Censorship case of a private secret code.', 1, 1, 3,
        'Request a copy of A989 1943/235/1/2/19', ['183724']),
    row(1899, '1899', 'Telegrams in code from James Robert Dickson to Major-General Howell Gunter, Australian Club, Sydney',
        'James Robert Dickson (Queensland premier 1898-99) -> Maj.-Gen. Howell Gunter', 'Brisbane -> Sydney', 'English (code)', 'Other',
        '1801-1900', 'NAA: MP744/6, 547, item 10504567', 'Not digitised', 'C',
        'Title: "Telegrams in code to Major General Howell Gunter, Australian Club Sydney from James Robert Dickson". No decode noted.',
        'Private code telegrams between a colonial premier and a general on the eve of Federation.', 2, 2, 3,
        'Request a copy of MP744/6 547; check for a commercial code (ABC, Slater) or a private code-word list', ['10504567']),
    row(1939, '1939-1940', 'NSW Security Service: secret message relating to German sabotage', 'unknown -> unknown', 'New South Wales',
        'unknown', 'Other', '1901-1950', 'NAA: C320, SAB2, item 305911', 'Not digitised', 'C',
        'Catalogue title: "[NSW Security Service file - Secret message relating to German sabotage]". Whether in code, and whether read, unknown.',
        'A security-service file on a German sabotage message at the outbreak of WWII.', 2, 1, 3, 'Request a copy of C320 SAB2', ['305911']),
    row(1918, '1918', 'Wireless messages picked up at Long Beach, Sandy Bay (Tasmania) and intercepted by SS Manuka',
        'unknown -> unknown', 'Tasmania', 'unknown', 'Other', '1901-1950', 'NAA: MP1049/1, 1918/0291, item 407615', 'Not digitised', 'C',
        'Title only. 1918 was the year of the raider Wolf scare off Australia; nature of the messages unknown.',
        'Possible enemy or unexplained wireless traffic in Australian waters in 1918.', 2, 1, 4,
        'Request a copy of MP1049/1 1918/0291', ['407615']),
    row(1916, '1915-1918', 'Navy Department: copies of intercepted wireless messages and of messages between enemy firms and correspondents',
        'enemy (German) firms <-> correspondents; intercepted W/T', 'Australia', 'German / English', 'Other', '1901-1950',
        'NAA: A3200, TEM78, item 233108', 'Not digitised', 'C', 'Title only; code content not stated.',
        'WWI enemy commercial and wireless traffic intercepted in Australia.', 2, 1, 3, 'Request a copy of A3200 TEM78', ['233108']),
    row(1916, '1916', 'Telegraphy signals intercepted by the Fiji station', 'unknown -> unknown', 'Fiji', 'unknown', 'Other', '1901-1950',
        'NAA: B543, W389/3/125, item 412931', 'Not digitised', 'C', 'Title only.', 'A WWI Pacific intercept.', 1, 1, 4,
        'Request a copy of B543 W389/3/125', ['412931']),
    row(1916, '1916', 'Code telegrams not understood (2nd Military District, Sydney)', 'unknown -> District HQ Sydney', 'Sydney',
        'English (code)', 'Other', '1901-1950', 'NAA: SP1141/1, S6/1/19, item 679568', 'Not digitised', 'C',
        'Title only; probably garbled military code telegrams.', 'Low: probably corrupt telegrams in a known code.', 1, 1, 2,
        'Request a copy of SP1141/1 S6/1/19', ['679568']),
    row(1939, '1939', 'European war 1939: intercepted wireless messages (Navy)', 'unknown -> unknown', 'Australia', 'unknown', 'Other',
        '1901-1950', 'NAA: MP1049/5, 2037/2/27, item 503067', 'Not digitised', 'C', 'Title only.',
        'Early-WWII wireless intercepts held by the Navy Office.', 1, 1, 4, 'Request a copy of MP1049/5 2037/2/27', ['503067']),
    row(1927, '28 Mar - 12 Apr 1927', 'Naval Board: intercepted wireless/transmission messages', 'unknown -> unknown', 'Australia',
        'unknown', 'Other', '1901-1950', 'NAA: MP1074/8, 44, item 4169037', 'Not digitised', 'C',
        "Title only; the same series holds the Board's own decyphers.", 'Peacetime naval intercepts.', 1, 1, 4,
        'Request a copy of MP1074/8 44', ['4169037']),
]
json.dump(C, open('candidates.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(C))
