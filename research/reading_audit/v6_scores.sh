#!/bin/sh
# v6: score every file of v6_spelling_files.txt with v2_score.py (plain and explicit-hole shares)
cd "$(dirname "$0")/../.."
lang() { case "$1" in *carpio*|*ronquillo*|*esp318*) echo es;; *r2232*|*rakoczi*) echo fr;; *turculet*) echo la;; *) echo en;; esac; }
for f in $(cat research/reading_audit/v6_spelling_files.txt); do
  PYTHONUTF8=1 python research/reading_audit/v2_score.py "$f" "$(lang $f)" 2>&1 | tail -1
done
