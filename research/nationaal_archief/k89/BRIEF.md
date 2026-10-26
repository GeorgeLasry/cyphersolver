# Brief: flag cipher pages on KHA contact sheets (K8/K9)

Folder: C:\Users\dbour\cypher\research\nationaal_archief\k89. Each `sheet_<item>_<nn>.jpg` holds 60 thumbnails
labelled `<scan number>:<image id>` in red. Items are 1786-1819 letters to/from Princess Wilhelmina and the future
Willem I (Van de Spiegel, Van Reede, Nagell, Thulemeier, Stamford, Bentinck, d'Yvoy, Hogguer, Van der Hoop).

Look at every sheet you are given (Read tool). Flag any thumbnail that shows cipher: runs or pages of numbers
(e.g. "52,1,2, 128; 147"), symbol cipher, a key table or alphabet grid, or a letter with numbers between the
lines. For each flagged thumbnail, if unsure, open `th/<id>.jpg` (400 px) to check. Do not try to read the cipher.

Append one line per flagged scan to your output file as soon as you see it (tab-separated):
item, scan number, image id, kind (numbers in text / solid numbers / interlined decipherment / key table /
symbols / other), one-line note (date or heading if legible at 400 px, decipherment visible yes/no).
After each sheet, append a line `# done <sheet file> flagged <n>`. ASCII only. End by replying with flagged
counts per item and the most promising items (a cipher letter with a decipherment or a key nearby).
