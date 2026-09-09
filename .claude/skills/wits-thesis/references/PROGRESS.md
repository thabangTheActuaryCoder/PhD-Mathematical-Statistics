# PROGRESS (orchestrator updates after each compile)

## Page-budget audit, 2026-09-09 (thesis-page-budget-auditor)

Sources: working copies `"~/Desktop/PhD Thesis/Council" Workspace/thesis/chapters/*.tex`, `appendices/*.tex`; compiled `"~/Desktop/PhD Thesis/main.pdf`" (159 pages, built 16:10:53 from the repository copy, `report` class, 12pt, 1.5 spacing, 40/30 mm margins).
Method: words = source words after stripping comments and control sequences (`sed`), not `pdftotext` words; estimate = words/300; typeset = page span in main.pdf. Calibration on this build: ch2 260 source words per typeset page (proof-heavy, many displays), ch3 300, App C 318. `pdftotext` word counts overshoot by about 35 % because mathematics tokenises as words; do not use them.
Caveat: ch3 was edited at 16:13:08, after the compile; the typeset span below is from the 11,389-word repository copy, the word count from the 12,032-word working copy. Stub chapters cost 2 typeset pages each (heading page plus `openright` blank).

| Part | File(s) | Words | Est. pages @300 | Typeset pages (main.pdf) | Budget | Status | Delta vs budget (typeset) |
|---|---|---|---|---|---|---|---|
| Front matter | frontmatter/*.tex (5 files) | 360 | 1 | 22 (pp 1-22) | 12 | drafted shell; abstract and acknowledgements are `\gap{}`; 3-level TOC = 5 pp | +10 |
| Ch1 Introduction | ch1-introduction.tex | 12 | 0 | 2 (pp 23-24) | 24 | stub | -22 |
| Ch2 Preliminaries | ch2-preliminaries.tex | 15,097 | 50 | 58 (pp 25-82) | 48 | drafted; under finance review; 1 gap box (Prop 2 curvature accounting), 4 `\figplan`, 3 `\datanote`, 40 theorem-type envs / 37 proofs | +10 |
| Ch3 Certification | ch3-certification.tex | 12,032 | 40 | 40 (pp 83-122) | 44 | drafted; under statistics review; being edited during audit; 1 gap box, 3 `\figplan`, 5 `\datanote`, 18 envs / 18 proofs | -4 |
| Ch4 Sharpness and blocking | ch4-sharpness-blocking.tex | 15 | 0 | 2 (pp 123-124) | 40 | stub; blocked on Theorem 9 propagation | -38 |
| Ch5 Identifiability | ch5-identifiability.tex | 16 | 0 | 2 (pp 125-126) | 44 | stub | -42 |
| Ch6 USD validation | ch6-usd-validation.tex | 17 | 0 | 2 (pp 127-128) | 40 | stub; data spec exists in App C | -38 |
| Ch7 ZAR coda | ch7-zar-coda.tex | 16 | 0 | 2 (pp 129-130) | 20 | stub; data spec exists in App C | -18 |
| Ch8 Conclusions | ch8-conclusions.tex | 12 | 0 | 2 (pp 131-132) | 10 | stub (end-game) | -8 |
| App A Tenor consistency | appA-tenor.tex | 16 | 0 | 2 (pp 133-134) | 14 | stub | -12 |
| App B Standard proofs | appB-proofs-standard.tex | 15 | 0 | 1 (p 135) | 30 | stub | -29 |
| App C Data, code, reproducibility | appC-data-code.tex + appC-usd-data.tex (3,645) + appC-zar-data.tex (2,175) + appC-code.tex (846) | 6,687 | 22 | 21 (pp 136-156, typeset under the App B header, see R4) | 16 | data sections drafted; code section has `rates` only; reproducibility protocol is a `\gap{}` | +5 |
| Bibliography | bibliography.tex (53 `\bibitem`) / References.bib (50 entries) | - | 3 | 3 (pp 157-159) | 10 | verified; will grow | -7 |
| **Total** | | **34,311** | **116** | **159** | **352** | 3 of 13 parts drafted | drafted parts 119 vs 108 budgeted (+11); 233 budgeted pages unwritten |

### Missing content, drafted parts

**Ch3 (4 pages under budget, about 1,200 words).** Every item below is a rule already on file, not new scope.
1. Positioning remark after Theorem 3.x (`thm:cov`) against Barber and Pananjady (2026): marginal coverage without blocking at cost 2 beta(tau)+2 beta(tau*), rate N^{-r/(r+1)}; Theorem 6(i) is the blocked route whose payoff is the conditional Beta(k, n+1-k) statement (ii). GROUND-TRUTH correction 12 requires the citation wherever 6(i) is discussed. ch3 cites `barber2023` and `oliveira2024` once each and never `barber2026`, `halkiewicz2026`, `ramos2026`; all three keys exist in bibliography.tex. About 1 page.
2. Chapter notes on the 2026 literature: Ramos, Graziadei and Cabezas (2026, Prop. 13: the drift penalty d_K(P,Q) in print); Zheng and Proutiere (2024) and Allohibi (2026) gapped/thinned splits; Zwart (2025) and Vovk (2012) so the "2.3 times tighter than DKW" remark is not claimed as new. About 1 page.
3. Figures 3.1-3.3 are all `\figplan`. Figures 3.2 (Beta density against the DKW bound) and 3.3 (AR(1) Monte Carlo against block length) need no market data and are producible now from `thesis/code/certify`; they are the chapter's only figure content. About 1.5 pages when real.
4. Table 3.1 and the exact coverage 0.9089 are hand-computed; regenerate from `certify` and add the cross-check `\datanote{}` with the code-run figures already on file (marginal 0.8853, Beta quantile 0.8239, conditional 0.8126, Monte Carlo 0.9310, seed 20260909).
5. The FRTB PLA thresholds in the Section 3.8.3 `\datanote{}` are quoted from memory; verify against `bcbs2019` before Chapter 6 uses them.

**Ch2 (10 pages over budget) with App B empty (30-page budget).** STANDARD allows standard results to be proved "in the chapter or Appendix B". Candidates to move to App B with a back-reference: Section 2.8.3 Berbee and Yu proofs (pp 47-49), Sections 2.9.3-2.9.4 W1 identity and Bobkov-Ledoux (pp 54-56), and the Hagan derivation sketch (2.5.3), expanded to the full derivation STANDARD asks for. Items STANDARD lists as "proved in full" that are only stated in ch2: uniform DKW (`thm:prelim-dkw`, stated and cited; only the pointwise corollary is used), Hagan formula components (sketch), SABR uniqueness in law (cited). App B is where these belong. Net effect: ch2 to about 50 pages, App B gains 8-10 pages of real content.

**App C (5 pages over, and still incomplete).** Still to write: `certify` package subsection under Code architecture (only `rates` is present) with the `uv run --with numpy --with scipy python certify/tests/test_certify.py` command; the reproducibility protocol (SARB range-selector exports must record range, earliest date returned and timestamp; USD user-supplied LIBOR CSV reader); projected +3 pages, so about 24 against 16. Compression already recommended by the USD data engineer: register tables (USD Table, ZAR Table) to compact form, quality-issue itemised lists to prose.

### Risk register, 2026-09-09

| # | Risk | Evidence | Impact | Owner / action |
|---|---|---|---|---|
| R1 | Theorem 9 restatement: landed, propagation pending | Third version in `13-mathematics-3yr.tex` (16:14) and GROUND-TRUTH.md (16:15) today: blocked rate N^{-r/(2r+3)} is not minimax; deficit is the expected calibration-conditional shortfall from Thm 6(ii); exact minimiser (2(r+1))^{2/(2r+3)} N^{3/(2r+3)}; lower bound (iii) route only, delta-dependence open. ch3 does not yet cite Barber-Pananjady (2026) or Halkiewicz (2026); ch4 (40 pp, the doctoral spine) unwritten; ch1, ch8, abstract inherit | 40 of 352 pages and the doctoral claim | statistician and adversary-thm9: restate in ch3 remark; write ch4 only from the third version |
| R2 | ZAR data sponsor | App C ZAR: JIBAR/ZARONIA cap, floor and swaption vols are sponsor-only; no screen quotes exist (MPG 2025); decision point month 12; fallback is a historical-volatility policy with ch7 relabelled | Ch7 (20 pp) reserve decomposition; ch5 empirical illustration | supervisor liaison: approach a dealer under the aggregate-only data agreement in App C |
| R3 | USD data licence | App C USD: no public USD LIBOR fixing history or option surface; SOFR non-linear quoted only from Nov 2021 | Ch6 (40 pp, empirical spine) cannot be written on public data | supervisor liaison: university Bloomberg/LSEG access |
| R4 | Label mismatches in the compiled build | (a) `Thesis/Annexures/annexureC_data_code.tex` has no `\chapter` line although `sync_from_workdir.sh` line 19 emits one: App C typesets as B.1-B.4 under "Proofs of Standard Results"; `Appendix ??` on pp 115, 116, 141 (`\ref{appC-data-code}`); TOC and page headers wrong for 21 pages. (b) `Chapter ??` p 86: repository ch3 refers to the Preliminaries chapter by a label ch2 does not define (ch2 carries only `ch:prelim`); working copy corrected 16:13, repository not resynced. (c) Two label conventions coexist: ch2 has only the canonical label, ch3 has `ch:cert` and `ch:certification` and no file-name label, the other nine files carry both; 55 `\ref` uses of file-name labels in ch3 and App C against STANDARD's canonical rule. (d) `\figplan` has no label argument; labels sit inside captions | Wrong TOC, wrong headers, four unresolved references in the submitted-looking PDF | crossref checker: re-run sync, rebuild, keep a `.log`; decide one label convention |
| R5 | Appendix C over its share of budget | 21 typeset against 16 with protocol and `certify` sections still to come; projected 24 (+50 %) | Squeezes App B and Ch7 if the total is held at 352 | writer-appC-data: compress tables and lists as above; or raise App C budget to 24 and take 8 from App B after the ch2 proofs move in |
| R6 | Ch2 over budget while App B is empty | 58 against 48; App B 0 against 30 | Preliminaries dominate the statistics-first reading | redundancy cutter and appB writer: move the standard proofs listed above |
| R7 | Front matter over budget | 22 against 12: 5-page three-level TOC (Wits guide requires three levels), lists of figures and tables already populated by planned figures, `openright` blanks | Budget line unreachable | orchestrator: reset front-matter budget to about 18; do not cut TOC depth |
| R8 | Two build trees diverge | Working `main.tex` (book class, no natbib, `\cite` prints bracket labels) against repository `main.tex` (report class, natbib, glossaries); compile is from the repository; ch3 working copy newer than the compiled copy | Audit figures and reviewer reading differ from the PDF | latex-builder: retire the working `main.tex` at round two as LOOP says; record source mtime with every compile |
| R9 | Publication before submission | Faculty rule FSO 10.5; nothing extracted yet | Cannot submit without a manuscript under review or a waiver letter | publication strategist: ch3/ch4 paper once Theorem 9 is stable |
| R10 | Unverified numerical claim in ch3 | FRTB PLA zone thresholds in a `\datanote{}` from memory | Ch6 regulatory backtest section | citation enforcer: verify against `bcbs2019` |
| R11 | Concurrent editing | ch3 mtime 16:13:08 during this audit | Conflict-rule breach; snapshot counts | orchestrator: one editor per file per stage |

## Compile log
| Date | Chapter | Status | Pages (chapter) | Pages (total) | Notes |
|---|---|---|---|---|---|
| 2026-09-09 | ch2-preliminaries | drafted, under finance review | 58 | 159 | over budget by 10; 1 gap box |
| 2026-09-09 | ch3-certification | drafted, under statistics review | 40 | 159 | under budget by 4; compiled copy older than working copy |
| 2026-09-09 | appC-data-code | data and code sections drafted | 21 | 159 | typeset under App B header (R4); protocol missing |
| 2026-09-09 | all others | stub | 2 each | 159 | 9 stubs = 17 pages of the 159 |
