# Pricing and Hedging Through a Benchmark Transition Without an Options Market

Identifiability, Smile Transport and Finite-Sample Model-Risk Certification for the JIBAR-to-ZARONIA Derivatives Book.

PhD thesis in **Mathematical Statistics**. Institution, faculty and school are set in three macros at the top of `main.tex`; the repository holds a conditional offer from the University of the Free State for the 2027 intake (`Offer/`), and the manuscript is currently framed for the University of the Witwatersrand pending the candidate's decision.

**Author:** Thabang Bongani Junior Baloyi
**Supervisor:** To be confirmed
**Programme:** Three years, statistics spine first, USD LIBOR-to-SOFR transition as the empirical spine, South African converted book as the coda

## Overview

On 31 December 2026 JIBAR is published for the last time. Under the fallback adopted by the SARB Market Practitioners Group and ISDA, every legacy JIBAR cap, floor and swaption becomes an option on compounded ZARONIA plus a fixed credit adjustment spread (16.19 bp for three months, fixed 3 December 2025). Unlike the USD LIBOR-to-SOFR transition, the successor rate has no options market and none is expected before the transition completes. Banks must value, hedge and reserve against a converted option book whose volatility smile cannot be observed.

The thesis treats this as a problem of identifiability and finite-sample inference, in three parts.

1. **Certification** (statistics). For a fixed valuation-and-hedging policy applied to the converted book, a split-conformal certificate on realised hedging error under serial dependence and drift: a finite-sample coverage bound whose deficit is an explicit Kolmogorov-distance drift term plus a Beta-quantile concentration term plus a coupling term. The drift term is shown to be sharp, and the block length that minimises the deficit is derived together with a minimax lower bound over a mixing class. This is the doctoral contribution.

2. **Identifiability** (mathematical finance). A decomposition of the map from the observable JIBAR-world inputs to the unobservable compounded-rate smile into an identified component (strike shift, deterministic time change, curvature) and a non-identified component driven by the two correlations between the JIBAR-ZARONIA basis and the rate and volatility drivers. The successor at-the-money volatility is identified only within an interval of half-width equal to the basis volatility. Two models are exhibited that match every South African instrument and disagree on the converted book.

3. **Validation and application** (empirical). The theory is validated on the USD LIBOR-to-SOFR transition of 2021 to 2023, where both option markets eventually traded and the target smile became observable, and then applied to the South African converted book to produce a model-risk reserve with a stated confidence level.

## Status

Draft manuscript under construction by a write, review, revise, compile loop. Results marked **To be established** in the text are targets with a stated proof route, not proved theorems. The running log is `Claude Workspace/CHANGES_REVIEW.md`.

## Methods and Tools

- **Statistics:** split conformal prediction, Beta law of conditional coverage, Berbee coupling for beta-mixing sequences, Kolmogorov and Wasserstein distances, adversarial and minimax lower bounds, stationary block bootstrap
- **Finance:** forward measures, backward-looking compounded rates, Lyashenko-Mercurio volatility decay, time-changed SABR, Hagan asymptotics, ISDA fallback mechanics
- **Language:** Python (NumPy, SciPy) for the reference implementations in `Code/`
- **Typesetting:** LaTeX (`report` class, natbib author-year, glossaries), compiled with Tectonic

## Repository Structure

```
.
├── README.md
├── main.tex                          # Root LaTeX document
├── References.bib                    # Bibliography (BibTeX, natbib author-year)
├── .claude/                          # Agent + skill definitions (must stay at repo root
│                                      # for Claude Code to discover them — not moved below)
├── Claude Workspace/                 # Everything else AI/agent-related, gitignored except:
│   ├── CHANGES_REVIEW.md             #   write, review, revise, compile log (tracked)
│   ├── AGENTS.md                     #   agent roster notes (tracked)
│   ├── sync_from_workdir.sh          #   pulls council-agent drafts into Thesis/ (tracked)
│   └── thesis/, 01-...13-...         #   council drafting scratch space (untracked)
├── Code/                             # Reference implementations with tests
│   ├── rates/                        # Multi-curve bootstrap, time-changed SABR caplets
│   └── certify/                      # Blocked conformal certificate, drift bound, bootstrap
├── Thesis/                           # LaTeX source by chapter
│   ├── Chapter 1/ ... Chapter 10/    # Each with src/ and Figures/; 9-10 are placeholders
│   ├── Annexures/                    # A tenor consistency, B standard proofs, C data and code
│   ├── Abstract/  Acknowledgments/  Acronym Definitions/  Cover Page/  Declarations/
│   ├── List of Equations/            # Notation table
│   └── macros.tex                    # Shared macros used by every chapter
├── References/                       # Papers (PDF/), highlight notes, and:
│   └── Books/                        # Full reference textbooks (not individual papers)
├── Research Proposal/                # Proposal, mathematics and three-year plan, council verdicts
└── Offer/                            # Admission correspondence
```

## Thesis Structure

| Chapter | Title | Content |
|---------|-------|---------|
| 1 | Introduction | The South African transition, the valuation problem, contributions |
| 2 | Preliminaries | Forward measures, compounded rates, time-changed SABR, conformal prediction, mixing |
| 3 | Finite-Sample Certification of Hedging Error | The certificate theorem and the drift bound |
| 4 | Sharpness and Optimal Blocking | Sharpness of the drift term; optimal block length and minimax rate |
| 5 | Identifiability of the Successor-Rate Smile | Identified and non-identified components; two models |
| 6 | Validation on the USD LIBOR-to-SOFR Transition | Natural experiment for Chapters 3 to 5 |
| 7 | The South African Converted Book | Reserve decomposition on available data |
| 8 | Conclusions | Limitations, contributions, future work |
| 9 | *Untitled (placeholder)* | Topic not yet decided — not part of the current GROUND-TRUTH/STANDARD plan |
| 10 | *Untitled (placeholder)* | Topic not yet decided — not part of the current GROUND-TRUTH/STANDARD plan |
| A | Tenor Consistency of Compounded-Rate Smiles | |
| B | Proofs of Standard Results | |
| C | Data, Code and Reproducibility | |

## Building

```
tectonic main.tex
```

### Compiling one chapter alone

Every chapter/annexure `.tex` file is a `subfiles` document: it has its own
`\documentclass[<path to main.tex>]{subfiles}` / `\begin{document}` wrapper
around the same `\chapter{...}` content, and `main.tex` pulls it in with
`\subfile{}` instead of `\input{}`. That lets any one file compile alone —
useful for a fast side-by-side PDF preview while editing, instead of
rebuilding the whole thesis.

To open a file's own preview: build just that file (`Cmd+Alt+B` in VS Code
with LaTeX Workshop, or `tectonic "path/to/file.tex"` in the terminal), then
view the PDF beside the editor (`Cmd+Alt+V`). It rebuilds in a couple of
seconds instead of the full thesis's ~30s+.

**If you add a new chapter or annexure**, give it the same wrapper:

1. At the top of the new file, before `\chapter{...}`:
   ```latex
   \documentclass[<relative-path-to-main.tex>]{subfiles}
   \begin{document}
   ```
   The path is relative to the new file's own location — count directories
   up to the repo root. A chapter at `Thesis/Chapter N/src/file.tex` uses
   `../../../main.tex`; an annexure at `Thesis/Annexures/file.tex` uses
   `../../main.tex`.
2. At the end of the file, add a blank line then:
   ```latex
   \end{document}
   ```
3. In `main.tex`, change that file's `\input{...}` line to `\subfile{...}`
   (same path, no other change needed — `subfiles` is already loaded in the
   preamble).
4. Do one full `tectonic main.tex` build so the new subfile's `.aux` exists
   and its cross-references resolve when compiled alone.

## How to Cite

```
Baloyi, T.B.J. (2029). Pricing and Hedging Through a Benchmark Transition Without an
Options Market: Identifiability, Smile Transport and Finite-Sample Model-Risk
Certification for the JIBAR-to-ZARONIA Derivatives Book. PhD thesis.
```

## Keywords

conformal prediction, beta-mixing, finite-sample coverage, minimax lower bound, benchmark reform, JIBAR, ZARONIA, compounded rates, SABR, identifiability, model risk, hedging error

## Licence

All rights reserved under the intellectual property policy of the awarding institution.
