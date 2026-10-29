#!/usr/bin/env bash
# Rounds 60-65: remaining coverage-matrix gaps, low prior, full power (115 long runs), own controls, shuffles.
cd "$(dirname "$0")"; export PYTHONUTF8=1
while ps -ef 2>/dev/null | grep -v grep | grep -q "bigsolve.py"; do sleep 20; done     # let R58/R59 finish first
run(){ tag=$1; shift; echo "== $tag"; env "$@" python bigsolve.py "${ARGS[@]}" 2>&1 | grep -v Warning; env "$@" python bigsolve.py "${NARGS[@]}" 2>&1 | grep -v Warning; }
{
for m in nl-modern pt-modern da-modern sv-modern cy-modern hu-modern pl-modern; do ARGS=(misread 115 6); NARGS=(misread 115 6 --nulls); run "R60 $m + misreads" DORA_SLIP=both DORA_MODEL=$m; done
for m in it-modern es-modern; do ARGS=(homo 115 0); NARGS=(homo 115 0 --nulls); run "R61 homophones $m" DORA_MODEL=$m; done
for tf in backslang reversed abbrev3 skeleton; do ARGS=(misread 115 6); NARGS=(misread 115 6 --nulls); run "R62 $tf + misreads" DORA_SLIP=both DORA_TF=$tf; done
for c in ct_measured.txt ct_jager.txt; do ARGS=(homo 115 0 --ct=$c --noctl); NARGS=(homo 115 0 --ct=$c --nulls); run "R63 homophones $c" DORA_MODEL=en-modern; done
ARGS=(misread 115 6); NARGS=(misread 115 6 --nulls); run "R64 phonetic + misreads" DORA_SLIP=both DORA_TF=phon25 DORA_CMU="$DORA_CMU"
for c in ct_columns.txt ct_linesrev.txt; do ARGS=(misread 115 6 --ct=$c --noctl); NARGS=(misread 115 6 --ct=$c --nulls); run "R65 $c + misreads" DORA_SLIP=both DORA_MODEL=en-modern; done
} > runs/r60_65.txt
echo "R60-R65 done"
