# Brief: transcribe d'Yvoy cipher passages (KHA A35-1450-1452, London 1797-99), with any decipherment

Folder: C:\Users\dbour\cypher\targets\yvoy1797. Fetch each page at full size:
  curl -sL -A "Mozilla/5.0 Chrome/120" -o full/<id>.jpg "https://cms.koninklijkeverzamelingen.nl/api/images/rendition/<id>/original/"
(mkdir full first). View in horizontal strips (python PIL crops of about 1/6 of the page height at full width,
saved in your scratch folder, opened with the Read tool); zoom more where needed.

Letters of Maximilien d'Yvoy (London) to the Hereditary Prince, and letters to d'Yvoy, 1797-99, in French or
Dutch, with code numbers (1-4 digits, up to about 1,400) among clear words. Often a decipherment (Dutch or French
words) is written above the numbers, e.g. 1341 = "Zeeland", "101 1216 723" = "in Hamptoncourt men".
Some scans are photocopies of the page beside them: say so, and transcribe only the better copy.

For each run (groups between clear words, or one manuscript line of groups):

    # id <id> run <k>
    BEFORE: <up to 8 clear words just before the run>
    CT: <the numbers in order, space separated; marks as in N_ (underline), N' (prime), N^bar; ? if unreadable>
    AFTER: <up to 8 clear words just after>
    PT: <the decipherment written over the run, exactly; else: none>
    AL: <number=word ... when the decipherment is written word by word over the numbers; else: none>

ASCII only (drop accents). Append each block as soon as done. Start the file for each page with a line
`# page <id> <date/heading as written> <language of the clear text>`. Final reply: pages, runs, numbers, how many
runs glossed, and the repeated number=word pairs you noticed.
