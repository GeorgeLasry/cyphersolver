O=/c/Users/dbour/cypher/.work/hathi_scan
python scan.py 'title:("calendar of state papers" AND domestic) AND NOT title:colonial' 120 > $O/d1.txt 2>&1
python scan.py 'title:("state papers" AND (domestic OR "foreign series") AND calendar) AND (date:[1860-01-01 TO 1930-12-31])' 120 > $O/d2.txt 2>&1
