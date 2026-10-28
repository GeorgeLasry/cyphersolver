#!/usr/bin/env bash
cd "$(dirname "$0")"; export PYTHONUTF8=1
run(){ tag=$1; shift; echo "== $tag"; env "$@" python bigsolve.py "${ARGS[@]}" 2>&1 | grep -v Warning; env "$@" python bigsolve.py "${NARGS[@]}" 2>&1 | grep -v Warning; }
{
for c in ct_diag.txt ct_spiral.txt ct_colsrev.txt; do ARGS=(misread 115 0 --ct=$c --noctl); NARGS=(misread 115 0 --ct=$c --nulls); run "R48 order $c" DORA_MODEL=en-modern; done
for m in la fr-modern de-modern it-modern es-modern; do ARGS=(misread 115 0 --ct=ct_measured.txt --noctl); NARGS=(misread 115 0 --ct=ct_measured.txt --nulls); run "R49 measured $m" DORA_MODEL=$m; done
for m in la fr-modern de-modern it-modern es-modern; do ARGS=(misread 115 0 --ct=ct_jager.txt --noctl); NARGS=(misread 115 0 --ct=ct_jager.txt --nulls); run "R50 jager $m" DORA_MODEL=$m; done
} > runs/r48_50.txt
