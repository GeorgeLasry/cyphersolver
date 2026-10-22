#!/bin/sh
# EN: Recompute every control in controls/results.txt (needs wordfreq). 対照をすべて計算し直す
cd "$(dirname "$0")/.."
run() { printf '%s\n' "## $*"; python3 src/control.py "$@" | tail -1; }
run data/key.tsv data/transcription_f50.txt 1000
run data/key.tsv data/transcription_f50.txt 1000 --table-only
run controls/key_without_target.tsv data/transcription_f50.txt 1000
run data/key.tsv controls/heldout_last_fifth.txt 1000
run controls/key_without_target.tsv controls/heldout_last_fifth.txt 1000
for f in second/codex_pass1.txt second/codex_pass2.txt second/codex_pass3.txt second/codex_pass4_halves.txt second/codex_pass5_halves.txt; do run data/key.tsv "$f" 1000; done
