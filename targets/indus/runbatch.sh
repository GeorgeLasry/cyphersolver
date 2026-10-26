#!/bin/sh
# runbatch.sh <first_set> <first_loop> <streak> mod1 mod2 ...: run session-2 loops in order, carrying the streak.
n=$1; loop=$2; streak=$3; shift 3
for m in "$@"; do
  out=$(PYTHONUTF8=1 python mydriver.py $n $loop $streak $m 2>&1)
  echo "== set $n loop $loop $m"; echo "$out" | grep -E "^- |\*\*|STREAK|Error|Traceback"
  s=$(echo "$out" | grep STREAK | awk '{print $2}'); [ -z "$s" ] && { echo "STOP: no streak"; exit 1; }
  streak=$s; n=$((n+1)); loop=$((loop+1))
  [ "$streak" -ge 20 ] && { echo "GOAL: streak 20"; exit 0; }
done
echo "NEXT $n $loop $streak"
