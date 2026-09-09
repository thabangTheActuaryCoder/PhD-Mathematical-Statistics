# zwart2025 — Zwart, P. H. (2025). Probabilistic conformal coverage guarantees in small-data settings. arXiv:2509.15349.

**Record check (p. 1):** "Probabilistic Conformal Coverage Guarantees in Small-Data Settings — Petrus H. Zwart, PHZwart@lbl.gov, Berkeley … Lawrence Berkeley National Laboratory — arXiv:2509.15349v1 [cs.LG] 18 Sep 2025." Matches References.bib (misc, arXiv:2509.15349, 2025). Version read: v1.
**Source / licence:** arXiv, https://arxiv.org/abs/2509.15349 (arXiv non-exclusive licence). File: `References/PDF/zwart2025.pdf` (17 pp; printed page = PDF page). Highlighted copy: `References/PDF/zwart2025.highlighted.pdf`.

| Page | As printed | Verbatim excerpt | Why it matters | Locator |
|---|---|---|---|---|
| 1 | Abstract | "However, in split conformal prediction this guarantee is training-conditional only in expectation: across many calibration draws, the average coverage equals the nominal level, but the realized coverage for a single calibration set may vary substantially." | Motivation for the conditional statement Thm 6(ii). | `[p.~1]` |
| 2 | eq. (2) | "with probability at least 1 − δ over any random calibration draw, the achieved coverage is near the nominal level (Vovk, 2012): Pr(coverage ≥ 1 − α − ε) ≥ 1 − δ." | Independent attribution of the PAC form to Vovk 2012. | `[eq.~(2), p.~2]` |
| 2 | after eq. (3) | "DKWM (Massart, 1990) and Hoeffding (Hoeffding, 1963) bounds yield ε = O(sqrt(ln(1/δ)/n)), implying O(α^{−2}) sample complexity when α is small." | Why the thesis prefers the Beta quantile to DKW (GROUND-TRUTH correction 4). | `[p.~2]` |
| 2 | eq. (4) | "If n calibration points are available and the nominal miscoverage is α, the infinite-test coverage behaves as C ∼ Beta(k, n + 1 − k), k = ⌈(1 − α)(n + 1)⌉". | The Beta(k, n+1−k) law in exactly the thesis's notation, already in use before the thesis (LESSONS scout-literature: not new). | `[eq.~(4), p.~2]` |
| 3 | eq. (7) and text | "C_∞ ∼ Beta(k, n + 1 − k). This arises because the empirical quantile induces a random acceptance threshold distributed according to a Beta law." | Same. Zwart attributes the derivation to Marques Filho (2025), not in References.bib. | `[Sec.~2.1, p.~3]` |
| 3 | Section 1 / eq. (5), (11) | "Compared with concentration-based adjustments, SSBC yields markedly sharper guarantees—improving sample complexity from O(α^{−2}) to O(1/α) up to logarithmic factors". SSBC: "α_adj is the largest adjusted miscoverage rate such that, with probability at least 1 − δ over any calibration draw, the realized coverage meets or exceeds the target level." | Operational use of the Beta quantile b_{n,k}(δ) as a calibration-conditional guarantee = the practice Thm 6(ii) certifies; the "2.3× tighter than DKW" remark is prior art. | `[Sec.~2.2, p.~3]` |
| 4 | eq. (14) | "α*_∞(n, δ) = 1 − δ^{1/n}." "with a calibration set of size n, one cannot demand simultaneously vanishing miscoverage α and vanishing risk δ." | Feasibility limit relevant to ch3 worked example (n = 25) and ch7 (small ZAR record). | `[eq.~(14), p.~4]` |

## Notes for writers
- Cite `\citep[eq.~(4)]{zwart2025}` alongside `\citep[Prop.~2b]{vovk2012}` when stating the Beta law; say the thesis's contribution is the extension to β-mixing calibration plus drift, not the Beta quantile itself.
- Preprint, not peer reviewed as of 2026-09-09; say "preprint" in text.
