#!/bin/zsh
# Copies chapter/appendix sources written by the council agents in the
# working directory into this repository's MSc-style layout.
set -u
cpif(){ if [ -f "$1" ]; then cp "$1" "$2"; else echo "skip (not yet written): $1"; [ -f "$2" ] || printf '\\chapter{%s}\\label{%s}\n\\gap{Chapter not yet drafted; scheduled in the loop order of LOOP.md.}\n' "$3" "$(basename "$1" .tex)" > "$2"; fi; }
W=~/PhD-Topic-Council/thesis
R=~/PhD-Mathematical-Statistics
cpif "$W/chapters/ch1-introduction.tex" "$R/Thesis/Chapter 1/src/chapter1_introduction.tex" "Introduction"
cpif "$W/chapters/ch2-preliminaries.tex" "$R/Thesis/Chapter 2/src/chapter2_preliminaries.tex" "Preliminaries"
cpif "$W/chapters/ch3-certification.tex" "$R/Thesis/Chapter 3/src/chapter3_certification.tex" "Finite-Sample Certification of Hedging Error"
cpif "$W/chapters/ch4-sharpness-blocking.tex" "$R/Thesis/Chapter 4/src/chapter4_sharpness_blocking.tex" "Sharpness and Optimal Blocking"
cpif "$W/chapters/ch5-identifiability.tex" "$R/Thesis/Chapter 5/src/chapter5_identifiability.tex" "Identifiability of the Successor-Rate Smile"
cpif "$W/chapters/ch6-usd-validation.tex" "$R/Thesis/Chapter 6/src/chapter6_usd_validation.tex" "Validation on the USD LIBOR-to-SOFR Transition"
cpif "$W/chapters/ch7-zar-coda.tex" "$R/Thesis/Chapter 7/src/chapter7_zar_coda.tex" "The South African Converted Book"
cpif "$W/chapters/ch8-conclusions.tex" "$R/Thesis/Chapter 8/src/chapter8_conclusions.tex" "Conclusions"
cpif "$W/appendices/appA-tenor.tex" "$R/Thesis/Annexures/annexureA_tenor_consistency.tex" "Tenor Consistency of Compounded-Rate Smiles"
cpif "$W/appendices/appB-proofs-standard.tex" "$R/Thesis/Annexures/annexureB_standard_proofs.tex" "Proofs of Standard Results"
# Appendix C is assembled from its parts
{ echo '\chapter{Data, Code and Reproducibility}\label{appC-data-code}';
  echo '\section{USD data}'; cat "$W/appendices/appC-usd-data.tex" 2>/dev/null || true;
  echo '\section{ZAR data}'; cat "$W/appendices/appC-zar-data.tex" 2>/dev/null || true;
  echo '\section{Code architecture}'; cat "$W/appendices/appC-code.tex" 2>/dev/null || true;
  echo '\section{Reproducibility protocol}'; echo '\gap{Written by thesis-writer-appC-data once code and data sections exist.}'; } > "$R/Thesis/Annexures/annexureC_data_code.tex"
[ -d "$W/code" ] && rsync -a --delete "$W/code/" "$R/Code/"
echo synced
