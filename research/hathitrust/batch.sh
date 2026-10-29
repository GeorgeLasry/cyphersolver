O=/c/Users/dbour/cypher/.work/hathi_scan
python scan.py 'title:("calendar of the manuscripts" OR "report on the manuscripts") AND (salisbury OR hatfield)' 25 > $O/c1.txt 2>&1
python scan.py 'title:("calendar of state papers" OR "calendar of the state papers") AND (domestic OR foreign OR colonial OR ireland)' 30 > $O/c2.txt 2>&1
python scan.py 'title:(clarendon OR thurloe OR "treasury papers" OR "home office papers") AND title:calendar' 15 > $O/c3.txt 2>&1
python scan.py 'title:("official records of the union")' 12 > $O/c4.txt 2>&1
python scan.py 'title:("continental congress" OR "archives of maryland" OR "pennsylvania archives" OR "colonial history of the state of new york")' 25 > $O/c5.txt 2>&1
